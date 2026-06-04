import numpy
import pandas
import scipy
import sys

current_path = sys.path[0]+'/'
strain_data_file_name = sys.argv[1]
strain_data_file_location = current_path+strain_data_file_name
stress_data_file_name = sys.argv[2]
stress_data_file_location = current_path+stress_data_file_name
output_critical_data_file_location = current_path+'critical_data-'+stress_data_file_name+'-'+strain_data_file_name+'.txt'
scale_factor_x = float(sys.argv[3])
scale_factor_y = float(sys.argv[4])

strain_data = numpy.loadtxt(strain_data_file_location)
stress_data = numpy.loadtxt(stress_data_file_location)

x = strain_data[:,-1]*scale_factor_x
y = stress_data[:,-1]*scale_factor_y

y_integral = numpy.zeros(len(x))
for i in range(1,len(x)):
    y_integral[i] = scipy.integrate.simpson(y=y[0:i],x=x[0:i])

max_stress = numpy.max(y)
max_strain_energy = numpy.max(y_integral)

fracture_stress = 0.1*max_stress
fracture_strain = 0.0
fracture_strain_energy = 0.9*max_strain_energy

for i in range(0,len(x)):
    if abs(y[i]) < fracture_stress and y_integral[i] > fracture_strain_energy:
        fracture_strain = strain_data[i,-1]
        fracture_stran_energy = y_integral[i]
        break

#critical_data = (max_stress,fracture_strain,fracture_strain_energy)
critical_data = (max_stress,fracture_strain,max_strain_energy)

numpy.savetxt(output_critical_data_file_location, critical_data)
