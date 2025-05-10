Equation Constraint
^^^^^^^^^^^^^^^^^^^

An equation constraint relates a certain dof at a constrained node to certain dofs at retained nodes by the equation of::

    cCoef * cDOF(cNode)
 + rCoef1 * rDOF1(rNode1)
 + rCoef2 * rDOF2(rNode2)
 + ...
 + rCoefn * rDOFn(rNoden) = 0

.. function:: equationConstraint $cNodeTag $cDOF $cCoef $rNodeTag1 $rDOF1 $rCoef1 $rNodeTag2 $rDOF2 $rCoef2 ... $rNodeTagn $rDOFn $rCoefn

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $cNodeTag, |integer|, integer tag identifying the constrained node (cNode)
   $cDOF, |integer|,  nodal degrees-of-freedom that is constrained at the cNode
   $cCoef, |float|,  coefficient associated with cNode
   $rNodeTag1, |integer|, integer tag identifying the 1st retained node (rNode1)
   $rDOF1, |integer|,  nodal degrees-of-freedom that is retained at the rNode1
   $rCoef1, |float|,  coefficient associated with rNode1
   $rNodeTag2, |integer|, integer tag identifying the 2nd retained node (rNode2)
   $rDOF2, |integer|,  nodal degrees-of-freedom that is retained at the rNode2
   $rCoef2, |float|,  coefficient associated with rNode2
   $rNodeTagn, |integer|, integer tag identifying the nth retained node (rNoden)
   $rDOFn, |integer|,  nodal degrees-of-freedom that is retained at the rNoden
   $rCoefn, |float|,  coefficient associated with rNoden

Code developed by: Yuli Huang
