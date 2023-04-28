import ROOT

c = ROOT.TCanvas()
rdf = ROOT.RDF.FromCSV("outputs/all.csv")
rdf.GetColumnNames()
rdf.Display().Print()

# convert platform names to integers (C++ lambda function - ROOT framework && PyROOT.)
platform_conversion_code = '''
int platform_to_int(const std::string &platform) {
    if (platform == "source") return 1;
    else if (platform == "macos") return 2;
    else if (platform == "win32") return 3;
    else if (platform == "win64") return 4;
    else if (platform == "Linux") return 5;
    else return 0;
}
'''

# Add lambda function to ROOT 
ROOT.gInterpreter.Declare(platform_conversion_code)

# New column in dataframe with int values
rdf = rdf.Define("Platform_int", "platform_to_int(Platform)")


hP = rdf.Histo1D(ROOT.RDF.TH1DModel("Platform", "ROOT Downloads 10.04-23.04.2023", 5, 0.5, 5.5), "Platform_int")
hP.Draw()
hP.SetLineWidth(5)
hP.SetLineColor(ROOT.kOrange)
hP.SetFillColor(ROOT.kOrange)
hP.GetXaxis().SetLabelSize(0.04)
hP.GetXaxis().SetTitle("Platform")
hP.GetXaxis().SetTitleSize(0.045)

platform_labels = ["", "Source", "macOS", "Win32", "Win64", "Linux"]
for i, label in enumerate(platform_labels):
    hP.GetXaxis().SetBinLabel(i, label)

ROOT.gPad.Update()
c.SaveAs("Platform.png")
print("Saved figure as Platform.png")
