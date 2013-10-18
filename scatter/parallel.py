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

"""
import math
import argparse
import sys
import pandas
import matplotlib
import random
import copy
from matplotlib.backends import backend_agg as agg
from matplotlib.backends import backend_svg as svg

class PlottingError(Exception): pass

def rerange(intranges):
    """ convert a set of intranges into a list of integers """
    if intranges is None:
        return None
    thelist = []
    for therange in intranges:
        thelist.extend(therange)
    return thelist

def intrange(arg):
    """ convert a command-line argument to a list of integers """
    acceptable_chars = [str(x) for x in range(10)]
    acceptable_chars.append("-")

    partial = []
    first = None

    msg = "Could not convert {0} to index range.".format(arg)
    err = TypeError(msg)

    for char in arg:
        if char not in acceptable_chars:
            raise err
        if char == "-":
            if len(partial) == 0:
                raise err
            elif first is None:
                first = int("".join(partial))
                partial = []
            else: # this means there's a second -, which is not ok
                raise err
        else:
            partial.append(char)

    second = None
    if first is None:
        first = int("".join(partial))
    elif len(partial) == 0:
        raise err
    else:
        second = int("".join(partial))

    if second is None:
        return [first]
    else:
        return range(first, second+1)

def prepare_axes(ax):
    """ set up the axes """
    ax.set_frame_on(False)
    ax.set_ylim(-0.15, 1.1)
    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_xticks([])

def draw_axes(ax, names, limits):
    """ 
    draw the axis lines

    ax: a matplotlib axes for drawing on
    names: a list of names, one for each axis
    limits: a list of tuples, one for each axis, containing the 
            low and high limits for each axis.  These may be strings
            and they probably should because they will use default 
            formatting.
    """
    if len(names) != len(limits):
        raise PlottingError("Different numbers of column names and limits.")

    naxes = len(limits)
    echs = range(naxes)

    # make the axis lines
    ax.set_xticks(echs)
    for tick in ax.get_xticklines(): #make the ticks disappear
        tick.set_color((0, 0, 0, 0))
    ax.vlines(echs, -0.1, 1.1, colors=(0.6, 0.6, 0.6))

    ax.set_xticklabels(names, rotation=270)

    # label the limits
    for xx in echs:
        ax.text(xx, -0.15, limits[xx][0], ha="center", va="bottom")
        ax.text(xx, 1.1, limits[xx][1], ha="center", va="bottom")
 
def draw_lines(ax, table, limits, **kwargs):
    """ 
    draw lines for a data set
    ax: a matplotlib axes object
    table: a pandas data table with the data to plot.  
    limits: lower and upper limits for the data

    keyword args:
    *color* the color to use for data from the table
    *lw* linewidth
    """
    xs = range(len(limits))
    color = kwargs.get("color", 'k')
    lw = kwargs.get("lw", 1)
    for row in table.itertuples(False):
        zorder = random.random()
        ys = [(x-l)/(h-l) for x, (l, h) in zip(row, limits)]
        ax.plot(xs, ys, color=color, zorder=zorder, lw=lw)

def draw_legend(ax, naxes, names, colors, title):
    """
    first draw lines off the plot to feed the legend,
    then make the legend itself

    ax: a matplotlib axes object for drawing
    """
    newcolors = []
    for color in colors:
        if len(color) == 4:
            newcolors.append([])
            newcolors[-1].extend(color[:3])
            newcolors[-1].append(1.0)
        else:
            newcolors.append(color)

    for (name, color) in zip(names, newcolors):
        ax.plot([-10, -9], [0, 0], lw=2, color=color, label=name)

    anchor = (1.14*naxes, 0.5)
    ax.legend(loc='right', bbox_to_anchor=(anchor),
              bbox_transform=ax.transData, title=title)

def desired_columns(table, columns):
    """
    return a new table with the desired columns in it
    """
    data = {}
    for ii, cc in zip(range(len(columns)), columns):
        data[ii] = table[cc]

    return pandas.DataFrame(data=data)

def find_limits(tables, precisions, wrap):
    """ find lower and upper limits for each column across all tables """
    mins = tables[0].min()
    maxs = tables[0].max()

    for table in tables:
        for col in table.columns:
            mins[col] = min(table[col].min(), mins[col])
            maxs[col] = max(table[col].max(), maxs[col])

    wrappedmins = []
    wrappedmaxs = []
    for ii in range(wrap):
        mm = mins[ii]
        mx = maxs[ii]
        jj = 0
        while ii + jj*wrap < len(mins):
            index = ii + jj*wrap
            mm = min(mm, mins[index])
            mx = max(mx, maxs[index])
            jj+=1
        wrappedmins.append(mm)
        wrappedmaxs.append(mx)

    while len(wrappedmins) < len(mins):
        wrappedmins.extend(wrappedmins)
        wrappedmaxs.extend(wrappedmaxs)
    while len(precisions) < len(mins):
        precisions.extend(precisions)

    wrappedmins = wrappedmins[:len(mins)]
    wrappedmaxs = wrappedmaxs[:len(mins)]
    precisions = precisions[:len(mins)]

    viewmins = [math.floor(wrappedmins[ii] / precisions[ii]) * precisions[ii]
                for ii in range(len(precisions))]
    viewmaxs = [math.ceil(wrappedmaxs[ii] / precisions[ii]) * precisions[ii]
                for ii in range(len(precisions))]

    return [[mm, mx] for mm, mx in zip(viewmins, viewmaxs)]

def init_figures(issplit, isvector, naxes, nplots):
    """
    initialize figures and set up backends

    issplit: true if we're making separate vector and raster figures
    isvector: true if we're making vector lines
    naxes: number of axes, used for sizing
    nplots: number of subplots, used for sizing
    """
    figsize = (3 + 0.6 * naxes, 2 + (4/3) * nplots)
    if issplit:
        raster = matplotlib.figure.Figure(figsize=figsize)
        agg.FigureCanvasAgg(raster)
        vector = matplotlib.figure.Figure(figsize=figsize)
        svg.FigureCanvasSVG(vector)
    elif isvector:
        vector = matplotlib.figure.Figure(figsize=figsize)
        svg.FigureCanvasSVG(vector)
        raster = vector
    else:
        raster = matplotlib.figure.Figure(figsize=figsize)
        agg.FigureCanvasAgg(raster)
        vector = raster

    return raster, vector

def interpret_color(color):
    """
    interpret a color argument

    color: A list.  If it has one element, that element may be a 
           single letter color code, from among "bgrcmykw", or
           a single float indicating a grayscale value.
           If it has multiple elements, there must be three 
           or four, and must be floats in the range [0,1].
    """
    msg = "{0} is not a color".format(color)
    err = PlottingError(msg)

    if len(color) == 1:
        try:
            gs = float(color[0])
            if gs < 0.0 or gs > 1.0:
                raise err
            return str(gs)
        except ValueError:
            if color[0][:1] in "bgrcmykw":
                return color[0][:1]
            else:
                raise err
    if len(color) not in [3,4]:
        raise err
    
    try:
        return [float(x) for x in color]
    except ValueError:
        raise err

def get_args(argv):
    """ command line arguments """

    parser = argparse.ArgumentParser(argv.pop(0))

    parser.add_argument("output", type=str,
                        help="base name for the output file")
    parser.add_argument("files", nargs="+", type=argparse.FileType("r"),
                        help="files containing sets to plot")
    parser.add_argument("-c", "--colors", nargs="+", action='append',
                        help="add a color to the color cycle")
    parser.add_argument("-C", "--columns", type=intrange, nargs="+",
                        help="columns containing data to plot")
    parser.add_argument("-p", "--precisions", nargs='+', type=float,
                        help="precision for each column")
    parser.add_argument("-a", "--axis-names", nargs='+', type=str,
                        help="names for the axes")
    parser.add_argument("-n", "--names", nargs='+', type=str,
                        help="label for the input files")
    parser.add_argument("-H", "--header", type=int, default=0,
                        help="number of header lines in input files")
    parser.add_argument("-S", "--split", action='store_true',
                        help="produce two output files: a PNG for the "\
                             "data, and an SVG for the axes")
    parser.add_argument("-V", "--vector", action='store_true',
            help="Produce vector output.  WARNING: Will produce "\
                 "very large output files if the input is too large.  "\
                 "More than 50 rows of data, and possibly far fewer, "\
                 "is asking for trouble. Use -S unless you're "
                 "absolutely sure you want this.")

    parser.add_argument("-w", "--wrap", type=int,
                        help="number of axes to draw before wrapping")

    parser.add_argument("-m", "--minima", type=float, nargs="+",
                        help="minimum values for each column")
    parser.add_argument("-M", "--maxima", type=float, nargs="+",
                        help="maximum values for each column")

    parser.add_argument("-W", "--linewidth", type=float, nargs="+",
                        help="linewidths for solution sets")

    args = parser.parse_args(argv)
    if args.columns is not None:
        args.columns = rerange(args.columns)

    if args.colors is None:
        args.colors = ['k']
    else:
        args.colors = [interpret_color(c) for c in args.colors]

    if len(args.files) > len(args.colors):
        colors = []
        cycle = -1
        for _ in args.files:
            cycle = (cycle + 1) % len(args.colors)
            colors.append(args.colors[cycle])
        args.colors = colors

    if args.names is None:
        args.names = [f.name for f in args.files]
    elif len(args.files) > len(args.names):
        for ii in range(len(args.names), len(args.files)):
            args.names.append(args.files[ii].name)
    else:
        args.names = args.names[:len(args.files)]

    if args.axis_names is None:
        args.axis_names = [str(c) for c in args.columns]
    elif len(args.columns) > len(args.axis_names):
        for ii in range(len(args.axis_names), len(args.columns)):
            args.names.append(str(args.columns[ii]))
    else:
        args.axis_names = args.axis_names[:len(args.columns)]

    if args.wrap is None:
        args.wrap = len(args.columns)

    if args.precisions is None:
        args.precisions = [0.1] * len(args.columns)
    elif len(args.precisions) < args.wrap:
        args.precisions.extend([0.1] * (args.wrap - len(args.precisions)))
        while len(args.precisions) < len(args.columns):
            args.precisions.extend(args.precisions)
    args.precisions = args.precisions[:len(args.columns)]

    if args.linewidth is None:
        args.linewidth = [1] * len(args.files)
    elif len(args.linewidth) < len(args.files):
        args.linewidth.extend([1] * (len(args.files) - len(args.linewidth)))

    return args

def cli(argv):
    """ command-line interface """
    args = get_args(argv)

    tables = [pandas.read_table(f, header=None, skiprows=args.header, sep=" ") 
              for f in args.files]
    for fp in args.files:
        fp.close()
    if args.columns is not None:
        tables = [desired_columns(t, args.columns) for t in tables]

    ncolumns = len(tables[0].columns)

    limits = find_limits(tables, args.precisions, args.wrap)

    if args.wrap is None:
        nplots = 1
        naxes = ncolumns
    else:
        nplots = int(math.ceil(ncolumns / args.wrap))
        naxes = args.wrap

    if args.minima is not None:
        for ii in range(nplots):
            for mm, lim in zip(args.minima, limits[ii*naxes:]):
                lim[0] = mm
    if args.maxima is not None:
        for ii in range(nplots):
            for mx, lim in zip(args.maxima, limits[ii*naxes:]):
                lim[1] = mx

    raster, vector = init_figures(args.split, args.vector, naxes, nplots)

    for fig in [raster, vector]:
        fig.subplots_adjust(hspace=0, bottom=0.15, top=0.95, left=0.05, right=0.95)

    for ii in range(nplots):
        rax = raster.add_subplot(nplots, 1, ii+1)
        if vector != raster:
            vax = vector.add_subplot(nplots, 1, ii+1)
        else:
            vax = rax

        prepare_axes(rax)
        prepare_axes(vax)

        xmax = 1.2*naxes
        rax.set_xlim((0, xmax))
        vax.set_xlim((0, xmax))

        for table, color, lw in zip(tables, args.colors, args.linewidth):
            indices = range(ii*naxes, min(ii*naxes + naxes, ncolumns))
            subtable = table.select(lambda cc: cc in indices, axis=1)
            sublimits = [limits[jj] for jj in indices]
#            print("drawing lines on axes {0} with color {1} and limits {2}".format(rax, color, sublimits))
            draw_lines(rax, subtable, sublimits, color=color, lw=lw)
        if ii == nplots // 2:
            draw_legend(vax, naxes, args.names, args.colors, "File")

        drawlimits = []
        for _ in range(len(limits)):
            drawlimits.append(["", ""])

        dlp = zip(drawlimits, limits, args.precisions)
        if ii == 0:
            for dl, lim, prec in dlp:
                dl[1] = format_of(prec).format(lim[1])
        if ii + 1 == nplots:
            for dl, lim, prec in dlp:
                dl[0] = format_of(prec).format(lim[0])
            axis_names = args.axis_names[:naxes]
        else:
            axis_names = [""]*naxes
        drawlimits = drawlimits[:naxes]
        draw_axes(vax, axis_names, drawlimits)

    raster.savefig(args.output)
    if vector != raster:
        vector.savefig(args.output)

def format_of(precision):
    """
    return an appropriate format for the precision
    """
    if precision <= 0.0:
        return "{0}"
    elif precision < 1e-3:
        return "{0:.2g}"
    elif precision < 1e-2:
        return "{0:.3f}"
    elif precision < 1e-1:
        return "{0:.2f}"
    elif precision < 1:
        return "{0:.1f}"
    return "{0:.0f}"

if __name__ == "__main__":
    cli(sys.argv)

