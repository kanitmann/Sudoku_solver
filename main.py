#Code By Kanit



sudoku_board = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,3,0,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]#Hardest Sudoku puzzle according to "The Telegraph UK"




#printing the sudoku puzzle(unsolved)
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


#Finding empty spaces in the sudoku and returning their values for variable "pos"
def find_space(sudoku):
  for i in range(len(sudoku)):
    for j in range(len(sudoku[0])):
      if sudoku[i][j]==0:
        return(i,j) #Returning position of blank space

  return None #In case there is no plank space
  

def eligible(sudoku, num, pos):

  #Checking eligibilty in rows
  for i in range(len(sudoku[0])):   
      if sudoku[pos[0]][i] == num and pos[1]!=i:
        return False

  #Checking eligibilty in columns
  for i in range(len(sudoku)):   
    if sudoku[i][pos[1]] == num and pos[0]!=i:
      return False

  #Checking elgibility in boxes
  box_x = pos[1]//3
  box_y = pos[0]//3

  for i in range(box_y*3, box_y*3+3):
    for j in range(box_x*3, box_x*3+3):
      if sudoku[i][j] == num and (i,j) != pos:
        return False
  return True

#Solving the sudoku using above defined methods
def solve(sudoku):
  find = find_space(sudoku)
  if not find:
    return True
  else:
    row, col = find                         #assigning row and column from find_space(sudoku) function, ie the position of empty spaces in sudoku
  
  for i in range(1,10):
    if eligible(sudoku,i,(row,col)):        #calling eligible() function
      sudoku[row][col] = i

      if solve(sudoku):                     #This function triggers recursion (ie the concept of backtracking that we are using here)
        return True
      
      sudoku[row][col] = 0                  #resetting the row and col to '0' to recheck the value
  return False

print_board(sudoku_board)
solve(sudoku_board)
print("______________________")
print_board(sudoku_board)