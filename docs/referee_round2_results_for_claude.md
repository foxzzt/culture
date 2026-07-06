# Referee Round 2 Results for Claude

Date: 2026-07-06

Codex completed Tickets 12-14 from `2026-07-06_tickets_referee_round2.md` and pushed the public deliverables to GitHub paths under `tables/` and `docs/`.

## Ticket 12: Kitagawa Fix and Lagged Denominator Table

Main result: Table A10 now reports absolute additive contributions, not share-of-gap values. This fixes the referee's P0 credibility issue caused by unstable share values when the total gap is near zero.

Quality gates:

- Table A10 row count: 31.
- Table A11 row count: 31.
- Additivity max absolute residual: 2.220e-16.
- Degenerate contribution flags: 2.
- Guangdong adjusted IPR: 0.596501, which rounds to 0.597.

Key files:

- `tables/table_A10_composition_adjusted_ipr.tex`
- `tables/table_A10_composition_adjusted_ipr_absolute.csv`
- `tables/table_A11_lagged_denominator_ipr.tex`
- `tables/table_A11_lagged_denominator_ipr.csv`
- `docs/ticket12_methods_note.md`
- `docs/ticket12_summary.md`

## Ticket 13: Match-Rate Precision and Category Dimension

Main result: Exact-only match rates, full-linkage match rates, category-level match rates, a 100-link fuzzy precision audit, and parity-flip recounts are now documented.

Quality gates:

- Exact-only > full-linkage violations: 0.
- Fuzzy-only audit sample size: 100.
- Estimated fuzzy false-positive rate: 0.000.
- Standard-category project count sum: 20823.
- National full-linkage match rate: 0.510658, which rounds to 0.511.

Tie-rule note:

- Symmetric 2010 flip count with strict-below rule: 9.
- Symmetric 2010 flip count with tie-as-below rule: 8.
- Liaoning's symmetric 2010 value is exactly 1.000, so its flip status changes across the two tie rules.

Key files:

- `tables/table_A12_exact_vs_fuzzy_match_rate.tex`
- `tables/table_A12_exact_vs_fuzzy_match_rate.csv`
- `tables/table_A13_category_match_rate.tex`
- `tables/table_A13_category_match_rate.csv`
- `tables/table_A14_parity_flip_recount.tex`
- `tables/table_A14_parity_flip_recount.csv`
- `tables/ticket13_fuzzy_precision_audit_sample.csv`
- `docs/ticket13_summary.md`

## Ticket 14: Scenic-Area Zero Check

Main result: The zero scenic-area values are not true zeros.

- Xinjiang was a join error: source workbooks report 598 A-level scenic areas and 15 5A scenic areas.
- Hainan is absent from the available scenic-area registry snapshot, so it should be treated as a source coverage gap / missing value.
- Table A2 was corrected: Xinjiang source counts are used and Hainan is excluded from the scenic-area descriptive rows.

Key files:

- `docs/ticket14_scenic_area_zero_check.md`
- `tables/ticket14_scenic_area_zero_crosscheck.csv`
- `tables/table_A2_descriptive_statistics.csv`
- `tables/table_A2_descriptive_statistics.tex`

## Claude Review Instructions

Please verify the following:

1. GitHub `tables/` contains A10, A11, A12, A13, A14, and corrected A2 files.
2. GitHub `docs/` contains the Ticket 12 methods note and Tickets 12-14 summaries.
3. Table A10 no longer reports composition/within-category shares.
4. Table A11 makes the lagged-denominator results visible in table form.
5. Ticket 13's fuzzy audit and category table are internally consistent.
6. Ticket 14's interpretation is reflected in any manuscript edit: Xinjiang is corrected; Hainan is missing in the available registry snapshot, not true zero.
7. Preserve the earlier Ticket 03 caveat: the project-inheritor linkage has a 12.6% inheritor-side unmatched rate and should be described as diagnostic unless editor-approved.

## Round 2b Results

### Ticket 15: Downstream Scenic-Area Fix

Main result: Ticket 14's scenic-area correction has now been propagated to Table A3, Figure 3, and Table A2.

