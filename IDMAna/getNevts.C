#include <algorithm>
#include <iomanip>
#include <stdlib.h>
#include <iostream>
#include <fstream>

#include "TFile.h"
#include "TTree.h"

int getNevts(TString filename){


  TFile *fin = TFile::Open(filename);
  if (!fin) return -1;
  fin->cd();

  TTree *tree = (TTree*)gDirectory->Get("events");
  if (!tree) return 0;
  return tree->GetEntries();

}
