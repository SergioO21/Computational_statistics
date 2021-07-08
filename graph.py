
from bokeh.plotting import figure, show
from bokeh.io import curdoc


def graph(x, y):
    """  """
    curdoc().theme = "dark_minimal"
    graphic = figure(title="Random Walks", x_axis_label="Steps", y_axis_label="Distance",
                     plot_width=1200, plot_height=650)
    graphic.line(x, y)

    show(graphic)
