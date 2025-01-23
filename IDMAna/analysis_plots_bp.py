import ROOT
ecm = 365

# global parameters
#already applied in final stage
intLumi        = 1 #5.0e+06 #in pb-1
if (ecm==365): intLumiLabel = "L = 3 ab^{-1}" #pb^-1
if (ecm==240): intLumiLabel = "L = 10.8 ab^{-1}" #pb^-1
ana_tex        = 'e^{+}e^{-} #rightarrow l^{+}l^{-} + E^{miss}'
delphesVersion = '3.4.2'
energy         = ecm
collider       = 'FCC-ee'
inputDir       = 'iDM/final/'
formats        = ['png','pdf']
yaxis          = ['lin','log']
stacksig       = ['nostack']
outdir         = 'iDM/plots_%d/'%(ecm)
plotStatUnc    = True

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
scaleSig       = 1.
#scaleBack      = 0.
#splitLeg       = True
legendCoord = [0.55,0.45,0.92,0.9]

#variables = ['mZzoom']

variables = ['n_seljets','n_photons',
             'mZ','mZzoom','ptZ','mZrecoil',
             'photon1_pt','photon1_eta','photon1_e',
             'lep1_pt','lep1_eta','lep1_e','lep1_charge',
             'lep2_pt','lep2_eta','lep2_e','lep2_charge',
             'lep_chargeprod',
             'jet1_pt','jet1_eta','jet1_e',
             'MET_e','MET_pt',
             'pZ','pzZ','eZ','povereZ','costhetaZ',
             'cosDphiLep','cosThetaStar','cosThetaR',
             #'bdt_output_bp1','bdt_output_bp2','bdt_output_bp3','bdt_output_bp4',
             #'bdt_output_bp5','bdt_output_bp6','bdt_output_bp7','bdt_output_bp8',
             #'bdt_output_bp9','bdt_output_bp10','bdt_output_bp11','bdt_output_bp12',
             #'bdt_output_bp13','bdt_output_bp14','bdt_output_bp18','bdt_output_bp19',
             #'bdt_output_bp20'
]

#rebin = [1]
rebin = [1,1,
         1,1,1,1,
         1,1,1,
         1,1,1,1,
         1,1,1,1,
         1,
         1,1,1,
         1,1,
         1,1,1,1,1,
         1,1,1,
         #5,1,1,1,
         #1,1,1,1,
         #1,1,1,1,
         #1,1,1,1,
         #1
         ] # uniform rebin per variable (optional)

###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['Zee']   = ["TwoEle","TwoEleVetoObj","TwoEleLepCuts","TwoElePoverE"]
selections['Zmumu']   = ["TwoMu","TwoMuVetoObj","TwoMuLepCuts","TwoMuPoverE"]
#selections['Zmumu']   = ["TwoMuPoverE"]

