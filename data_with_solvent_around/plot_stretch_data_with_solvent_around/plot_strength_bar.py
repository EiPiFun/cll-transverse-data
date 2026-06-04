import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

chart_title = ''
chart_xlabel = ''
chart_ylabel = 'Strength (GPa)'

x1 = numpy.arange(8)
x1ticks = ('DMF','DMSO','EDA','EtOH','IPA','MeOH',r'$\rm{H_2O}$','NONE')

legend_array = ('I','II')

y1 = numpy.array((185,205,136,151,182,168,154,162))*0.001
y2 = numpy.array((227,237,219,248,238,237,199,181))*0.001

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.06
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.xticks(x1, x1ticks, rotation=40)
plt.ylim(0.0, 0.4)

plt.bar(x1-0.2, y1, width=0.4)
plt.bar(x1+0.2, y2, width=0.4)

#plt.title(chart_title, fontsize=20)
plt.legend(legend_array, fontsize=20)

plt.tick_params(labelsize=20)
plt.xlabel(chart_xlabel, fontsize=20)
plt.ylabel(chart_ylabel, fontsize=20)

plt.savefig(current_path+'strength.'+image_file_extension)

