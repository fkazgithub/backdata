#coding: utf-8


import csv

f = open('walkinnavi.csv','rb')

dataReader = csv.reader(f)

for row in dataReader:
	print row