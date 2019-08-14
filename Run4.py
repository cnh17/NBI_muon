import ROOT
import math

input_files = "/home/atlas/ATLAS-DataAndTools/Input/Data/DataMuons.root"
max_events = 1000
#------------------------------------------------#
f = ROOT.TFile(input_files)
t = f.Get("mini;3")   #tree specification
print "tree", t

num_events = t.GetEntries()
print "num events", num_events

if max_events < 0:
   max_events = num_events

output_file = ROOT.TFile("output2.root","RECREATE")
#------------------------------------------------#
h_num = ROOT.TH1F("h_num","",1000,-0.5,4.5) #construct hist
h_pt  = ROOT.TH1F("h_pt", "",100, 0.0,100.0) #no. of bins, range
h_eta = ROOT.TH1F("h_eta","",100,-5.0,  5.0)
h_phi = ROOT.TH1F("h_phi","",100,-3.2,  3.2)
h_E   = ROOT.TH1F("h_E","",100, -0.5, 300.0)
h_q   = ROOT.TH1F("h_q","",196,-1.5, 1.5)
h_mass= ROOT.TH1F("h_mass","",97, -0.5, 150)
#------------------------------------------------#
for n in range(max_events):

    t.GetEntry(n)

    if (n % 100) == 0:
        print "processing event...", n

    lep_n = t.lep_n #no. of preselected leptons in an event

    if lep_n ==2:
        h_num.Fill(lep_n)

        charge=[]
        for i in range(lep_n):
            lep_q = t.lep_charge[i]
            charge.append(lep_q)

        if charge[0]!=charge[1]:

            Energy=[]
            PT=[]
            PHI=[]
            ETA=[]
            for i in range(lep_n):

                lep_pt  = t.lep_pt [i]/1000.0
                lep_eta = t.lep_eta[i]
                lep_phi = t.lep_phi[i]
                lep_E = t.lep_E[i]/1000.0
                lep_q = t.lep_charge[i]

                Energy.append(lep_E)
                PT.append(lep_pt)
                PHI.append(lep_phi)
                ETA.append(lep_eta)

                h_pt .Fill(lep_pt)
                h_eta.Fill(lep_eta)
                h_phi.Fill(lep_phi)
                h_E.Fill(lep_E)
                h_q.Fill(lep_q)

            p1x=PT[0]*math.cos(PHI[0])*1000
            p1y=PT[0]*math.sin(PHI[0])*1000
            p1z=PT[0]*math.sinh(ETA[0])*1000

            p2x=PT[1]*math.cos(PHI[1])*1000
            p2y=PT[1]*math.sin(PHI[1])*1000
            p2z=PT[1]*math.sinh(ETA[1])*1000

            P=[p1x+p2x, p1y+p2y, p1z+p2z]
            P2=[P[0]*P[0], P[1]*P[1], P[2]*P[2]]
            P3=P2[0]+P2[1]+P2[2]
            E = (Energy[0]+Energy[1])*1000
            m=math.sqrt(E*E - P3 )/1000

            h_mass.Fill(m)
        else:
            print "charge",charge
            print "event no.", n

#------------------------------------------------#
h_num.Write()
h_pt. Write()
h_eta.Write()
h_phi.Write()
h_E.Write()
h_q.Write()
h_mass.Write()

output_file.Close()
##################################################
