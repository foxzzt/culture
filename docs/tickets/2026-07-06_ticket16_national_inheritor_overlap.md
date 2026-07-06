# Codex Ticket 16: Provincial Roster Overlap with National Inheritor List

Date: 2026-07-06
Origin: Strategy agent, follow-up to Tony's M13 Part B policy check
status: open

## Ticket 16: national_inheritor_roster_overlap

Task: national_inheritor_roster_overlap
Output needed: (1) A province-level table reporting, for each of the 31 provinces: provincial-roster inheritor count, number of those inheritors who also appear on the national representative inheritor list (name plus project fuzzy match, same method as Ticket 03), overlap share, and national inheritors attributed to the province who do NOT appear on the provincial roster. (2) A short MD note stating whether any province shows an overlap share that is a clear low outlier, with Guangdong explicitly discussed. (3) If the national inheritor list is not yet in the project data, acquire it from the official China ICH network (ihchina.cn) national inheritor pages; that acquisition is part of this ticket.
Context (why): Guangdong's 2022 provincial inheritor evaluation explicitly excluded national-level inheritors (546 counted, "not including national-level inheritors"). If Guangdong's published provincial roster also excludes nationally promoted inheritors while other provinces retain them, Guangdong's IPR numerator is mechanically depressed relative to other provinces, and Guangdong is the paper's lead case. This is a measurement-validity check a referee will demand. The project-side registry question is settled (cumulative layers); this is the inheritor-side analogue.
Use existing outputs or rebuild from raw?: existing provincial rosters; acquire new for the national inheritor list if absent
Target script if known: linkage method from Ticket 03; source scripts UNKNOWN
Definition/sample: all 31 provinces; national list = all six batches of national representative inheritors (about 3,000+ individuals); match on normalized name plus project name with the 0.88 threshold; report exact-only and fuzzy counts separately
Deliverable format: CSV + TEX + MD summary
Overwrite allowed?: no, new files (suggest table_A15_national_overlap)
Writer-facing summary needed?: yes
GitHub destination: culture/tables/ and culture/docs/; raw national list stays local, push aggregated table only
Quality gates: row count 31; national inheritor total must be reported against an external anchor (published batch totals from official announcements, state the anchor used); overlap share must be between 0 and 1 everywhere; report the min and max province and flag any province more than 2 standard deviations below the mean overlap share
