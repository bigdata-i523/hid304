# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 20:16:52 2017

@author: Rick
"""

#https://piazza.com/class/j5wll7vzylg25j?cid=320

import yaml

lineDict = {}
tabDict = {}
lineCount = 0
in_yaml = False

with open("readme.txt", "r") as text: #https://stackoverflow.com/questions/7485458/python-reading-text-file
    text = text.readlines()
    
    for line in text:
        
        lineCount = lineCount + 1
        #print(line)
        if in_yaml:
            lineDict[lineCount] = line
            print(line)
        elif not in_yaml and line.startswith("```"):
            in_yaml = True
            try: #https://stackoverflow.com/questions/855759/python-try-else
                lineDict[lineCount] = line
            except:
                print(lineCount, line)
                print("Line is not in yaml format")
        elif in_yaml and not line.startswith("```"):
            in_yaml = False
    
        elif "\t" in line:
            tabDict[lineCount] = line

     

     