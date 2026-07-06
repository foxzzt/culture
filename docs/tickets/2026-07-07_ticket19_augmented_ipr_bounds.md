# Codex Ticket 19: Augmented IPR Bounds

Date: 2026-07-07
Origin: Strategy agent, acceptance of Ticket 16
status: open

## Ticket 19: augmented_ipr_bounds

Task: augmented_ipr_bounds
Output needed: table_A16 (TEX + CSV), one row per province: provincial roster inheritors, national inheritors attributed to the province not found on the provincial roster (from A15), projects, roster IPR, augmented IPR = (roster + national_not_on_roster) / projects, below-parity flags under both. Add a second augmented variant using exact-only overlap classification (more nationals classified as missing, larger add-back) so the two variants bracket the correction. MD summary must state that the 114 non-provincial national rows are excluded and that cross-level project-name mismatch inflates the missing count, so the augmented IPR is an upper-bound correction.
Context (why): Ticket 16 shows Guangdong (0.174), Liaoning (0.187), Jilin (0.188) are the only provinces more than 2 SD below the mean share of their national inheritors found on the provincial roster (mean 0.637). These are the paper's three case provinces, so the manuscript must report IPR under both roster and augmented numerators.
Use existing outputs or rebuild from raw?: existing (A15 + A12 project counts)
Target script if known: extends Ticket 16 script
Definition/sample: 31 provinces; augmentation adds national_not_on_provincial_roster to the numerator only
Deliverable format: TEX + CSV + MD
Overwrite allowed?: no, new files
Writer-facing summary needed?: yes
GitHub destination: culture/tables/ and culture/docs/
Quality gates: anchors Guangdong augmented 0.771, Liaoning 0.956, Jilin 0.545, Jiangsu 0.735 (fuzzy-overlap variant, rounding tolerance 0.002); below-parity count under fuzzy-overlap augmentation must be 8; report the 8-province set explicitly