extralabel = {}
#if (ecm==240): extralabel['TwoEle'] = "Selection: N_{e} = 2, |p_{z}^{ee}|<70 GeV, M_{ee}<120 GeV, E_{T}^{miss}>5 GeV"
#if (ecm==365): extralabel['TwoEle'] = "Selection: N_{e} = 2, |p_{z}^{ee}|<140 GeV, M_{ee}<(-9.0/14.0 * |p_{z}^{ee}| + 200), E_{T}^{miss}>5 GeV"
#extralabel['TwoEleVetoObj'] = "Selection: N_{e} = 2, N_{jet}<1, no other lep or #gamma"
#extralabel['TwoEleLepCuts'] = "Selection: N_{e} = 2, p^{e}_{T}<80,60 GeV"
#extralabel['TwoElePoverE'] = "Selection: N_{e} = 2, p(ee)/E(ee)>0.1"
#if (ecm==240): extralabel['TwoMu'] = "Selection: N_{#mu} = 2,  |p_{z}^{#mu#mu}|<70 GeV, M_{#mu#mu}<120 GeV, E_{T}^{miss}>5 GeV"
#if (ecm==365): extralabel['TwoMu'] = "Selection: N_{#mu} = 2,  |p_{z}^{#mu#mu}|<140 GeV, M_{#mu#mu}<<(-9.0/14.0 * |p_{z}^{#mu#mu}| + 200), E_{T}^{miss}>5 GeV"
#extralabel['TwoMuVetoObj'] = "Selection: N_{#mu} = 2, N_{jet}<1, no other lep or #gamma"
#extralabel['TwoMuLepCuts'] = "Selection: N_{#mu} = 2, p^{#mu}_{T}<80,60 GeV"
#extralabel['TwoMuPoverE'] = "Selection: N_{#mu} = 2, p(#mu#mu)/E(#mu#mu)>0.1"
if (ecm==240): extralabel['TwoEle'] = "Selection: N_{e} = 2, presel"
if (ecm==365): extralabel['TwoEle'] = "Selection: N_{e} = 2, presel"
extralabel['TwoEleVetoObj'] = "Selection: N_{e} = 2, no other obj"
if (ecm==240): extralabel['TwoEleLepCuts'] = "Selection: N_{e} = 2, p^{e}_{T}<80,60 GeV"
if (ecm==365): extralabel['TwoEleLepCuts'] = "Selection: N_{e} = 2, p^{e}_{T}<140,80 GeV"
extralabel['TwoElePoverE'] = "Selection: N_{e} = 2, p(ee)/E(ee)>0.1"
if (ecm==240): extralabel['TwoMu'] = "Selection: N_{#mu} = 2, presel"
if (ecm==365): extralabel['TwoMu'] = "Selection: N_{#mu} = 2, presel"
extralabel['TwoMuVetoObj'] = "Selection: N_{#mu} = 2, no other obj"
if (ecm==240): extralabel['TwoMuLepCuts'] = "Selection: N_{#mu} = 2, p^{#mu}_{T}<80,60 GeV"
if (ecm==365): extralabel['TwoMuLepCuts'] = "Selection: N_{#mu} = 2, p^{#mu}_{T}<140,80 GeV"
extralabel['TwoMuPoverE'] = "Selection: N_{#mu} = 2, p(#mu#mu)/E(#mu#mu)>0.1"


colors = {}
colors['nunuH'] = ROOT.kRed
colors['ffH'] = ROOT.kRed+2
#colors['mumuH'] = ROOT.kRed+4
#colors['tautauH'] = ROOT.kRed-2
#colors['qqH'] = ROOT.kRed-4
colors['eem30'] = ROOT.kViolet
colors['tautau'] = ROOT.kViolet-1
colors['mumu'] = ROOT.kViolet+1
colors['WW'] = ROOT.kBlue+1
colors['ZZ'] = ROOT.kGreen+2
colors['iDM1'] = ROOT.kBlack
colors['iDM2'] = ROOT.kGray+1
colors['iDM3'] = ROOT.kGray
#colors['iDM8'] = ROOT.kGray

