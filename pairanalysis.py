import csv

evnum=[]
with open('pairs_muons.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        evnum.append(int(row[0]))
with open('pairs_egamma.csv', 'r') as csvfile1:
    reader1 = csv.reader(csvfile1)
    for row in reader1:
        evnum.append(int(row[0]))

evnum.sort()
print "no. of event numbers", len(evnum), "Min:", min(evnum), "Max:", max(evnum)

dupes = []
for n in range(len(evnum)):
    if (n % 5000) == 0:
        print "processing event number...", n
    x = evnum[n]
    if n+1 < len(evnum):
        n+=1
        y = evnum[n]
    else:
        y = 0
    if x==y :
        dupes.append(x)

print "no. of dupes", len(dupes), dupes

csvfile.close()
csvfile1.close()
