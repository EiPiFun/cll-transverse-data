import matplotlib.pyplot as plt
import numpy
import pandas
import scipy
import sys

current_path = sys.path[0]+'/'
strain_data_file_name = sys.argv[1]
strain_data_file_location = current_path+strain_data_file_name
stress_data_file_name = sys.argv[2]
stress_data_file_location = current_path+stress_data_file_name
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

output_strain_energy_data_file_location = current_path+'smoothed_'+stress_data_file_name+'-'+strain_data_file_name+'_integral.txt'
output_image_file_location = current_path+'smoothed_'+stress_data_file_name+'-'+strain_data_file_name+'_integral.'+image_file_extension

strain_data = numpy.loadtxt(strain_data_file_location)
stress_data = numpy.loadtxt(stress_data_file_location)

x = strain_data[:,-1]*scale_factor_x
y = stress_data[:,-1]*scale_factor_y

window_size = numpy.max((numpy.min((int(len(x)/30),30)),1))
ys = y.copy()
ys[0:len(y)] = pandas.Series(y).rolling(window_size,min_periods=1).mean().tolist()

ys_integral = numpy.zeros(len(x))
for i in range(1,len(x)):
    ys_integral[i] = scipy.integrate.simpson(y=ys[0:i],x=x[0:i])

output_strain_energy = stress_data.copy()
output_strain_energy[:,-1] = ys_integral
numpy.savetxt(output_strain_energy_data_file_location, output_strain_energy)

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.xlim((-0.1,1.3))
plt.ylim((-0.02,0.20))

#plt.scatter(x,y)
plt.plot(x,ys_integral,color=plot_color)

plt.title(chart_title, fontsize=20)
plt.xlabel(chart_xlable, fontsize=20)
plt.ylabel(chart_ylable, fontsize=20)
plt.tick_params(labelsize=20)
plt.savefig(output_image_file_location)
