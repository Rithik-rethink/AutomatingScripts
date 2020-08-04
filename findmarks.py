#!/usr/bin/env python3

import sys
import re
import csv 
import pandas as pd

csv_file = sys.argv[1]
student_usn = sys.argv[2]

def findmarks(csv_file,student_usn):
	with open(csv_file) as file:
		lines = csv.reader(file)
		next(lines)
		s = pd.DataFrame(lines)
		res =''
		
		res += s[s[0]==student_usn]
		print(res)
findmarks(csv_file,student_usn)
				
		
