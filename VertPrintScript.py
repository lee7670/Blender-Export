import bpy
print("start")
print("verts")
for i in range(len(bpy.data.objects["Crate"].data.vertices)):
    print("point: "+str(i));
    print('x: '+str(bpy.data.objects["Crate"].data.vertices[i].co.x))
    print('y: '+str(bpy.data.objects["Crate"].data.vertices[i].co.y))
    print('z: '+str(bpy.data.objects["Crate"].data.vertices[i].co.z))