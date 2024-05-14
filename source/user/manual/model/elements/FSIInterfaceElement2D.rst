.. _FSIInterfaceElement2D:

FSIInterfaceElement2D Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Description
###########
This command is used to construct an FSIInterfaceElement2D element object. The FSIInterfaceElement2D element is a 2-node linear acoustic-structure interface element object with the following features:

#. It is based on the Eulerian pressure formulation ([ZienkiewiczEtAl1978]_ , [ZienkiewiczEtAl2000]_ , [LøkkeEtAl2017]_ ) for (Class I) fluid-structure interaction problems.
#. It couples the structure and fluid domains.
#. It uses a 2 integration points Gauss quadrature.
#. It has three DOFs per node: two displacements and one pressure DOF. The nodes on the fluid side of the interface between the acoustic/fluid and the solid domains share the same coordinates.

Input Parameters
################

.. function:: element FSIInterfaceElement2D $eleTag $n1 $n2 $rho <-thickness $thickness>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, integer, unique integer tag identifying element object
   $n1 $n2, 2 integers, the two nodes defining the element (-ndm 2 -ndf 3)
   $rho, float, the mass density of the fluid domain (acoustic medium)
   Optional:
   $thickness, float, the thickness in 2D problems (default 1.0).

.. figure:: figures/FSI_FE/FSIInterfaceElement2D_geometry.png
	:align: center
	:figclass: align-center
	:width: 50%
       
	**Figure 1. Nodes and local coordinate system**

Theory
######

For additional documentation regarding the derivation of the implemented finite elements (`FSIFluidElement2D <https://github.com/esimbort/OpenSeesDocumentation/blob/master/source/user/manual/model/elements/FSIFluidElement2D.rst>`_, `FSIFluidBoundaryElement2D <https://github.com/esimbort/OpenSeesDocumentation/blob/master/source/user/manual/model/elements/FSIFluidBoundaryElement2D.rst>`_, FSIInterfaceElement2D) based on the Eulerian pressure formulation, please refer to the attached PDF document (`Link to PDF <https://drive.google.com/drive/folders/1QnWEC6kJrFct5korO89bqL1lcn7zi4yG>`_)

Example on how to define a single interface element
################################################### 

   1. **Tcl Code**

   .. code-block:: tcl

      # set up a 2D-3DOF model
      model Basic -ndm 2 -ndf 3
      node 11  0.0  0.0
      node 22  1.0  1.0
      
      # create the acoustic-structure interface element with input variable rhoW
      set rhoW 1.000000e+03;  # mass density of water
      element FSIInterfaceElement2D 2   11 22   $rhoW -thickness 1.0

   2. **Python Code**

   .. code-block:: python

      # set up a 2D-3DOF model
      model('Basic', '-ndm', 2, '-ndf', 3)
      node(11, 0.0, 0.0)
      node(22, 1.0, 1.0)
      
      # create the acoustic-structure interface element with input variable rhoW
      rhoW = 1.000000e+03  # mass density of water
      element('FSIInterfaceElement2D', 2, 11, 22, rhoW, thickness=1.0)

Code Developed, implemented and tested by:

| `Massimo Petracca <mailto:m.petracca@asdea.net>`_ (ASDEA Software),
| `Enrique Simbort <mailto:egsimbortzeballos@ucsd.edu>`_ (UC San Diego),
| `Joel Conte <mailto:jpconte@ucsd.edu>`_ (UC San Diego).

References
##########

.. [ZienkiewiczEtAl1978] Zienkiewicz O.C., Bettess P. (1978) "Fluid-structure dynamic interaction and wave forces. An introduction to numerical treatment", Inter. J. Numer. Meth. Eng.., 13(1): 1–16. (`Link to article <https://onlinelibrary.wiley.com/doi/10.1002/nme.1620130102>`_)
.. [ZienkiewiczEtAl2000] Zienkiewicz O.C., Taylor R.L. (2000) "The Finite Element Method", Butterworth-Heinemann, Vol.1, 5th Ed., Ch.19.
.. [LøkkeEtAl2017] Løkke A., Chopra A.K. (2017) "Direct finite element method for nonlinear analysis of semi-unbounded dam–water–foundation rock systems", Earthquake Engineering and Structural Dynamics 46(8): 1267–1285. (`Link to article <https://onlinelibrary.wiley.com/doi/abs/10.1002/eqe.2855>`_)
