NDTest Command
**************

The NDTest command provides a comprehensive suite of testing functions for nDMaterial objects, allowing users to directly manipulate and query material states for testing, validation, and educational purposes. This functionality is particularly useful for material model development, verification, and understanding material behavior under controlled loading conditions.

.. warning::
   These commands are intended for material testing and debugging purposes. They should not be used in regular structural analysis models where materials should be tested through elements.

Command Syntax
==============

The general syntax for NDTest commands is:

.. code-block:: tcl

   NDTest $command $arguments

Where ``$command`` specifies the specific operation to perform on the material, and ``$arguments`` are the command-specific parameters.

Available Commands
==================

The following commands are available within the NDTest framework:

SetStrain
----------

Sets trial strain components on a specified nDMaterial.

.. code-block:: tcl

   NDTest SetStrain $matTag $eps11 $eps22 $eps33 $gamma12 $gamma23 $gamma31

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, Unique tag identifying the nDMaterial object
   $eps11, |double|, Normal strain in direction 1 (ε₁₁)
   $eps22, |double|, Normal strain in direction 2 (ε₂₂)
   $eps33, |double|, Normal strain in direction 3 (ε₃₃)
   $gamma12, |double|, Engineering shear strain γ₁₂
   $gamma23, |double|, Engineering shear strain γ₂₃
   $gamma31, |double|, Engineering shear strain γ₃₁

**Example:**

TCL:

.. code-block:: tcl

   # Set a uniaxial strain state
   NDTest SetStrain 1 0.001 0.0 0.0 0.0 0.0 0.0

Python:

.. code-block:: python

   # Set a uniaxial strain state
   op.NDTest("SetStrain", 1, 0.001, 0.0, 0.0, 0.0, 0.0, 0.0)

CommitState
-----------

Commits the current trial state of the material, making it the converged state.

.. code-block:: tcl

   NDTest CommitState $matTag

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, Unique tag identifying the nDMaterial object

**Example:**

TCL:

.. code-block:: tcl

   NDTest CommitState 1

Python:

.. code-block:: python

   op.NDTest("CommitState", 1)

PrintStrain
-----------

Prints the current strain state of the material to the OpenSees output stream.

.. code-block:: tcl

   NDTest PrintStrain $matTag

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, Unique tag identifying the nDMaterial object

PrintStress
-----------

Prints the current stress state of the material to the OpenSees output stream.

.. code-block:: tcl

   NDTest PrintStress $matTag

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, Unique tag identifying the nDMaterial object

GetStrain
----------

Returns the current strain components as a list that can be assigned to a Tcl variable.

.. code-block:: tcl

   set strainList [NDTest GetStrain $matTag]

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, Unique tag identifying the nDMaterial object

**Returns:** A list of 6 double values [ε₁₁, ε₂₂, ε₃₃, γ₁₂, γ₂₃, γ₃₁]

**Example:**

TCL:

.. code-block:: tcl

   set strains [NDTest GetStrain 1]
   puts "Strain components: $strains"

Python:

.. code-block:: python

   strains = op.NDTest("GetStrain", 1)
   print("Strain components:", strains)

GetStress
----------

Returns the current stress components as a list that can be assigned to a Tcl variable.

.. code-block:: tcl

   set stressList [NDTest GetStress $matTag]

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, Unique tag identifying the nDMaterial object

**Returns:** A list of 6 double values [σ₁₁, σ₂₂, σ₃₃, τ₁₂, τ₂₃, τ₃₁]

**Example:**

TCL:

.. code-block:: tcl

   set stresses [NDTest GetStress 1]
   puts "Stress components: $stresses"

Python:

.. code-block:: python

   stresses = op.NDTest("GetStress", 1)
   print("Stress components:", stresses)

GetTangentStiffness
-------------------

Returns the current tangent stiffness matrix as a flat list of 36 values.

.. code-block:: tcl

   set stiffnessList [NDTest GetTangentStiffness $matTag]

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, Unique tag identifying the nDMaterial object

**Returns:** A list of 36 double values representing the 6×6 tangent stiffness matrix in row-major order:
[C₁₁, C₁₂, C₁₃, C₁₄, C₁₅, C₁₆, C₂₁, C₂₂, ..., C₆₆]

