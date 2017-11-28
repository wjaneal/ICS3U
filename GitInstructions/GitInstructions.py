#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:01:53 2017
GitHub Command Line Instructions
@author: wneal

Using Git:  Work Flow
(1) Use the command line - it will avoid problems later.
(2) These instructions assume that your GitHub folder is 
in your documents folder.
(3) To start using git:.....
    (a) Windows - start Git Bash
    (b) Mac / Linux - start a terminal
(4) cd Documents/GitHub  #'cd' changes directories
(5)  Where am I? - type pwd #pwd - present working directory
(6) make a new directory with your name - mkdir Joe
(7) change to this directory - cd Joe
(8) change back one directory cd ..

(9) Making changes to the source code....
    (a) git status - check which branch you are in 
    (b) git pull - update the current branch
    (c) git checkout -b Joe1
    (d)  Make some changes in the Joe directory
        ...use spyder or use command line for example
(10) Add/commit/merge the changes using Git:
    (a) git pull #Update!!!!!
    (b) git add -A #This adds all the files you have changed.
    (c) git commit -m "Added some files"
    (d) git push origin Joe1
    
(11) Merge into main branch (one person per group should do this)
    (a) Only do this if you are sure the code works!
    (b) git checkout master #Switches to the master branch
    (c) git merge Joe1 #Merge the changes Joe made
    (d) git push origin master #Update to GitHub website



"""



