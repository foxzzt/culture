# Codex Ticket 18: A11 National Row and A2 Polish

Date: 2026-07-06
Origin: Strategy agent, v3 draft defect list from the writing agent
status: open

## Ticket 18: a11_national_row_and_a2_polish

Task: a11_national_row_and_a2_polish
Output needed: (1) Regenerated table_A11 (TEX and CSV) identical to the current version plus one final National row reporting aggregate baseline IPR, lagged IPR k=3 and k=5, projects and matched projects 2015-2024, and the national batch match share (must reproduce 0.309 from column totals). (2) Repolished table_A2 TEX using the v2 manuscript's display formatting (human-readable variable labels, thousands separators) with the corrected post-Ticket-14 numbers and the N=30 scenic rows and Xinjiang/Hainan note retained. Do not change any numeric values from the current corrected version.
Context (why): the manuscript cites a national batch match share of 0.309 with no table row to anchor it, and the corrected A2 reverted to raw variable names (GDP_per_capita) which cannot appear in a published table.
Use existing outputs or rebuild from raw?: existing outputs from Tickets 12 and 14
Target script if known: A11 script from Ticket 12; A2 script from Ticket 14
Definition/sample: unchanged from the parent tickets
Deliverable format: TEX + CSV
Overwrite allowed?: yes for both tables
Writer-facing summary needed?: yes, one paragraph
GitHub destination: culture/tables/
Quality gates: A11 province rows unchanged to 6 decimal places vs current version; National row batch share must equal 0.309 within rounding; A2 numeric values unchanged vs current corrected version, formatting only
