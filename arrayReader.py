def read(x):
    if x==[]:
        return 0
    else:
        print(x[0]+x[1]+x[2]+x[3])

read([x.split()for x in open ("C:/Users/Labing960Clon/Documents/ModelosII/matriz.txt").readlines()])
