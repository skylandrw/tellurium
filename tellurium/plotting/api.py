from __future__ import print_function, division, absolute_import

# _plot_index = 0
def plot(x, y, show=True, **kwargs):
    """ Create a 2D scatter plot.

    :param x: A numpy array describing the X datapoints. Should have the same number of rows as y.
    :param y: A numpy array describing the Y datapoints. Should have the same number of rows as x.
    :param color: The color to use.
    :param tag: A tag so that all traces of the same type are plotted using same color/label (for e.g. multiple stochastic traces).
    :param tags: Like tag, but for multiple traces.
    :param name: The name of the trace.
    :param name: Like name, but for multiple traces.
    :param alpha: Floating point representing the opacity ranging from 0 (transparent) to 1 (opaque).
    :param mode: Either 'lines' or 'markers' (defaults to 'lines').
    """
    from .. import getPlottingEngine
    # global _plot_index
    return getPlottingEngine().plot(x, y, show=show, **kwargs)

def show(reset=True):
    from .. import getPlottingEngine
    return getPlottingEngine().show(reset=reset)
