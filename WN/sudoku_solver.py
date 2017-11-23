#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:14:10 2017
Sudoku Solver - enter a sudoku puzzle and the program will (hopefully) solve it.
@author: wneal
"""
size = 9 #Must be a perfect square
puzzle_grid = [0 for i in range(size*size)]
puzzle_grid = [2,0,5,0,0,0,0,8,9,
               1,0,3,0,0,5,0,4,0,
               0,8,0,0,3,0,1,2,0,
               6,7,0,0,1,0,2,0,8,
               0,0,0,7,0,2,0,0,0,
               9,0,1,0,4,0,0,5,7,
               0,4,2,0,9,0,0,7,0,
               0,5,0,4,0,0,9,0,2,
               3,1,0,0,0,0,8,0,4]
possibilities_grid =[]
for i in range(0,len(puzzle_grid)):
    if puzzle_grid[i]==0:
        possibilities_grid.append([1,2,3,4,5,6,7,8,9])
    else:
        possibilities_grid.append(puzzle_grid[i])
        
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
def scan_cross_count(puzzle_grid, possibilities_grid):
    global size
    for i in range(0,size):
        for j in range(0,size):
            intersect(puzzle_grid, possibilities_grid,i,j)

#Intersect            
def intersect(puzzle_grid, possibilities_grid, i, j):
    #Scan columns
    global size
    for square in range(0,size):
        if puzzle_grid[size*i+square] in possibilities_grid[size*i+square]and square!=j:
            possibilities_grid[size*i+square].remove(puzzle_grid[size*i+square])
    #Scan rows
    for square in range(0,size):
        if puzzle_grid[size*square+j] in possibilities_grid[size*square+j] and square!=i:
            possibilities_grid[size*square+j].remove(puzzle_grid[size*i+square])            
    for item in block_count(puzzle_grid, i, j ):
        possibilities_grid[i,j].remove(item)
#Block counts
def block_count(puzzle_grid, i,j):
    block_items = []
    block_row = int(i/3)
    block_column = int(j/3)
    for row in range(0,int(size/3)):
        for column in range(0,int(size/3)):
            if puzzle_grid[3*size*(block_row)+int(size/3)*block_column+size*row+column] not in block_items:
                if int(size/3)*block_row+row != i or int(size/3)*block_column+column != j:
                    blockitems.append(puzzle_grid[3*size*block_row_int(size/3)*block_column+size*row+column])
    return block_items
            
#Triple cross check
def triple_cross_check(puzzle_grid, i,j):
    for number in range(size):
        if number_in_other_rows(puzzle_grid, i,j,number)==2 and number_in_other_columns(puzzle_grid, i,j,number)==2:
            grid_possibilities(i,j)==number            
            
#Numbers in other rows
def number_in_other_rows(i,j,number):
    count = 0
    block_row = int(i/3)
    block_column = int(j/3)
    block_sub_row = i % 3
    block_sub_column = j % 3
    for row in range(0, int(size/3)):
        if row != block_sub_row:
            for column in range(0,size):
                if int(column/3)!=block_column:
                    if puzzle_grid[3*size*block_row+column+size*row]==number:
                        count+=1
    return count
            
#Numbers in other columns
def number_in_other_columns(i,j,number):
    count = 0
    block_row = int(i/3)
    block_column = int(j/3)
    block_sub_row = i % 3
    block_sub_column = j % 3
    for column in range(0,int(size/3)):
        if column != block_sub_column:
            for row in range(0,size):
                if int(row/3)!=block_row:
                    if puzzle_grid[3*size+block_row+int(size/3)*block_column]==number:
                        count+=1
    return count
#Main Loop
complete = False
while not complete:
    print(puzzle_grid, possibilities_grid)
    scan_cross_count(puzzle_grid, possibilities_grid)
    print(puzzle_grid, possibilities_grid)
    complete = True
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
