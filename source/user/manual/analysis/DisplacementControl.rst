DisplacementControl Command
---------------------------

This command is used to construct a DisplacementControl integrator object. In an analysis step with Displacement Control we seek to determine the time step that will result in a displacement increment for a particular degree-of-freedom at a node to be a prescribed value.

.. function:: integrator DisplacementControl $node $dof $incr <$numIter :math`\Delta U \text{min}` $:math:\Delta U \text{max}`>

   $node, |integer|, node whose response controls solution
   $dof, |integer|, degree of freedom at the node, valid options: 1 through ndf at node.
   $incr, |float|, first displacement increment <math>\Delta U_{\text{dof}}</math>
   $numIter, |integer|, the number of iterations the user would like to occur in the solution algorithm. Optional, default = 1.0.
   $:math:`\Delta U \text{min}`, |float|,   the min step size the user will allow. optional: default :math`= \Delta U_{min} = \Delta U_0`
   $<math>\Delta U \text{max}</math>, |float|, the max step size the user will allow. optional: default :math:`= \Delta U_{max} = \Delta U_0`
   



integrator DisplacementControl 1 2 0.1; # displacement control algorithm seeking constant increment of 0.1 at node 1 at 2'nd dof.


THEORY
^^^^^^

If we write the governing finite element equation at :math:`t + \Delta t\` as:

.. math::

    R(U_{t+\Delta t}, \lambda_{t+\Delta t}) = \lambda_{t+\Delta t} F^{ext} - F(U_{t+\Delta t}) \!`

where :math:`F(U_{t+\Delta t})\!` are the internal forces which are a function of the displacements :math:`U_{t+\Delta t}\!`, :math:`F^{ext}\!` is the set of reference loads and :math:`\lambda\!` is the load multiplier. Linearizing the equation results in:

.. math::

   K_{t+\Delta t}^{*i} \Delta U_{t+\Delta t}^{i+1} = \left ( \lambda^i_{t+\Delta t} + \Delta \lambda^i \right ) F^{ext} - F(U_{t+\Delta t})

This equation represents n equations in <math> n+1</math> unknowns, and so an additional equation is needed to solve the equation. For displacement control, we introduce a new constraint equation in which in each analysis step we set to ensure that the displacement increment for the degree-of-freedom <math>\text{dof}</math> at the specified node is:

.. math::

   \Delta U_\text{dof} = \text{incr}\!</math>

MORE TO COME:


In Displacement Control the <math>\Delta_U\text{dof}</math> set to <math>t + \lambda_{t+1}</math> where,


<math> \Delta U_\text{dof}^{t+1} = \max \left ( \Delta U_{min}, \min \left ( \Delta U_\text{max}, \frac{\text{numIter}}{\text{lastNumIter}} \Delta U_\text{dof}^{t} \right ) \right ) </math>
