processList = {
    #'p8_ee_ZZ_ecm240':{},
    #'p8_ee_WW_ecm240':{},
    #'p8_ee_ZH_ecm240':{},
    'Delphes_EDM4HEPevents_e240_bp1':{},
    'Delphes_EDM4HEPevents_e240_bp2':{}
    #'p8_ee_ZH_ecm240_out':{'output':'MySample_p8_ee_ZH_ecm240'} #Run over the full statistics from stage1 input file <inputDir>/p8_ee_ZH_ecm240_out.root. Change the output name to MySample_p8_ee_ZH_ecm240
}

#Mandatory: input directory when not running over centrally produced edm4hep events. 
#It can still be edm4hep files produced standalone or files from a first analysis step (this is the case in this example it runs over the files produced from analysis.py)
inputDir  = "iDM/stage1/"

#Optional: output directory, default is local dir
outputDir   = "iDM/stage2/"

#Optional: ncpus, default is 4
nCPUS       = 4

#Optional running on HTCondor, default is False
runBatch    = False

##USER DEFINED CODE
#import ROOT
#ROOT.gInterpreter.Declare("""
#bool myFilter(ROOT::VecOps::RVec<float> mass) {
#    for (size_t i = 0; i < mass.size(); ++i) {
#        if (mass.at(i)>80. && mass.at(i)<100.)
#            return true;
#    }
#    return false;
#}
#""")
##END USER DEFINED CODE

#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():

    #__________________________________________________________
    #Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):
        df2 = (df
               .Filter("zed_mumu_m.size()==1 || zed_ee_m.size()==1")
               .Define("Zcand_m","if (zed_mumu_m.size()==1) return zed_mumu_m.at(0); else if (zed_ee_m.size()==1) return zed_ee_m.at(0); else return float(-1);")
               .Define("Zcand_pt","if (zed_mumu_pt.size()==1) return zed_mumu_pt.at(0); else if (zed_ee_pt.size()==1) return zed_ee_pt.at(0); else return float(-1);")
               .Define("Zcand_pz","if (zed_mumu_pz.size()==1) return zed_mumu_pz.at(0); else if (zed_ee_pz.size()==1) return zed_ee_pz.at(0); else return float(-1000);")
               .Define("Zcand_p","if (zed_mumu_p.size()==1) return zed_mumu_p.at(0); else if (zed_ee_p.size()==1) return zed_ee_p.at(0); else return float(-1);")
               .Define("Zcand_e","return sqrt(pow(Zcand_m,2)+pow(Zcand_p,2));")
               .Define("Zcand_povere","return Zcand_p/Zcand_e;")
               .Define("Zcand_costheta","if (zed_mumu_theta.size()==1) return TMath::Cos(zed_mumu_theta.at(0)); else if (zed_ee_theta.size()==1) return TMath::Cos(zed_ee_theta.at(0)); else return double(-1.1);")
               .Define("Zcand_recoil_m","if (zed_mumu_recoil_m.size()==1) return zed_mumu_recoil_m.at(0); else if (zed_ee_recoil_m.size()==1) return zed_ee_recoil_m.at(0); else return float(-1);")
               .Define("lep1_pt","if (selected_muons_pt.size()>=2) return selected_muons_pt.at(0); else if (selected_electrons_pt.size()>=2) return selected_electrons_pt.at(0); else return float(-1);")
               .Define("lep2_pt","if (selected_muons_pt.size()>=2) return selected_muons_pt.at(1); else if (selected_electrons_pt.size()>=2) return selected_electrons_pt.at(1); else return float(-1);")
               .Define("lep1_eta","if (selected_muons_eta.size()>=2) return selected_muons_eta.at(0); else if (selected_electrons_eta.size()>=2) return selected_electrons_eta.at(0); else return float(-5);")
               .Define("lep2_eta","if (selected_muons_eta.size()>=2) return selected_muons_eta.at(1); else if (selected_electrons_eta.size()>=2) return selected_electrons_eta.at(1); else return float(-5);")
               .Define("cosDphiLep","if (selected_muons_eta.size()>=2) return TMath::Cos(selected_muons_phi.at(0)-selected_muons_phi.at(1)); else if (selected_electrons_eta.size()>=2) return TMath::Cos(selected_electrons_phi.at(0)-selected_electrons_phi.at(1)); else return double(-1.1);")
               .Define("jet1_pt","if (seljet_pt.size()>=1) return seljet_pt.at(0); else return float(-1.);")
               .Define("jet1_eta","if (seljet_eta.size()>=1) return seljet_eta.at(0); else return float(-5.);")
               .Define("jet2_pt","if (seljet_pt.size()>=2) return seljet_pt.at(1); else return float(-1.);")
               .Define("jet2_eta","if (seljet_eta.size()>=2) return seljet_eta.at(1); else return float(-5.);")
               .Define("n_seljets","return seljet_pt.size()")

               #Gen info
               .Define("FSGen_ll_pt","if (n_FSGenElectron>1) return FSGen_ee_pt; else if (n_FSGenMuon>1) return FSGen_mm_pt; else return float(-1);") 
               .Define("FSGen_ll_mass","if (n_FSGenElectron>1) return FSGen_ee_invMass; else if (n_FSGenMuon>1) return FSGen_mm_invMass; else return float(-1);") 


               #Define new var rdf entry (example)
               #.Define("entry", "rdfentry_")
               #Define a weight based on entry (inline example of possible operations)
               #.Define("weight", "return 1./(entry+1)")
               #Define a variable based on a custom filter
               #.Define("MyFilter", "myFilter(zed_leptonic_m)")
               )
        return df2

    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list.
    def output():
        branchList = [
            "Zcand_m",
            "Zcand_pt",
            "Zcand_pz",
            "Zcand_p",
            "Zcand_povere",
            "Zcand_e",
            "Zcand_costheta",
            "Zcand_recoil_m",
            "lep1_pt","lep1_eta",
            "lep2_pt","lep2_eta",
            "jet1_pt","jet1_eta",
            "jet2_pt","jet2_eta",
            "cosDphiLep",
            "n_GenH","FSGen_ll_pt","FSGen_ll_mass",
            "n_jets","n_seljets",
            "MET_e","MET_pt","MET_eta","MET_phi",
            "n_photons","n_muons","n_electrons"

        ]
        return branchList




