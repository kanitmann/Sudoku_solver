board = [[1," ",3," ",5," ",7,8,9],
          [1,2,3,4," ",6,7," ",9],
          [1,2,3," ",5,6,7," ",9],
          [1,2," ",4," ",6,7,8,9],
          [1," ",3,4,5," "," "," ",9],
          [" ",2,3,4," ",6,7," "," "],
          [1," "," ",4,5,6,7,8," "],
          [1," ",3,4," ",6," ",8,9],
          [" ",2," ",4,5,6,7,8," "]]

def print_board(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0  and i!=0:
            print("---------------------")
        for j in range(len(sudoku[0])):
            if j % 3 ==0 and j!=0:
                print("|", end="")
            if j == 8:
              print(sudoku[i][j])
            else:
              print(str(sudoku[i][j]) + " ",end="")

def find_space(sudoku):
  for i in range(len(sudoku)):
    for j in range(len(sudoku[0])):
      if sudoku[i][j]==" ":
        return(i,j)