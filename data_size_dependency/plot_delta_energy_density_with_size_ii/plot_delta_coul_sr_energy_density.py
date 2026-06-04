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
chart_ylabel = r'delta Coul-SR density (kJ/mol/$\rm{nm^3}$)'

x1 = (numpy.log(8)/numpy.log(2.0)-3.0,
      numpy.log(16)/numpy.log(2.0)-3.0,
      numpy.log(24)/numpy.log(2.0)-3.0,
      numpy.log(36)/numpy.log(2.0)-3.0,
      numpy.log(48)/numpy.log(2.0)-3.0,
      numpy.log(64)/numpy.log(2.0)-3.0,
      numpy.log(80)/numpy.log(2.0)-3.0)
x1ticks = (8,16,24,32,40,56,80)#(40,160,360,640,1000,1960,4000)

y1 = (-64.09,-33.11,-33.78,-29.39,-23.32,-21.59,-22.11)
y2 = ( 37.68, 29.39, 27.46, 26.24, 25.06, 26.26, 25.35)

#legend_array = ('Coul-SR','LJ-SR')

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.xticks(x1, x1ticks)
plt.ylim((-80.0, 0.0))

plt.plot(x1,y1)
#plt.plot(x1,y2)
plt.scatter(x1,y1)
#plt.scatter(x1,y2)

plt.title(chart_title, fontsize=20)
#plt.legend(legend_array, fontsize=20)

plt.tick_params(labelsize=20)
plt.xlabel(chart_xlabel, fontsize=20)
plt.ylabel(chart_ylabel, fontsize=18)

plt.savefig(current_path+'delta_coul_sr_energy_density.'+image_file_extension)

