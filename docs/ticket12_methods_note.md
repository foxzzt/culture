# Ticket 12 Methods Note: Absolute Kitagawa Decomposition

The decomposition uses the 31 mainland provinces and the ten standard ICH categories. Non-standard project records are excluded before category cells are formed; the exclusion count is **101** project records.

For province `i` and category `c`, let `P_ic` be project count, `H_ic` be inheritor count, `w_ic = P_ic / sum_c(P_ic)` be the province-specific project mix, and `r_ic = H_ic / P_ic` be the category-specific IPR. Let `w_Nc` and `r_Nc` be the corresponding national standard-category project mix and national category-specific IPR. The national benchmark is the national standard-category aggregate IPR, **1.073861**.

The additive decomposition is:

```text
raw_IPR_i - national_IPR = sum_c((w_ic - w_Nc) * r_Nc) + sum_c(w_ic * (r_ic - r_Nc))
```

The first term is the absolute composition contribution. The second term is the absolute within-category contribution. `composition_adjusted_IPR` is computed by reweighting province category rates to the national project mix:

```text
composition_adjusted_IPR_i = sum_c(w_Nc * r_ic)
```

Degenerate contribution flags mark provinces where either absolute contribution is more than three times the absolute total gap. These flags are diagnostic and replace the earlier share-of-gap presentation that produced unstable values when the total gap was near zero.
