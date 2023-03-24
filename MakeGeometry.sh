python clearfolder.py

#python TNT_3D.py
#python RP503_LevelSetMesh_test.py
python ConeBlastGeometry_LS.py
#mpirun -np 3 ./MeshfreeVis
#python AirBackedChamberv2.py
#python CompositePlateStretched.py
#matlab -batch "NodeSetGenerator('Plate1.txt')" #Optional for application of BC on Peridigm Side


#python ConeBlastGeometry_Qsim.py
#mpirun -np 3 ./MeshfreeVis
#python AirBackedChamberv2.py
#python CompositePlateStretched.py
#matlab -batch "NodeSetGenerator('Plate1.txt')"

#mpirun -np 4 ./MeshfreeVis

tar -vcf Foreground.tar.gz ./fore*

#scp foreground* *txt Geometry.dat  sshende@stampede2.tacc.utexas.edu:\$WORK2/AirBlastTest3D_withCompB/

scp Foreground* *txt Block1.txt sshende@stampede2.tacc.utexas.edu:\$SCRATCH/ConeBlast_Final_5e8_timestep17/

#scp Fore* *txt Geometry.dat ElementInfo* sshende@stampede2.tacc.utexas.edu:\$SCRATCH/Peridynamic_UNDEX_NoAir_FULL_TEST8_152mm/
#cp foreground* *txt Geometry.dat Plate1.txt ~/Desktop/petsc-3.15.2/PetIGA/demo/PeridigmIGA/PeridigmDriver/GCC_4.7.2_OPT/src/
#scp  Geometry.dat sshende@stampede2.tacc.utexas.edu:\$SCRATCH/LevelSets/LevelSet_TNT/Geo
#scp  Geometry.dat sshende@stampede2.tacc.utexas.edu:\$SCRATCH/LevelSets/LevelSet_TNT/Geo
#scp  Geometry.dat Fore* *.txt sshende@stampede2.tacc.utexas.edu:\$SCRATCH/LevelSets/LevelSet_RP503_Elastic_Plastic_Shell/

#scp foreground* *txt Geometry.dat Block1.txt sshende@stampede2.tacc.utexas.edu:\$SCRATCH/ConeBlast_Final_5e8_timestep2/
#tar -vcf Foreground.tar.gz ./fore*
#scp Fore* *txt Geometry.dat ElementInfo* sshende@stampede2.tacc.utexas.edu:\$SCRATCH/Peridynamic_UNDEX_NoAir_FULL_TEST8_152mm/
#cp foreground* *txt Geometry.dat Plate1.txt ~/Desktop/petsc-3.15.2/PetIGA/demo/PeridigmIGA/PeridigmDriver/GCC_4.7.2_OPT/src/
#scp Foreground* *txt Geometry.dat Block1.txt sshende@stampede2.tacc.utexas.edu:\$SCRATCH/ConeBlast_Final_5e8_timestep11/

#scp *.txt   sshende@stampede2.tacc.utexas.edu:\$WORK2/Peridynamic_UNDEX
#scp Left.txt   sshende@stampede2.tacc.utexas.edu:\$HOME/petsc-3.15.2/PetIGA/demo/PeridigmIGA/PeridigmDriver/GCC_4.7.2_OPT/src
#scp Top.txt   sshende@stampede2.tacc.utexas.edu:\$HOME/petsc-3.15.2/PetIGA/demo/PeridigmIGA/PeridigmDriver/GCC_4.7.2_OPT/src
#scp Bottom.txt sshende@stampede2.tacc.utexas.edu:\$HOME/petsc-3.15.2/PetIGA/demo/PeridigmIGA/PeridigmDriver/GCC_4.7.2_OPT/src
#scp Geometry.dat Geometry.vtk sshende@stampede2.tacc.utexas.edu:\$WORK2/ConeBlast_FULL_TEST/Geo/
#scp Geometry.dat Geometry.vtk sshende@stampede2.tacc.utexas.edu:\$WORK2/Peridynamic_UNDEX_NoAir_FULL_TEST4/Geo/

#scp Plate1.txt   sshende@stampede2.tacc.utexas.edu:\$WORK2/Peridynamic_UNDEX
