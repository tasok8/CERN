import ROOT

c = ROOT.TCanvas()
rdf = ROOT.RDF.FromCSV("outputs/all.csv")
rdf.GetColumnNames()	
rdf.Display().Print()

hV = rdf.Histo1D(ROOT.RDF.TH1DModel("Version", "ROOT Downloads 10.04-23.04.2023", 300, 400, 700), "Version")
hV.Draw()
hV.SetLineWidth(5)
hV.SetLineColor(ROOT.kOrange)
hV.SetFillColor(ROOT.kOrange)
hV.GetXaxis().SetLabelSize(0.04) 
hV.GetXaxis().SetTitle("version x100") 
hV.GetXaxis().SetTitleSize(0.045)

ROOT.gPad.Update()
c.SaveAs("Version.png")
print("Saved figure to Version.png")