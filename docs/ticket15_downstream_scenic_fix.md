# Ticket 15 Summary: Downstream Scenic-Area Fix

## Result

The corrected scenic-area treatment was propagated to the public processed panel, Table A2, Table A3, and Figure 3. Xinjiang is corrected to **598** A-level scenic areas and **15** 5A scenic areas. Hainan is treated as missing for scenic-area series, so both scenic rows in Table A2/Table A3 use **N = 30**.

Figure option taken: **regenerated Figure 3 with corrected scenic curves retained**. Both scenic Lorenz curves remain in Panel A; their Gini labels now reflect the corrected N = 30 series.

## Scenic Gini Change

| Series | Old Gini | Old N | New Gini | New N |
| --- | ---: | ---: | ---: | ---: |
| 5A Scenic Areas (count) | 0.3161 | 31 | 0.2643 | 30 |
| All A-Level Scenic Areas (count) | 0.3332 | 31 | 0.2806 | 30 |

## Non-Scenic Quality Gate

| Measure | Gini after fix | N | Status |
| --- | ---: | ---: | --- |
| ICH Projects (count) | 0.2374 | 31 | unchanged |
| ICH Inheritors (count) | 0.2430 | 31 | unchanged |
| ICH Inheritor-to-Project Ratio | 0.1722 | 31 | unchanged |
| Hist. & Cultural Cities (count) | 0.3962 | 31 | unchanged |
| Provincial GDP Total | 0.4411 | 31 | unchanged |
| Provincial GDP per Capita | 0.2192 | 31 | unchanged |
| Prefecture GDP per Capita | 0.2646 | 295 | unchanged |

## Files Written

- `data/processed/province_ipr_final.csv`
- `tables/table_A2_descriptive_statistics.csv`
- `tables/table_A2_descriptive_statistics.tex`
- `tables/table_A3_gini_summary.csv`
- `tables/table_A3_gini_summary.tex`
- `figures/fig_3_lorenz_curves.png`
- `figures/fig_3_lorenz_curves.pdf`
- `docs/ticket15_downstream_scenic_fix.md`
