# Placement Strategy Evaluation: HPWL and Runtime Comparison

This repository presents a comparative study of **Half-Perimeter Wire Length (HPWL)** and **Runtime** across multiple ASIC designs using three placement strategies. The goal is to evaluate the impact of placement initialization and transport-aware modeling on placement quality and performance.

---

## Repository Structure

```text
Metrics_Extraction_and_Results/
├── Baseline_No_Place_Init/
│   ├── README.md
│   ├── ASAP7/
│   │   ├── GCD/
│   │   ├── IBEX/
│   │   └── ...
│   └── NanGate45/
│       ├── GCD/
│       ├── IBEX/
│       └── ...
├── Baseline_DREAMPlace/
│   ├── README.md
│   ├── ASAP7/
│   │   ├── GCD/
│   │   ├── IBEX/
│   │   └── ...
│   └── NanGate45/
│       ├── GCD/
│       ├── IBEX/
│       └── ...
├── Baseline_Transport_Informed_DREAMPlace
│   ├── README.md
│   ├── ASAP7/
│   │   ├── GCD/
│   │   ├── IBEX/
│   │   └── ...
│   └── NanGate45/
│       ├── GCD/
│       ├── IBEX/
│       └── ...
├── Results
```

Each `<DESIGN>/` directory contains:
- Synthesis and placement output files  
- Intermediate netlists and DEFs  
- Logs (especially `3_3_place_gp.log`) with HPWL and runtime data  
- Any relevant flow configuration or script modifications  

---

## Placement Strategies

### 🔹 RePlAce (Baseline)
Standard global placement using the RePlAce engine.

### 🔹 DREAMPlace → RePlAce
DREAMPlace initializes the placement. The output DEF is then used by RePlAce to complete global placement.

### 🔹 Transport-Informed DREAMPlace → RePlAce
An enhanced DREAMPlace model that accounts for transport effects is used for initialization. RePlAce is then used for global placement.

---

## Objective

Evaluate the impact of advanced placement flows on:
- **HPWL** — as an indicator of routing quality  
- **Runtime** — to measure flow efficiency  

---

## How to Use This Repository

- Each strategy folder includes a dedicated `README.md` detailing:
  - Input preparation steps
  - Flow configuration
  - How to run and extract results

- HPWL and runtime values can be found in:
  ```
  <strategy>/<TECHNOLOGY_NODE>/<DESIGN>/Logs/3_3_place_gp.log
  ```
- Results are aggregated in the Results/ directory.

---

## Notes

- Designs are grouped into **training** and **test** datasets.
- Technology nodes:
  - `ASAP7`
  - `NanGate45`
- Example designs include:
  - `GCD`, `IBEX`, `AES`, and `JPEG`

---

This repository provides a reproducible setup to benchmark and compare placement strategies across multiple designs and technology nodes.
