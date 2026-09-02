.. _build:

********************
Building Application
********************

This chapter is geared to provide information about building OpenSees applications and its Python Modules. Besides this document, there are Github Action workflows for Windows, Mac OS, and Ubuntu, which is located in ``.github/workflows/build_cmake.yml``. They will be good samples to build, though there are some differences between your computer and remote runner hosted by Github Actions because they are pre-installed many applications used for building applications.

The OpenSees applications are built using `CMake <https://cmake.org/>`_, an extensible open-source system that manages the build system. It provides a uniform build process across a range of operating systems: Windows, MacOS and different version of Linux. Thus, following applications need to be installed:

* CMake

   * Version 3.20 or later is recommended.

* Git
* C, C++, Fortran Compiler

   * Microsoft Visual Studio and Intel oneAPI Fortran Compiler (for Windows)
   * AppleClang in XCode Command Developer Tools and gfortran (for Mac)
   * gcc, g++, and gfortran (for Linux)

* Python 3.11

   * It's necessary to OpenSeesPy and also required to install conan with PyPI.

* Package Manager

   * Conan (for Windows, Linux)

      * A package build manager for C/C++ applications.

   * Homebrew (for Mac)

* MUMPS

   * A parallel solver used in OpenSees
   * This should be cloned from GitHub and built.
   * Following procedure specifies its location with relative location and assumes mumps and opensees foldera are located in a same directory.

* Libraries

   * eigen
   * hdf5
   * tcl (for Windows)
   * zlib (for Windows)
   * Intel MPI Libray (for Windows)
   * open-mpi (for Mac, Linux)
   * scalapack (for Mac, Linux)
   * lapack (for Linux)
   * Intel oneAPI Math Kernel Library (for Windows)
   * mkl (for Linux)

Obtaining OpenSees Source Code
******************************

Source codes will be obtained by Git and its command is same across different OSs.
From a terminal **cd** to the directory you want to place OpenSees. Then type the following and you'll get the source codes in the directory named ``OpenSees``.:

   .. code::

      git clone https://github.com/OpenSees/OpenSees.git

If you plan on contributing source code to the OpenSees effort, you should fork the OpenSees repository on GitHub and clone your own fork. To clone your own fork, replace OpenSees in above with your github username.

   .. code::

      git clone https://github.com/YOUR_USER_NAME/OpenSees.git

Once the repository is forked, you can catch up with ``OpenSees/OpenSees`` by ``Sync fork`` on GitHub. Once the repository is cloned, you can get updates on GitHub to type:

   .. code::

      git pull

.. note::

   Most code instructions below are run from a **Terminal** application. Type **cmd** in the Windows search or **terminal** in MacOS spotlight to start the application. If you are on a Unix machine this note may cause you some amusement!

Windows 10
**********

Software Requirements
^^^^^^^^^^^^^^^^^^^^^

For Windows 10 the user must have the following applications installed on their computer:

* CMake
* Git
* Microsoft VisualStudio
* Intel oneAPI Basic and HPC Toolkits
* Python 3.11
* conan 1.64.1
* MUMPS

Other applications will be installed by conan in the building section.

CMake
=====

   Install from `<https://cmake.org/download/>`_. Version 3.20 or later is recommended.

Git
===

   Install from `<https://gitforwindows.org/>`_.

Microsoft Visual Studio
=======================

   `Visual Studio (Community Edition) <https://visualstudio.microsoft.com/vs/>`_ can be used. Some extensions of Visual Studio are also needed: Open Visual Studio Installer, go to Installed / More / Modify, under the Workloads tab, check Desktop development with C++ and Visual Studio extension development;

   .. warning::

      The very latest release of MSVC, 2022.2, does not currently work with Intel OneAPI. Install the version 2022.1 or the 2019 version of MSVC.

Intel oneAPI Basic & HPC Toolkits
=================================

   Intel's `oneAPI <https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html>`_ toolkits. You need to install ``Intel oneAPI Math Kernel Library`` from `Base Toolkit <https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html>`_ and ``Intel MPI Library`` and ``Intel Fortran Comipler & Intel Fortran Compiler Classic`` from `HPC Toolkit <https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit-download.html>`_. One advantage of installing the HPC one to obtain the Fortran compiler is that it comes with **MPI** for building and running the parallel OpenSees applications.

   .. note::

      When downloading, you do not need to sign up with Intel. After you select the Download button a new window pops up titled 'Get Your Download'. In bottom left had corner you can select the 'Continue as Guest' link to start a download without logging in.

   .. warning::

      You should install these toolkits after Microsoft Visual Studio is installed and the integration with Microsoft Visual Studio should be enabled. If you reverse the order or if the install was not successfull, cmake when running below will give an error message about failing to find a fortran compiler.

