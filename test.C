{
   TCanvas c1; //= new TCanvas("test","title");
   TFile f1("DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root");
   TH1F *hist1 = (TH1F*) f1.Get("DQMData/Run 1/Tracking/Run summary/Track/cutsReco_quickAssociatorByHits/efficPt");
   hist1->SetLineColor(kRed);
   hist1->Draw();
 
   TFile f2("val.RelValQCD_Pt_3000_3500_p5.root");
   TH1F *hist2 = (TH1F*) f2.Get("DQMData/Run 1/Tracking/Run summary/Track/cutsRecoHp_AssociatorByHitsRecoDenom/efficPt");
   hist2->SetLineColor(kBlue);
   gPad->SetLogx();
   hist2->Draw("same");  

   c1->SetGrid();
   //c1->SetGridx(3);
   c1->SaveAs("test3_p5.pdf"); 
}
