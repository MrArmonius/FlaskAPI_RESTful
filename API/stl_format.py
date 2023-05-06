import numpy
from stl import mesh

X_Print_Board, Y_Print_Board, Z_Height = 220.0, 220.0, 250.0 

def refactor_stl(path):
    my_mesh = mesh.Mesh.from_file(path)
    
    # Modify Stl functions:
    translate_center(my_mesh)

    # save the new stl file:
    my_mesh.save(path)

def translate_center(my_mesh):
    size_cube = my_mesh.max_ - my_mesh.min_

    #positionning the cube to the center, the Height Z stay at 0
    x_delta = -my_mesh.min_[0] - size_cube[0]/2
    y_delta = -my_mesh.min_[1] - size_cube[1]/2

    #Apply the delta
    my_mesh.x = my_mesh.x + x_delta
    my_mesh.y = my_mesh.y + y_delta
    my_mesh.z = my_mesh.z - my_mesh.min_[2]
    my_mesh.update_min()

    print("Position: ", my_mesh.min_)
    print("Size cube: ", size_cube)

    

