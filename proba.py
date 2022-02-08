import re

sampletostring = {}
count = 0
listofsample = []
filename = input("Enter filename:\n")
with open(filename) as f:
    for line in f:
        sample = re.findall(r'\|1\|0\|(\d{1,2})(\d\d)\|', line)
        if sample:
            listofsample.append([int(sample[0][0]), int(sample[0][1]), count])
        count += 1

maxsample = {}
for i, item in enumerate(listofsample):
    if item[0] not in maxsample:
        maxsample[item[0]] = item[1]
    elif item[1] > maxsample[item[0]]:
        maxsample[item[0]] = item[1]

print(maxsample)
wrongtoright = {31: 1, 32: 2, 33: 3, 34: 4, 35: 5, 36: 6, 37: 7, 38: 8, 49: 9, 41: 10}
linecount = 0
with open(filename, "r+") as fo:
    tervefile = fo.readlines()
for line1 in tervefile:
    sample1 = re.findall(r'\|1\|0\|(\d{1,2})(\d\d)\|', line1)
    if sample1 and int(sample1[0][0]) in [31, 32, 33, 34, 35, 36, 37, 38, 49, 41, 40, 42]:
        number1 = str(wrongtoright[int(sample1[0][0])]) + str(
            maxsample[wrongtoright[int(sample1[0][0])]] + int(sample1[0][1]))
        line1 = re.sub(r'\|1\|0\|(\d{1,2}\d\d)\|', '|1|0|' + number1 + '|', line1)
        tervefile[linecount] = line1
    linecount += 1
fo.close()
with open('new_'+filename, 'w') as fp:
    fp.writelines(tervefile)
