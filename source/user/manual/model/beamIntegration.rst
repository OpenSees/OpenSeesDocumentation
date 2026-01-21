.. _beamIntegration:

Beam Integration Command
************************

This command is used to construct an integration object for certain beam elements. A wide range of numerical integration options are available in OpenSees to represent either distributed plasticity or concentrated plasticity within a single element such as the :ref:`forceBeamColumn` element.

.. function:: beamIntegration $integtaionType $tag $arg1 ...

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $integrationType, |string|, integration type
   $tag,  |integer|, unique beam integration tag.
   $args, |list|,  a list of arguments with number dependent on integration type

Following are beamIntegration types available in the OpenSees:

1. Integration Methods for Distributed Plasticity. Distributed plasticity methods permit yielding at any integration point along the element length.

.. toctree::
   :maxdepth: 4

   beamIntegrations/Lobatto
   beamIntegrations/Legendre
   beamIntegrations/NewtonCotes
   beamIntegrations/Radau
   beamIntegrations/Trapezoidal
   beamIntegrations/CompositeSimpson
   beamIntegrations/userDefined
   beamIntegrations/FixedLocation
   beamIntegrations/LowOrder
   beamIntegrations/MidDistance
   
2. Plastic Hinge Integration Methods. Plastic hinge integration methods confine material yielding to regions of the element of specified length while the remainder of the element is linear elastic. A summary of plastic hinge integration methods is found in (Scott and Fenves 2006).

.. toctree::
   :maxdepth: 4

   beamIntegrations/ConcentratedPlasticity	      
   beamIntegrations/ConcentratedCurvature
   beamIntegrations/UserHinge
   beamIntegrations/HingeMidpoint
   beamIntegrations/HingeRadau
   beamIntegrations/HingeRadauTwo
   beamIntegrations/HingeEndpoint   
   
