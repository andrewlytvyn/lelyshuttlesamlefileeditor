import re
import array as arr
import time
sampletostring={}
count=0
listofsample=[]
with open('1.txt') as f:
    for line in f:
        sample = re.findall(r'\|1\|0\|(\d{1,2})(\d\d)\|', line)
        if sample:
            listofsample.append([int(sample[0][0]),int(sample[0][1]),count])
            #sampletostring[int(sample[0][0])+int(sample[0][1])
        count+=1
'''['158', '101', 7150] 101 101 102 201
    find max normal sample
    store max normal sample
    find abnormal first sample
    rewrite abnormal sapmle with max normal+1 until abnormal true'''
#перебор и поиск максимальных значений пробирок и всех рам
maxsample={}

for i,item in enumerate(listofsample):
    if item[0] not in maxsample:
        maxsample[item[0]]=item[1]
    elif item[1] > maxsample[item[0]]:
        maxsample[item[0]]=item[1]
        
print(maxsample)
wrongtoright={31:1,32:2,33:3,34:4,35:5,36:6,37:7,38:8,49:9,41:10}
linecount=0
fo = open("1.txt", "r+")
wholefile = fo.readlines()
for line1 in wholefile:
    sample1 = re.findall(r'\|1\|0\|(\d{1,2})(\d\d)\|', line1)
    if sample1 and int(sample1[0][0]) in [31,32,33,34,35,36,37,38,49,41,40,42]:
        print(sample1)
        number1=str(wrongtoright[int(sample1[0][0])])+str(maxsample[wrongtoright[int(sample1[0][0])]]+int(sample1[0][1]))
        line1=re.sub(r'\|1\|0\|(\d{1,2}\d\d)\|','|1|0|'+number1+'|',line1)
        print(line1)
        
        wholefile[linecount]=line1
    linecount+=1

        
#fo.seek(0)
#fo.writelines(wholefile)
fo.close()
with open('foo.txt', 'w') as fp:
    fp.writelines(wholefile)

