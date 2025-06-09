# DREAMPlace Setup and Usage Guide

## Description

To perform placement for our designs, we used the DREAMPlace tool available at this GitHub repository: [DREAMPlace GitHub Repository](https://github.com/limbo018/DREAMPlace). The repository was cloned and set up according to the provided instructions.

## Testing and Setup

The tool was tested using the default benchmark files included in the repository. The results were successfully reproduced:

- **Runtime**: ~36 seconds (vs. 27 seconds reported in the repo, due to lack of GPU).
- **Final HPWL**: `7.282350E+07` (vs. ~`6.82E+07` in the repo).

## Using Custom Training Designs

To use custom designs generated via OpenROAD:

- Moved the respective `LEF`, `DEF`, and `Verilog` files into the appropriate folders inside the DREAMPlace source directory.
- Followed folder structure as outlined in the official DREAMPlace instructions.

## JSON Configuration

The JSON configuration was modified as follows:

- `"gpu": 0` — as no GPU was available.
- Removed `"aux_input"` — since the bookshelf format wasn't used.
- Updated `"lef_input"`, `"def_input"`, and `"verilog_input"` — to match the custom file paths.
- Other parameters (e.g., design name, die area) were set based on the `config.mk` files from the training dataset.

## Output and Interpretation

- Output files were organized by standard cell library (ASAP7 or NANGATE45).
- The tool was run for **275 iterations** to obtain final results.
- We were not able to generate def files for the designs- swerv_wrapper, ariane136 and nangate-aes because ...

## Instructions to Run DREAMPlace (CPU Version using Docker)

### Step 1: Clone the Repository

```bash
git clone --recursive https://github.com/limbo018/DREAMPlace.git
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Pull the Docker Image

```bash
docker pull limbo018/dreamplace:cuda
```

---

## Running Without GPU (CPU Mode) on Linux

### Step 4: Start Docker Container

```bash
docker run -it -v $(pwd):/DREAMPlace limbo018/dreamplace:cuda bash
```

### Step 5: Build and Install DREAMPlace Inside the Container

```bash
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=../install -DPython_EXECUTABLE=$(which python)
make
make install
```

(Optional) Clean up build folder:

```bash
rm -r build
```

---

## Copying Custom Folders into Docker Container

### Step 6: Copy Folder consisting of test and train metadata

```bash
docker cp train_and_test_sample_metadata <container-id>:DREAMPlace/DREAMPlace/install/train_and_test_sample_metadata
```

### Step 7: Copy Folder consisting of input json files 

```bash
docker cp train_and_test_input_json <container-id>:DREAMPlace/install/test/train_and_test_input_json
```

---

## Running a Custom DREAMPlace Test

```bash
cd DREAMPlace/dreamplace/install
python dreamplace/Placer.py test/train_and_test_input_json/asap7_gcd.json
```

(Replace JSON file with the one for your specific design)

---

## Other Folders

- **`DREAMPlace_output_def_files`**
  Contains DEF files generated using the baseline Electrostatics-based DREAMPlace flow.

- **`DREAMPlace_output_logs`**
  Contains the corresponding log files for each test design used to generate the DEF files.



