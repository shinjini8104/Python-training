matrix =[
    [1, 2, 3,20],
    [4, 5, 6,30],
    [7, 8, 9,40],
    [10, 11, 12,50],
    [2,3,4,1]   
    
]
rows = len(matrix)
cols = len(matrix[0])

top = 0
bottom = rows - 1   
left = 0
right = cols - 1

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        print(matrix[top][i], end=" ")
    top=top+1

    for i in range(top, bottom+1):
        print(matrix[i][right], end=" ")
    right=right-1

    
    for i in range(right, left -1,-1):
        print(matrix[bottom][i], end=" ")
    bottom=bottom-1

    for i in range(bottom, top -1,-1 ):
        print(matrix[i][left], end=" ")
    left=left+1 

    