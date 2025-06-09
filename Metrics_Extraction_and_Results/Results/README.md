# Transport-Informed Placement Initialization Results



## HPWL Results

### After Initialization via DREAMPlace

| S.No | Design            | HPWL (Electrostatic DREAMPlace) | HPWL (Transport-Informed DREAMPlace) |
|------|-------------------|----------------------------------|--------------------------------------|
| 1    | GCD - ASAP7       | 1,132,950 um                    | 918,478 um                           |
| 2    | GCD - NanGate45   | 14,334,565 um                   | 6,357,470 um                         |
| 3    | IBEX - ASAP7      | 213,920,210 um                  | 70,081,116 um                        |
| 4    | IBEX - NanGate45  | 474,917,592 um                  | 424,702,867 um                       |
| 5    | AES - ASAP7       | 45,387,092 um                   | 35,093,639 um                        |
| 6    | JPEG - ASAP7      | 772,177,376 um                  | 4,983,061,775 um                     |
| 7    | JPEG - NanGate45  | 1,293,352,066 um                | 1,384,533,707 um                     |

---

### After Global Placement via RePlAce

**Conclusion:**  
Overall, the gain from using transport-informed DREAMPlace was positive in 5 out of 7 designs, showing modest improvements in post-global placement HPWL. While two designs saw slight degradations, the majority trend suggests a generally beneficial impact.

| S.No | Design            | Post-GP HPWL (Electrostatic → RePlAce) | Post-GP HPWL (Transport-Informed → RePlAce) | Gain (%) |
|------|-------------------|-----------------------------------------|---------------------------------------------|----------|
| 1    | GCD - ASAP7       | 630,002 um                             | 628,701 um                                  | 0.207    |
| 2    | GCD - NanGate45   | 4,365,094 um                           | 4,380,887 um                                | -0.362   |
| 3    | IBEX - ASAP7      | 82,538,455 um                          | 82,512,491 um                               | 0.031    |
| 4    | IBEX - NanGate45  | 487,683,018 um                         | 487,678,062 um                              | 0.001    |
| 5    | AES - ASAP7       | 50,939,133 um                          | 50,889,318 um                               | 0.098    |
| 6    | JPEG - ASAP7      | 224,228,460 um                         | 224,854,673 um                              | -0.279   |
| 7    | JPEG - NanGate45  | 1,777,643,504 um                       | 1,769,225,398 um                            | 0.474    |

---

## Timing Results

### Initialization via DREAMPlace

> Each design was run for 275 iterations under both the baseline and modified approaches.  
> An exception was observed with GCD-NanGate45 using the Electrostatics-based DREAMPlace, which converged earlier and stopped after fewer iterations.

| S.No | Design            | Runtime (Electrostatic) | Runtime (Transport-Informed) |
|------|-------------------|--------------------------|-------------------------------|
| 1    | GCD - ASAP7       | 1.538 s                  | 175.894 s                     |
| 2    | GCD - NanGate45   | 6.723 s (186 iter)       | 384.648 s                     |
| 3    | IBEX - ASAP7      | 6.093 s                  | 498.694 s                     |
| 4    | IBEX - NanGate45  | 147.074 s                | 537.438 s                     |
| 5    | AES - ASAP7       | 4.147 s                  | 501.517 s                     |
| 6    | JPEG - ASAP7      | 13.379 s                 | 559.428 s                     |
| 7    | JPEG - NanGate45  | 482.770 s                | 908.203 s                     |

---

### Global Placement via RePlAce

> The iteration count is reported along with the runtime, and may differ across designs based on their complexity and convergence behavior.

**Conclusion:**  
Overall, 4 out of 7 designs showed positive runtime gains when using transport-informed DREAMPlace during RePlAce global placement. Despite some degradation in runtime for a few cases, the modified approach demonstrated notable efficiency improvements in larger or more complex designs.

| S.No | Design            | Runtime (Electrostatic → RePlAce) | Runtime (Transport-Informed → RePlAce) | Gain (%) |
|------|-------------------|------------------------------------|----------------------------------------|----------|
| 1    | GCD - ASAP7       | 3.35 s (310 iter)                 | 3.77 s (310 iter)                      | -12.537  |
| 2    | GCD - NanGate45   | 1.99 s (360 iter)                 | 2.08 s (360 iter)                      | -4.523   |
| 3    | IBEX - ASAP7      | 70.39 s (410 iter)                | 68.91 s (410 iter)                     | 2.103    |
| 4    | IBEX - NanGate45  | 97.01 s (2030 iter)               | 87.99 s (1870 iter)                    | 9.298    |
| 5    | AES - ASAP7       | 36.67 s (390 iter)                | 36.42 s (390 iter)                     | 0.682    |
| 6    | JPEG - ASAP7      | 209.40 s (470 iter)               | 228.47 s (470 iter)                    | -9.107   |
| 7    | JPEG - NanGate45  | 323.68 s (2820 iter)              | 294.94 s (2130 iter)                   | 8.879    |

---

## Density Results (After Initialization via DREAMPlace)

| S.No | Design            | Density (Electrostatic) | Density (Transport-Informed) |
|------|-------------------|--------------------------|-------------------------------|
| 1    | GCD - ASAP7       | 5.000E+00                | 2.372E+01                     |
| 2    | GCD - NanGate45   | 2.176E+01                | 3.338E+01                     |
| 3    | IBEX - ASAP7      | 3.802E+01                | 6.097E+01                     |
| 4    | IBEX - NanGate45  | 1.485E+03                | 5.200E+01                     |
| 5    | AES - ASAP7       | 5.857E+01                | 5.715E+02                     |
| 6    | JPEG - ASAP7      | 1.565E+02                | 3.192E+01                     |
| 7    | JPEG - NanGate45  | 4.661E+03                | 5.161E+01                     |

