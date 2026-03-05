import ROOT

def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if make_value is None:
        make_value = lambda bin_content: bin_content
    
    graph = ROOT.TGraphErrors()
    
    for i in range(1, hist.GetNbinsX() + 1):
        bin_content = hist.GetBinContent(i)
        bin_center = hist.GetBinCenter(i)
        
        x, y = bin_center, make_value(bin_content)
        
        if get_coordinate == "left":
            x -= hist.GetBinWidth(i) / 2
        elif get_coordinate == "right":
            x += hist.GetBinWidth(i) / 2
        
        graph.SetPoint(graph.GetN(), x, y)
    
    if scale is True:
        graph.SetTitle(f"{hist.GetTitle()};{field_names[0]};{field_names[1]}")
    
    return graph