import ROOT
import math
"""
Script to find potential Higgs particle from event no. 45441783
"""
input_path = "/home/atlas/ATLAS-DataAndTools/Input/Data/"
tree_name   = "mini;3"
t = ROOT.TChain(tree_name)
t.Add(input_path+"DataMuons.root")

num_events = t.GetEntries()
P_z1=[]
E_z1=[]
for n in range(num_events):
    t.GetEntry(n)
    eventnum = t.eventNumber
    lep_n = t.lep_n
    if eventnum ==45441783:
        px=[]
        py=[]
        pz=[]
        Energy=[]
        print "Muons = no. of vertices:", t.pvxp_n, "run number", t.runNumber, "no. of jets", t.jet_n
        for i in range(lep_n):
            lep_pt  = t.lep_pt [i]/1000
            lep_eta = t.lep_eta[i]
            lep_phi = t.lep_phi[i]
            lep_E = t.lep_E[i]/1000

            p_x=lep_pt*math.cos(lep_phi)
            p_y=lep_pt*math.sin(lep_phi)
            p_z=lep_pt*math.sinh(lep_eta)

            px.append(p_x)
            py.append(p_y)
            pz.append(p_z)
            Energy.append(lep_E)

        P=[px[0]+px[1], py[0]+py[1], pz[0]+pz[1]]
        E = Energy[0]+Energy[1]
        P_z1.append(P[0])
        P_z1.append(P[1])
        P_z1.append(P[2])
        E_z1.append(E)


t2 = ROOT.TChain(tree_name)
t2.Add(input_path+"DataEgamma.root")
num_events = t2.GetEntries()

P_z2=[]
E_z2=[]
for n in range(num_events):
    t2.GetEntry(n)
    eventnum = t2.eventNumber
    lep_n = t2.lep_n
    if eventnum ==45441783:
        px=[]
        py=[]
        pz=[]
        Energy=[]
        print "Egamma = no. of vertices:", t2.pvxp_n, "run number:", t2.runNumber, "no. of jets:", t2.jet_n
        for i in range(lep_n):
            lep_pt  = t2.lep_pt [i]/1000
            lep_eta = t2.lep_eta[i]
            lep_phi = t2.lep_phi[i]
            lep_E = t2.lep_E[i]/1000

            p_x=lep_pt*math.cos(lep_phi)
            p_y=lep_pt*math.sin(lep_phi)
            p_z=lep_pt*math.sinh(lep_eta)

            px.append(p_x)
            py.append(p_y)
            pz.append(p_z)
            Energy.append(lep_E)

        P=[px[0]+px[1], py[0]+py[1], pz[0]+pz[1]]
        E = Energy[0]+Energy[1]
        P_z2.append(P[0])
        P_z2.append(P[1])
        P_z2.append(P[2])
        E_z2.append(E)

P=[P_z1[0]+P_z2[0], P_z1[1]+P_z2[1], P_z1[2]+P_z2[2]]
print "Momentum",P
P1=P[0]*P[0] + P[1]*P[1] + P[2]*P[2]
E = E_z1[0]+E_z2[0]
print "Higgs Energy",E
m=math.sqrt(E*E - P1)
print "Higgs mass",m
