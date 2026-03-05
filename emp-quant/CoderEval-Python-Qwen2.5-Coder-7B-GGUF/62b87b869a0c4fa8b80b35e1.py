import numpy as np
from ROOT import TGraph, TGraphErrors

def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if make_value is None:
        make_value = lambda bin_: bin_

    x_values = []
    y_values = []
    errors = []

    for bin_ in hist:
        value = make_value(bin_)
        if isinstance(value, tuple):
            x, y, error = value
        else:
            x, y, error = bin_.GetBinCenter(), value, 0

        if get_coordinate == "left":
            x_values.append(bin_.GetBinLowEdge())
        elif get_coordinate == "right":
            x_values.append(bin_.GetBinUpEdge())
        elif get_coordinate == "middle":
            x_values.append(bin_.GetBinCenter())

        y_values.append(y)
        errors.append(error)

    if len(field_names) != 2:
        raise ValueError("field_names must have 2 elements")

    if scale is True:
        scale = hist.GetSumOfWeights()

    if scale is not None:
        y_values = [y / scale for y in y_values]

    if len(x_values) == len(y_values) == len(errors):
        graph = TGraphErrors(len(x_values), np.array(x_values), np.array(y_values), np.zeros(len(x_values)), np.array(errors))
    else:
        graph = TGraph(len(x_values), np.array(x_values), np.array(y_values))

    graph.SetNameTitle(f"{hist.GetName()}_graph", f"{hist.GetTitle()} graph")
    graph.GetXaxis().SetTitle(field_names[0])
    graph.GetYaxis().SetTitle(field_names[1])

    return graph