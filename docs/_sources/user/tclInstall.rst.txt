Tcl
===

Windows
-------

To download OpenSees.exe you can proceed to the `download page <https://opensees.berkeley.edu/OpenSees/user/download.php>`_ and enter your email address (New users may be asked to register).  Click on the link to download the file, extract it,  and place in a C:\OpenSees directory (you can place wherever you want just make appropriate changes below)

Modify the Environment Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You now need to make some changes to your environment variables as OpenSees does not include an installer which typically performs this task.

1. Open the Start Search, type in “env”, and choose “Edit the system environment variables”
2. Click the ``Environment Variables…`` button at the bottom right of the application that pop up.
3. Now we are going to edit the  **PATH** variable. Select the Path variable row to highlight it and then press the ``Edit`` button.
4. to the variables value you want to **APPEND** the following:

.. :code-block:: none
   
   C:\OpenSees\bin;

Test the Install of OpenSees
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Steps to Test:
   1. Open a command window window(type `cmd` in search)
   2. Type `OpenSees` in the application that starts (this should bring up the OpenSees interpreter)
   3. Enter the following to exit this program:
   
   .. :code-block:: tcl

      exit

MacOS
-----

To download OpenSees.exe you can proceed to the `download page <https://opensees.berkeley.edu/OpenSees/user/download.php>`_ and enter your email address (New users may be asked to register).  

Click on the link to download the file, extract it,  and place in a C:\OpenSees directory (you can place wherever you want just make appropriate changes below)

