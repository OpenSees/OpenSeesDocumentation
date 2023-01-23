.. _rayleigh:

Rayleigh Damping Command
*******************

.. function:: rayleigh $alphaM $betaK $betaKInit $betaKcomm

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $alphaM, |float|,      factor applied to elements or nodes mass matrix
   $betaK,  |float|,     factor applied to elements current stiffness matrix.
   $betaKInit, |float|,     factor applied to elements initial stiffness matrix
   $betaKcomm, |float|,     factor applied to elements committed stiffness matrix


This command is used to assign damping to all previously-defined elements and nodes. When using rayleigh damping in OpenSees, the damping matrix for an element or node, D is specified as a combination of stiffness and mass-proportional damping matrices: 

:math:`D = \alpha_m M + \beta_k K_{current} + \beta_{k_{init}} K_{init} + \beta_{K_{comm}} K_{last commit}`


.. note::
  * The command overwrites any existing damping coeeficients at the Elements and Nodes.
  * The usage of Rayleigh damping may provide incorrect result when used with Non-Linear Time History Analysis using Concentrated Plasticity Model. [ChopraMcKenna2015]_



