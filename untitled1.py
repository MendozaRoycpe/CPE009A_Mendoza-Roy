# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:42:45 2026

@author: TIPQC
"""

name = "Royce Chua"
file = open("newfilel.txt",'w')
file.write(f"Hello, {name}!\n")
file.write("Isn't this amazing!\n")
file.write("that we can create and write on text files\n")
file.write("using Python.")
file.close()