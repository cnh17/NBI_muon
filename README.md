# Instructions
- Download small virtual box or ROOT software and data sets by clicking "download" on http://opendata.atlas.cern/index.php
- run Run.py to create histograms of the lepton properties of the decays in the data sets DataEgamma.root and DataMuons.root.
  - Specify use of mini;3
- Histogram of invariant mass refers to Z bosons

- Folder named DuplicateEventList contains lists of eventnumbers which are considered more than once in the analysis and so should not be considered.
- Folder named HiggsAnalysis contains csv files with event numbers that have two leptons decaying from a Z boson.
  - Zpairanalysis.py used to find event with two Z bosons produced in one decay
  - Higgsanalysis.py attempts to find Higgs invariant mass

# This is a LOG of my analysis steps made in the virtual box on my computer.
14/08/19
- First Commit : Working code for producing histogram of invariant mass.
- Run over all events : Now includes all 680760 events in tree mini;3.
- Cleaned up code : cleaner for loop in calculating momentum.

15/08/19
- Second Commit : histograms made for both e and muons so easier to run codes with different dominant lepton eg. just change source of data and leave the rest of the code.
  - Sources: DataMuons.root & DataEgamma.root

16/08/19
- Third Commit : Also considers missing transverse energy of neutrinos.

20/08/19
- Fourth commit : Contains analysis work on duplication of event numbers.

22/08/19
- Fifth commit : Finished analysis on duplication work. This commit contains four text files with the duplicate event numbers for both Egamma and Muons data sets and each TTree mini;3 and mini;4.

26/08/19
- Sixth commit : Includes code to make text files with the eventnumbers that produce lepton pairs

27/08/19
- Seventh commit: Includes work on finding Higgs particle mass
