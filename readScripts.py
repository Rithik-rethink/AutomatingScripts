#!/usr/bin/env python3

import csv 
import sys

csv_filename = sys.argv[1]
name_list = sys.argv[2]
def generate_report(csv_file,name_list):
	report = []
	with open(csv_file) as file:
		line = csv.reader(file)	
		next(line)
		for row in line:
			s = ''
			mark = int(row[1])/50
			marks = mark * 100
			with open(name_list) as files:
				lines = csv.reader(files)
				next(lines)
				for i in lines:
					if i[0] == row[0]:
						s += i[1]
						break
			s += '                  ' +str(marks) + '(' + row[1] + ')'
			report.append(s)
	make_report(report)

def make_report(report):
	file = open('generated_report.txt','w+')
	for i in report:
		file.write(i + '\n')
	file.close()
generate_report(csv_filename,name_list)


