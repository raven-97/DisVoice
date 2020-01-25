#@s_adharsh
from statistics import mean
import csv

fh = open('mamID.txt')
counts = dict()


for line in fh:
    line = line.strip()
    counts[line] = counts.get(line,0)+1
length = [0]*len(counts.keys())

for i in range(len(counts.keys())):
    length[i] = int(counts.get(str(i+1)))

print('===============================')
print(len(length))
print('===============================')
for j in range(len(length)):
    print(j+1,length[j])

fh2 = open('mam.txt')
files = 384
c = 0
f = 0
arr = list()
final = list()
print(arr)
for j in fh2:

    if c  == length[f]:
        f += 1
        print(map(mean, zip(*arr)))
        final.append(list(map(mean, zip(*arr))))
        arr = []
        c = 0
    b = list(map(float, j.split()))
    b.append(f)
    arr.append(b)
    c += 1

with open("mam.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(final)

print(f)
