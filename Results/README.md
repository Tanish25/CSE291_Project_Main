# Transport-Informed Placement Initialisation Results

## Placement Visualised

## HPWL Results

### After Initialization via DREAMPlace

| S.No. | Design             | Post-Initialization HPWL (Electrostatic DREAMPlace) | Post-Initialization HPWL (Transport-informed DREAMPlace) |
|-------|--------------------|------------------------------------------------------|-----------------------------------------------------------|
| 1     | GCD - ASAP7        |                                                      |                                                           |
| 2     | GCD - NanGate45    |                                                      |                                                           |
| 3     | IBEX - ASAP7       |                                                      |                                                           |
| 4     | IBEX - NanGate45   |                                                      |                                                           |
| 5     | AES - ASAP7        |                                                      |                                                           |
| 6     | JPEG - ASAP7       |                                                      |                                                           |
| 7     | JPEG - NanGate45   |                                                      |                                                           |

### After Global Placement via RePlAce

| S.No. | Design             | Post-GP HPWL (Electrostatic DREAMPlace → RePlAce) | Post-GP HPWL (Transport-informed DREAMPlace → RePlAce) |
|-------|--------------------|---------------------------------------------------|---------------------------------------------------------|
| 1     | GCD - ASAP7        |                                                   |                                                         |
| 2     | GCD - NanGate45    |                                                   |                                                         |
| 3     | IBEX - ASAP7       |                                                   |                                                         |
| 4     | IBEX - NanGate45   |                                                   |                                                         |
| 5     | AES - ASAP7        |                                                   |                                                         |
| 6     | JPEG - ASAP7       |                                                   |                                                         |
| 7     | JPEG - NanGate45   |                                                   |                                                         |

---

## Timing Results

### Initialization via DREAMPlace

> Each design was run for 275 iterations under both the baseline and modified approaches. 
> An exception was observed with GCD-NanGate45 using the Electrostatics-based DREAMPlace, 
> which converged earlier and stopped after fewer iterations; this has been noted accordingly.

| S.No. | Design           | Runtime (Electrostatic DREAMPlace) | Runtime (Transport-informed DREAMPlace) |
|-------|------------------|-------------------------------------|------------------------------------------|
| 1     | GCD - ASAP7      | 1.538 s                             | 175.894 s                                |
| 2     | GCD - NanGate45  | 6.723 s (186 iter)                  | 384.648 s                                |
| 3     | IBEX - ASAP7     | 6.093 s                             | 498.694 s                                |
| 4     | IBEX - NanGate45 | 147.074 s                           | 537.438 s                                |
| 5     | AES - ASAP7      | 4.147 s                             | 501.517 s                                |
| 6     | JPEG - ASAP7     | 13.379 s                            | 559.428 s                                |
| 7     | JPEG - NanGate45 | 482.770 s                           | 908.203 s                                |

---

### Global Placement via RePlAce

> The iteration count is reported along with the runtime, and may differ across designs 
> based on their complexity and convergence behavior.

| S.No. | Design           | RePlAce Runtime (Electrostatic DREAMPlace → RePlAce) | RePlAce Runtime (Transport-informed DREAMPlace → RePlAce) |
|-------|------------------|-------------------------------------------------------|-------------------------------------------------------------|
| 1     | GCD - ASAP7      |                                                       |                                                             |
| 2     | GCD - NanGate45  |                                                       |                                                             |
| 3     | IBEX - ASAP7     |                                                       |                                                             |
| 4     | IBEX - NanGate45 |                                                       |                                                             |
| 5     | AES - ASAP7      |                                                       |                                                             |
| 6     | JPEG - ASAP7     |                                                       |                                                             |
| 7     | JPEG - NanGate45 |                                                       |                                                             |

---

## Density Results (After Initialization via DREAMPlace)

| S.No. | Design           | Post-Initialization Density (Electrostatic) | Post-Initialization Density (Transport-informed) |
|-------|------------------|---------------------------------------------|--------------------------------------------------|
| 1     | GCD - ASAP7      | 5.000E+00                                   | 2.372E+01                                        |
| 2     | GCD - NanGate45  | 2.176E+01                                   | 3.338E+01                                        |
| 3     | IBEX - ASAP7     | 3.802E+01                                   | 6.097E+01                                        |
| 4     | IBEX - NanGate45 | 1.485E+03                                   | 5.200E+01                                        |
| 5     | AES - ASAP7      | 5.857E+01                                   | 5.715E+02                                        |
| 6     | JPEG - ASAP7     | 1.565E+02                                   | 3.192E+01                                        |
| 7     | JPEG - NanGate45 | 4.661E+03                                   | 5.161E+01                                        |

