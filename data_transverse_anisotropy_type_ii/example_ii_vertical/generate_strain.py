import numpy
import sys

current_path = sys.path[0]+'/'
box_length_data_file_name = sys.argv[1]
box_length_data_file_location = current_path+box_length_data_file_name
output_strain_data_file_name = sys.argv[2]
output_strain_data_file_location = current_path+output_strain_data_file_name

box_length_data = numpy.loadtxt(box_length_data_file_location)
output_strain_data = box_length_data.copy()
output_strain_data[:,-1] = abs(box_length_data[:,-1]/box_length_data[0,-1]-1.0)

numpy.savetxt(output_strain_data_file_location, output_strain_data)
