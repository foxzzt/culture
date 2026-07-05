# Ticket 14 Summary: Scenic-Area Zero Check

The final covariate panel showed two provinces with both `A_level_scenic_area_count = 0` and `five_A_scenic_area_count = 0`: **Xinjiang** and **Hainan**. Cross-checking the 2025 scenic-area total workbook and the geocoded workbook shows that Xinjiang is a data-processing join error, not a true zero: the source contains **598** A-level scenic areas and **15** 5A scenic areas for Xinjiang in both source workbooks. Hainan is absent from the available scenic-area registry snapshot, so its zero should be treated as a **source coverage gap / missing value**, not a true zero. Table A2 was corrected accordingly: Xinjiang's source counts are used, Hainan is excluded from scenic-area descriptive statistics, and the scenic rows now have count 30 rather than 31.

## Zero-Province Cross-Check

| province | province_name_english | A_level_scenic_area_count | five_A_scenic_area_count | province_key | source_A_level_geocoded_workbook | source_A_level_total_workbook | source_5A_geocoded_workbook | source_5A_total_workbook |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 新疆维吾尔自治区 | Xinjiang | 0 | 0 | Xinjiang | 598.0 | 598.0 | 15.0 | 15.0 |
| 海南省 | Hainan | 0 | 0 | Hainan |  |  |  |  |

## Files Written

- `output/tables/ticket14_scenic_area_source_counts.csv`
- `output/tables/ticket14_scenic_area_zero_crosscheck.csv`
- `output/tables/ticket14_scenic_area_zero_check.md`
- `output/final_tables/table_A2_descriptive_statistics.csv`
- `output/final_tables/table_A2_descriptive_statistics.tex`
- Public copies under `tables/` and `docs/`.
