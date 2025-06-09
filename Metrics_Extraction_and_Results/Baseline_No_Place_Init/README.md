# Baseline Flow: RePlAce Without Placement Initialization

This directory contains results for running the ASIC flow using **RePlAce alone**, without any placement initialization (i.e., no DREAMPlace). The goal is to evaluate baseline HPWL and runtime after global placement.

---

## Steps to Generate HPWL and Runtime

### Step 1: Clone OpenROAD Flow Scripts

Clone the official OpenROAD flow repository:

```bash
git clone https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts.git
```

---

### Step 2: Navigate to Flow Directory

Change into the `flow/` directory. This is where the main `Makefile` resides.

Design configuration files (`config.mk`) for various RTLs and technology nodes are located at:

```
flow/designs/<technology-node>/<design-name>/config.mk
```

---

### Step 3: Run the Flow (Only Up to Placement)

To start the flow (synthesis through placement and routing), use the command:

```bash
DESIGN_CONFIG=./designs/<technology-node>/<design-name>/config.mk make
```

> ⚠️ **Important:** By default, this command will run the *entire* flow (synthesis → placement → routing).  
Since we are only interested in **placement**, we avoid post-placement steps using the following approach:

#### Recommended Option (Used in Our Setup):
- Let the flow start normally.
- **Manually kill the run after placement finishes** to avoid memory/time overhead from routing and later steps.

---

### Step 4: Extract HPWL and Runtime

After placement (specifically after **global placement**), the following log file contains the metrics of interest:

```
flow/logs/<technology-node>/<design-name>/base/3_3_place_gp.log
```

In this file, you can find:
- **HPWL (Half-Perimeter Wire Length)**
- **Global placement runtime**

---

## Additional Notes

### Note 1: Repetition Across Designs

This process is repeated for **every design** in both:
- **Training dataset**
- **Test dataset**

---

### Note 2: Location of Results

This repository includes results for:

- **Training designs**:
  - Gcd - Asap7
  - Gcd - NanGate45
  - Ibex - Asap7
  - Ibex - NanGate45
  - Aes - Asap7

- **Test designs**:
  - Jpeg - Asap7
  - Jpeg - NanGate45

Result files are located under:

```
Baseline_No_Place_Init/<technology-node>/<design-name>/
```

- HPWL:  
  `Logs/3_3_place_gp.log`
- Runtime:  
  `Logs/3_3_place_gp.log`

---

### Note 3: Generating DEF Files Before Global Placement

To run **DREAMPlace** or **Transport-Informed DREAMPlace**, we need the **DEF file just before global placement**. Here's how to generate it:

#### 1. Edit I/O Placement Script

Modify `flow/scripts/io_placement.tcl` as shown below:

![image](https://github.com/user-attachments/assets/564d175f-33fe-4c98-843e-c7523f9740e8)

#### 2. Run the Flow Again

```bash
DESIGN_CONFIG=./designs/<technology-node>/<design-name>/config.mk make
```

This generates the required pre-global placement files.

- DEF before global placement:  
  `results/<technology-node>/<design-name>/base/3_2_place_iop.def`

- Synthesized gate-level netlist:  
  `results/<technology-node>/<design-name>/1_synth.v`

These files are used as inputs to:
- `DREAMPlace` scripts
- `Transport-Informed DREAMPlace` scripts

---
