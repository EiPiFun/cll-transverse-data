#!/usr/bin/sh

python_name=python3
plot_color=black
image_file_extension=png

if [ $# -gt 0 ];then
python_name=$1
fi
if [ $# -gt 1 ];then
plot_color=$2
fi
if [ $# -gt 2 ];then
image_file_extension=$3
fi

echo "Python name: $python_name"
echo "Plot color: $plot_color"
echo "Image file extension: $image_file_extension"

# Critical data

$python_name generate_strain.py box_size_y_stretch.xvg.txt strain_y_stretch.xvg.txt
$python_name extract_critical_data.py strain_y_stretch.xvg.txt stress_y_stretch.xvg.txt "1.0" "-0.1"
$python_name extract_smoothed_critical_data.py strain_y_stretch.xvg.txt stress_y_stretch.xvg.txt "1.0" "-0.1"

# Relaxation-1

$python_name plot_rmsd.py rmsd-1.xvg.txt rmsd-1.xvg.txt "" "Time (ns)" "RMSD (nm)" "0.001" "1.0" $plot_color $image_file_extension

# Stretch

$python_name plot_and_save_the_smoothed_stress.py strain_y_stretch.xvg.txt stress_y_stretch.xvg.txt "" "Strain" "Stress (GPa)" "1.0" "-0.0001" $plot_color $image_file_extension
$python_name plot_and_save_the_smoothed_integral_stress.py strain_y_stretch.xvg.txt stress_y_stretch.xvg.txt "" "Strain" "Strain energy (GPa)" "1.0" "-0.0001" $plot_color $image_file_extension

$python_name plot_and_save_the_smoothed_delta_to_minimal_hbond.py strain_y_stretch_cut.xvg.txt hbnum_stretch.xvg.txt "" "Strain" "delta Hydrogen Bond Number" "1.0" "1.0" $plot_color $image_file_extension

$python_name plot_and_save_the_smoothed_delta_to_minimal_energy.py strain_y_stretch_cut.xvg.txt stretch-energy-coul-sr.xvg.txt "" "Strain" "delta Coul-SR (kJ/mol)" "1.0" "1.0" $plot_color $image_file_extension
$python_name plot_and_save_the_smoothed_delta_to_minimal_energy.py strain_y_stretch_cut.xvg.txt stretch-energy-lj-sr.xvg.txt "" "Strain" "delta LJ-SR (kJ/mol)" "1.0" "1.0" $plot_color $image_file_extension

$python_name plot_angle.py strain_y_stretch_cut.xvg.txt stretch_direction_angle.txt "" "Strain" "Direction angle" "1.0" "1.0" $plot_color $image_file_extension