**Example:**

TCL:

.. code-block:: tcl

   set tangent [NDTest GetTangentStiffness 1]
   # Access C11 component
   set C11 [lindex $tangent 0]
   # Access C26 component  
   set C26 [lindex $tangent 17]

Python:

.. code-block:: python

   tangent = op.NDTest("GetTangentStiffness", 1)
   # Access C11 component
   C11 = tangent[0]
   # Access C26 component  
   C26 = tangent[17]

GetResponse
-----------

Queries the material for custom responses specific to the material type.

.. code-block:: tcl

   set responseList [NDTest GetResponse $matTag $responseType]

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, Unique tag identifying the nDMaterial object
   $responseType, |string|, Type of response to query (material-dependent)

**Returns:** A list of double values containing the requested response data.

**Common Response Types:** (varies by material type)
- "stress" - stress components
- "strain" - strain components  
- "tangent" - tangent stiffness
- "plasticStrain" - plastic strain components
- "backstress" - backstress tensor components
- Custom material-specific responses

**Example:**

TCL:

.. code-block:: tcl

   # Get plastic strain from a plasticity model
   set plasticStrain [NDTest GetResponse 1 "plasticStrain"]
   
   # Get damage variable from a damage model
   set damage [NDTest GetResponse 1 "damage"]

Python:

.. code-block:: python

   # Get plastic strain from a plasticity model
   plastic_strain = op.NDTest("GetResponse", 1, "plasticStrain")
   
   # Get damage variable from a damage model
   damage = op.NDTest("GetResponse", 1, "damage")

UpdateIntegerParameter
-----------------------

Updates an integer parameter in the material during runtime.

.. code-block:: tcl

   NDTest UpdateIntegerParameter $matTag $paramID $newValue

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, Unique tag identifying the nDMaterial object
   $paramID, |integer|, Integer parameter identifier (material-specific)
   $newValue, |integer|, New integer value for the parameter

**Example:**

TCL:

.. code-block:: tcl

   NDTest UpdateIntegerParameter 1 1 0

Python:

.. code-block:: python

   op.NDTest("UpdateIntegerParameter", 1, 1, 0)

UpdateDoubleParameter
----------------------

Updates a double-precision parameter in the material during runtime.

.. code-block:: tcl

   NDTest UpdateDoubleParameter $matTag $paramID $newValue

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, Unique tag identifying the nDMaterial object
   $paramID, |integer|, Integer parameter identifier (material-specific)
   $newValue, |double|, New double value for the parameter

**Example:**

TCL:

.. code-block:: tcl

   NDTest UpdateDoubleParameter 1 1 2.1e-5

Python:

.. code-block:: python

   op.NDTest("UpdateDoubleParameter", 1, 1, 2.1e-5)

Usage Examples
===============

Complete Material Test Procedure
--------------------------------

Here's a complete example of how to use NDTest commands to test a material:

TCL:

.. code-block:: tcl

   # Create a simple elastic material
   nDMaterial ElasticIsotropic 1 200000 0.3

   # Test procedure 1: Uniaxial tension
   puts "=== Uniaxial Tension Test ==="
   
   # Apply strain increment
   NDTest SetStrain 1 0.001 0.0 0.0 0.0 0.0 0.0
   
   # Get and display results
   set strains [NDTest GetStrain 1]
   set stresses [NDTest GetStress 1]
   puts "Strain: $strains"
   puts "Stress: $stresses"
   
   # Commit the state
   NDTest CommitState 1

   # Test procedure 2: Shear test  
   puts "=== Pure Shear Test ==="
   NDTest SetStrain 1 0.0 0.0 0.0 0.002 0.0 0.0
   set stresses [NDTest GetStress 1]
   puts "Shear stress: $stresses"
   NDTest CommitState 1

   # Test procedure 3: Get tangent stiffness
   puts "=== Tangent Stiffness ==="
   set tangent [NDTest GetTangentStiffness 1]
   puts "C11 = [lindex $tangent 0]"
   puts "C12 = [lindex $tangent 1]"

Python:

