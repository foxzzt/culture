# Ticket 12 Summary: Kitagawa Fix and Lagged Denominator Table

## Quality Gates

- Table A10 row count: **31**.
- Table A11 row count: **31**.
- Additivity max absolute residual: **2.220e-16**.
- Degenerate contribution flags: **2** provinces.
- Guangdong composition-adjusted IPR: **0.596501**, which rounds to **0.597** and reproduces the 0.597 anchor.

## Degenerate Contribution Flags

| province_name_english | total_gap_vs_national | composition_contribution | within_category_contribution |
| --- | --- | --- | --- |
| Inner Mongolia | -0.0039811168026089305 | -0.05569489217284484 | 0.05171377537023601 |
| Hebei | 0.00622150064871585 | 0.09796531730942576 | -0.09174381666070971 |

## Files Written

- `output/tables/ticket12_kitagawa_absolute.csv`
- `output/final_tables/table_A10_composition_adjusted_ipr.tex`
- `output/tables/ticket12_table_A11_lagged_denominator_ipr.csv`
- `output/final_tables/table_A11_lagged_denominator_ipr.tex`
- `output/tables/ticket12_methods_note.md`
- `output/tables/ticket12_summary.md`
- Public copies under `tables/` and `docs/`.
