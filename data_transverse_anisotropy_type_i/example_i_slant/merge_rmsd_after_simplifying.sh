#!/usr/bin/sh

rm rmsd-1.xvg
for i in 1 2 3;do
total_line_number=$(wc rmsd-1-$i.xvg.txt|awk '{print $1}')
head -n $((total_line_number-1)) rmsd-1-$i.xvg.txt >> rmsd-1.xvg;done
cat rmsd-1-4.xvg.txt >> rmsd-1.xvg
awk '{printf "%e %s\n",10*(NR-1),$2}' rmsd-1.xvg > rmsd-1.xvg.txt