.. code-block:: python

   import openseespy.opensees as op
   
   # Create a simple elastic material
   op.nDMaterial("ElasticIsotropic", 1, 200000, 0.3)

   # Test procedure 1: Uniaxial tension
   print("=== Uniaxial Tension Test ===")
   
   # Apply strain increment
   op.NDTest("SetStrain", 1, 0.001, 0.0, 0.0, 0.0, 0.0, 0.0)
   
   # Get and display results
   strains = op.NDTest("GetStrain", 1)
   stresses = op.NDTest("GetStress", 1)
   print("Strain:", strains)
   print("Stress:", stresses)
   
   # Commit the state
   op.NDTest("CommitState", 1)

   # Test procedure 2: Shear test  
   print("=== Pure Shear Test ===")
   op.NDTest("SetStrain", 1, 0.0, 0.0, 0.0, 0.002, 0.0, 0.0)
   stresses = op.NDTest("GetStress", 1)
   print("Shear stress:", stresses)
   op.NDTest("CommitState", 1)

   # Test procedure 3: Get tangent stiffness
   print("=== Tangent Stiffness ===")
   tangent = op.NDTest("GetTangentStiffness", 1)
   print("C11 =", tangent[0])
   print("C12 =", tangent[1])

Cyclic Loading Test
-------------------

TCL:

.. code-block:: tcl

   # Create a material with cyclic behavior
   nDMaterial J2Plasticity 1 27 0.3 0.001 300 20.0 0.0

   # Cyclic loading parameters
   set cycles 5
   set maxStrain 0.01
   set strainIncrement 0.001

   # Apply cyclic loading
   for {set cycle 0} {$cycle < $cycles} {incr cycle} {
       puts "Cycle $cycle"
       
       # Loading
       for {set i 0} {$i <= $maxStrain/$strainIncrement} {incr i} {
           set strain [expr {$i * $strainIncrement}]
           NDTest SetStrain 1 $strain 0.0 0.0 0.0 0.0 0.0
           set stress [lindex [NDTest GetStress 1] 0]
           puts "$strain $stress"
           NDTest CommitState 1
       }
       
       # Unloading
       for {set i [expr {$maxStrain/$strainIncrement}]} {$i >= 0} {incr i -1} {
           set strain [expr {$i * $strainIncrement}]
           NDTest SetStrain 1 $strain 0.0 0.0 0.0 0.0 0.0
           set stress [lindex [NDTest GetStress 1] 0]
           puts "$strain $stress"
           NDTest CommitState 1
       }
   }

Python:

.. code-block:: python

   import openseespy.opensees as op
   
   # Create a material with cyclic behavior
   op.nDMaterial("J2Plasticity", 1, 27, 0.3, 0.001, 300, 20.0, 0.0)

   # Cyclic loading parameters
   cycles = 5
   max_strain = 0.01
   strain_increment = 0.001

   # Apply cyclic loading
   for cycle in range(cycles):
       print(f"Cycle {cycle}")
       
       # Loading
       num_steps = int(max_strain / strain_increment)
       for i in range(num_steps + 1):
           strain = i * strain_increment
           op.NDTest("SetStrain", 1, strain, 0.0, 0.0, 0.0, 0.0, 0.0)
           stress = op.NDTest("GetStress", 1)[0]
           print(f"{strain} {stress}")
           op.NDTest("CommitState", 1)
       
       # Unloading
       for i in range(num_steps, -1, -1):
           strain = i * strain_increment
           op.NDTest("SetStrain", 1, strain, 0.0, 0.0, 0.0, 0.0, 0.0)
           stress = op.NDTest("GetStress", 1)[0]
           print(f"{strain} {stress}")
           op.NDTest("CommitState", 1)

Parameter Study
---------------

TCL:

.. code-block:: tcl

   # Create material
   nDMaterial ElasticIsotropic 1 200000 0.3

   # Study effect of Poisson's ratio
   set poissons {0.15 0.20 0.25 0.30 0.35 0.40}
   
   foreach nu $poissons {
       # Update Poisson's ratio
       NDTest UpdateDoubleParameter 1 2 $nu
       
       # Apply uniaxial strain
       NDTest SetStrain 1 0.001 0.0 0.0 0.0 0.0 0.0
       
       # Get lateral strain (should be -nu*axial_strain for elastic material)
       set strains [NDTest GetStrain 1]
       set lateralStrain [lindex $strains 1]
       
       puts "Poisson's ratio: $nu, Lateral strain: $lateralStrain"
       
       NDTest CommitState 1
   }