plots = {}
plots['Zee'] = {
    'signal':{
        'iDM1':['e%d_mH60_mA160_h2h2ll'%(ecm),'e%d_mH60_mA160_h2h2llvv'%(ecm)],
        'iDM2':['e%d_mH80_mA130_h2h2ll'%(ecm),'e%d_mH80_mA130_h2h2llvv'%(ecm)],
        'iDM3':['e%d_mH100_mA120_h2h2ll'%(ecm),'e%d_mH100_mA120_h2h2llvv'%(ecm)],
#        'iDM1':['e%d_bp1_h2h2ll'%(ecm),'e%d_bp1_h2h2llvv'%(ecm)],
#        'iDM2':['e%d_bp2_h2h2ll'%(ecm),'e%d_bp2_h2h2llvv'%(ecm)],
#        'iDM6':['e%d_bp6_h2h2ll'%(ecm),'e%d_bp6_h2h2llvv'%(ecm)],
#        'iDM8':['e%d_bp8_h2h2ll'%(ecm),'e%d_bp8_h2h2llvv'%(ecm)],
    },
    'backgrounds':{
        'eem30':['wzp6_ee_ee_Mee_30_150_ecm%d'%(ecm)],
        #'mumu':['wzp6_ee_mumu_ecm%d'%(ecm)],
        'tautau':['wzp6_ee_tautau_ecm%d'%(ecm)],
        'WW':['p8_ee_WW_ecm%d'%(ecm)],
        'ZZ':['p8_ee_ZZ_ecm%d'%(ecm)],
        'ffH':['wzp6_ee_eeH_ecm%d'%(ecm),'wzp6_ee_mumuH_ecm%d'%(ecm),'wzp6_ee_tautauH_ecm%d'%(ecm),'wzp6_ee_qqH_ecm%d'%(ecm)],
        #'mumuH':['wzp6_ee_mumuH_ecm%d'%(ecm)],
        #'tautauH':['wzp6_ee_tautauH_ecm%d'%(ecm)],
        #'qqH':['wzp6_ee_qqH_ecm%d'%(ecm)],
        'nunuH':['wzp6_ee_nunuH_ecm%d'%(ecm)],
    }
}
plots['Zmumu'] = {
    'signal':{
        'iDM1':['e%d_mH60_mA160_h2h2ll'%(ecm),'e%d_mH60_mA160_h2h2llvv'%(ecm)],
        'iDM2':['e%d_mH80_mA130_h2h2ll'%(ecm),'e%d_mH80_mA130_h2h2llvv'%(ecm)],
        'iDM3':['e%d_mH100_mA120_h2h2ll'%(ecm),'e%d_mH100_mA120_h2h2llvv'%(ecm)],
#        'iDM1':['e%d_bp1_h2h2ll'%(ecm),'e%d_bp1_h2h2llvv'%(ecm)],
#        'iDM2':['e%d_bp2_h2h2ll'%(ecm),'e%d_bp2_h2h2llvv'%(ecm)],
#        'iDM6':['e%d_bp6_h2h2ll'%(ecm),'e%d_bp6_h2h2llvv'%(ecm)],
#        'iDM8':['e%d_bp8_h2h2ll'%(ecm),'e%d_bp8_h2h2llvv'%(ecm)],
    },
    'backgrounds':{
        #'eem30':['wzp6_ee_ee_Mee_30_150_ecm%d'%(ecm)],
        'mumu':['wzp6_ee_mumu_ecm%d'%(ecm)],
        'tautau':['wzp6_ee_tautau_ecm%d'%(ecm)],
        'WW':['p8_ee_WW_ecm%d'%(ecm)],
        'ZZ':['p8_ee_ZZ_ecm%d'%(ecm)],
        'ffH':['wzp6_ee_eeH_ecm%d'%(ecm),'wzp6_ee_mumuH_ecm%d'%(ecm),'wzp6_ee_tautauH_ecm%d'%(ecm),'wzp6_ee_qqH_ecm%d'%(ecm)],
        #'mumuH':['wzp6_ee_mumuH_ecm%d'%(ecm)],
        #'tautauH':['wzp6_ee_tautauH_ecm%d'%(ecm)],
        #'qqH':['wzp6_ee_qqH_ecm%d'%(ecm)],
        'nunuH':['wzp6_ee_nunuH_ecm%d'%(ecm)],
    }
}
#plots['Zmumu'] = plots['Zee']

legend = {}
legend['nunuH'] = '#nu#nuH'
legend['ffH'] = 'llH+qqH'
#legend['mumuH'] = '#mu#muH'
#legend['tautauH'] = '#tau#tauH'
#legend['qqH'] = 'qqH'
legend['eem30'] = 'ee30-150GeV'
legend['mumu'] = '#mu#mu'
legend['tautau'] = '#tau#tau'
legend['WW'] = 'WW'
legend['ZZ'] = 'ZZ'
legend['iDM1'] = 'iDM mH60-mA160'
legend['iDM2'] = 'iDM mH80-mA130'
legend['iDM3'] = 'iDM mH100-mA120'
#legend['iDM8'] = 'iDM BP8'
