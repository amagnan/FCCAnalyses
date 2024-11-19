import numpy as np


ecm = 240
#Input directory where the files produced at the pre-selection level are
inputDir  = "/eos/user/a/amagnan/FCC/iDMprod/Analysis/stage2/"


outputDir  = "iDM/final/"

#Integrated luminosity for scaling number of events (required only if setting doScale to true)
if (ecm==365): intLumi = 3.e6 #pb^-1
if (ecm==240): intLumi = 10.8e6 #pb^-1

#Scale event yields by intLumi and cross section (optional)
doScale = True

saveTabular = False

processList = {
#    'p8_ee_ZZ_ecm%d'%ecm:{},
#    'p8_ee_WW_ecm%d'%ecm:{},
#    'wzp6_ee_eeH_ecm%d'%ecm:{},
#    'wzp6_ee_mumuH_ecm%d'%ecm:{},
#    'wzp6_ee_nunuH_ecm%d'%ecm:{},
#    'wzp6_ee_tautauH_ecm%d'%ecm:{},
#    'wzp6_ee_qqH_ecm%d'%ecm:{},
#    'wzp6_ee_ee_Mee_30_150_ecm%d'%ecm:{},
#    'wzp6_ee_mumu_ecm%d'%ecm:{},
#    'wzp6_ee_tautau_ecm%d'%ecm:{},
    'e%d_mH60_mA160_h2h2ll'%ecm:{},
    'e%d_mH60_mA160_h2h2llvv'%ecm:{},
    'e%d_mH80_mA130_h2h2ll'%ecm:{},
    'e%d_mH80_mA130_h2h2llvv'%ecm:{},
    'e%d_mH100_mA120_h2h2ll'%ecm:{},
    'e%d_mH100_mA120_h2h2llvv'%ecm:{},
#    'e%d_bp1_h2h2ll'%ecm:{},'e%d_bp1_h2h2llvv'%ecm:{},
#    'e%d_bp2_h2h2ll'%ecm:{},'e%d_bp2_h2h2llvv'%ecm:{},
    #'e%d_bp3_h2h2ll'%ecm:{},'e%d_bp3_h2h2llvv'%ecm:{},
    #'e%d_bp4_h2h2ll'%ecm:{},'e%d_bp4_h2h2llvv'%ecm:{},
    #'e%d_bp5_h2h2ll'%ecm:{},'e%d_bp5_h2h2llvv'%ecm:{},
#    'e%d_bp6_h2h2ll'%ecm:{},'e%d_bp6_h2h2llvv'%ecm:{},
    #'e%d_bp7_h2h2ll'%ecm:{},'e%d_bp7_h2h2llvv'%ecm:{},
#    'e%d_bp8_h2h2ll'%ecm:{},'e%d_bp8_h2h2llvv'%ecm:{},
    #'e%d_bp9_h2h2ll'%ecm:{},'e%d_bp9_h2h2llvv'%ecm:{},
    #'e%d_bp10_h2h2ll'%ecm:{},'e%d_bp10_h2h2llvv'%ecm:{},
    #'e%d_bp11_h2h2ll'%ecm:{},'e%d_bp11_h2h2llvv'%ecm:{},
    #'e%d_bp12_h2h2ll'%ecm:{},'e%d_bp12_h2h2llvv'%ecm:{},
    #'e%d_bp13_h2h2ll'%ecm:{},'e%d_bp13_h2h2llvv'%ecm:{},
    #'e%d_bp14_h2h2ll'%ecm:{},'e%d_bp14_h2h2llvv'%ecm:{},
#    'e%d_bp18_h2h2ll'%ecm:{},'e%d_bp18_h2h2llvv'%ecm:{},
    #'e%d_bp19_h2h2ll'%ecm:{},'e%d_bp19_h2h2llvv'%ecm:{},
    #'e%d_bp20_h2h2ll'%ecm:{},'e%d_bp20_h2h2llvv'%ecm:{},
}

data = np.loadtxt('input_arguments_check.txt', delimiter=',')

for mh,ma in data:
    processList.update({"e%d_mH%d_mA%d_h2h2ll"%(ecm,int(mh),int(ma)):{}})
    processList.update({"e%d_mH%d_mA%d_h2h2llvv"%(ecm,int(mh),int(ma)):{}})
    

if (ecm==365): processList.update({'p8_ee_tt_ecm%d'%ecm:{}})


#Link to the dictonary that contains all the cross section informations etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Add signals as it is not an offical process
# Open and read the JSON file
signal=open('FCCee_signal.txt', 'r')

procDictAdd=signal.readlines()


#Number of CPUs to use
nCPUS = 4

