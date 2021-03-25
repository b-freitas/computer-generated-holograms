import base64
from datetime import datetime
from io import BytesIO
import flask
from flask import Flask, render_template, request, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and isinstance(int(request.form['ell']), int):
        ell = request.form['ell']
    else:
        ell = 0
    return render_template("index.html", ell=ell)


@app.route("/plot-<int:ell>.png")
def generate_mask(ell=0):
    import math

    import numpy as np

    lambda0 = 633e-9
    k = 2*math.pi/lambda0
    step = 2**7-1
    x0 = (np.array(range(0, step+1)) - step/2.0)
    y0 = np.array(x0)
    x, y = np.meshgrid(x0, y0)
    theta = np.arctan(y/x)
    mask = (1+np.cos((k*x)-(ell*theta))/2)
    mask = mask[::-1]

    fig = Figure(frameon=False)
    ax = fig.subplots()
    ax.pcolormesh(mask, cmap='gray', shading='gouraud')
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    FigureCanvas(fig).print_png(buf)
    return Response(buf.getvalue(), mimetype="image/png")


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
