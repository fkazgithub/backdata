
import pandas as pd
filename = pd.read_csv('sample.csv',encoding="SHIFT-JIS")


listA = []
listB = []

listA=filename['学生番号']
listB = filename['点数']
max=0
leng = len(listA)

for n in range(leng):
	print (n)
	if listB[n]>max:
		max=listB[n]
		num = n
print ('最高得点をとった学生番号は'+str(listA[num]))

# sort=filename.sort_values(by='点数', ascending=False).head(1)['学生番号'].values[0]
#
# print (sort)
