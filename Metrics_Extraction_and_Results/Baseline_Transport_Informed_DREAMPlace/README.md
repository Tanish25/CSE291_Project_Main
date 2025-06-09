# Transport-Informed DREAMPlace + Replace Placement Flow

This directory contains results for placement using **Transport-Informed DREAMPlace as a global placement initializer**, followed by **Replace** for global placement.

---

## Input Requirements

The Transport-Informed DREAMPlace script requires:
- A **gate-level netlist**
- A **DEF file (before global placement)**

The steps to generate these inputs are described in the [`Baseline_No_Place_Init/README.md`](../Baseline_No_Place_Init/README.md).

---

## Flow Overview

1. **Run the Transport-Informed DREAMPlace script** with the netlist and DEF file.
   - Output:  
     ```
     <technology-node>_<design-name>.def
     ```

2. **Use this DEF file to initialize placement in Replace:**
   ```bash
   cd flow/
   mkdir -p results/<technology-node>/<design-name>/base
   cp <path-to-output-def>/<technology-node>_<design-name>.def results/<technology-node>/<design-name>/base/
   ```

3. **Modify the global placement script:**
   - Go to `flow/scripts/`
   - Edit `global_place.tcl` to read `<technology-node>_<design-name>.def` before starting global placement  
     (refer to the modification shown in the global_place.tcl script present in this repository)
     Note - Be careful to not load the design using the load_design function that is defined in load.tcl. global_place.tcl is modified to read sdc, lef files and RC values seprately.

4. **Run the flow using:**
   ```bash
   DESIGN_CONFIG=./designs/technology-node/design-name/config.mk make
   ```

---

## Output Logs

- HPWL and runtime values can be found at:
  ```
  flow/logs/<technology-node>/<design-name>/base/3_3_place_gp.log
  ```

---

## Notes

- This process is repeated for **all designs** and **technology nodes**.
- The repository contains:
  - Results/logs for the **training dataset** (cd - Asap7, Gcd - NanGate45, Ibex - Asap7, Ibex - NanGate45, Aes - Asap7)
  - Results/logs for the **test dataset** (Jpeg - Asap7, Jpeg - NanGate45)
- For convenience, log files are also located at:
  ```
  Baseline_Transport_Informed_DREAMPlace/<technology-node>/<design-name>/Logs/3_3_place_gp.log
  ```
