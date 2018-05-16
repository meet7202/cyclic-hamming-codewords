'''
Created by Meet on 6/4/18
'''
f = open('input','r')
lines = f.readlines()
k = len(lines)
j=0
code = []
for i in range(len(lines)):
	words = lines[i].split(' ')
	words_int = map(int,words)
	code.append(words_int)
	n = len(words_int)
print "N =" + str(n)
print "K= " + str(k)
temps=[]
for b in range(k-1):
	
	for l in range(k-b-1):
		temp=[]
		for a in range(n):
			test = (code[b][a] + code[b+l+1][a])%2
			temp.append(test)
		flag=1
		for i in range(len(code)):
			if code[i]==temp:
				flag=0
		if flag==1:
			temps.append(temp)
			code.append(temp)



for d in range(3,k+1):
	temps2 = []			
	for b in range(len(temps)):
		for l in range(k):
			temp=[]
			
			for a in range(n):
				test = (temps[b][a] + code[l][a])%2
				temp.append(test)
			flag=1
			for i in range(len(code)):
				if code[i]==temp:
					flag=0
			if flag==1:
				temps2.append(temp)
				code.append(temp)
	temps=temps2
mini = 0
for p in range(len(code)):
	zero = code[p].count(0)
	if zero>mini:
		mini=zero
d = n-mini
print "D = " + str(d)

code.append([0]*n)
print "All Codewords :"
for i in range(len(code)):
	print(code[i])
