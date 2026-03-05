import numpy as np
from pyne.filter import Filter

def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    """
    Convert a :class:`.histogram` to a :class:`.graph`.

    *make_value* is a function to set the value of a graph's point.
    By default it is bin content.
    *make_value* accepts a single value (bin content) without context.

    This option could be used to create graph's error bars.
    For example, to create a graph with errors
    from a histogram where bins contain
    a named tuple with fields *mean*, *mean_error* and a context
    one could use

    >>> make_value = lambda bin_: (bin_.mean, bin_.mean_error)

    *get_coordinate* defines what the coordinate
    of a graph point created from a histogram bin will be.
    It can be "left" (default), "right" and "middle".

    *field_names* set field names of the graph. Their number
    must be the same as the dimension of the result.
    For a *make_value* above they would be
    *("x", "y_mean", "y_mean_error")*.

    *scale* becomes the graph's scale (unknown by default).
    If it is ``True``, it uses the histogram scale.

    *hist* must contain only numeric bins (without context)
    or *make_value* must remove context when creating a numeric graph.

    Return the resulting graph.
    """
    if make_value is None:
        make_value = lambda bin_: bin_

    if get_coordinate == "left":
        x_values = np.arange(len(hist.bins)) - 0.5
    elif get_coordinate == "right":
        x_values = np.arange(len(hist.bins)) + 0.5
    elif get_coordinate == "middle":
        x_values = np.arange(len(hist.bins)) + 0.25
    else:
        raise ValueError("Invalid get_coordinate value")

    y_values = np.array([make_value(bin_) for bin_ in hist.bins])

    graph = Filter()
    graph.x = x_values
    graph.y = y_values
    graph.field_names = field_names
    graph.scale = scale

    return graph