# Claude Handoff and Review Guide

Repository: `https://github.com/foxzzt/culture`

Purpose of this file: explain what Codex has built, how to inspect the public GitHub repository, and how to use the paper-related results without confusing the public showcase repository with the full private working project.

## 1. Repository Role

This GitHub repository is the public-facing research portfolio version of the project. It is intended for professors, employers, and other reviewers who may receive the repository link from a resume or application.

It is not the full private working repository. The full working project remains local and contains raw Excel files, shapefiles, workflow logs, ticket outputs, and private revision artifacts. Those materials were intentionally excluded from the public repository.

The public repository should look professional, compact, and easy to inspect. It includes:

- A polished project overview in `README.md`.
- Processed aggregate data in `data/processed/`.
- Selected final figures in `figures/`.
- Final paper tables in `tables/`.
- Data and reproducibility notes in `docs/`.
- A clean public reproduction script in `analysis/reproduce_public_figures.py`.

## 2. How to Review the GitHub Repository

Start here:

1. Open `README.md`.
2. Confirm that the figure previews render correctly on GitHub.
3. Review `docs/data_note.md` to understand why raw data are not included.
4. Review `docs/reproducibility.md`.
5. Inspect `data/processed/province_ipr_final.csv` and `tables/`.
6. Optionally run the public reproduction script:

```bash
pip install -r requirements.txt
python analysis/reproduce_public_figures.py
```

The reproduction script writes selected regenerated non-map figures to:

```text
output/reproduced_figures/
```

The static map figures in `figures/` are final exports. The public repository does not include raw geographic boundary files.

## 3. Public Repository Design Choices

Codex deliberately did not push the entire local working directory to GitHub. The local project contained raw and intermediate files that would make a public portfolio look cluttered and could raise data-redistribution concerns.

Excluded from the public repository:

- Raw third-party Excel files.
- DBF, SHP, SHX, SBN, SBX, and other spatial source files.
- Local logs and machine-specific paths.
- Claude/Codex working files.
- Ticket-by-ticket debug outputs.
- Large raw source data.

Included instead:

- Aggregated province-level processed data.
- Final figures as PNGs suitable for GitHub preview.
- Final CSV and LaTeX tables.
- Clean documentation.
- A minimal reproducible script without machine-specific paths.

This design is intentional. If a reviewer wants to evaluate research presentation, this public repository is the right object. If a collaborator needs to rerun the full private raw-data pipeline, a separate private working repository should be created.

## 4. Core Paper Result

The project studies whether formally listed provincial intangible cultural heritage projects are proportionally matched with certified representative inheritors.

Core descriptive measure:

```text
IPR = certified representative inheritors / representative ICH projects
```

Key final sample:

- 31 mainland provincial-level units.
- 20,924 provincial ICH project records.
- 22,361 certified inheritor records.
- National IPR: 1.069.

Lowest IPR provinces:

| Province | IPR |
| --- | ---: |
| Jilin | 0.486 |
| Guangdong | 0.585 |
| Guizhou | 0.698 |
| Jiangsu | 0.703 |
| Tianjin | 0.736 |

Highest IPR provinces:

| Province | IPR |
| --- | ---: |
| Shanghai | 2.015 |
| Hainan | 1.724 |
| Shanxi | 1.594 |
| Hubei | 1.518 |
| Gansu | 1.513 |

Regional pattern:

- East aggregate IPR: 0.996.
- Central aggregate IPR: 1.265.
- West aggregate IPR: 1.077.
- Northeast aggregate IPR: 0.775.

Interpretive headline: the mismatch is not simply a poor-versus-rich story. Several wealthy eastern provinces remain below parity, while the Northeast is consistently low.

## 5. Codex Revision Tickets Completed Before Public Repo Design

Codex previously completed paper-revision Tickets 03-11 in the private working project. These results were not all pushed as raw ticket outputs to the public repository, but their manuscript-facing implications are summarized below.

### Ticket 03: Project-Level Inheritor Match Rate

Outputs in private working project included project-inheritor linkage files, a match-quality report, and `table_A9_match_rate.tex`.

Key results:

- National project-level match rate: 0.511.
- 10,685 of 20,924 analytical project records have at least one linked inheritor.
- Provincial minimum: Guizhou, 0.305.
- Provincial maximum: Xinjiang, 0.795.
- Spearman correlation between provincial match rate and baseline cumulative IPR: 0.638, p = 0.0001132.
- Projects with no linked inheritor: 10,239.
- Inheritor records whose associated project was not found: 2,819 of 22,361, or 12.6%.

Important caveat:

The unmatched inheritor share exceeds the 10% quality gate. Do not treat Table A9 or match-rate estimates as final without editor review of match quality.

