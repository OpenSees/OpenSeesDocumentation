.. _mpcoRecorder:

MPCO Recorder
^^^^^^^^^^^^^

| The MPCO recorder type records the response of a number of nodes and/or elements at every (or some) converged step.
| Results are stored in a HDF5 database (https://www.hdfgroup.org/solutions/hdf5/). **Hierarchical Data Format** (HDF) is designed to store and organize large amounts of data. Originally developed at the U.S. National Center for Supercomputing Applications, it is now supported by The HDF Group.
| The MPCO recorder is developed by ASDEA Software Technology (https://asdea.eu/software/) to produce a result database that can be read by the pre/post-processor **STKO** (Scientific ToolKit for OpenSees, https://asdea.eu/software/about-stko/).
| However the output file is a HDF5 database, so it can also be read/edited by any other tool that can handle HDF5 databases. Among them it is worth mentioning:
* **HDFView**, a browser and editor for HDF files (https://www.hdfgroup.org/downloads/hdfview/).
* **h5py**, the python interface to HDF5 files (https://www.h5py.org/, https://pypi.org/project/h5py/).
| The command to create a MPCO recorder is:

.. function::
   recorder mpco $fileName
   <-N $NResp1 $NResp2 ... $NRespN>
   <-E $EResp1 $EResp2 ... $ERespN>
   <-NS $NSResp1 $SPar1 $NSResp2 $SPar2 ... $NSRespN $SParN>
   <-R $regionTag> <-T dt $deltaTime> <-T nsteps $numSteps>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $fileName, |string|, "Name of file to which output is sent"
   -N, |string|, "Optional, used to start the list of node responses to record"
   NResp1 $NResp2 ... $NRespN, list of |string|, "Strings indicating the requested node responses (they follow the -N option)"
   -E, |string|, "Optional, used to start the list of element responses to record"
   $EResp1 $EResp2 ... $ERespN, list of |string|, "Strings indicating the requested element responses (they follow the -E option)"
   -NS, |string|, "Optional, used to start the list of node sensitivity responses to record"
   $NSResp1 $SPar1 $NSResp2 $SPar2 ... $NSRespN $SParN, list of (|string| + |integer|), "Strings indicating the requested node sensitivity responses. Each string must be followed by an integer indicating the associated sensitivity parameter. (they follow the -NS option)"
   -R $regionTag, |string| + |integer|, "Optional, used to specify a region of the model to be recorded. If omitted (Default) the recorder will record the whole model. This pair can be repeated multiple times if you want to record multiple regions"
   -T dT $deltaTime, 2 |string| + |float|, "Optional, used to specify the time interval for recording. If omitted, the recorder will record every time step. $deltaTime is the time interval for recording. Will record when then next step is $deltaTime greater than the last recorded step"
   -T nsteps $numSteps, 2 |string| + |integer|, "Optional, used to specify the step interval for recording. If omitted, the recorder will record every time step. $numSteps is the time step interval for recording. Will record every $numSteps steps"

Usage Notes
"""""""""""

.. note::
   1. The recording frequency options **<-T dT $deltaTime>** and **<-T nsteps $numSteps>** are mutually exclusive. If you define the -T option more than once, only the last one will be considered.
   
   2. **Node responses** are the following:
      
      .. csv-table:: 
         :header: "Name", "Description"
         :widths: 10, 40
      
         **displacement**, "Translational part of the displacement field"
         **rotation**, "Rotational part of the displacement field"
         **velocity**, "Translational part of the velocity field"
         **angularVelocity**, "Rotational part of the velocity field"
         **acceleration**, "Translational part of the acceleration field"
         **angularAcceleration**, "Rotational part of the acceleration field"
         **reactionForce**, "Translational part of the reaction field"
         **reactionMoment**, "Rotational part of the reaction field"
         **reactionForceIncludingInertia**, "Translational part of the reaction field with inertia terms"
         **reactionMomentIncludingInertia**, "Rotational part of the reaction field with inertia terms"
         **rayleighForce**, "Translational part of the damping force field"
         **rayleighMoment**, "Rotational part of the damping force field"
         **unbalancedForce**, "Translational part of the unbalanced force field"
         **unbalancedForceIncludingInertia**, "Translational part of the unbalanced force field with inertia terms"
         **unbalancedMoment**, "Rotational part of the unbalanced force field"
         **unbalancedMomentIncludingInertia**, "Rotational part of the unbalanced force field with inertia terms"
         **pressure**, "Pore pressure field"
         **modesOfVibration**, "Translational part of the eigenvector fields (all modes are recorded)"
         **modesOfVibrationRotational**, "Rotational part of the eigenvector fields (all modes are recorded)"
   
   
   3. **Node sensitivity responses** are the following:
      
      .. csv-table:: 
         :header: "Name", "Description"
         :widths: 10, 40
      
         **displacementSensitivity**, "Translational part of the displacement sensitivity field"
         **rotationSensitivity**, "Rotational part of the displacement sensitivity field"
         **velocitySensitivity**, "Translational part of the velocity sensitivity field"
         **angularVelocitySensitivity**, "Rotational part of the velocity sensitivity field"
         **accelerationSensitivity**, "Translational part of the acceleration sensitivity field"
         **angularAccelerationSensitivity**, "Rotational part of the acceleration sensitivity field"
   
   
   4. | **Element responses** in OpenSees depend on the element/section/material used in the model.
      | Assuming **“RES”** is a valid response type for some elements in the model:
      * **RES** will record the element result “RES”. In this case “RES” must be a valid response for the element.
      * **material.RES** will record the material result “RES” for each integration point in continuum elements. In this case “RES” must be a valid response for the materials assigned to the element’s integration points.
      * **section.RES** will record the section result “RES” for each section in structural elements (truss, beams, shells, etc..). In this case “RES” must be a valid response for the sections assigned to the element’s integration points.
      * **section.fiber.RES** will record the material result “RES” for each fiber in each section in structural elements (beams or shells). In this case “RES” must be a valid response for the material assigned to the fibers of the fiber cross section at the element’s integration points.

Examples
""""""""

.. admonition:: Example 1

   .. code:: tcl

      recorder mpco "fiber_beams.mpco" \
         -N displacement rotation reactionForce reactionMoment modesOfVibration \
         -E force section.force section.fiber.stress

   This example creates the HDF5 database “fiber_beams.mpco”. It records the following node responses: displacement, rotation, reactionForce, reactionMoment and modesOfVibration. Furthermore it records the following element responses: force (forces at element nodes), section.force (generalized beam forces at each section in local coordinate system), and section.fiber.stress (uniaxial stress field in each fiber of each section of the elements).

.. admonition:: Example 2

   .. code:: tcl

      recorder mpco "fiber_beams.mpco" \
         -N displacement rotation reactionForce reactionMoment modesOfVibration \
         -E force section.force section.fiber.stress \
         -R 1

   Same as example 1, but records only nodes and elements in region 1 of the model.

.. admonition:: Example 3

   .. code:: tcl

      recorder mpco "fiber_beams.mpco" \
         -N displacement rotation reactionForce reactionMoment modesOfVibration \
         -E force section.force section.fiber.stress \
         -R 1 \
         -T dt 0.01

   Same as example 2, but records a step only if the domain time of the current step minus the domain time of the previous recorded step is greater then 0.01 seconds.


Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.