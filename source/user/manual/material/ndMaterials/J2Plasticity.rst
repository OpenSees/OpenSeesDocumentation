.. _J2Plasticity:

J2 Plasticity Material
^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct an multi dimensional material object that has a von Mises (J2) yield criterion and isotropic hardening.

.. function:: nDMaterial J2Plasticity $matTag $K $G $sig0 $sigInf $delta $H

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, unique tag identifying material
   $K, |float|,	   bulk modulus
   $G, |float|,	   shear modulus
   $sig0, |float|,	   initial yield stress
   $sigInf, |float|,	   final saturation yield stress
   $delta, |float|,	   exponential hardening parameter
   $H, |float|,linear hardening parameter

.. note::

   The material formulations for the J2 object are "ThreeDimensional," "PlaneStrain," "Plane Stress," "AxiSymmetric," and "PlateFiber."

THEORY:

The theory for the non hardening case can be found [[1]]

J2 isotropic hardening material class

Elastic Model

.. math::

   \sigma = K*trace(\epsilon_e) + (2*G)*dev(\epsilon_e)

Yield Function

.. math::

   \phi(\sigma,q) = || dev(\sigma) || - \sqrt(\tfrac{2}{3}*q(xi)

Saturation Isotropic Hardening with linear term

.. math::
   
   q(xi) = \sigma_0 + (\sigma_\inf - \sigma_0)*exp(-delta*\xi) + H*\xi

Flow Rules

.. math::

   \dot {\epsilon_p} = \gamma * \frac{\partial \phi}{\partial \sigma}

   \dot \xi = -\gamma * \frac{\partial \phi}{\partial q}

Linear Viscosity: :math:`\gamma = \frac{\phi}{\eta}` ( if :math:`\phi > 0` )

Backward Euler Integration Routine Yield condition enforced at time n+1

set :math:`\eta = 0` for rate independent case

Code Developed by: **Ed Love**
