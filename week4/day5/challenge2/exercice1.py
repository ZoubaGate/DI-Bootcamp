triangle = [
    [0,0,1,0,0],
    [0,1,1,1,0],
    [1,1,1,1,1]
]
def triangle_isocele(triangle):
    for row in triangle:
        for slot in row:
            if slot:
                print("*",end="")
            else:
                print(" ",end="")
        print(" ")
triangle_isocele(triangle)
