# Project Directory Overview

## DREAMPlace_baseline
Contains DREAMPlace source files and testing configurations for the training and test designs given for the project.

## Metrics Extraction and Results

This section contains the methods and files that produce/contain Half-Perimeter Wirelength (HPWL) and run time values that are generated during the 'Global Placement' phase in the physical design of chips. The files corresponding to different designs (both training and test dataset) are organized in the spedific design's directory.

For the current project, we are buidling our custom machine learning model (that is an extension of DREAMPlace (Transport-informed DREAMPlace)) that will serve as a 'Placement Initializer'. To evaluate our model, we compare the HPWL and runtimes after global placement (running through RePlAce) on three different schemes i.e., Without Placement Initialization, DREAMPlace-based Placement Initialization and Transpoort-Informed DREAMPlace-based Placement Initialization.

We have segregated this repository into four directories -

--> Baseline_No_Place_Init: This contains results using RePlAce global placer without placement initialization.

--> Baseline_DREAMPlace: This contains results using RePlAce global placer with DREAMPlace-based placement initialization. Also has files required by DREAMPlace script to produce placement initialization.

--> Baseline_Transport_Informed_DREAMPlace: This contains results using RePlAce global placer with Transport-Informed DREAMPlace-based placement initialization. Also has files required by Transport-Informed DREAMPlace script to produce placement initialization.

--> Results: This contains comparisons of HPWL and Runtime values between DREAMPlace and Transport-Informed DREAMPlace across mulitple designs and technology nodes.

## transport_informed_dreamplace
Contains our fork of the DREAMPlace repository with our implementation of the Flow Based Density Overflow operation. When you navigate to this forked submodule, please view the top of the README, which contains a link to our code. We've included our report at this level of the repo as well titled: Transport Informed Gradient Fields for DREAMPlace.

**Note:** Please visit the `transport_informed_dreamplace` submodule to see our implementation of the Transport-Informed DREAMPlace. Our implementation can be used exactly as you would use the original DREAMPlace.

## Cloning Instructions

To ensure the submodule is properly cloned when cloning this repository, use:

```bash
git clone --recurse-submodules <repository-url>
```

If you've already cloned the repository without submodules, you can initialize and update them with:

```bash
git submodule update --init --recursive
```

