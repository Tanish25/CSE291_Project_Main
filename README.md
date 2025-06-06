# Project Directory Overview

## DREAMPlace_Baseline_Top
Contains DREAMPlace source files and testing configurations for the training circuits given for the project.

## Synthetic_Netlist_Generator
Contains source files for generating netlists based on parameter configurations and source LEF files.

## Results
Contains results of Global Placement using RePlAce, and DEF and Gate-Level Netlists of training and test designs as required by DREAMPlace script.

This section contains the methods and files that produce/contain Half-Perimeter Wirelength (HPWL) and run time values thatt are generated during the 'Global Placement' phase in the physical design of chips. The files corresponding to different designs (both training and test dataset) are organized in the spedific design's directory.

For the current project, we are buidling our custom machine learning model (that is an extension of DREAMPlace (Transport-informed DREAMPlace)) that will serve as a 'Placement Initializer'. To evaluate our model, we compare the HPWL and runtimes after global placement (running through RePlAce) on three different schemes i.e., Without Placement Initialization, DREAMPlace-based Placement Initialization and Transpoort-Informed DREAMPlace-based Placement Initialization.

We have segregated this repository into three directories -

Baseline_No_Place_Init: This contains results using RePlAce global placer without placement initialization.
Baseline_DREAMPlace: This contains results using RePlAce global placer with DREAMPlace-based placement initialization.
Baseline_Transport_Informed_DREAMPlace: This contains results using RePlAce global placer with Transport-Informed DREAMPlace-based placement initialization.

## transport_informed_dreamplace
Contains our fork of the DREAMPlace repository with our implementation of the Flow Based Density Overflow operation. When you navigate to this forked submodule, please view the top of the README, which contains a link to our code and current progress. We've included our report at this level of the repo as well titled: Transport Informed Gradient Fields for Global Placement
