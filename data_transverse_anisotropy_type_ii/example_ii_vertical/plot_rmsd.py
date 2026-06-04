import matplotlib.pyplot as plt
import numpy
import sys

current_path = sys.path[0]+'/'
x_data_file_name = sys.argv[1]
x_data_file_location = current_path+x_data_file_name
y_data_file_name = sys.argv[2]
y_data_file_location = current_path+y_data_file_name
chart_title = sys.argv[3]
chart_xlable = sys.argv[4]
chart_ylable = sys.argv[5]
scale_factor_x = float(sys.argv[6])
scale_factor_y = float(sys.argv[7])

try:
    plot_color = sys.argv[8]
except:
    plot_color = 'black'

try:
    image_file_extension = sys.argv[9]
except:
    image_file_extension = 'png'

output_image_file_location = current_path+y_data_file_name+'-'+x_data_file_name+'.'+image_file_extension

x_data = numpy.loadtxt(x_data_file_location)
y_data = numpy.loadtxt(y_data_file_location)

x = x_data[:,-1]*scale_factor_x
y = y_data[:,-1]*scale_factor_y

if x_data_file_location == y_data_file_location:
    x = x_data[:,0]*scale_factor_x

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.xlim((-0.05,0.55))
plt.ylim((0.0,0.3))
plt.yticks((0.0,0.1,0.2,0.3))

#plt.scatter(x,y)
plt.plot(x,y,color=plot_color)

plt.title(chart_title, fontsize=20)
plt.xlabel(chart_xlable, fontsize=20)
plt.ylabel(chart_ylable, fontsize=20)
plt.tick_params(labelsize=20)
plt.savefig(output_image_file_location)
