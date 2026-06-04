#!/usr/bin/sh

cat ./hbnum_stretch_1.xvg >> ./hbnum_stretch.xvg
for i in 2 3 4 5;do
total_line_number=$(wc hbnum_stretch_$i.xvg|awk '{print $1}')
tail -n $((total_line_number-25)) hbnum_stretch_$i.xvg >> hbnum_stretch.xvg;done

