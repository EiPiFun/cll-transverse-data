import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

chart_title = ''
chart_xlabel = 'Unit block length and width'
chart_ylabel = 'Toughness (GPa)'

x1 = numpy.arange(3)
x1ticks = ('6','9','12')

legend_array = ('Cross', 'Cross horizontal', 'Symmetric', 'Symmetric horizontal','Crystal')

y1 = numpy.array((353,159, 61))*0.001
y2 = numpy.array((137, 88, 94))*0.001
y3 = numpy.array((226,211,203))*0.001
y4 = numpy.array(( 82, 69, 58))*0.001

y5 = numpy.array((142, 98,115))*0.001

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.xticks(x1, x1ticks)
plt.ylim(0.0, 1.2)

plt.bar(x1-0.2, y1, width=0.1)
plt.bar(x1-0.1, y2, width=0.1)
plt.bar(x1+0.0, y3, width=0.1)
plt.bar(x1+0.1, y4, width=0.1)
plt.bar(x1+0.2, y5, width=0.1)

#plt.title(chart_title, fontsize=20)
plt.legend(legend_array, fontsize=14)

plt.tick_params(labelsize=20)
plt.xlabel(chart_xlabel, fontsize=20)
plt.ylabel(chart_ylabel, fontsize=20)

plt.savefig(current_path+"toughness.png")

