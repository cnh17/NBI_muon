import ROOT
import math

input_files = "/home/atlas/ATLAS-DataAndTools/Input/Data/DataMuons.root"
max_events = -1 #insert negative number to run all events
#------------------------------------------------#
f = ROOT.TFile(input_files)
t = f.Get("mini;3")   #tree specification
print "tree", t

num_events = t.GetEntries()
print "num events", num_events

if max_events < 0:
   max_events = num_events

output_file = ROOT.TFile("output3.root","RECREATE")
#------------------------------------------------# Histograms
h_num    = ROOT.TH1F("h_num","",1000,-0.5,4.5)
h_pt_mu  = ROOT.TH1F("h_pt_mu", "Transverse Momentum of Muons",100, 0.0,100.0)
h_eta_mu = ROOT.TH1F("h_eta_mu","Pseudorapidity of Muons",100,-5.0,  5.0)
h_phi_mu = ROOT.TH1F("h_phi_mu","Azimuthal Angle of Muons",100,-3.2,  3.2)
h_E_mu   = ROOT.TH1F("h_E_mu","Energy of Muons",100, -0.5, 300.0)
h_q_mu   = ROOT.TH1F("h_q_mu","Charge of Muons",196,-1.5, 1.5)
h_mass_mu= ROOT.TH1F("h_mass_mu","Invariant mass (muon)",1000, -0.5, 150)
h_cut_mu = ROOT.TH1F("h_cut_mu", "Cuts (muon)", 10000, -0.5, 3.5)
h_type   = ROOT.TH1F("h_type", "Lepton Type", 100, -0.5, 50)
#------------------------------------------------#
h_pt_e  = ROOT.TH1F("h_pt_e", "Transverse Momentum of Electrons",100, 0.0,100.0)
h_eta_e = ROOT.TH1F("h_eta_e","Pseudorapidity of Electrons",100,-5.0,  5.0)
h_phi_e = ROOT.TH1F("h_phi_e","Azimuthal Angle of Electrons",100,-3.2,  3.2)
h_E_e   = ROOT.TH1F("h_E_e","Energy of Electrons",100, -0.5, 300.0)
h_q_e   = ROOT.TH1F("h_q_e","Charge of Electrons",196,-1.5, 1.5)
h_mass_e= ROOT.TH1F("h_mass_e","Invariant mass (e)",1000, -0.5, 150)
h_cut_e = ROOT.TH1F("h_cut_e", "Cuts (e)", 10000, -0.5, 3.5)

#-----------------------------------------------#

for n in range(max_events):

    t.GetEntry(n)

    if (n % 100000) == 0:
        print "processing event...", n

    lep_n = t.lep_n
    h_cut_mu.Fill(0.0) #all lepton events
    h_cut_e.Fill(0.0)
    h_num.Fill(lep_n)

    typ=[]
    for i in range(lep_n):
        lep_type = t.lep_type[i]
        h_type.Fill(lep_type)
        typ.append(lep_type)

    charge=[]
    for i in range(lep_n):
        lep_q = t.lep_charge[i]
        charge.append(lep_q)

    if typ==[13,13]:
        h_cut_mu.Fill(1.0)

        charge=[]
        for i in range(lep_n):
            lep_q = t.lep_charge[i]
            charge.append(lep_q)

        if charge[0]!=charge[1]:
            px=[]
            py=[]
            pz=[]
            Energy=[]
            for i in range(lep_n):

                lep_pt  = t.lep_pt [i]/1000
                lep_eta = t.lep_eta[i]
                lep_phi = t.lep_phi[i]
                lep_E = t.lep_E[i]/1000
                lep_q = t.lep_charge[i]

                h_pt_mu .Fill(lep_pt)
                h_eta_mu.Fill(lep_eta)
                h_phi_mu.Fill(lep_phi)
                h_E_mu.Fill(lep_E)
                h_q_mu.Fill(lep_q)

                p_x=lep_pt*math.cos(lep_phi)
                p_y=lep_pt*math.sin(lep_phi)
                p_z=lep_pt*math.sinh(lep_eta)

                px.append(p_x)
                py.append(p_y)
                pz.append(p_z)
                Energy.append(lep_E)

            P=[px[0]+px[1], py[0]+py[1], pz[0]+pz[1]]
            P1=P[0]*P[0] + P[1]*P[1] + P[2]*P[2]
            E = Energy[0]+Energy[1]
            m=math.sqrt(E*E - P1)

            h_mass_mu.Fill(m)
            h_cut_mu.Fill(2.0) #only oppositely charged muon pairs

    elif typ==[11,11]:
        h_cut_e.Fill(1.0)

        charge=[]
        for i in range(lep_n):
            lep_q = t.lep_charge[i]
            charge.append(lep_q)

        if charge[0]!=charge[1]:
            px=[]
            py=[]
            pz=[]
            Energy=[]
            for i in range(lep_n):

                lep_pt  = t.lep_pt [i]/1000
                lep_eta = t.lep_eta[i]
                lep_phi = t.lep_phi[i]
                lep_E = t.lep_E[i]/1000
                lep_q = t.lep_charge[i]

                h_pt_e.Fill(lep_pt)
                h_eta_e.Fill(lep_eta)
                h_phi_e.Fill(lep_phi)
                h_E_e.Fill(lep_E)
                h_q_e.Fill(lep_q)

                p_x=lep_pt*math.cos(lep_phi)
                p_y=lep_pt*math.sin(lep_phi)
                p_z=lep_pt*math.sinh(lep_eta)

                px.append(p_x)
                py.append(p_y)
                pz.append(p_z)
                Energy.append(lep_E)

            P=[px[0]+px[1], py[0]+py[1], pz[0]+pz[1]]
            P1=P[0]*P[0] + P[1]*P[1] + P[2]*P[2]
            E = Energy[0]+Energy[1]
            m=math.sqrt(E*E - P1)

            h_mass_e.Fill(m)
            h_cut_e.Fill(2.0) #only oppositely charged electron pairs
#------------------------------------------------#
h_num.Write()
h_pt_mu. Write()
h_eta_mu.Write()
h_phi_mu.Write()
h_E_mu.Write()
h_q_mu.Write()
h_mass_mu.Write()
h_cut_mu.Write()
h_type.Write()

h_pt_e. Write()
h_eta_e.Write()
h_phi_e.Write()
h_E_e.Write()
h_q_e.Write()
h_mass_e.Write()
h_cut_e.Write()

output_file.Close()
##################################################
