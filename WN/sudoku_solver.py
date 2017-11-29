 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:14:10 2017
Sudoku Solver - enter a sudoku puzzle and the program will (hopefully) solve it.
@author: wneal
"""
size = 9 #Must be a perfect square
#puzzle_grid = [0 for i in range(size*size)]
'''puzzle_grid = [2,0,0,0,8,0,7,9,0,
               0,1,0,6,3,0,4,0,0,
               0,0,0,0,0,9,0,0,0,
               0,7,3,0,0,0,5,0,1,
               5,0,0,0,0,0,0,0,4,
               4,0,1,0,0,0,9,8,0,
               0,0,0,7,0,0,0,0,0,
               0,0,8,0,2,1,0,4,0,
               0,6,5,0,9,0,0,0,2]
'''
puzzle_grid = [2,0,4,0,8,0,7,9,0,
               0,1,7,6,3,0,4,0,0,
               0,0,0,0,0,9,0,0,0,
               0,7,3,0,0,0,5,0,1,
               5,0,0,0,0,0,0,0,4,
               4,0,1,0,0,0,9,8,0,
               0,0,0,7,0,0,0,0,0,
               0,0,8,0,2,1,0,4,0,
               0,6,5,0,9,0,0,0,2]

G =[]
for i in range(0,len(puzzle_grid)):
    if puzzle_grid[i]==0:
        G.append([1,2,3,4,5,6,7,8,9])
    else:
        G.append([puzzle_grid[i]])
#Possibilities count:
def possibilities_count(G):
    total = 0
    for i in range(0, len(G)):
        total+=len(G[i])
    return total
#Functions used to design row-by-row and column-by column operations
def adjust_row(puzzle_grid, row):
    for i in range(0,size):
        puzzle_grid[row*size+i] += 1
        
def adjust_column(puzzle_grid,column):
    for i in range(0,size):
        puzzle_grid[column+i*size]+=1        

#Function to design block-by-block operations
def adjust_block(puzzle_grid, block_row, block_column):
    for i in range(0, int(size/3)):
        for j in range(0,int(size/3)):
            puzzle_grid[int(size/3)*block_column+size*3*block_row+i*int(size)+j]+=10

#Scan cross counts
def scan_cross_count(G):
    global size
    for i in range(0,size):
        for j in range(0,size):
            #print(G[i*size+j],i,j,i*size+j)
            if len(G[i*size+j])!=1:
                intersect(G,i,j)

#Intersect            
def intersect(G, i, j):
    #Scan row
    global size
    #print(G[i*size+j])
    for square in range(0,size):
        if len(G[size*i+square])==1 and size*i+square != size*i+j:
            if G[size*i+square][0] in G[size*i+j]:
                if len(G[size*i+j])==1:
                    print ("Length error!!!")
                if len(G[size*i+j])>1:
                    G[size*i+j].remove(G[size*i+square][0])
                #print (i,j,G[size*i+square][0], "row")
    #print(G[i*size+j])
    #Scan column
    for square in range(0,size):
        #print(square,size*square+j,G[size*square+j], "...details")
        if len(G[size*square+j])==1 and size*square+j != size*i+j:
            if G[size*square+j][0] in G[size*i+j]:
                if len(G[size*i+j])==1:
                    print ("Length error!!!")
                if len(G[size*i+j])>1:
                    G[size*i+j].remove(G[size*square+j][0])
            
                #print (i,j,G[size*i+square][0], "column")
    #print(G[i*size+j])
    #print(block_count(G,i,j), "Block count")
    for item in block_count(G, i, j ):
        #print (block_count(puzzle_grid,i,j))
        #print(i,j)
        if item in G[i*size+j]:
            if len(G[i*size+j])==1:
                print("Length Error!! 2")
            if len(G[i*size+j])>1:
                G[i*size+j].remove(item)
#Block counts
def block_count(G, i,j):
    block_items = []
    block_row = int(i/3)
    block_column = int(j/3)
    for row in range(0,int(size/3)):
        for column in range(0,int(size/3)):
            if len(G[3*size*(block_row)+int(size/3)*block_column+size*row+column])==1 and G[3*size*(block_row)+int(size/3)*block_column+size*row+column][0] not in block_items:
                if int(size/3)*block_row+row != i or int(size/3)*block_column+column != j:
                    block_items.append(G[3*size*block_row+int(size/3)*block_column+size*row+column][0])
    return block_items
            
#Triple cross check
def triple_cross_check(G):
    global size
    #print ("###########################")
    for i in range(0,size):
        for j in range(0,size):
            for number in range(1,size+1):
                #total=0
                #if i == 8 and j == 2 and number ==9:
                    #print ("At number level 4")
                if len(G[i*size+j])!=1 and number in G[i*size+j]:
                    other_rows_and_columns(G,i,j,number)
                    #if i == 8 and j == 2 and number ==9:
                        #print ("At number level 5")
                #print (i,j,total)
    #print ("###########################")
        
#Numbers in other rows
def other_rows_and_columns(G, i,j,number):
    global size
    row_count = 0
    column_count = 0
    block_row = int(i/3)
    block_column = int(j/3)
    block_sub_row = i % 3
    block_sub_column = j % 3
    for ii in range(0,size):
        for jj in range(0,size):
            block_row_ii = int(ii/3)
            block_column_jj = int(jj/3)
            block_sub_row_ii = ii%3
            block_sub_column_jj = jj%3
            if block_row_ii==block_row and block_column_jj !=block_column:
                if block_sub_row_ii!=block_sub_row:
                    if G[size*ii+jj]==[number]:
                        row_count+=1
            if block_column_jj==block_column and block_row_ii != block_row:
                if block_sub_column_jj !=block_sub_column:
                    if G[size*ii+jj]==[number]:
                        column_count+=1
    if row_count == 2:
        if not_in_block(G,number,block_row,block_column)==True and block_row_free(G, block_row, block_column, block_sub_row)== 1:
            if not_in_row(G,i,j,number)==True and not_in_column(G,i,j,number)==True:
                G[i*size+j]=[number]
                print ("2 count row: ", i, j, number)
              
            
    if column_count == 2:
        if not_in_block(G,number, block_row,block_column)==True and block_column_free(G, block_row, block_column, block_sub_column) == 1:
            if not_in_row(G,i,j,number)==True and not_in_column(G,i,j,number)==True:
                G[i*size+j]=[number]
                print("2 count column: ", i,j, number)
    
    if column_count==2 and row_count ==2:
          if not_in_row(G,i,j,number) and not_in_column(G,i,j,number):
              G[i*size+j] = [number]
              print ("4 count, ",i,j, number)

def not_in_block(G, number, block_row,block_column):
    for i in range(0,int(size/3)):
        for j in range(0,int(size/3)):
            if G[3*size*block_row+int(size/3)*block_column+size*i+j]==[number]:
                return False
    return True

def not_in_row(G,i,j,number):
    for jj in range(0,9):
        if jj != j:
            if number == G[i*size+jj][0]:
                return False
    return True


def not_in_column(G,i,j,number):
    for ii in range(0,9):
        if ii != i:
            if number == G[ii*size+j][0]:
                return False
    return True

def block_row_free(G, block_row,block_column, block_sub_row):
    global size
    free_blocks = 3
    for i in range(0,int(size/3)):
        if len(G[3*size*block_row+int(size/3)*block_column+int(size)*block_sub_row+i])==1:
            free_blocks -= 1
    return free_blocks

def block_column_free(G, block_row,block_column, block_sub_column):
    global size
    free_blocks = 3
    for i in range(0,int(size/3)):
        if len(G[3*size*block_row+int(size/3)*block_column+block_sub_column+size*i])==1:
            free_blocks -= 1
    return free_blocks

def display_grid(G):
    global size
    for i in range(0,9):
        display_string = ""
        for j in range(0,9):
            if len(G[i*size+j])==1:
                display_string+=str(G[i*size+j][0])
            else:
                display_string+="-"
        print(display_string)
        
def row_check(G):
    global size
    for row in range(0,size):
        for number in range(1,size+1):
            index = 0
            total = 0
            number_possibilities = []
            for column in range(0,size):
                try:
                    for item in G[row*size+column]:
                        if item == number:
                            number_possibilities.append(1)
                            index = column
                            total +=1    
                        else:
                            number_possibilities.append(0)
                except:
                    print("Error!", G[row*size+column])
            if row == 0 and number ==1 and len(G[row*size+index])>1:
                print(number_possibilities, "Row 0, number 1")
                print(G[row*size+index])
            if total==1 and len(G[row*size+index])>1:
                for i in range(0,size):
                    print(G[row*size+i])
                print("Setting from row: ", index, row*size+index)
                G[row*size+index] = [number]

def column_check(G):
    global size
    for column in range(1,size):
        for number in range(1,size+1):
            index = 0
            total = 0
            number_possibilities = []
            for row in range(0,size):
                #print(row,column,size, "col")
                try:
                    if number in G[row*size+column]:
                        number_possibilities.append(1)
                        index = row
                        total +=1
                    else:
                        number_possibilities.append(0)
                except:
                    print("Error!",G[row*size+column])
            if total==1 and len(G[index*size+column])>1:
                for i in range(0,9):
                    print (G[i*size+column])
                print(index*size+column, " set column ", index)    
                G[index*size+column] = [number]

def check_solution(G):
    global size
    #Check that all cells have one possibility:
    for i in range(0,len(G)):
        if len(G[i])!=1:
            print("Solution not yet complete")
            return False
    #check rows
    for row in range(0,size):
        rowcheck = [0]*size
        for column in range(0,size):
            rowcheck[G[row*size+column][0]-1]=1
        for i in range(0,size):
            if rowcheck[i]==0:
                print("Problem in row ",row)
                return False
    #check columns
    for column in range(0,size):
        columncheck = [0]*size
        for row in range(0,size):
            columncheck[G[row*size+column][0]-1]=1
        for i in range(0,size):
            if columncheck[i]==0:
                print("Problem in column ",column)
                return False
    #check blocks
    for blockrow in range(0,int(size/3)):
        for blockcolumn in range(0,int(size/3)):
            blockcheck = [0]*size
            for blocksubrow in range(0,int(size/3)):
                for blocksubcolumn in range(0,int(size/3)):
                     blockcheck[G[3*size*blockrow+int(size/3)*blockcolumn+size*blocksubrow+blocksubcolumn][0]-1]=1           
            for i in range(0,size):
                if blockcheck[i]==0:
                    print("Problem in block ", blockrow, blockcolumn)
                    return False
    print ("A correct solution has been found")
    return True

#Solve function - four operations to solve the puzzle
def solve(G):
    scan_cross_count(G) # (1) Check row, column and box for each square
    #Eliminate possibilities for each square based on contents of the row, column and box
    triple_cross_check(G) # (2)  For each box, and each number, fill in numbers
    #Based on numbers found in different sub-rows and sub-columns in other boxes
    row_check(G) #Identify squares in each row that are the unique possibility for a given number
    column_check(G) #Same as row check but for columns
    

#Main Loop
count_limit = 100

count = 0
complete = False
print("Before: ", possibilities_count(G))
display_grid

while not complete:
    solve(G) #send the puzzle to the Solve function
    print(possibilities_count(G))
    count+=1
    complete = check_solution(G)
    if count == count_limit:
        complete = True
        
print("After: ", possibilities_count(G))
print(G)
display_grid(G)
#print(G)


'''print("Block Rows")
for br in range(0,3):
    for bc in range(0,3):
        for i in range(0,3):
            print (G[br*9+bc*3+int(size)*i],
                   G[br*9+bc*3+1+int(size)*i],
                   G[br*9+bc*3+2+int(size)*i],
                   block_row_free(G,br,bc,i))
print("Block Columns")
for br in range(0,3):
    for bc in range(0,3):
        for i in range(0,3):
            print (G[br*3*size+bc*3+i],
                   G[br*3*size+bc*3+size+i],
                   G[br*3*size+bc*3+2*size+i],
                   block_column_free(G,br,bc,i))
'''
#Scan cross counts
    #Scan block counts
    #Scan triple rows and columns by number
        
    
'''
print(puzzle_grid)
adjust_row(puzzle_grid, 2)
adjust_column(puzzle_grid, 3)
adjust_row(puzzle_grid, 5)
adjust_column(puzzle_grid,5)
adjust_block(puzzle_grid, 0,0)
adjust_block(puzzle_grid, 2,2)
print(puzzle_grid)
print(puzzle_possibilities)
'''
