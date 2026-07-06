# Codex Ticket 15: Downstream Scenic-Area Fix

Date: 2026-07-06
Origin: Strategy agent, acceptance review of Tickets 12-14
status: done

## Ticket 15: downstream_scenic_fix

Task: downstream_scenic_fix
Output needed: (1) Regenerated table_A3 Gini summary using the corrected scenic-area data (Xinjiang 598 A-level / 15 5A; Hainan treated as missing, so scenic series use N=30). Report old vs new Gini for both scenic series in the summary note. (2) Regenerated fig_3_lorenz_curves with the corrected scenic series, or, if simpler, a version that drops the two scenic curves from the figure and keeps them in table_A3 only; state which option was taken. (3) Cleaned table_A2 TEX: remove the empty library_count row; remove cultural_capacity_proxy unless it is referenced in the manuscript (it is not, as of v2); keep the Xinjiang/Hainan note.
Context (why): Ticket 14 corrected the covariate panel but the correction was not propagated. table_A3 still reports scenic Ginis computed on the erroneous Xinjiang zero with N=31 (5A 0.3161, A-level 0.3332), and fig_3 Lorenz scenic curves are contaminated the same way. The A2 TEX also carries a dead all-NaN row that cannot appear in a published table.
Use existing outputs or rebuild from raw?: rebuild from corrected covariate panel
Target script if known: gini/lorenz scripts from the original figure pipeline; A2 script from Ticket 14
Definition/sample: 31 provinces for ICH and economic series; 30 provinces for both scenic series with Hainan missing; note the N difference in the table
Deliverable format: TEX + CSV + PNG/PDF + MD summary
Overwrite allowed?: yes for table_A3, table_A2 TEX, fig_3
Writer-facing summary needed?: yes
GitHub destination: culture/tables/, culture/figures/, culture/docs/
Quality gates: non-scenic Gini values must be unchanged to 4 decimal places vs the current table_A3 (projects 0.2374, inheritors 0.2430, IPR 0.1722, GDP series unchanged); scenic series must report N=30 explicitly; report old vs new scenic Gini side by side; figure regenerates without errors and the summary states which figure option was taken.
