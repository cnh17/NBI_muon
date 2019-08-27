"""
Script to find ZZ processes. Found just one at event number: 45441783
"""
import csv
import ROOT

ev1=[]
ev2=[]
with open('pairs_muons.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        ev1.append(int(row[0]))
with open('pairs_egamma.csv', 'r') as csvfile1:
    reader1 = csv.reader(csvfile1)
    for row in reader1:
        ev2.append(int(row[0]))

evnum=ev1 +ev2
evnum.sort()
print "no. of Z producing event numbers", len(evnum), "Min:", min(evnum), "Max:", max(evnum)

dupes = []
for n in range(len(evnum)):
    if (n % 15000) == 0:
        print "processing event number...", n
    x = evnum[n]
    if n+1 < len(evnum):
        n+=1
        y = evnum[n]
    else:
        y = 0
    if x==y :
        dupes.append(x)
print "no. of overlapping Z producing event numbers in two trees:", len(dupes), "event number:", dupes
print "Verification:"

### verification to check I haven't just found a duplicate pairs in one tree ###
for n in range(len(ev1)):
    if dupes[0] == ev1[n]:
        print "in DataMuons tree", ev1[n]
for n in range(len(ev2)):
    if dupes[0] == ev2[n]:
        print "in DataEgamma tree", ev2[n]

csvfile.close()
csvfile1.close()

#-------------------------------------------------------------------
### CHECK it is actually a ZZ boson process not same Z repeated ###
input_path = "/home/atlas/ATLAS-DataAndTools/Input/Data/"
tree_name   = "mini;3"
t = ROOT.TChain(tree_name)
t.Add(input_path+"DataMuons.root")

num_events = t.GetEntries()
a=[]
for n in range(num_events):
    t.GetEntry(n)
    eventnum = t.eventNumber
    lep_n = t.lep_n
    if eventnum ==dupes[0]:
        for i in range(lep_n):
            lep_type = t.lep_type[i]
            a.append(lep_type)

t2 = ROOT.TChain(tree_name)
t2.Add(input_path+"DataEgamma.root")
num_events = t2.GetEntries()
b=[]
for n in range(num_events):
    t2.GetEntry(n)
    eventnum = t2.eventNumber
    lep_n = t2.lep_n
    if eventnum ==dupes[0]:
        for i in range(lep_n):
            lep_type = t2.lep_type[i]
            b.append(lep_type)

print "Leptons in decay", a ,b
