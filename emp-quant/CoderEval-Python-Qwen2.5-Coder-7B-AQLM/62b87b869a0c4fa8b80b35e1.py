import numpy as np

def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if make_value is None:
        make_value = lambda bin_content: bin_content

    if get_coordinate == "left":
        get_coordinate = lambda bin_edges: bin_edges[0]
    elif get_coordinate == "right":
        get_coordinate = lambda bin_edges: bin_edges[1]
    elif get_coordinate == "middle":
        get_coordinate = lambda bin_edges: (bin_edges[0] + bin_edges[1]) / 2

    x_values = []
    y_values = []
    for bin_edges, bin_content in zip(hist.edges, hist.contents):
        x = get_coordinate(bin_edges)
        y = make_value(bin_content)
        x_values.append(x)
        y_values.append(y)

    graph = {
        "x": np.array(x_values),
        "y": np.array(y_values),
        "field_names": field_names
    }

    if scale is True:
        graph["scale"] = hist.scale

    return graph