### Ticket 04: Asymmetric Recent-Cohort IPR

Key results:

- Spearman baseline vs asymmetric 2010/full rescaled: 0.534, p = 0.001962.
- Spearman baseline vs asymmetric 2015/full rescaled: 0.233, p = 0.2078.
- Below/above parity status flips: 10 provinces for 2010/full and 12 provinces for 2015/full.
- Hainan and Liaoning are small-base or recent-window sensitive cells.

Use this ticket to discuss whether recent-period numerator and denominator timing changes alter the headline pattern.

### Ticket 05: Batch Timing Robustness

Key results:

- Spearman baseline vs k=3 lagged IPR: 0.799, p = 7.009e-08.
- Spearman baseline vs k=5 lagged IPR: 0.776, p = 2.942e-07.
- Bottom-five k=3: Beijing, Guangdong, Jilin, Liaoning, Shandong.
- Bottom-five k=5: Guangdong, Guizhou, Jilin, Liaoning, Shaanxi.
- Guangdong's gap does not shrink materially under k=3 or k=5.
- Jiangsu rises above literal parity under lagged denominators, but its 2015-2024 batch match share remains below the national rate.

Caveat:

Ticket 05 uses Ticket 03 linkage, so it inherits the Ticket 03 match-quality warning.

### Ticket 06: Composition-Adjusted IPR Decomposition

Key results:

- 101 non-standard project records were excluded from ten-category composition cells.
- 12 provinces remain below parity after national-category-mix adjustment.
- National standard-category aggregate IPR: 1.074.
- Guangdong gap is mostly within-category rather than category-mix driven.
- Jiangsu gap is also mostly within-category.
- Jilin adjusted IPR: 0.513, adjusted rank 31.
- Liaoning adjusted IPR: 0.746, adjusted rank 28.
- Heilongjiang adjusted IPR: 1.073, adjusted rank 16.

Interpretation:

Guangdong and Jiangsu gaps are not mainly artifacts of having the wrong category mix. Jilin and Liaoning remain low after adjustment.

### Ticket 07: HC3 Table 3 and beta=1 Tests

Key results:

- Column (1): beta=1 not rejected at 5%, p = 0.149.
- Column (2): beta=1 not rejected at 5%, p = 0.170.
- Column (3): beta=1 not rejected at 5%, p = 0.404.
- Column (4): beta=1 rejected at 5%, p = 0.00000611.
- Project-count coefficients remain positive under HC3.

Interpretation:

Text claiming a positive association between project counts and certified inheritors remains supported. Strong proportionality claims should be framed through the beta=1 tests.

### Ticket 08: GDP per Capita Minimum Check

Key results:

- Exact minimum GDP per capita in final analysis sample: 51,000.457.
- Province: Gansu.
- Covariate year recorded in the pipeline log: 2023.
- No table file was modified.

### Ticket 09: Roster Transcription Spot-Check

Key results:

- Random seed: 20260705.
- Sampled project records: 30.
- Sampled inheritor records: 30.
- Field-level discrepancy count in sampled retained rows: 0.
- Dropped rows are summary/comment rows, not analytical mainland observations.

### Ticket 10: CV Dispersion Robustness

Key results:

- 2007 CV: 1.370.
- 2008 CV: 0.697.
- 2024 CV: 0.314.
- Post-2015 CV range: 0.314 to 0.399.

Interpretation:

The CV series preserves a large 2007-to-2008 break and supports a post-2015 plateau.

### Ticket 11: Figure 5 Without CI Band

Key result:

- Figure 5 was regenerated without the shaded 95% confidence band.
- The fitted line and labels for Shanghai, Guangdong, Jiangsu, and Jilin were retained.
- The public repository includes the resulting `figures/fig_5_ipr_vs_gdp_per_capita.png`.

## 6. What Claude Should Verify

Please verify the following:

1. The GitHub repository opens cleanly and looks professional as a public portfolio.
2. The README makes the project understandable to someone who has not seen the private working directory.
3. The included data are aggregate and appropriate for public release.
4. No raw Excel, DBF, SHP, or local workflow files were accidentally published.
5. Figures render correctly in GitHub.
6. The public reproduction script runs and writes non-map figure outputs.
7. The paper-result caveats above are reflected in any manuscript edits, especially the Ticket 03 match-quality warning.

## 7. Recommended Claude Response to User

If this repository passes review, tell the user that:

- The public GitHub repository is suitable as a resume or application link.
- It is intentionally a polished public showcase, not the full private raw-data repository.
- For long-term Claude/Codex collaboration on raw data, the user should create a separate private repository.

If changes are needed, propose specific edits to `README.md`, `docs/data_note.md`, this `CLAUDE.md`, or the public file structure.

