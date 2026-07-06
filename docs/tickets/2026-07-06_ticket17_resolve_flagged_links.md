# Codex Ticket 17: Resolve Three Flagged Fuzzy Links

Date: 2026-07-06
Origin: Strategy agent, independent re-review of the 100-link precision audit
status: open

## Ticket 17: resolve_flagged_fuzzy_links

Task: resolve_flagged_fuzzy_links
Output needed: A short MD adjudication note plus an updated audit CSV resolving three links that an independent review flagged as uncertain. For each, check the underlying provincial roster and answer: does the roster contain a separate project entry matching the inheritor's stated project name, and does the inheritor's city or declaring unit match the linked project's declaring unit?
Link 1: inheritor_id 4019, Guangxi Guilin, inheritor project 桂林米粉制作技艺, linked to 桂林马肉米粉制作技艺. Question: does the Guangxi roster contain a standalone 桂林米粉制作技艺 entry distinct from the horse-meat variant?
Link 2: inheritor_id 17750, Tianjin, inheritor project 小王庄民间吹打乐, linked to 王庄民间吹打乐. Question: are 小王庄 and 王庄 the same village in the roster's declaring-unit field, or two places?
Link 3: inheritor_id 3649, Guangxi Liuzhou, inheritor project 苗族芦笙制作技艺, linked to 苗族芦笙柱制作技艺. Question: instrument-making versus pillar-making are different crafts; does the roster contain a separate lusheng-instrument entry, and which declaring unit does the inheritor belong to?
Final deliverable: for each link a verdict of same_project or false_positive with one line of roster evidence, an updated false-positive count out of 100, and the implied exact binomial 95 percent upper bound.
Use existing outputs or rebuild from raw?: existing rosters and linkage output
Target script if known: linkage script from Ticket 03 plus manual roster lookup
Definition/sample: the three links above only
Deliverable format: MD + updated CSV
Overwrite allowed?: yes for ticket13_fuzzy_precision_audit_sample.csv (add a second_review column, do not delete original judgments)
Writer-facing summary needed?: yes
GitHub destination: culture/docs/ and culture/tables/
Quality gates: each verdict must cite the roster row (project id and declaring unit) it rests on; if a separate matching entry exists for any link, mark that link false_positive and report the corrected rate
