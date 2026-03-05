import ROOT

def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if make_value is None:
        make_value = lambda bin_content: bin_content
    
    graph = ROOT.TGraphErrors()
    
    for i in range(1, hist.GetNbinsX() + 1):
        bin_content = hist.GetBinContent(i)
        bin_error = hist.GetBinError(i)
        
        x_value = hist.GetBinCenter(i)
        if get_coordinate == "left":
            x_value -= hist.GetBinWidth(i) / 2
        elif get_coordinate == "right":
            x_value += hist.GetBinWidth(i) / 2
        
        y_value, y_error = make_value(bin_content)
        
        graph.SetPoint(graph.GetN(), x_value, y_value)
        graph.SetPointError(graph.GetN() - 1, 0, y_error)
    
    if scale is True:
        graph.SetTitle(hist.GetTitle())
        graph.GetXaxis().SetTitle(hist.GetXaxis().GetTitle())
        graph.GetYaxis().SetTitle(hist.GetYaxis().GetTitle())
    
    return graph