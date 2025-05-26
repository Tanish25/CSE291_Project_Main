
###### Steps to generate HPWL value for baseline i.e., RePLACE ######

#### START ####

## Step 1 ##

clone the OpenROAD flow scripts repository. You can find the repository here at https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts.git

## Step 2 ##

Change into the flow directory. This is where the Makefile is defined. We can find config files (config.mk) of various rtls with different technology nodes under the /flow/designs directory (the directory hierarchy is /flow/designs/technology-node/design-name/config.mk).

Run the entire flow i.e., synthesis -> Placement and Routing as defined in the makefile using the following command (read the following step (Step 3) before running this command):
DESIGN_CONFIG=./designs/tech_node/rtl/config.mk make

## Step 3 ##

The above command will start the entire ASIC flow. Since we are only interested in the placement results, we modify the makefile to avoid unnecessary runtime and memory resources on post-placement tasks. Commenting  out lines after placement in Makefile would throw errors as the final part of Makefile has code to move all files into correct directories.

We have three ways to proceed -
  1. Modify the Makefile to stop after placement and also ensure files are saved appropriately in the required directories.
  2. Run the entire process and get required information from the files that are saved after placement.
  3. Run the entire process, kill the run after we see that the tool has finished the placement phase.

We recommend using method 3 for now. We are working to update the github repository with another version of makefile that uses method 1.

## Step 4 ##

We are using HPWL values and runtimes after global placement step as metric. We can find the HPWL values and the time taken for global placement in the "3_3_place_gp.log" file under the /flow/logs/ directory.

#### END ####

Note 1: We repeat the process for every data point (both training and test dataset).

Note 2: We have updated the github repository with result files for training dataset (Gcd - Asap7, Gcd - NanGate45, Ibex - Asap7, Ibex - NanGate45, Aes - Asap7, Aes - NanGate45, Ariane - NanGate45) and for test dataset (Jpeg - Asap7, Jpeg - NanGate45). The results are under Baseline_Files_Synthesis_and_PnR/technology-node/design-name/. The HPWL values for a design are under Baseline_Files_Synthesis_and_PnR/technology-node/design-name/Logs/3_3_place_gp.log. The runtimes for a design are also under Baseline_Files_Synthesis_and_PnR/technology-node/design-name/3_3_place_gp.log.

###### Steps to generate required files for running DreamPLACE in place of RePLACE (for Global Placement) ######

DreamPLACE script requires def file before global placement and the gate-level netlist of the design as input to procude global placement files and results. The current openroad flow gives the gate level netlist only, not the def file. To generate the def file before global placement step, we proceed with the following steps.

#### START ####

## Step 1 ##

Change into the /flow/scripts/ directory and add the following line to /flow/scripts/floorplan.tcl at the end: write_def $::env(RESULTS_DIR)/floorplan.def

## Step 2 ##

Change into the flow directory. This is where the Makefile is defined. We can find config files (config.mk) of various rtls with different technology nodes under the /flow/designs directory (the directory hierarchy is /flow/designs/technology-node/design-name/config.mk).

Run the entire flow i.e., synthesis -> Placement and Routing as defined in the makefile using the following command (read the following step (Step 3) before running this command):
DESIGN_CONFIG=./designs/tech_node/rtl/config.mk make

## Step 3 ##

The above command will start the entire ASIC flow. Since we are only interested in generating the def and gate-level netlist files for DreamPLACE script, we modify the makefile to avoid unnecessary runtime and memory resources on post-floorplan tasks. Commenting  out lines after floorplanning in Makefile would throw errors as the final part of Makefile has code to move all files into correct directories.

We have three ways to proceed -
  1. Modify the Makefile to stop after floorplanning and also ensure files are saved appropriately in the required directories.
  2. Run the entire process and get the def and the gate-level netlist files from /flow/results/technology-node/design-name/base directory.
  3. Run the entire process, kill the run after we see that the tool has finished the floorplan phase.

We recommend using method 3 for now. We are working to update the github repository with another version of makefile that uses method 1.

## Step 4 ##

Then the gate level netlist along with the def file is given as input to DreamPLACE code for global placement. This way we can obtain the HPWL values from DreamPLACE script. 

#### END ####

Note 1: This process is repeated for every data point (both training and test dataset).

Note 2: We have updated the github repository with result files for training dataset (Gcd - Asap7, Gcd - NanGate45, Ibex - Asap7, Ibex - NanGate45, Aes - Asap7, Aes - NanGate45, Ariane - NanGate45) and for test dataset (Jpeg - Asap7, Jpeg - NanGate45). The def and gate-level netlist files are under Baseline_Files_For_DreamPLACE/technology-node/design-name/.

Note 3: The results directory (in the main repository) has a table that compares the runtimes of RePLACE, DreamPLACE and Customized Approach. It appears that the runtime values don't follow a trend i.e., sometimes runtime from DreamPLACE is more when compared to RePLACE and vice versa but this is because of the difference in the number of iterations both tool go through. DreamPLACE script also asks for the number of iterations. For valid comparions, We can fix on one arbitrary number of iterations and get the runtime per iteration from DreamPLACE. The "3_3_place_gp.log" file from RePLACE also shows the number of iterations the tool went through before arriving at the final state, we can get the runtime per iteration from RePLACE and compare the results. This way we need not go put manual effort in checking the "3_3_place_gp.log" file for number of iterations and then feeding the same number to the DreamPLACE script.
