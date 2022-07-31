.. _build:

********************
Building Application
********************

The OpenSees applications are built using `CMake <https://cmake.org/>`_, an extensible open-source system that manages the build system. It provides a uniform build process across a range of operating systems: Windows, MacOS and different version of Linux. CMake needs to be installed on your system. For it to work, other applications such as C, C++ and Fortran compilers need to be also installed.


.. note::
   
   Most code instructions below are run from a **Terminal** application. Type **cmd** in the Windows search or **terminal** in MacOS spotlight to start the application. If you are on a Unix machine this note may cause you some amusement!


Windows 10
**********

Software Requirements
^^^^^^^^^^^^^^^^^^^^^

For Windows 10 the user must have the following applications installed on their computer: CMake, VisualStudio Basic, Intel One Basic and HPC Toolkits and Conan:

1. **CMake**: We use `CMake <https://cmake.org/download/>`_ for managing the build process. Version 3.20 or later is recommended.  

2. **Visual Studio**: `Visual Studio (Community Edition) <https://visualstudio.microsoft.com/vs/>`_ can be used. Some extensions of Visual Studio are also needed: Open Visual Studio Installer, go to Installed / More / Modify, under the Workloads tab, check Desktop development with C++ and Visual Studio extension development;   

3. **IntelOne Basic & HPC Toolkits**: Intel's `oneAPI <https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html"`_ toolkits. To install the Fortran compiler you need to install TWO toolkits, the `base toolkit <https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html>`_ and the `HPC toolkit <https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit-download.html>`_.  One advantage of installing the HPC one to obtain the Fortran compiler is that it comes with **MPI** for building and running the parallel OpenSees applications.

  .. note::

       When downloading, you do not need to sign up with Intel. After you select the Download button a new window pops up titled 'Get Your Download'. In bottom left had corner you can select the 'Continue as Guest' link to start a download without logging in.

   .. warning::

         1. The install of the latest version of the base toolkit failed for me due to issues installing Python. The error pops up right at the end. To overcome the problem, I choose to install the selected components option and choose every package BUT Python.
         2. On windows order matters, the INtel compilers come after Visual Studio. If you reverse the order or if the install was not successfullm cmake when running below will give an error message about failing to find a fortran compiler.

4. **Python**: Conan is installed via Python and as a conseequence Python must be installed. Conan requires at least Python 3.7. Builing the OpenSeesPy library requires development version installation so you have the Python header and lib files.

5. **Conan**: The build process for OpenSees uses `Conan <https://conan.io/>`_ for dependency management. Conan is a python library and can be installed using the following `instructions <https://docs.conan.io/en/latest/installation.html>`_. Version 1.25 or later is recommended. Python is installed using the Terminal application. Type the following in the Terminal window.

.. code:: console

        pip install conan
        conan profile new default --detect
	conan profile show


.. note::
    
       If the compiler name and compiler version are *not* listed, you will need to select a specific compiler. For instance, on Windows using Visual Studio 2019, you can specify the compiler as follows:

    .. code:: console

       conan profile update settings.compiler="Visual Studio" default
       conan profile update settings.compiler.version="16" default
  

Building the OpenSees Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With everything installed the build process is somewhat simple!

1. Obtain the source code:

      .. code::

         git clone https://github.com/OpenSees/OpenSees.git
	 "C:\Program Files (x86)\Intel\oneAPI\setVars" intel64 mod
	 cd OpenSees
         mkdir build
         cd build
         conan install .. --build missing
         cmake .. 
         cmake --build . --config Release --target OpenSees

.. note::

   If you plan on contributing source code to the OpenSees effort, you should fork the OpenSees github repo and clone your own fork. To clone your own fork, replace OpenSees in above with your github username.

      .. code::

         git clone https://github.com/YOUR_USER_NAME/OpenSees.git   

   
MacOS
*****

Software Requirements
^^^^^^^^^^^^^^^^^^^^^


For MacOS the user must have the following applications installed on their computer: xcode command line tools, brew, cmake, gcc, gfortran, python, and open-mpi. All the applications are installed via the command line. Some of these you can skip as you may already have them installed.

1. **XCODE Command Line Tools**: To make Apple Clang and git available, type the following in a terminal application:

   .. code:: 

      xcode-select install

.. note::
   
   #. if `xcode-select: error: command line tools are already installed, use "Software Update" to install updates` appears, skip because it's already installed.
      
   #. if `xcode-select: error: command line tools are already installed, use "Software Update" to install updates` appears, skip because it's already installed.

2. **brew**: To install the HomeBrew package manager, type the following in a terminal window:

   .. code::

      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)


3. **cmake, gfortran, python & open-mpi**. Now we will use brew to install these applications. Again from the command line type:
   

   .. code::
      
      brew install cmake
      brew install gfortran
      brew install open-mpi
      brew install python@3.9


4. **conan** In a new terminal window type
   
   .. code::
   
      pip3 install conan


Building the OpenSees Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With everything installed the build process is somehwat simple! Again from a terminal window:

      .. code::

         git clone https://github.com/OpenSees/OpenSees.git
	 cd OpenSees
         mkdir build
         cd build
         conan install .. --build missing
         cmake .. 
         cmake --build . --config Release --target OpenSees	 


.. note::

   If you plan on contributing source code to the OpenSees effort, you should fork the OpenSees github repo and clone your own fork. To clone your own fork, replace OpenSees in above with your github username.

      .. code::

         git clone https://github.com/YOUR_USER_NAME/OpenSees.git   
