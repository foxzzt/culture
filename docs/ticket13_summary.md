# Ticket 13 Summary: Match-Rate Precision and Category Dimension

## Quality Gates

- Exact-only rate <= full-linkage rate violations: **0**.
- Fuzzy-only precision audit sample size: **100**.
- Fuzzy-only false-positive estimate: **0.000** (0/100).
- Standard-category project count sum: **20823**.
- National full-linkage project match rate: **0.510658**, which rounds to **0.511** and reproduces the 0.511 anchor.

## Parity-Flip Recount

| design | window | tie_rule | flip_count | liaoning_baseline_IPR | liaoning_comparison_value | liaoning_baseline_below | liaoning_comparison_below | liaoning_flip |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| symmetric_literal | 2010_2024 | strict_below | 9 | 0.7482993197278912 | 1.0 | True | False | True |
| symmetric_literal | 2015_2024 | strict_below | 9 | 0.7482993197278912 | 0.0 | True | True | False |
| asymmetric_national_relative | 2010_2024 | strict_below | 10 | 0.7482993197278912 | 0.6307070102507054 | True | True | False |
| asymmetric_national_relative | 2015_2024 | strict_below | 12 | 0.7482993197278912 | 0.0 | True | True | False |
| symmetric_literal | 2010_2024 | tie_as_below | 8 | 0.7482993197278912 | 1.0 | True | True | False |
| symmetric_literal | 2015_2024 | tie_as_below | 10 | 0.7482993197278912 | 0.0 | True | True | False |
| asymmetric_national_relative | 2010_2024 | tie_as_below | 10 | 0.7482993197278912 | 0.6307070102507054 | True | True | False |
| asymmetric_national_relative | 2015_2024 | tie_as_below | 12 | 0.7482993197278912 | 0.0 | True | True | False |

## Files Written

- `output/tables/ticket13_exact_vs_fuzzy_match_rate.csv`
- `output/final_tables/table_A12_exact_vs_fuzzy_match_rate.tex`
- `output/tables/ticket13_fuzzy_precision_audit_sample.csv`
- `output/tables/ticket13_category_match_rate.csv`
- `output/final_tables/table_A13_category_match_rate.tex`
- `output/tables/ticket13_parity_flip_recount.csv`
- `output/final_tables/table_A14_parity_flip_recount.tex`
- `output/tables/ticket13_summary.md`
- Public copies under `tables/` and `docs/`.