Python:

.. code-block:: python

   import openseespy.opensees as op
   
   # Create material
   op.nDMaterial("ElasticIsotropic", 1, 200000, 0.3)

   # Study effect of Poisson's ratio
   poissons = [0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
   
   for nu in poissons:
       # Update Poisson's ratio
       op.NDTest("UpdateDoubleParameter", 1, 2, nu)
       
       # Apply uniaxial strain
       op.NDTest("SetStrain", 1, 0.001, 0.0, 0.0, 0.0, 0.0, 0.0)
       
       # Get lateral strain (should be -nu*axial_strain for elastic material)
       strains = op.NDTest("GetStrain", 1)
       lateral_strain = strains[1]
       
       print(f"Poisson's ratio: {nu}, Lateral strain: {lateral_strain}")
       
       op.NDTest("CommitState", 1)

Implementation Details
======================

The NDTest command framework is implemented in ``OpenSeesNDTestCommands.cpp`` and consists of:

Core Components
---------------

1. **Command Registration System**: Uses a function map to associate command strings with their corresponding handler functions
2. **Material Interface**: Interfaces directly with the NDMaterial class hierarchy
3. **Error Handling**: Comprehensive error checking and reporting through the OpenSees opserr stream
4. **Data Conversion**: Handles conversion between OpenSees internal data structures and Tcl variables

Technical Specifications
------------------------

**Strain/Stress Ordering**: All 6-component vectors follow the engineering convention:
- Normal components: (ε₁₁, ε₂₂, ε₃₃) or (σ₁₁, σ₂₂, σ₃₃)
- Shear components: (γ₁₂, γ₂₃, γ₃₁) or (τ₁₂, τ₂₃, τ₃₁)

**Tangent Stiffness Matrix**: Returned as a flat array in row-major order for the 6×6 matrix C where:
dσ = C : dε (using tensor notation)

**Parameter Updates**: Parameter IDs are material-specific and typically defined in the material's documentation or source code.

Error Handling
==============

The NDTest commands include comprehensive error checking:

- **Material Existence**: Verifies the material tag exists before operations
- **Input Validation**: Checks for correct number and type of arguments
- **Parameter Validation**: Validates parameter ranges where applicable
- **Memory Management**: Ensures proper handling of temporary data structures

Common error messages and their meanings:

.. code-block:: text

   WARNING too few arguments: NDTest cmd?
   # Command requires additional arguments

   WARNING NDTest type UnknownCommand is unknown  
   # Command not recognized

   material with tag X does not exist
   # Material tag not found in model

   need 6 components of floating-point strains
   # SetStrain requires exactly 6 strain components

Best Practices
==============

When using NDTest commands, consider these best practices:

1. **Material Testing**: Use for isolated material testing, not in structural analyses
2. **State Management**: Always commit states when appropriate to maintain material history
3. **Error Checking**: Wrap commands in try-catch blocks when possible
4. **Documentation**: Document parameter IDs and response types for custom materials
5. **Performance**: Consider performance implications when using in loops

Integration with Analysis
=========================

While NDTest commands are primarily for material testing, they can be integrated with analysis workflows:

- **Pre-analysis Calibration**: Calibrate material parameters before main analysis
- **Post-analysis Verification**: Verify material states after analysis completion
- **Batch Testing**: Automate material testing procedures
- **Educational Use**: Demonstrate material behavior concepts

For detailed examples and advanced usage patterns, see :ref:`NDTest_examples`.

See Also
========

- :ref:`nDMaterial` - Main nDMaterial command documentation
- :ref:`matTestCommands` - Basic material testing commands
- :ref:`NDTest_examples` - Comprehensive usage examples
- Material-specific documentation for available response types and parameter IDs
- OpenSees examples repository for complete testing procedures