#produces ROOT TTrees, default is False
doTree = False

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
#ecm=240
if (ecm==240):
    cutList = {
#        "TwoLep":"n_electrons==2 || n_muons==2",
        "TwoEle":"n_electrons==2 && n_muons==0",
        "TwoElepz":"n_electrons==2 && n_muons==0 && TMath::Abs(Zcand_pz)<70",
        "TwoElem":"n_electrons==2 && n_muons==0 && Zcand_m<120 && TMath::Abs(Zcand_pz)<70",
        "TwoElemet":"n_electrons==2 && n_muons==0 && Zcand_m<120 && TMath::Abs(Zcand_pz)<70 && MET_pt[0]>5",
        "TwoMu":"n_electrons==0 && n_muons==2",
        "TwoMupz":"n_electrons==0 && n_muons==2 && TMath::Abs(Zcand_pz)<70",
        "TwoMum":"n_electrons==0 && n_muons==2 && Zcand_m<120 && TMath::Abs(Zcand_pz)<70",
        "TwoMumet":"n_electrons==0 && n_muons==2 && Zcand_m<120 && TMath::Abs(Zcand_pz)<70 && MET_pt[0]>5",
#        "TwoEle":"n_electrons==2 && n_muons==0 && Zcand_m<120 && TMath::Abs(Zcand_pz)<70 && MET_pt[0]>5",
#        "TwoEleVetoObj":"Zcand_m<120 && TMath::Abs(Zcand_pz)<70 && n_electrons==2 && n_muons==0 && n_seljets<1 && n_photons==0 && MET_pt[0]>5",
#        "TwoEleLepCuts":"Zcand_m<120 && TMath::Abs(Zcand_pz)<70 && n_electrons==2 && n_muons==0 && n_seljets<1 && n_photons==0 && MET_pt[0]>5 && lep1_pt<80 && lep2_pt<60",
#        "TwoElePoverE":"Zcand_m<120 && TMath::Abs(Zcand_pz)<70 && n_electrons==2 && n_muons==0 && n_seljets<1 && n_photons==0 && MET_pt[0]>5 && lep1_pt<80 && lep2_pt<60 && Zcand_povere>0.1",
#        "TwoMu":"n_electrons==0 && n_muons==2 && Zcand_m<120 && TMath::Abs(Zcand_pz)<70 && MET_pt[0]>5",
#        "TwoMuVetoObj":"Zcand_m<120 && TMath::Abs(Zcand_pz)<70 && n_electrons==0 && n_muons==2 && n_seljets<1 && n_photons==0 && MET_pt[0]>5",
#        "TwoMuLepCuts":"Zcand_m<120 && TMath::Abs(Zcand_pz)<70 && n_electrons==0 && n_muons==2 && n_seljets<1 && n_photons==0 && MET_pt[0]>5 && lep1_pt<80 && lep2_pt<60",
#        "TwoMuPoverE":"Zcand_m<120 && TMath::Abs(Zcand_pz)<70 && n_electrons==0 && n_muons==2 && n_seljets<1 && n_photons==0 && MET_pt[0]>5 && lep1_pt<80 && lep2_pt<60 && Zcand_povere>0.1",
    }
