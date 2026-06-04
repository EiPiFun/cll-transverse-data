import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

chart_title = ''
chart_xlable = 'Stretching velocity (nm/ns)'
chart_ylable = 'Direction angle'

x1 = (numpy.log(0.1)/numpy.log(2.0)+4.0,
      numpy.log(1.0)/numpy.log(2.0)+4.0,
      numpy.log(2.0)/numpy.log(2.0)+4.0,
      numpy.log(4.0)/numpy.log(2.0)+4.0,
      numpy.log(10.0)/numpy.log(2.0)+4.0,
      numpy.log(20.0)/numpy.log(2.0)+4.0,
      numpy.log(40.0)/numpy.log(2.0)+4.0)
x1ticks = (0.1,1.0,2.0,4.0,10.0,20.0,40.0)

y1 = (0.45,0.45,0.45,0.45,0.45,0.45,0.45)
y2 = (0.82,0.74,0.73,0.72,0.69,0.67,0.69)

y1e= (0.0002,0.0001,0.0001,0.0001,0.0001,0.0001,0.0001)
y2e= (0.038,0.010,0.009,0.010,0.010,0.010,0.010)

legend_array = ('Relaxation','Fracture')

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.10
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.xticks(x1,x1ticks,rotation=30)
plt.ylim((0.0, 1.0))

#plt.plot(x1,y1)
#plt.plot(x1,y2)
#plt.scatter(x1,y1)
#plt.scatter(x1,y2)
plt.errorbar(x1,y1,fmt=':',yerr=y1e,elinewidth=6,capsize=9)
plt.errorbar(x1,y2,fmt=':',yerr=y2e,elinewidth=6,capsize=9)

plt.title(chart_title)

plt.legend(legend_array, fontsize=20)
plt.tick_params(labelsize=20)
plt.xlabel(chart_xlable, fontsize=20)
plt.ylabel(chart_ylable, fontsize=20)

plt.savefig(current_path+'direction_angle.'+image_file_extension)

