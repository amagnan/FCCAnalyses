import ROOT

# global parameters
intLumi        = 5.0e+06 #in pb-1
ana_tex        = 'e^{+}e^{-} #rightarrow l^{+}l^{-} + H + H'
delphesVersion = '3.4.2'
energy         = 240.0
collider       = 'FCC-ee'
inputDir       = 'iDM/final/'
formats        = ['png','pdf']
yaxis          = ['lin','log']
stacksig       = ['nostack']
outdir         = 'iDM/plots/'
plotStatUnc    = True

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
scaleSig       = 1.
#scaleBack      = 0.
#splitLeg       = True

variables = ['n_seljets','n_jets','n_photons',
             'mZ','ptZ','mZrecoil',
             'lep1_pt','lep1_eta',
             'lep2_pt','lep2_eta',
             'jet1_pt','jet1_eta',
             'MET_e','MET_pt',
             'pZ','pzZ','eZ','povereZ','costhetaZ',
             'cosDphiLep']

rebin = [1,1,1,
         1,1,1,
         1,1,
         1,1,
         1,1,
         1,1,
         1,1,1,1,1,
         1] # uniform rebin per variable (optional)

###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['Zee']   = ["TwoEle","TwoEleVetoObj","TwoEleMET10"]
selections['Zmumu']   = ["TwoMu","TwoMuVetoObj","TwoMuMET10"]

extralabel = {}
extralabel['TwoEle'] = "Selection: N_{e} = 2"
extralabel['TwoEleVetoObj'] = "Selection: N_{e} = 2, N_{jet}<1, no other lep or #gamma"
extralabel['TwoEleMET10'] = "Selection: N_{e} = 2, N_{jet}<1, no other lep or #gamma, E_{T}^{miss} > 10 GeV"
extralabel['TwoMu'] = "Selection: N_{#mu} = 2"
extralabel['TwoMuVetoObj'] = "Selection: N_{#mu} = 2, N_{jet}<1, no other lep or #gamma"
extralabel['TwoMuMET10'] = "Selection: N_{#mu} = 2, N_{jet}<1, no other lep or #gamma, E_{T}^{miss} > 10 GeV"

colors = {}
colors['nunuH'] = ROOT.kRed
colors['eeH'] = ROOT.kRed+2
colors['mumuH'] = ROOT.kRed+4
colors['tautauH'] = ROOT.kRed-2
colors['qqH'] = ROOT.kRed-4
colors['eem30'] = ROOT.kViolet
colors['tautau'] = ROOT.kViolet-1
colors['mumu'] = ROOT.kViolet+1
colors['WW'] = ROOT.kBlue+1
colors['ZZ'] = ROOT.kGreen+2
colors['iDM1'] = ROOT.kBlack
colors['iDM2'] = ROOT.kGray+1

plots = {}
plots['Zee'] = {
    'signal':{
        'iDM1':['Delphes_EDM4HEPevents_e240_bp1'],
        'iDM2':['Delphes_EDM4HEPevents_e240_bp2']
    },
    'backgrounds':{
        'eem30':['wzp6_ee_ee_Mee_30_150_ecm240'],
        'mumu':['wzp6_ee_mumu_ecm240'],
        'tautau':['wzp6_ee_tautau_ecm240'],
        'WW':['p8_ee_WW_ecm240'],
        'ZZ':['p8_ee_ZZ_ecm240'],
        'eeH':['wzp6_ee_eeH_ecm240'],
        'mumuH':['wzp6_ee_mumuH_ecm240'],
        'tautauH':['wzp6_ee_tautauH_ecm240'],
        'qqH':['wzp6_ee_qqH_ecm240'],
        'nunuH':['wzp6_ee_nunuH_ecm240'],
    }
}
plots['Zmumu'] = plots['Zee']

legend = {}
legend['nunuH'] = '#nu#nuH'
legend['eeH'] = 'eeH'
legend['mumuH'] = '#mu#muH'
legend['tautauH'] = '#tau#tauH'
legend['qqH'] = 'qqH'
legend['eem30'] = 'ee30-150GeV'
legend['mumu'] = '#mu#mu'
legend['tautau'] = '#tau#tau'
legend['WW'] = 'WW'
legend['ZZ'] = 'ZZ'
legend['iDM1'] = 'iDM BP1'
legend['iDM2'] = 'iDM BP2'
