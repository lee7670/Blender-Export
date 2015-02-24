import bpy
import sys
#some code taken from Jim McCann's export code
objname = None
for j in range(0, len(sys.argv)):
	if sys.argv[j] == '--':
		if len(sys.argv) == j + 2:
			objname = sys.argv[j+1]
if objname == None:
	print("Please pass '-- <object>' after the script name")
	bpy.ops.wm.quit_blender()
selobj = None
for obj in bpy.data.objects:
    if obj.name == objname:
        selobj = obj
if selobj == None:
    print("object not in scene")
    bpy.ops.wm.quit_blender()
bpy.ops.object.mode_set(mode='OBJECT')
selobj.data = selobj.data.copy() #"make single user" (?)
bpy.context.scene.layers = selobj.layers
#First, triangulate the mesh:
bpy.ops.object.select_all(action='DESELECT')
selobj.select = True
bpy.context.scene.objects.active = selobj
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
#use_beauty went away in 2.70, now use:
bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
bpy.ops.object.mode_set(mode='OBJECT')
print("start")
tri=0
for poly in selobj.data.polygons:
    print("triangle: "+str(tri))
    pnt = 1
    assert(len(poly.vertices) == 3)
    for vi in poly.vertices:

        print("vert: "+str(pnt))
        print("x: " + str(selobj.data.vertices[vi].co.x))
        print("y: " + str(selobj.data.vertices[vi].co.y))
        print("z: " + str(selobj.data.vertices[vi].co.z))
        pnt = pnt + 1
    tri=tri+1
            
    
    