#!/usr/bin/sh

gmx_name=gmx

if [ $# -gt 0 ];then
gmx_name=$1
fi

echo "gmx name: $gmx_name"

$gmx_name trjconv -f relaxation-1-1.xtc -s em.tpr -pbc nojump -dt 10 -o relaxation-1-1_nojump.gro
$gmx_name trjconv -f relaxation-1-2.xtc -s em.tpr -pbc nojump -dt 10 -o relaxation-1-2_nojump.gro
$gmx_name trjconv -f relaxation-1-3.xtc -s em.tpr -pbc nojump -dt 10 -o relaxation-1-3_nojump.gro
$gmx_name trjconv -f relaxation-1-4.xtc -s em.tpr -pbc nojump -dt 10 -o relaxation-1-4_nojump.gro

$gmx_name rms -f relaxation-1-1_nojump.gro -s em.tpr -o rmsd-1-1.xvg
$gmx_name rms -f relaxation-1-2_nojump.gro -s em.tpr -o rmsd-1-2.xvg
$gmx_name rms -f relaxation-1-3_nojump.gro -s em.tpr -o rmsd-1-3.xvg
$gmx_name rms -f relaxation-1-4_nojump.gro -s em.tpr -o rmsd-1-4.xvg

# Stretch

$gmx_name energy -f stretch.edr -o box_size_y_stretch.xvg
$gmx_name energy -f stretch.edr -o stress_y_stretch.xvg

#$gmx_name hbond -s stretch.tpr -f stretch.xtc -num hbnum_stretch.xvg

#$gmx_name mindist -s stretch.tpr -f stretch.xtc -on numcont_stretch.xvg


