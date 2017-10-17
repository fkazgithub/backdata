# import pandas as pd

# df = pd.read_csv('walkingnavi2.csv')

# print (df)
# print df['A']

import pandas as pd
df = pd.read_csv("walkingnavi2.csv", encoding="SHIFT-JIS")
#print (df['D'])

listB = []
listC = []
listD = []

listB = df['B']
listC = df['C']
listD = df['D']
maxmin=8888888

for n in range(7146):
	maxmin=8888888
	for i in range(7146):
	 	if listB[n]==listB[i] and n!=i:
	 		min=abs(listC[n]-listC[i])
	 		if maxmin >= min:
	 			maxmin=min
	 			number=i+1
	 	
	 	# if maxmin >= min:
	 	# 	maxmin=min
	 	# 	number=i+1
	number2=n+1
	print ('id{0}はid{1}と最小誤差{2}をとる'.format(number2,number,maxmin))
	





	 	






