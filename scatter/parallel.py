"""
Copyright (C) 2013 Matthew Woodruff

This script is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This script is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this script. If not, see <http://www.gnu.org/licenses/>.

===========================================================
parallel.py

Parallel coordinate plot, with values for my particular data
hard-coded 
"""
import matplotlib
import recalc
import pandas
from matplotlib.backends import backend_agg as agg
import numpy

def parallel(ax, ten, three, mins, maxes, cols):
    naxes = 10
    echs = range(naxes)
    ax.vlines(echs, -0.1, 1.1, colors=(0.6,0.6,0.6))
    ax.set_ylim(-0.15,1.1)
    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_xticks(echs)

    for ii in range(len(ten)):
        row = ten.irow(ii)[cols].values
        endpoints = [(row[jj] - mins[jj]) / (maxes[jj] - mins[jj]) for jj in range(naxes)]
        ll = ax.plot(echs, endpoints, color=(1.0,0.0,0.0,0.05))    
    ll = ax.plot(echs, [2] * naxes, color=(1.0,0.0,0.0))
    ll[0].set_label("ten")

    for ii in range(len(three)):
        row = three.irow(ii)[cols].values
        endpoints = [(row[jj] - mins[jj]) / (maxes[jj] - mins[jj]) for jj in range(naxes)]
        ll = ax.plot(echs, endpoints, color=(0.0,0.0,1.0,0.2))

    ll = ax.plot(echs, [2] * naxes, color=(0.0,0.0,1.0))
    ll[0].set_label("three")
    ax.set_xlim(0, naxes + 1.5)
    tix = ax.get_xticklines()
    for tic in tix:
        tic.set_color((0,0,0,0))


def doit(fig, ten, three):
    naxes = 10
    table = pandas.concat([three, ten])
    outputnames = recalc.outputnames()
    groups = []
    gmins = []
    gmaxes = []
    for ii in range(3):
        cols = outputnames[9*ii:9*ii+9]
        cols.append("PFPF")
        groups.append(cols)
        gmins.append(table.min()[cols].values)
        gmaxes.append(table.max()[cols].values)

    mins = []
    maxes = []
    for ii in range(naxes):
        mins.append(min(gmins[0][ii], gmins[1][ii], gmins[2][ii]))
        maxes.append(max(gmaxes[0][ii], gmaxes[1][ii], gmaxes[2][ii]))

    precisions = [0.1, 10, 1, 0.01, 10, 100, 10, 0.1, 10, 0.1]
    formats = {0.1: "{0:.1f}", 0.01: "{0:.2f}"}
    viewmins = [numpy.floor(mins[ii] / precisions[ii]) * precisions[ii]
                for ii in range(naxes)]
    viewmaxes = [numpy.ceil(maxes[ii] / precisions[ii]) * precisions[ii]
                for ii in range(naxes)]
    
    for ii in range(3):
        cols = groups[ii]
        ax = fig.add_subplot(3,1,ii+1, frameon=False)
        parallel(ax, ten, three, mins, maxes, cols)

        if ii == 1:
            ax.legend(loc='right', bbox_to_anchor=(naxes + 1.4, 0.5), 
                      bbox_transform=ax.transData)

        if ii == 0:
            for jj in range(naxes):
                form = formats.get(precisions[jj], "{0:.0f}")
                ax.text(jj, 1.1, form.format(viewmaxes[jj]), ha="center",
                        va="bottom")
        
    for jj in range(naxes):
        form = formats.get(precisions[jj], "{0:.0f}")
        ax.text(jj, -0.15, form.format(viewmins[jj]), ha="center",
                va="bottom")
    ax.set_xticklabels(recalc.objnames(10), rotation=270)

if __name__ == "__main__":
    fig = matplotlib.figure.Figure(figsize=(9, 6))
    agg.FigureCanvasAgg(fig)
    three = recalc.reevaluate(27,3,0.1)
    ten = recalc.reevaluate(27,10,1.0)
    doit(fig, ten, three)
    fig.subplots_adjust(hspace=0, bottom=0.15, top=0.95)
    fig.savefig("parallel.png")
# vim:ts=4:sw=4:expandtab:ai:colorcolumn=68:number:fdm=indent
