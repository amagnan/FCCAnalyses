import ROOT as rt
# A little setup for drawing
rt.gStyle.SetOptStat(0)
cvs = rt.TCanvas()
cvs.SetCanvasSize(800,600)
fnameS = ("iDM/stage2/e240_bp1_h2h2ll.root")
fS = rt.TFile.Open(fnameS)
fS.ls()
treeS = fS.events
fnameS2 = ("iDM/stage2/e240_bp1_h2h2llvv.root")
fS2 = rt.TFile.Open(fnameS2)
treeS2 = fS2.events
fnameB = ("iDM/stage2/p8_ee_WW_ecm240.root")
fB = rt.TFile.Open(fnameB)
fB.ls()
treeB = fB.events
fnameB2 = ("iDM/stage2/p8_ee_ZZ_ecm240.root")
fB2 = rt.TFile.Open(fnameB2)
treeB2 = fB2.events
fnameB3 = ("iDM/stage2/wzp6_ee_ee_Mee_30_150_ecm240.root")
fB3 = rt.TFile.Open(fnameB3)
treeB3 = fB3.events
fnameB4 = ("iDM/stage2/wzp6_ee_mumu_ecm240.root")
fB4 = rt.TFile.Open(fnameB4)
treeB4 = fB4.events
fnameB5 = ("iDM/stage2/wzp6_ee_tautau_ecm240.root")
fB5 = rt.TFile.Open(fnameB5)
treeB5 = fB5.events
fnameB6 = ("iDM/stage2/wzp6_ee_nunuH_ecm240.root")
fB6 = rt.TFile.Open(fnameB6)
treeB6 = fB6.events

# we can use this file later to analyse the results
outputFile = rt.TFile.Open('TMVA_output.root', 'recreate')
# we give it a name which it uses in the output, the outputfile, and
# some options (for instance, remove ! in front of Silent to suppress
# output)
factory = rt.TMVA.Factory('TMVAClassification', outputFile,
'!V:!Silent:Color:!DrawProgressBar:AnalysisType=Classification')
# create a dataloader and tell it the tree it sould use for signal and background
loader = rt.TMVA.DataLoader('dataset')
# in our case, the same tree holds signal and background, we will tell
# it later how to select the actual signal and background events we
# could also optionally add weights if we had several trees for
# e.g. different background processes
loader.AddSignalTree(treeS,0.0069/500000)
loader.AddSignalTree(treeS2,0.001303/500000)
loader.AddBackgroundTree(treeB,16.4385/373375386)
loader.AddBackgroundTree(treeB2,1.359/56162093)
loader.AddBackgroundTree(treeB3,8.305/85400000)
loader.AddBackgroundTree(treeB4,5.288/53400000)
loader.AddBackgroundTree(treeB5,4.668/52400000)
loader.AddBackgroundTree(treeB6,0.0462/3500000)
# now we define the variables to be used in the analysis, do not give it a name...
loader.AddVariable('Zcand_e')
loader.AddVariable('Zcand_m')
loader.AddVariable('Zcand_pt')
loader.AddVariable('TMath::Abs(Zcand_pz)')
loader.AddVariable('Zcand_costheta')
loader.AddVariable('Zcand_povere')
loader.AddVariable('Zcand_recoil_m')
loader.AddVariable('cosThetaStar')
loader.AddVariable('cosThetaR')
loader.AddVariable('cosDphiLep')
loader.AddVariable('MET_pt[0]')
loader.AddVariable('lep1_pt')
loader.AddVariable('lep2_pt')

# finally tell it how to read signal and background and prepare the test/train

preselCut="((n_electrons==0 && n_muons==2) ||(n_electrons==2 && n_muons==0)) &&  Zcand_m<120 && TMath::Abs(Zcand_pz)<70 && MET_pt[0]>5 && n_seljets<1 && n_photons==0 && lep1_pt<80 && lep2_pt<60 && Zcand_povere>0.1"

loader.PrepareTrainingAndTestTree(preselCut, preselCut, # signal cut, then background cut
"nTrain_Signal=100000:nTrain_Background=100000:SplitMode=Random:NormMode=NumEvents:!V")

# Boosted Decision Trees
factory.BookMethod(loader,rt.TMVA.Types.kBDT, "BDT",
"!V:NTrees=200:MinNodeSize=2.5%:MaxDepth=2:BoostType=AdaBoost:AdaBoostBeta=0.5:"+
"UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20")

# Multi-Layer Perceptron (= Neural Network)
#factory.BookMethod(loader, rt.TMVA.Types.kMLP, "MLP",
#"!H:!V:NeuronType=tanh:VarTransform=N:NCycles=100:HiddenLayers=N+5:"+
#"TestRate=5:!UseRegulator")
# Train
factory.TrainAllMethods()
# Test
factory.TestAllMethods()
# Evaluate, these will compute various quantities of interest and output them into the output file
factory.EvaluateAllMethods()
# the output file will have the results of the training
outputFile.Close()





#    def getReader():
#        reader = ROOT.TMVA.Reader()
#TMVAClassification_BDT.weights.xml
#reader.BookMVA("BDT","dataset/weights/TMVAClassification_BDT.weights.xml")
    
