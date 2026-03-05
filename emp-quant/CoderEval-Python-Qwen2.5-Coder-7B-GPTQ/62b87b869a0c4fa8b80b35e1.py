import ROOT

def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if make_value is None:
        make_value = lambda x: x
    
    graph = ROOT.TGraphErrors()
    
    for i in range(1, hist.GetNbinsX() + 1):
        bin_content = hist.GetBinContent(i)
        bin_center = hist.GetBinCenter(i)
        
        if get_coordinate == "left":
            x = bin_center - hist.GetBinWidth(i) / 2
        elif get_coordinate == "right":
            x = bin_center + hist.GetBinWidth(i) / 2
        elif get_coordinate == "middle":
            x = bin_center
        
        y, ey = make_value(bin_content)
        
        graph.SetPoint(graph.GetN(), x, y)
        graph.SetPointError(graph.GetN() - 1, 0, ey)
    
    if scale is True:
        graph.Scale(hist.GetScaleFactor())
    
    graph.SetNameTitle(hist.GetName(), hist.GetTitle())
    graph.GetXaxis().SetTitle(hist.GetXaxis().GetTitle())
    graph.GetYaxis().SetTitle(hist.GetYaxis().GetTitle())
    
    return graph