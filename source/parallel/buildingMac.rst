Building On a MAC
=================

Building OpenSees Sequential Version
------------------------------------


Building Parallel Versions
--------------------------

1. Download latest stable release from `OpenMPI <https://www.open-mpi.org/>`_, which at time of writing was openmpi-4.0.2. We downloaded into Downloads: openmpi-4.0.2.tar.gz

.. code:: bash

   cd ~/Downloads
   tar zxBf openmpi-4.0.2.tar.gz
   cd openmpi-4.0.2/
   ./configure --prefix=/usr/local/openmpi
   make -j 4
   sudo make install
   usr/local/openmpi/bin/mpirun --version

   	mpirun (Open MPI) 4.0.2

	Report bugs to http://www.open-mpi.org/community/help/
   
.. note::
   gfortran was previously installed on our machine. 

2. Install Some Other Software
------------------------------


