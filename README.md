# Project Directory Overview

## DREAMPlace_baseline
Contains DREAMPlace source files and testing configurations for the training and test designs given for the project.

## RePlAce_HPWL_evaluation
Contains results of Global Placement using RePlAce, and DEF and Gate-Level Netlists of training and test designs as required by both Electrostatic(baseline) and Transport-informed(modified) DREAMPlace scripts.

## Results
Includes result documentation comparing HPWL, runtime, and density between the baseline and modified DREAMPlace frameworks for the given training and test designs.

## transport_informed_dreamplace
Contains our fork of the DREAMPlace repository with our implementation of the Flow Based Density Overflow operation. When you navigate to this forked submodule, please view the top of the README, which contains a link to our code. We've included our report at this level of the repo as well titled: Transport Informed Gradient Fields for DREAMPlace.

# Stages of Implementation

1. The `3_2_place_iop.def` and corresponding netlist files for all test designs are sourced from OpenROAD.

2. Using these DEF and netlist files, along with reference LEF files, we run the designs through the original (Electrostatics-based) DREAMPlace framework to generate new DEF files with initial placement information.

3. These output DEF files are then used as input to RePlAce (within OpenROAD) to perform global placement and produce the final DEF files.

4. With the baseline results established, we repeat steps 2 and 3 using our modified DREAMPlace framework (transport-informed DREAMPlace) to generate placement results based on our proposed approach.

