#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:14:10 2017
Sudoku Solver - enter a sudoku puzzle and the program will (hopefully) solve it.
@author: wneal
"""
size = 9
puzzle_grid = [0 for i in range(size*size)]
puzzle_possibilities = [[1,2,3,4,5,6,7,8,9] for i in range(size*size)]

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


print(puzzle_grid)
adjust_row(puzzle_grid, 2)
adjust_column(puzzle_grid, 3)
adjust_row(puzzle_grid, 5)
adjust_column(puzzle_grid,5)
adjust_block(puzzle_grid, 0,0)
adjust_block(puzzle_grid, 2,2)
print(puzzle_grid)
print(puzzle_possibilities)