Python 3.11
===========

   Install from `<https://www.python.org/downloads/windows/>`_. Python **3.12** or newer is not supported by OpenSeesPy currently. Python 3.10 or older version may work. Of course you can install from other channels, i.e. Anaconda, Microsoft Stores.

Conan
=====

   Conan is used to install Eigen, HDF5, Tcl and Zlib. Type the following to install:

   .. code::

      pip install conan

MUMPS
=====

   Mumps is one of the defaults solvers used in OpenSessMP and OpenSeesMP. Like OpenSees it  must be installed using **cmake**. Open a terminal window and type the following to set the intel env variables, download and then build the MUMPS library.

   .. code::

      git clone https://github.com/OpenSees/mumps.git
      cd mumps
      mkdir build
      cd build
      call "C:\Program Files (x86)\Intel\oneAPI\setVars.bat" intel64 mod
      cmake .. -Darith=d -DCMAKE_MSVC_RUNTIME_LIBRARY="MultiThreaded" -G Ninja
      cmake --build . --config Release --parallel 4

   .. note::

      Environment variables set by ``"C:\Program Files (x86)\Intel\oneAPI\setVars"`` are only available in Command Prompt just after the batch file is called. That means you should call the batch file from Command Prompt and should not from Powershell.

Building the OpenSees Applications and Python module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With everything installed the build process is somewhat simple! From a terminal window move to the folder that contains the OpenSees folder and issue the following:

.. code::

   mkdir build
   cd build
   call "C:\Program Files (x86)\Intel\oneAPI\setVars.bat" intel64 mod
   conan profile detect
   conan install .. --output-folder=conan --build=missing --settings compiler.runtime="static"
   cmake .. -DBLA_STATIC=ON -DMKL_LINK=static -DMKL_INTERFACE_FULL=intel_lp64 -DMUMPS_DIR="..\..\mumps\build" -DCMAKE_TOOLCHAIN_FILE=conan/conan_toolchain.cmake
   cmake --build . --config Release --target OpenSees -j8
   cmake --build . --config Release --target OpenSeesPy -j8
   move ./Release/OpenSeesPy.dll ./Release/opensees.pyd
   copy C:\Program Files (x86)\Intel\oneAPI\compiler\2024.1\bin\libiomp5md.dll ./Release/

When completed the executables (OpenSees, OpenSeesMP, and OpenSeesMP) and the python module (opensees.pyd) are located in the build/bin directory.

.. note::

   #. Environment variables set by ``"C:\Program Files (x86)\Intel\oneAPI\setVars"`` are only available in Command Prompt just after the batch file is called. That means you should call the batch file from Command Prompt and should not from Powershell.

   #. The -j option is used to compile the code in parallel. Change the **4** to how many cores is at your disposal.

   #. The last copy is needed as the OpenSeesPy.dll module at present actually needs to load from a file named **opensees.pyd**. To import this module in a python script you can do one of 2 things:

      #. If you have used pip to install openseespy, you can replace the opensees.pyd file in the site_package location with the opensees.pyd above. To find the location of this module, use the following:

         .. code::

            python3
            import opensees
            import inspect
            inspect.getfile(opensees)

         You may of course want to give the existing file a new name with the **copy** command before you overwrite it just in case! You can check the version of **opensees** installed by issuing ``opensees.version()`` at the python command prompt above.

      #. If you have not installed openseespy or you want to load the .pyd you built instead of the installed one you can add the path to opensees.pyd to your **PYTHONPATH** env variables. Search for **env settings** in search bar lower left. Add a line to the PYTHONPATH variable with your location of the **Release** folder. If you do this, you also need to copy the python39.dll (or the python310.dll is that is what was used INTO the bin folder). This is because of a security feature with python versions above 3.8 and the dll search path they now use.

   #. ``libiomp5md.dll`` should be located in a same folder as ``opensees.pyd`` or you'll get ``ImportError: DLL load failed while importing opensees: The specified module could not be found.`` when importing opensees on Python.

   #. Please note you will get a segmentation fault if you run with a different python exe than the one you build for. Look in output of **cmake ..** for the python library used.

   #. **conan install .. -build missing** may fail. If it is related to a **zlib** mismatch error see below. If something else and you had installed conan before, it may be related to the version ypu are using. First try installing the latest  by issuing  *pip install conan --upgrade**. Ty the build again. If it fails (and again it does not issue a warning about a zlib mismatch) try installing the bleeding head latest using the following commands issued at a terminal

      .. code::

         git clone https://github.com/conan-io/conan.git conan-io
         cd conan-io
         pip install -e .

   #. The **conan install .. --build missing** step may fail due to a **zlib mismatch**. This is due to fact that the **hdf5** and **tcl** packages used to build OpenSees both rely on **zlib** and the hdf5 group are more apt to update their package to the lastest zlib package than the tcl group. This sometimes results in the **conan** step failing. There is a fix, but it requires you do edit a file in the **tcl** package!

      In your home directory there is a **.conan** folder and in that folder there are some more folders. You need to edit the file **conanfile.py** in the folder **$HOME/.conan/data/tcl/8.6.10/_/_/export**. Change line **51** to use the same zlib as the hdf5 package, currently zlib 1.2.13, i.e. line 51 should now read **self.requires("zlib/1.2.13")**. Now go back to OpenSees/build folder and try again.

