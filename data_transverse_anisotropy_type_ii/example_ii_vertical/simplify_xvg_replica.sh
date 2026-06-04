#!/usr/bin/sh

python_name=python3
if [ $# -gt 0 ];then
python_name=$1
fi
echo "Python name: $python_name"

# Relaxation-1

$python_name simplify_xvg.py rmsd-1-1.xvg 18
$python_name simplify_xvg.py rmsd-1-2.xvg 18
$python_name simplify_xvg.py rmsd-1-3.xvg 18
$python_name simplify_xvg.py rmsd-1-4.xvg 18

# Stretch

$python_name simplify_xvg.py box_size_y_stretch.xvg 24
$python_name simplify_xvg.py stress_y_stretch.xvg 24

$python_name simplify_xvg.py hbnum_stretch.xvg 25

$python_name simplify_xvg.py stretch-energy-coul-sr.xvg 24
$python_name simplify_xvg.py stretch-energy-lj-sr.xvg 24