if (ecm==365):
    cutList = {
#        "TwoLep":"n_electrons==2 || n_muons==2",
        "TwoEle":"n_electrons==2 && n_muons==0",
        "TwoElepz":"n_electrons==2 && n_muons==0 && TMath::Abs(Zcand_pz)<140",
        "TwoElem":"n_electrons==2 && n_muons==0 && (Zcand_m<(-9.0/14.0 * abs(Zcand_pz) + 200)) && TMath::Abs(Zcand_pz)<140",
        "TwoElemet":"n_electrons==2 && n_muons==0 && (Zcand_m<(-9.0/14.0 * abs(Zcand_pz) + 200)) && TMath::Abs(Zcand_pz)<140 && MET_pt[0]>5",
        "TwoMu":"n_electrons==0 && n_muons==2",
        "TwoMupz":"n_electrons==0 && n_muons==2 && TMath::Abs(Zcand_pz)<140",
        "TwoMum":"n_electrons==0 && n_muons==2 && (Zcand_m<(-9.0/14.0 * abs(Zcand_pz) + 200)) && TMath::Abs(Zcand_pz)<140",
        "TwoMumet":"n_electrons==0 && n_muons==2 && (Zcand_m<(-9.0/14.0 * abs(Zcand_pz) + 200)) && TMath::Abs(Zcand_pz)<140 && MET_pt[0]>5",
#        "TwoEle":"n_electrons==2 && n_muons==0 && (Zcand_m<(-9.0/14.0 * abs(Zcand_pz) + 200)) && TMath::Abs(Zcand_pz)<140 && MET_pt[0]>5",
#        "TwoEleVetoObj":"n_electrons==2 && n_muons==0 && (Zcand_m<(-9.0/14.0 * abs(Zcand_pz) + 200)) && TMath::Abs(Zcand_pz)<140 && n_seljets<1 && n_photons==0 && MET_pt[0]>5",
#        "TwoEleLepCuts":"n_electrons==2 && n_muons==0 && (Zcand_m<(-9.0/14.0 * abs(Zcand_pz) + 200)) && TMath::Abs(Zcand_pz)<140 && n_seljets<1 && n_photons==0 && MET_pt[0]>5 && lep1_pt<140 && lep2_pt<80",
#        "TwoElePoverE":"n_electrons==2 && n_muons==0 && (Zcand_m<(-9.0/14.0 * abs(Zcand_pz) + 200)) && TMath::Abs(Zcand_pz)<140 && n_seljets<1 && n_photons==0 && MET_pt[0]>5 && lep1_pt<140 && lep2_pt<80 && Zcand_povere>0.1",
#        "TwoMu":"n_electrons==0 && n_muons==2 && (Zcand_m<(-9.0/14.0 * abs(Zcand_pz) + 200)) && TMath::Abs(Zcand_pz)<140 && MET_pt[0]>5",
#        "TwoMuVetoObj":"n_electrons==0 && n_muons==2 && (Zcand_m<(-9.0/14.0 * abs(Zcand_pz) + 200)) && TMath::Abs(Zcand_pz)<140 && n_seljets<1 && n_photons==0 && MET_pt[0]>5",
#        "TwoMuLepCuts":"n_electrons==0 && n_muons==2 && (Zcand_m<(-9.0/14.0 * abs(Zcand_pz) + 200)) && TMath::Abs(Zcand_pz)<140 && n_seljets<1 && n_photons==0 && MET_pt[0]>5 && lep1_pt<140 && lep2_pt<80",
#        "TwoMuPoverE":"n_electrons==0 && n_muons==2 && (Zcand_m<(-9.0/14.0 * abs(Zcand_pz) + 200)) && TMath::Abs(Zcand_pz)<140 && n_seljets<1 && n_photons==0 && MET_pt[0]>5 && lep1_pt<140 && lep2_pt<80 && Zcand_povere>0.1",
    }



#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {
#    "bdt_output_bp1":{"name":"bdt_output_bp1","title":"BDT output BP1","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp2":{"name":"bdt_output_bp2","title":"BDT output BP2","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp3":{"name":"bdt_output_bp3","title":"BDT output BP3","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp4":{"name":"bdt_output_bp4","title":"BDT output BP4","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp5":{"name":"bdt_output_bp5","title":"BDT output BP5","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp6":{"name":"bdt_output_bp6","title":"BDT output BP6","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp7":{"name":"bdt_output_bp7","title":"BDT output BP7","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp8":{"name":"bdt_output_bp8","title":"BDT output BP8","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp9":{"name":"bdt_output_bp9","title":"BDT output BP9","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp10":{"name":"bdt_output_bp10","title":"BDT output BP10","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp11":{"name":"bdt_output_bp11","title":"BDT output BP11","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp12":{"name":"bdt_output_bp12","title":"BDT output BP12","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp13":{"name":"bdt_output_bp13","title":"BDT output BP13","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp14":{"name":"bdt_output_bp14","title":"BDT output BP14","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp18":{"name":"bdt_output_bp18","title":"BDT output BP18","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp19":{"name":"bdt_output_bp19","title":"BDT output BP19","bin":100,"xmin":-1,"xmax":1},
#    "bdt_output_bp20":{"name":"bdt_output_bp20","title":"BDT output BP20","bin":100,"xmin":-1,"xmax":1},
    "n_seljets":{"name":"n_seljets","title":"Number of cleaned jets","bin":10,"xmin":0,"xmax":10},
    "n_photons":{"name":"n_photons","title":"Number of photons","bin":10,"xmin":0,"xmax":10},
