.. _build:

********************
Building Application
********************

The OpenSees applications are built using `CMake <https://cmake.org/>`_, an extensible open-source system that manages the build system. It provides a uniform build process across a range of operating systems: Windows, MacOS and different version of Linux. CMake needs to be installed on your system.

.. note::
   All code instructions below are run from a **Terminal** application. Type cmd in the Windows search or terminal in MacOS spotlight to start the application. If you are on a Unix machine this note may cause you some amusement!

To build the OpenSees applications you need C, C++ and Fortran compilers, MPI is and development Python is optional. The `Conan <https://conan.io/>`_ package manager system is also optional, but it will install on your system some needed external libraries which you are required to install by yourself if you don't wish to uses conan. These external libraries are: mysql, tcl, HDF5.

The following provides links to the software required.

* **C++17 compliant compiler**: many of the newer code being added by developers use C++17 features; consequently, a newer C++17 compliant compiler is suggested. For Windows users, MSVC in `Visual Studio (Community Edition) <https://visualstudio.microsoft.com/vs/>`_ can be used. Some extensions of Visual Studio are also needed: Open Visual Studio Installer, go to Installed / More / Modify, under the Workloads tab, check Desktop development with C++ and Visual Studio extension development;

* **Fortran Compiler**: There are not many free options for Windows. We suggest Intel's `oneAPI <https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html"`_ toolkits. To install the Fortran compiler you need to install TWO toolkits, the `base toolkit <https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html>`_ and the `HPC toolkit <https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit-download.html>`_.  One advantage of installing the HPC one to obtain the Fortran compiler is that it comes with **MPI** for building and running the parallel OpenSees applications.

  .. note::

       When downloading, you do not need to sign up with Intel. After you select the Download button a new window pops up titled 'Get Your Download'. In bottom left had corner you can select the 'Continue as Guest' link to start a download without logging in.

   .. warning::

         1. The install of the latest version of the base toolkit failed for me due to issues installing Python. The error pops up right at the end. To overcome the problem, I choose to install the selected components option and choose every package BUT Python.
         2. On windows order matters, the INtel compilers come after Visual Studio. If you reverse the order or if the install was not successfullm cmake when running below will give an error message about failing to find a fortran compiler.
   

* **CMake**: We use `CMake <https://cmake.org/download/>`_ for managing the build process. Version 3.20 or later is recommended.  

* **Python**: Conan requires at least Python 3.7. Builing the OpenSeesPy library requires development version installation so you have the Python header and lib files.

* **Conan**: This repository uses `Conan <https://conan.io/>`_ for dependency management. Conan is a python library and can be installed using the following `instructions <https://docs.conan.io/en/latest/installation.html>`_. Version 1.25 or later is recommended.

  1. Conan is installed with pip.

    .. code:: console

        pip install conan

    .. note::

       If on Mac or when you use python you invoke python3, use **pip3** instaed of **pip** in the above.
  
   2. Once installed, on Windows you need a default Conan profile to be set up for building packages.

    .. code:: console

        conan profile new default --detect

   3. You can check the default profile of your build environment using:

    .. code:: console

       conan profile show default

   4. If the compiler name and compiler version are *not* listed, you will need to select a specific compiler. For instance, on Windows using Visual Studio 2019, you can specify the compiler as follows:

    .. code:: console

       conan profile update settings.compiler="Visual Studio" default
       conan profile update settings.compiler.version="16" default
  
**********************************
Building the OpenSees Applications
**********************************

With everything installed the build process is somewhat simple!

1. Obtain the source code:

      .. code::

         git clone https://github.com/OpenSees/OpenSees.git

    #. To build the applications you need to now navigate to the **OpenSees** folder that was created with the **git clone** command. Once there you will issue the following set of commands to create a **build** folder, change director to that folder, install needed software using conan, and finally use **cmake** to build and install thge applications. The following are the set of commands to type in the terminal (see notes below the code block if the commands fail).

For those developers using the Windows operating system, in a terminal you need to type the following (NOTE Powershell is different):

     .. code:: console

	  "C:\Program Files (x86)\Intel\oneAPI\setVars" intel64 mod
          mkdir build
          cd build
          conan install .. --build missing
          cmake .. -G "Visual Studio 16 2019"
          cmake --build . --config Release
          cmake --install .
          cd ..

.. note::

   1. The intel compilers don't change anything on user PATH when installing. The first command is setting up the environment variables for the terminal shell you are in. It only needs to be called once.
   2. On Windows, it is necessary to specify a compiler for CMake. This is done with the -G option. If you have installed a different Visual Studio version, type the following at the command line to see options available.

     .. code:: console

          cmake --help
      
.. warning::

   If you have multiple Visual Studio's installed, it is necessary the conan profile and the -G selection to match otherwise the third step will fail.

