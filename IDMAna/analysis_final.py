#Input directory where the files produced at the pre-selection level are
inputDir  = "iDM/stage2/"


outputDir  = "iDM/final/"

#Integrated luminosity for scaling number of events (required only if setting doScale to true)
#intLumi = 5e6 #pb^-1

#Scale event yields by intLumi and cross section (optional)
#doScale = True

processList = {
    'p8_ee_ZZ_ecm240':{},
    'p8_ee_WW_ecm240':{},
    'wzp6_ee_eeH_ecm240':{},
    'wzp6_ee_mumuH_ecm240':{},
    'wzp6_ee_nunuH_ecm240':{},
    'wzp6_ee_tautauH_ecm240':{},
    'wzp6_ee_qqH_ecm240':{},
    'wzp6_ee_ee_Mee_30_150_ecm240':{},
    'wzp6_ee_mumu_ecm240':{},
    'wzp6_ee_tautau_ecm240':{},
    'Delphes_EDM4HEPevents_e240_bp1':{},
    'Delphes_EDM4HEPevents_e240_bp2':{}
}

#Link to the dictonary that contains all the cross section informations etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Add signals as it is not an offical process
procDictAdd={
    "Delphes_EDM4HEPevents_e240_bp1":{"numberOfEvents": 500000, "sumOfWeights": 500000, "crossSection": 0.0069, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "Delphes_EDM4HEPevents_e240_bp2":{"numberOfEvents": 500000, "sumOfWeights": 500000, "crossSection": 0.005895, "kfactor": 1.0, "matchingEfficiency": 1.0}
}

#Number of CPUs to use
nCPUS = 4

#produces ROOT TTrees, default is False
doTree = False

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    "TwoEle":"n_electrons==2 && n_muons==0",
    "TwoEleVetoObj":"n_electrons==2 && n_muons==0 && n_seljets<1 && n_photons==0",
    "TwoEleMET10":"n_electrons==2 && n_muons==0 && n_seljets<1 && n_photons==0 && MET_pt[0]>10",
    "TwoMu":"n_electrons==0 && n_muons==2",
    "TwoMuVetoObj":"n_electrons==0 && n_muons==2 && n_seljets<1 && n_photons==0",
    "TwoMuMET10":"n_electrons==0 && n_muons==2 && n_seljets<1 && n_photons==0 && MET_pt[0]>10",
}


#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {
    "n_seljets":{"name":"n_seljets","title":"Number of cleaned jets","bin":10,"xmin":0,"xmax":10},
    "n_jets":{"name":"n_jets","title":"Number of all jets","bin":10,"xmin":0,"xmax":10},
    "n_photons":{"name":"n_photons","title":"Number of photons","bin":10,"xmin":0,"xmax":10},
    "n_electrons":{"name":"n_electrons","title":"Number of electrons","bin":10,"xmin":0,"xmax":10},
    "n_muons":{"name":"n_muons","title":"Number of muons","bin":10,"xmin":0,"xmax":10},
    "mZ":{"name":"Zcand_m","title":"m_{Z} [GeV]","bin":60,"xmin":0,"xmax":240},
    "ptZ":{"name":"Zcand_pt","title":"p_{T}^{Z} [GeV]","bin":50,"xmin":0,"xmax":150},
    "mZrecoil":{"name":"Zcand_recoil_m","title":"Z recoil [GeV]","bin":50,"xmin":0,"xmax":250},
    "lep1_pt":{"name":"lep1_pt","title":"p_{T}^{lep1} [GeV]","bin":50,"xmin":0,"xmax":200},
    "lep1_eta":{"name":"lep1_eta","title":"#eta^{lep1}","bin":50,"xmin":-5,"xmax":5},
    "lep2_pt":{"name":"lep2_pt","title":"p_{T}^{lep2} [GeV]","bin":50,"xmin":0,"xmax":200},
    "lep2_eta":{"name":"lep2_eta","title":"#eta^{lep2}","bin":50,"xmin":-5,"xmax":5},
    "jet1_pt":{"name":"jet1_pt","title":"p_{T}^{jet1} [GeV]","bin":50,"xmin":0,"xmax":200},
    "jet1_eta":{"name":"jet1_eta","title":"#eta^{jet1}","bin":50,"xmin":-5,"xmax":5},
    "jet2_pt":{"name":"jet2_pt","title":"p_{T}^{jet2} [GeV]","bin":30,"xmin":0,"xmax":120},
    "jet2_eta":{"name":"jet2_eta","title":"#eta^{jet2}","bin":50,"xmin":-5,"xmax":5},
    "MET_e":{"name":"MET_e","title":"Emiss [GeV]","bin":50,"xmin":0,"xmax":250},
    "MET_pt":{"name":"MET_pt","title":"ETmiss [GeV]","bin":50,"xmin":0,"xmax":250},
    "pZ":{"name":"Zcand_p","title":"p^{Z} [GeV]","bin":50,"xmin":-200,"xmax":200},
    "pzZ":{"name":"Zcand_pz","title":"p_{z}^{Z} [GeV]","bin":100,"xmin":-200,"xmax":200},
    "eZ":{"name":"Zcand_e","title":"E^{Z} [GeV]","bin":50,"xmin":0,"xmax":250},
    "povereZ":{"name":"Zcand_povere","title":"p^{Z}/E^{Z}","bin":50,"xmin":-2,"xmax":2},
    "costhetaZ":{"name":"Zcand_costheta","title":"cos#theta^{Z}","bin":50,"xmin":-1,"xmax":1},
    "cosDphiLep":{"name":"cosDphiLep","title":"cos#Delta#phi(ll)","bin":50,"xmin":-1,"xmax":1},
    "pzZ_mZ_2D":{"cols":["Zcand_pz", "Zcand_m"],"title":"p_{z}^{Z} - m^{Z} [GeV]", "bins": [(100,-200,200), (100,0,250)]}, # 2D histogram
}