#    "n_electrons":{"name":"n_electrons","title":"Number of electrons","bin":10,"xmin":0,"xmax":10},
#    "n_muons":{"name":"n_muons","title":"Number of muons","bin":10,"xmin":0,"xmax":10},
    "mZ":{"name":"Zcand_m","title":"m_{ll} [GeV]","bin":60,"xmin":0,"xmax":370},
    "mZzoom":{"name":"Zcand_m","title":"m_{ll} [GeV]","bin":60,"xmin":0,"xmax":120},
    "ptZ":{"name":"Zcand_pt","title":"p_{T}^{ll} [GeV]","bin":50,"xmin":0,"xmax":200},
    "mZrecoil":{"name":"Zcand_recoil_m","title":"Z recoil [GeV]","bin":50,"xmin":0,"xmax":370},
    "photon1_pt":{"name":"photon1_pt","title":"p_{T}^{photon1} [GeV]","bin":50,"xmin":-1,"xmax":200},
    "photon1_eta":{"name":"photon1_eta","title":"#eta^{photon1}","bin":50,"xmin":-5,"xmax":5},
    "photon1_e":{"name":"photon1_e","title":"E^{photon1} [GeV]","bin":60,"xmin":-1,"xmax":180},
    "lep1_pt":{"name":"lep1_pt","title":"p_{T}^{lep1} [GeV]","bin":50,"xmin":0,"xmax":200},
    "lep1_eta":{"name":"lep1_eta","title":"#eta^{lep1}","bin":50,"xmin":-5,"xmax":5},
    "lep1_e":{"name":"lep1_e","title":"E^{lep1} [GeV]","bin":60,"xmin":0,"xmax":180},
    "lep1_charge":{"name":"lep1_charge","title":"charge^{lep1}","bin":4,"xmin":-2,"xmax":2},
    "lep2_pt":{"name":"lep2_pt","title":"p_{T}^{lep2} [GeV]","bin":50,"xmin":0,"xmax":200},
    "lep2_eta":{"name":"lep2_eta","title":"#eta^{lep2}","bin":50,"xmin":-5,"xmax":5},
    "lep2_e":{"name":"lep2_e","title":"E^{lep2} [GeV]","bin":60,"xmin":0,"xmax":180},
    "lep2_charge":{"name":"lep2_charge","title":"charge^{lep2}","bin":4,"xmin":-2,"xmax":2},
    "lep_chargeprod":{"name":"lep_chargeprod","title":"charge^{lep1}*charge^{lep2}","bin":4,"xmin":-2,"xmax":2},
    "jet1_pt":{"name":"jet1_pt","title":"p_{T}^{jet1} [GeV]","bin":50,"xmin":-1,"xmax":200},
    "jet1_eta":{"name":"jet1_eta","title":"#eta^{jet1}","bin":50,"xmin":-5,"xmax":5},
    "jet1_e":{"name":"jet1_e","title":"E^{jet1} [GeV]","bin":60,"xmin":-1,"xmax":180},
    "jet2_pt":{"name":"jet2_pt","title":"p_{T}^{jet2} [GeV]","bin":30,"xmin":-1,"xmax":180},
    "jet2_eta":{"name":"jet2_eta","title":"#eta^{jet2}","bin":50,"xmin":-5,"xmax":5},
    "jet2_e":{"name":"jet2_e","title":"E^{jet2} [GeV]","bin":60,"xmin":-1,"xmax":180},
    "MET_e":{"name":"MET_e","title":"Emiss [GeV]","bin":50,"xmin":0,"xmax":370},
    "MET_pt":{"name":"MET_pt","title":"ETmiss [GeV]","bin":50,"xmin":0,"xmax":370},
    "pZ":{"name":"Zcand_p","title":"p^{ll} [GeV]","bin":50,"xmin":0,"xmax":300},
    "pzZ":{"name":"Zcand_pz","title":"p_{z}^{ll} [GeV]","bin":100,"xmin":-250,"xmax":250},
    "eZ":{"name":"Zcand_e","title":"E^{ll} [GeV]","bin":50,"xmin":0,"xmax":380},
    "povereZ":{"name":"Zcand_povere","title":"p^{ll}/E^{ll}","bin":50,"xmin":0,"xmax":1.5},
    "costhetaZ":{"name":"Zcand_costheta","title":"cos#theta^{ll}","bin":50,"xmin":-1,"xmax":1},
    "cosThetaStar":{"name":"cosThetaStar","title":"cos#theta_{l}^{*}","bin":50,"xmin":-1,"xmax":1},
    "cosThetaR":{"name":"cosThetaR","title":"cos#theta_{R}","bin":50,"xmin":-1,"xmax":1},
    "cosDphiLep":{"name":"cosDphiLep","title":"cos#Delta#phi(ll)","bin":50,"xmin":-1,"xmax":1},
    "pzZ_mZ_2D":{"cols":["Zcand_pz", "Zcand_m"],"title":"p_{z}^{ll} - m^{ll} [GeV]", "bins": [(100,-300,300), (100,0,380)]}, # 2D histogram
}
