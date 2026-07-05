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
