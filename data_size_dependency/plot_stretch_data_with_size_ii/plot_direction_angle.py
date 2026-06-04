import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

chart_title = ''
chart_xlabel = 'Length'
chart_ylabel = 'Direction angle'

x1 = (numpy.log(8)/numpy.log(2.0)-3.0,
      numpy.log(16)/numpy.log(2.0)-3.0,
      numpy.log(24)/numpy.log(2.0)-3.0,
      numpy.log(36)/numpy.log(2.0)-3.0,
      numpy.log(48)/numpy.log(2.0)-3.0,
      numpy.log(64)/numpy.log(2.0)-3.0,
      numpy.log(80)/numpy.log(2.0)-3.0)
x1ticks = (8,16,24,32,40,56,80)#(40,160,360,640,1000,1960,4000)

y1 = (0.45,0.45,0.45,0.45,0.45,0.45,0.45)
y2 = (1.20,1.28,1.29,0.94,0.73,0.84,0.65)

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