MacOS
*****

Software Requirements
^^^^^^^^^^^^^^^^^^^^^

For MacOS the user must have the following applications installed on their computer:

* xcode command line tools
   * AppleClang
   * Git
* brew
   * cmake
   * eigen
   * gfortran
   * hdf5
   * open-mpi
   * scalapack.
* mumps

All the applications are installed via the command line. Some of these you can skip as you may already have them installed.

XCode Command Line Tools
========================

   To make sure latest Xcode Command Line Tools installed, type the following in a terminal application. It's required for AppleClang and git.

   .. code::

      xcode-select install

   .. note::

      #. If `xcode-select: error: command line tools are already installed, use "Software Update" to install updates` appears, skip because it's already installed.

      #. After update of OS, XCode Command Line Tools version may have a problem. To reinstall, type:

         .. code::

            sudo rm -rf /Library/Developer/CommandLineTools
            sudo xcode-select --install

Install other dependencies via Homebrew
=======================================

   You can install HomeBrew package manager with typing the following in a terminal window:

   .. code::

      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)

   Then, you can install dependencies via Homebrew. Again from the command line type:

   .. code::

      brew install cmake
      brew install eigen
      brew install gfortran
      brew install hdf5
      brew install open-mpi
      brew install scalapack

   Eigen via **brew** is installed in ``/usr/local/include/eigen3/Eigen`` by default but ``Eigen`` should be found in ``/usr/local/include``. Then, make link by typing:

   .. code::

      sudo ln -sf /usr/local/include/eigen3/Eigen /usr/local/include/Eigen

   .. note::

      The location where eigen is installed may differ. It can be ``/opt/homebrew/include/eigen3/Eigen``

MUMPS
=====

   Mumps is one of the defaults solvers used in OpenSessMP and OpenSeesMP. Like OpenSees it  must be installed using **cmake**. Open a terminal window and type the following to set the intel env variables, download and then build the MUMPS library.

   .. code::

      git clone https://github.com/OpenSees/mumps.git
      cd mumps
      mkdir build
      cd build
      cmake .. -Darith=d
      cmake --build . --config Release --parallel 4

Building the OpenSees Applications and Python module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With everything installed the build process is somehwat simple! Again from a terminal window:

.. code::

   mkdir build
   cd build
   cmake .. -DMUMPS_DIR=$PWD/../../mumps/build
   cmake --build . --target OpenSees -j8
   cmake --build . --target OpenSeesPy -j8
   mv ./OpenSeesPy.dylib ./opensees.so

