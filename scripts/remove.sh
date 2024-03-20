#!/bin/bash

# Script to clean up the directories after a VASP calculation
# Removes all the files except for the CONTCAR, INCAR, KPOINTS, POSCAR, POTCAR, and OUTCAR files

directories=$(ls -d */)


for dir in $directories; do
	cd $dir
        rm WAVECAR CHG CHGCAR  PCDAT XDATCAR DOSCAR EIGENVAL
        rm IBZKPT REPORT  vasp.err  vasp.out  vasprun.xml  XDATCARR
	cd ..
done


echo "done"