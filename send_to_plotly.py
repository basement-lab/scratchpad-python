
# import plotly
import plotly.plotly as py
import plotly.graph_objs as go

# Scientific libraries
import numpy as np

# points = np.array([(1, 1), (2, 4), (3, 1), (9, 3)])
points = np.array([
    (-3, 19925.7612291),
    (-2, 11205.3989125),
    (-1, 4978.38659603),
    (0, 1244.7242795),
    (1, 4.41196298026),
    (2, 1257.44964646),
    (3, 5003.83732993),
    (4, 11243.5750134),
    (5, 19976.6626969),
])

# get x and y vectors
x = points[:, 0]
y = points[:, 1]

# calculate polynomial
z = np.polyfit(x, y, 2)
f = np.poly1d(z)
print(f)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

# Creating the dataset, and generating the plot
trace1 = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=go.Marker(color='rgb(255, 127, 14)'),
    name='Data'
)

trace2 = go.Scatter(
    x=x_new,
    y=y_new,
    mode='lines',
    marker=go.Marker(color='rgb(31, 119, 180)'),
    name='Fit'
)

annotation = go.Annotation(
    x=6,
    y=-4.5,
    text='$\textbf{Fit}: 0.43X^3 - 0.56X^2 + 16.78X + 10.61$',
    showarrow=False
)
layout = go.Layout(
    title='Polynomial Fit in Python',
    plot_bgcolor='rgb(229, 229, 229)',
    xaxis=go.XAxis(zerolinecolor='rgb(255,255,255)',
                   gridcolor='rgb(255,255,255)'),
    yaxis=go.YAxis(zerolinecolor='rgb(255,255,255)',
                   gridcolor='rgb(255,255,255)'),
    annotations=[annotation]
)

data = [trace1, trace2]
fig = go.Figure(data=data, layout=layout)

py.plot(fig, filename='Polynomial-Fit-in-python')
