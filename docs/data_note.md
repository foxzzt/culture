# Data Note

This public repository contains processed and aggregated research data only. Raw third-party source files are not redistributed.

## Unit of Analysis

The main analytical unit is the provincial-level unit across China's 31 mainland provinces, municipalities, and autonomous regions. Hong Kong, Macau, and Taiwan are not included in the final mainland province sample.

## Core Measures

- `project_count`: number of provincial representative intangible cultural heritage project records.
- `inheritor_count`: number of certified representative inheritor records.
- `IPR`: inheritor-to-project ratio, calculated as `inheritor_count / project_count`.
- `region`: broad regional classification: East, Central, West, Northeast.
- `GDP_per_capita`: provincial GDP per capita covariate used in exploratory analysis.
- `fiscal_expenditure_per_capita`: fiscal-capacity proxy.
- `cultural_capacity_proxy`: composite proxy derived from cultural-sector indicators.

## Public Files

- `province_ipr_final.csv`: final province-level analytical dataset.
- `province_year_panel.csv`: cumulative province-year panel used for time-trend and dispersion checks.
- `ipr_by_batch.csv`: batch-level project and inheritor counts.
- `fig_5_source_data.csv`: minimal source data for the GDP per capita figure.

## Source Limitations

The larger working project uses raw ICH rosters, economic covariates, scenic-area records, and cultural-capacity datasets. Those raw files are intentionally excluded from the public repository because some are third-party or licensed data. The public files are therefore intended for reviewing the analysis and reproducing selected aggregate figures, not for reconstructing the entire raw-data cleaning pipeline.

## Interpretation

IPR is a descriptive ratio. It should not be read as a direct measure of cultural vitality or policy quality by itself. The ratio is useful for identifying where formally listed heritage projects have comparatively fewer certified representative inheritors attached to them.

