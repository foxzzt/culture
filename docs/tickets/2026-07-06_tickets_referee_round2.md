# Codex Tickets: Referee Round 2 Fixes (ICH paper)

Date: 2026-07-06
Origin: Strategy/Referee agent, round-2 referee report on manuscript v2
Priority order: Ticket 12 (P0), Ticket 13 (P1), Ticket 14 (P2)
Convention: read this file top to bottom. Each ticket is independent. Push deliverables to the GitHub paths given, raw data stays local. Report quality-gate results in the writer-facing summary for every ticket.

---

## Ticket 12: kitagawa_fix_and_lagged_denominator_tables

Task: kitagawa_fix_and_lagged_denominator_tables
Output needed: (1) regenerated table_A10 with the decomposition re-expressed as ABSOLUTE contributions, not shares. Define: province gap vs national benchmark = composition contribution + within-category contribution, additive. Add a flag column for degenerate cells. (2) New appendix table (new file, table_A11): per-province lagged-denominator IPR for k=3 and k=5, plus batch-cohort inheritor match share for 2015-2024 project batches. (3) A plain-text methods note stating the exact decomposition formula, benchmark, and reweighting rule, written so the writing agent can transcribe it into the paper.
Context (why): the current table_A10 reports share values like Inner Mongolia 13.990 / -12.990 and Hebei 15.746 / -14.746. These come from dividing by a near-zero total gap. Referee flagged as a P0 credibility problem. Additionally, the lagged-denominator results (Spearman 0.799 for k=3, 0.776 for k=5, Guangdong bottom-five under both lags, Jiangsu above parity under lags) currently exist only as prose in section 4.2 with no table anywhere.
Use existing outputs or rebuild from raw?: rebuild from existing cleaned rosters
Target script if known: extends the composition-adjustment and lagged-denominator scripts from Tickets 05 and 06
Definition/sample: 31 mainland provinces. Ten standard categories, 101 non-standard records excluded and the exclusion reported. National category mix as the reweighting benchmark, stated explicitly in the output.
Deliverable format: TEX + CSV + MD methods note
Overwrite allowed?: yes for table_A10; no for the new lagged table (create table_A11)
Writer-facing summary needed?: yes
GitHub destination: culture/tables/ and culture/docs/
Quality gates: row count = 31 in every table. Additivity check: composition + within = total gap to 1e-6, report the max residual. Flag any cell where abs(contribution) > abs(total gap) x 3. External anchor: Guangdong adjusted IPR must reproduce 0.597, or report exactly why it changed.

---

## Ticket 13: match_rate_precision_and_category_dimension

Task: match_rate_precision_and_category_dimension
Output needed: (1) exact-match-only provincial match rate alongside the current fuzzy rate, two-column comparison. (2) Precision audit: random sample of 100 fuzzy-only links, same-project or different-project judgment per link, and an estimated false-positive rate. (3) Category-level match rate table across the ten standard categories. (4) Parity-flip recount: separate flip counts for the symmetric design (literal parity at 1.0) and the asymmetric design (national-relative parity), with an explicit tie rule for values exactly equal to 1.000. Report Liaoning under both tie rules.
Context (why): the paper claims reported match rates are lower bounds. That holds only if fuzzy matching (SequenceMatcher 0.88) has zero false positives, which is unverified. The category-level match rate is missing even though the category gradient is the paper's headline claim. The nine-flip headline in section 5.3 depends on whether Liaoning's symmetric 2010 value of exactly 1.000 counts as a flip.
Use existing outputs or rebuild from raw?: rebuild from existing linkage output
Target script if known: linkage script from Ticket 03
Definition/sample: same linkage universe, 20,924 projects and 22,361 inheritors. Fuzzy threshold 0.88 unchanged. Audit sample seeded for reproducibility, report the seed.
Deliverable format: CSV + TEX + MD summary
Overwrite allowed?: no, all new files
Writer-facing summary needed?: yes
GitHub destination: culture/tables/ and culture/docs/
Quality gates: exact-match rate must be <= fuzzy rate in every province, report any violation. Audit false-positive rate reported with sample size. Category table project counts must sum to 20,823. External anchor: national fuzzy rate must reproduce 0.511.

---

## Ticket 14: scenic_area_zero_check

Task: scenic_area_zero_check
Output needed: one-paragraph MD note identifying which province or provinces show 0 A-level and 0 5A scenic areas in the covariate panel, and whether this is a registry coverage gap or a true zero. Corrected table_A2 if it is a data error.
Context (why): Table A2 reports min = 0 for both A-level and 5A scenic areas. No mainland province plausibly has zero A-level scenic areas. Referee flagged as a data-plausibility item.
Use existing outputs or rebuild from raw?: existing covariate panel
Target script if known: UNKNOWN
Definition/sample: 31 provinces, 2024 registry snapshot
Deliverable format: MD, plus TEX only if table_A2 changes
Overwrite allowed?: yes for table_A2 only if the error is confirmed
Writer-facing summary needed?: yes
GitHub destination: culture/docs/
Quality gates: name the zero province(s) explicitly. Cross-check against any second source field available in the panel.

---

## Not for Codex (routed to the writing agent, listed here for completeness)

- Fix the abstract's Jiangsu claim (it contradicts the lagged-denominator result in section 4.2).
- Disclose the 2-out 2-in membership change of the below-parity twelve (Beijing and Heilongjiang exit, Anhui and Hebei enter, on the adjusted measure).
- Align the conclusion's category language with section 7's gradient framing.
- Remove course-paper artifacts from the title page footnote.
