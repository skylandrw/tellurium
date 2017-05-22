from .engine import PlottingEngine, PlottingFigure, PlottingLayout, filterWithSelections
import plotly, numpy as np
from plotly.graph_objs import Scatter, Scatter3d, Layout, Data

class PlotlyFigure(PlottingFigure):
    def __init__(self, title=None, layout=PlottingLayout(), logx=False, logy=False, save_to_pdf=False):
        self.initialize(title=title, layout=layout, logx=logx, logy=logy)

    def makeLayout(self):
        kwargs = {}
        if self.title is not None:
            kwargs['title'] = self.title
        if self.logx:
            kwargs['xaxis'] = {
                type: 'log',
                autorange: True,
            }
        if self.logy:
            kwargs['yaxis'] = {
                type: 'log',
                autorange: True,
            }
        return Layout(**kwargs)

    def plot(self):
        """ Plot the figure. Call this last."""
        traces = []
        for dataset in self.getDatasets():
            kwargs = {}
            if 'name' in dataset and dataset['name'] is not None:
                kwargs['name'] = dataset['name']
            else:
                kwargs['showlegend'] = False
            traces.append(Scatter(
                x = dataset['x'],
                y = dataset['y'],
                mode = 'lines',
                **kwargs
            ))

        data = Data(traces)
        plotly.offline.iplot({
            'data': data,
            'layout': self.makeLayout()
        })

class PlotlyStackedFigure(PlotlyFigure):
    def __init__(self, title=None, layout=PlottingLayout(), logx=False, logy=False):
        self.initialize(title=title, layout=layout, logx=logx, logy=logy)
        self.zindex = 0

    def plot(self):
        """ Plot the figure. Call this last."""
        traces = []
        for dataset in self.xy_datasets:
            kwargs = {}
            if 'name' in dataset and dataset['name'] is not None:
                kwargs['name'] = dataset['name']
                self.zindex = kwargs['name']
            else:
                kwargs['showlegend'] = False
            zvals = np.full(np.size(dataset['x']), self.zindex)
            traces.append(Scatter3d(
                x = dataset['x'],
                z = dataset['y'],
                y = zvals,
                mode = 'lines',
                **kwargs
            ))
            if not isinstance(self.zindex, str):
                self.zindex += 1

        data = Data(traces)
        plotly.offline.iplot({
            'data': data,
            'layout': self.makeLayout()
        })

class PlotlyPlottingEngine(PlottingEngine):
    def __init__(self, save_to_pdf=False):
        PlottingEngine.__init__(self)

    def newFigure(self, title=None, logX=False, logY=False, layout=PlottingLayout()):
        """ Returns a figure object."""
        return PlotlyFigure(title=title, layout=layout)

    def newStackedFigure(self, title=None, logX=False, logY=False, layout=PlottingLayout()):
        """ Returns a figure object."""
        return PlotlyStackedFigure(title=title, layout=layout)
