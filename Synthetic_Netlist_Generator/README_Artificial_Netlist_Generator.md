# Artificial Netlist Generator

## Overview

This project utilizes and customizes the open-source **Artificial Netlist Generator** to generate synthetic netlists for digital design benchmarks. The original repository was cloned and modified to suit the specific requirements of our project, including adapting configurations for different LEF types and design constraints.

## Modifications and Customization

We enhanced the original codebase by adjusting the netlist generation parameters and configurations. These updates help match the output with our target design libraries and project-specific constraints.

## Dependencies Required for Building

To build the project, the following system dependencies are required:

```bash
sudo apt install libspdlog-dev
sudo apt install libboost-all-dev
sudo apt install flex
sudo apt install bison
sudo apt-get install tcl-dev
```

Additional modifications:

- Manually copied `tcl.h` to certain directories to resolve build errors.
- Added `#include <cstdint>` in a few header files to fix compilation issues.

## Output Organization

Generated netlists are categorized by standard cell library:

- **ASAP7**
- **NANGATE45**

Output files are located in:
```
Synthetic_Data_Generation/Sample_Output_Files/
```

Each configuration includes:

- `netlist.v`: Verilog netlist
- `netlist.sdc`: Synopsys Design Constraints

## Configurable Parameters

These parameters can be customized in the TCL scripts (`generate_netlist_ASAP.tcl` or `generate_netlist_NANGATE45.tcl`):

- `NUM_INSTS`: Number of logic gate instances
- `NUM_PRIMARY_IOS`: Number of I/O ports
- `COMB_RATIO`: Ratio of combinational gates
- `AVG_NET_DEGREE`: Average net fan-out
- `AVG_BBOX`: Average bounding box (normalized using bin size)
- `CELL_LIST`: Standard cells list (from `onlyUseCell.list`)
- `SPEC_PATH`: Output path for `.spec` file
- `AVG_TOPO_ORDER`: Average logic path order
- `AVG_GATE_DELAY`: Estimated average gate delay (ns)

## Instructions to Run

### Clone the Repository

```bash
git clone <repository_link>
cd Synthetic_Data_Generation/artificial_netlist_generator
```

### Build the Project

```bash
mkdir build
cd build
cmake ..
make -j$(nproc)
```

### Launch OpenROAD

```bash
cd src
./openroad
```

### Generate Netlists

Inside the OpenROAD shell, source the appropriate TCL script:

```tcl
# For ASAP7
source generate_netlist_ASAPy.tcl

# For NANGATE45
source generate_netlist_NANGATE45.tcl
```

Exit the OpenROAD shell:

```tcl
exit
```

### Output Files

The following files will be generated:

- `netlist.v`: Verilog netlist
- `netlist.sdc`: Timing constraints

These files are stored under:

```
Synthetic_Data_Generation/Sample_Output_Files/
```

## DREAMPlace Results

| S.No. | Design (LEF) | Post-Global Placement HPWL (DREAMPlace) | Runtime (s) |
|-------|--------------|------------------------------------------|-------------|
| 1     | ASAP7        | 2.569043E+04 × 54 = 1386288 um           | 4.77        |
| 2     | NANGATE45    | 8.989416E+03 × 380 = 3415978 um          | 38.3        |