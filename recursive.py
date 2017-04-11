# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:15:08 2017

@author: user
"""

import re
import regex

def recursive(string):
    
    string = string[1:-1]
    
    temp = []
    while string != "":

        #m = re.search("({(-*\d+\.*\d*;*)*})+", string)
        #m = re.search("({.*})+", string)
        m = regex.search("(?<rec>\{(?:[^{}]+|(?&rec))*\})", string)
        
        if m:
            temp.append(recursive(m.group(0)))
            string = string.replace(m.group(0), "")
        else:
            #temp.append( [ float(x) for x in re.findall("-*\d+\.*\d*", string) ] )
            for x in regex.findall("-*\d+\.*\d*", string):
                temp.append(float(x))
            string = ""
            
    return temp
    

if __name__ == '__main__':
    
    string = "{ { { 1.0; 1.1; 1.2 } { 1.3; 1.4 } } { { 1.5; 1.6 } { 1.7; 1.8; 1.9 } } }"
    vals = []
    
    string = string.replace(" ", "")
    vals = recursive(string)
    
    print(vals)
    