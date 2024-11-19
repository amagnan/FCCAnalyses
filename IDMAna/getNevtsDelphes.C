void getNevtsDelphes(TString file){
  gROOT->ProcessLine(".L  getNevts.C++");
  gROOT->ProcessLine("getNevts(\"" + file + "\")");
  gROOT->ProcessLine(".q");
}
