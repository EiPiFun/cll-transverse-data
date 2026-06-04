import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

chart_title = ''
chart_xlabel = 'Length and width'
chart_ylabel = 'Direction angle'

x1 = (numpy.log(6)/numpy.log(2.0)-3.0,
      numpy.log(9)/numpy.log(2.0)-3.0,
      numpy.log(12)/numpy.log(2.0)-3.0,
      numpy.log(18)/numpy.log(2.0)-3.0,
      numpy.log(24)/numpy.log(2.0)-3.0,
      numpy.log(36)/numpy.log(2.0)-3.0,
      numpy.log(48)/numpy.log(2.0)-3.0,
      numpy.log(64)/numpy.log(2.0)-3.0)
x1ticks = (6,9,12,18,24,36,48,64)#(36,81,144,324,576,1296,2304,4096)

y1 = (2.39,2.38,2.29,2.31,2.33,2.31,2.32,2.32)
y2 = (1.82,1.96,1.82,1.91,1.99,2.06,2.04,2.05)

legend_array = ('Relaxation','Fracture')

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.xticks(x1, x1ticks)
plt.ylim((0.0, 3.0))

plt.plot(x1,y1)
plt.plot(x1,y2)
plt.scatter(x1,y1)
plt.scatter(x1,y2)

#plt.title(chart_title, fontsize=20)
#plt.legend(legend_array, fontsize=20)

plt.tick_params(labelsize=20)
plt.xlabel(chart_xlabel, fontsize=20)
plt.ylabel(chart_ylabel, fontsize=20)

plt.savefig(current_path+'direction_angle.'+image_file_extension)