.. warning::
   #. The -j option is used to compile the code in parallel. Change the **8** to how many cores is at your disposal.

   #. Pre-installed python in ``/usr/bin`` may have problem especially on Apple Silicon Mac. It would be better to install ``python@3.11`` via brew. It will be installed in ``/usr/local/bin`` and called by ``python3.11``.

   #. ``cmake --build . --target OpenSeesPy`` yields ``OpenSeesPy.dylib`` as its target and this is exactly a python module. However, it can't be loaded from Python unless it's renamed to **opensees.so**.
      To import this module in your code, you have two options to do: 1. replacing a file of openseespy.opensees which is installed by pip3 and 2. set an environment variable ``$PYTHONPATH``.

      #. If you have used pip3 to install openseespy, you can replace the opensees.so file in the site_package location with the opensees.so above. To find the location of this module, use the following:

         .. code::

            python3
            import opensees
            import inspect
            inspect.getfile(opensees)

         You may of course want to give the existing file a new name with the **mv** command. You can check the version of **opensees** installed by issuing ``opensees.version()`` at the python command prompt above.

      #. If you have not installed openseespy or you want to load the .so you built instead of the installed one you can add the path to opensees.so to your **PYTHONPATH** env variables with ``export PYTHONPATH=$PWD`` or ``PYTHONPATH=$PWD:$PYTHONPATH`` depending on if PYTHONPATH exists when you type **env** in the terminal. NOTE: Using $PWD assumes you are in the directory containing the lib file, other put in the full path to the directory.

   #. Finally plase note you will get a segmentation fault if you run with a different python exe than the one you build for. Look in output of **cmake ..** for the python library used.

Ubuntu
******

Software Requirements
^^^^^^^^^^^^^^^^^^^^^

Needed Applications and Libraries
=================================

   For Ubuntu, the user must have a number of packages installed on their system. These can be installed following commands issued in a terminal window.

   .. code::

      sudo apt-get update
      sudo apt install -y cmake
      sudo apt install -y gcc g++ gfortran
      sudo apt install -y python3-pip
      sudo apt install -y liblapack-dev
      sudo apt install -y libopenmpi-dev
      sudo apt install -y libmkl-rt
      sudo apt install -y libmkl-blacs-openmpi-lp64
      sudo apt install -y libscalapack-openmpi-dev

Conan
=====

   Conan is used to install Eigen, HDF5, Tcl and Zlib. Type the following to install:

   .. code::

      pip install conan

Building the OpenSees Applications and Python module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With everything installed the build process is somewhat simple! Again from a terminal window enter the following commands:

   .. code::

      mkdir build
      cd build
      $HOME/.local/bin/conan profile detect
      $HOME/.local/bin/conan install .. --output-folder=conan --build missing
      cmake .. -DCMAKE_TOOLCHAIN_FILE=conan/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release
      cmake --build . --target OpenSees -j8
      cmake --build . --target OpenSeesPy -j8
      mv ./OpenSeesPy.so ./opensees.so

.. note::

   #. If you have more than **4** cores available, you can use the extra cores by changing the **4** value!

.. warning::

   #. This last copy is needed as the OpenSeesPy.dylib module at present actually needs to load from a file named **opensees.so** (go figure). Also to import this module now in your code you can do one of 2 things:

      #. If you have used pip3 to install openseespy, you can replace the opensees.so file in the site_package location with the opensees.so above. To find the location of this module, use the following:

         .. code::

            python3
            import opensees
            import inspect
            inspect.getfile(opensees)

         You may of course want to give the existing file a new name with the **mv** command. You can check the version of **opensees** installed by issuing ``opensees.version()`` at the python command prompt above.

      #. If you have not installed openseespy or you want to load the .so you built instead of the installed one you can add the path to opensees.so to your **PYTHONPATH** env variables with export PYTHONPATH=$PWD or PYTHONPATH=$PWD:$PYTHONPATH depending on if PYTHONPATH exists when you type **env** in the terminal. NOTE: Using $PWD assumes you are in the directory containg the lib file.

   #. Finally please note you will get a segmentation fault if you run with a different python exe than the one you build with. Look in output of **cmake ..** for the python library used.

   #. The **conan install .. --build missing** step may fail. This is due to fact that the **hdf5** and **tcl** packages used to build OpenSees both rely on **zlib** and the hdf5 group are more apt to update their package to the lastest zlib package than the tcl group. This sometimes results in the **conan** step failing. There is a fix, but it requires you do edit a file in the **tcl** package!

      In your home directory there is a **.conan** folder and in that folder there are some more folders. You need to edit the file **conanfile.py** in the folder **$HOME/.conan/data/tcl/8.6.10/_/_/export**. Change line **51** to use the same zlib as the hdf5 package, currently zlib 1.2.13, i.e. self.requires("zlib/1.2.13"). Now go back to OpenSees/build folder and try again.