- Xinjiang is corrected to 598 A-level scenic areas and 15 5A scenic areas.
- Hainan is treated as missing for scenic-area series, so scenic Gini rows use N = 30.
- 5A scenic-area Gini changed from 0.3161 (N = 31) to 0.2643 (N = 30).
- All A-level scenic-area Gini changed from 0.3332 (N = 31) to 0.2806 (N = 30).
- Non-scenic Gini values remain unchanged: projects 0.2374, inheritors 0.2430, IPR 0.1722, historical-cultural cities 0.3962, provincial GDP total 0.4411, provincial GDP per capita 0.2192, prefecture GDP per capita 0.2646.
- Figure 3 was regenerated with the corrected scenic curves retained.
- Table A2 was cleaned: the empty `library_count` row and unreferenced `cultural_capacity_proxy` row were removed.

Key files:

- `docs/ticket15_downstream_scenic_fix.md`
- `tables/table_A2_descriptive_statistics.csv`
- `tables/table_A2_descriptive_statistics.tex`
- `tables/table_A3_gini_summary.csv`
- `tables/table_A3_gini_summary.tex`
- `figures/fig_3_lorenz_curves.png`
- `figures/fig_3_lorenz_curves.pdf`

### Ticket 16: National Inheritor Overlap

Main result: Guangdong is low in the overlap distribution, but it is not a >2 SD low outlier under the 31-province diagnostic.

- Official ihchina source page text states six batches and 3,994 national representative inheritors as of December 2025.
- The official JSON endpoint returned 3,995 rows; the analysis uses those endpoint rows and records the page/API discrepancy.
- 3,881 national rows were mapped to the 31 mainland provincial units; 114 central-unit, Hong Kong, Macau, or otherwise non-provincial rows were left outside province rows.
- Mean provincial overlap share is 0.121; standard deviation is 0.072; the `mean - 2 sd` threshold is -0.024.
- Minimum overlap share is Jilin: 6 of 215 provincial roster rows, share 0.028.
- Maximum overlap share is Beijing: 102 of 280 provincial roster rows, share 0.364.
- Guangdong: 494 provincial roster rows; 190 national rows attributed to Guangdong; 33 provincial rows also appear on the national list; overlap share 0.067; 157 Guangdong national rows were not found in the 2005-2024 provincial roster.
- Provinces more than 2 SD below the mean: 0.

Key files:

- `docs/ticket16_national_inheritor_overlap.md`
- `tables/table_A15_national_overlap.csv`
- `tables/table_A15_national_overlap.tex`

### Ticket 17: Flagged Fuzzy-Link Review

Main result: The three independently flagged fuzzy links were checked against the underlying rosters and all remain `same_project`.

- `inheritor_id = 4019`: no standalone Guangxi project row exactly matching `桂林米粉制作技艺`; linked project is `project_id = 3494`, `桂林马肉米粉制作技艺`, declaring unit Guangxi/Guilin.
- `inheritor_id = 17750`: no standalone Tianjin project row exactly matching `小王庄民间吹打乐`; linked project is `project_id = 16765`, `王庄民间吹打乐`; both rows use Tianjin/不统计 as the declaring-unit field.
- `inheritor_id = 3649`: no standalone Guangxi project row exactly matching `苗族芦笙制作技艺`; linked project is `project_id = 3635`, `苗族芦笙柱制作技艺`, declaring unit Guangxi/Liuzhou.
- Corrected fuzzy-audit false positives: 0 of 100.
- Corrected false-positive rate: 0.000.
- Exact binomial 95 percent upper bound: 0.036, or 3.6 percent.

Key files:

- `docs/ticket17_resolve_flagged_links.md`
- `tables/ticket13_fuzzy_precision_audit_sample.csv`

### Round 2b Claude Checks

Please verify:

1. Ticket files 15, 16, and 17 are marked `status: done`.
2. Table A3 reports scenic series with N = 30 and keeps non-scenic Ginis unchanged.
3. Figure 3 includes corrected scenic Lorenz curves and has both PNG and PDF copies.
4. Table A15 has 31 rows, overlap shares in [0, 1], and explicitly reports Guangdong.
5. Ticket 17's updated audit CSV retains the original audit judgment columns and adds second-review columns.
6. Manuscript edits should use the Ticket 17 wording from `docs/writer_instructions_v3.md`: all 100 sampled fuzzy links were confirmed after re-review, implying an exact binomial 95 percent upper bound of roughly 3.6 percent on the fuzzy false-positive rate.
