#!/usr/bin/sh

gmx_name=$1
ntmpi_number=$2
ntomp_number=$3
mpirun_prefix=""
grompp_appendix=""
mdrun_appendix=""

home_directory=$(pwd)
echo "home directory: "$home_directory

for i in {0..9};do
for j in {0..9};do

current_working_directory=$home_directory/replica/$i$j/
echo "current working directory: "$current_working_directory
mkdir $current_working_directory

for k in vertical horizontal slant;do

cp -r $home_directory/$k/ $current_working_directory/

cd $current_working_directory/$k/

$gmx_name grompp -f em.mdp -c cellulose.gro -r cellulose.gro -p topol.top -n index.ndx -o em.tpr $grompp_appendix
$mpirun_prefix $gmx_name mdrun -deffnm em -ntmpi $ntmpi_number -ntomp $ntomp_number $mdrun_appendix

$gmx_name grompp -f relaxation-1-1.mdp -c em.gro -r em.gro -p topol.top -n index.ndx -o relaxation-1-1.tpr $grompp_appendix
$mpirun_prefix $gmx_name mdrun -deffnm relaxation-1-1 -ntmpi $ntmpi_number -ntomp $ntomp_number $mdrun_appendix
$gmx_name grompp -f relaxation-1-2.mdp -c relaxation-1-1.gro -r relaxation-1-1.gro -p topol.top -n index.ndx -o relaxation-1-2.tpr $grompp_appendix
$mpirun_prefix $gmx_name mdrun -deffnm relaxation-1-2 -ntmpi $ntmpi_number -ntomp $ntomp_number $mdrun_appendix
$gmx_name grompp -f relaxation-1-3.mdp -c relaxation-1-2.gro -r relaxation-1-2.gro -p topol.top -n index.ndx -o relaxation-1-3.tpr $grompp_appendix
$mpirun_prefix $gmx_name mdrun -deffnm relaxation-1-3 -ntmpi $ntmpi_number -ntomp $ntomp_number $mdrun_appendix
$gmx_name grompp -f relaxation-1-4.mdp -c relaxation-1-3.gro -r relaxation-1-3.gro -p topol.top -n index.ndx -o relaxation-1-4.tpr $grompp_appendix
$mpirun_prefix $gmx_name mdrun -deffnm relaxation-1-4 -ntmpi $ntmpi_number -ntomp $ntomp_number $mdrun_appendix

$gmx_name grompp -f stretch.mdp -c relaxation-1-4.gro -r relaxation-1-4.gro -p topol.top -n index.ndx -o stretch.tpr $grompp_appendix
$mpirun_prefix $gmx_name mdrun -deffnm stretch -ntmpi $ntmpi_number -ntomp $ntomp_number $mdrun_appendix

done
done
done


