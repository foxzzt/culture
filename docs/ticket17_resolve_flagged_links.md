# Ticket 17 Summary: Resolve Flagged Fuzzy Links

## Result

All three independently flagged fuzzy links were checked against the underlying provincial project and inheritor rosters. No separate project entry matching the inheritor's stated project name was found for any of the three links. Each link is therefore retained as **same_project** for the Ticket 13 fuzzy-link precision audit.

## Link-Level Adjudication

| inheritor_id | project_id | verdict | inheritor_source_row | inheritor_project | inheritor_declaring_unit | project_source_row | linked_project | linked_project_declaring_unit | standalone_project_rows_exact_name | finding |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4019 | 3494 | same_project | 4020 | 桂林米粉制作技艺 | 广西壮族自治区/桂林市 | 3495 | 桂林马肉米粉制作技艺 | 广西壮族自治区/桂林市 | 0 | No standalone project row exactly matching the inheritor project name was found in the same province/category; the only rice-noodle project row returned by exact title is the linked horse-meat variant. |
| 17750 | 16765 | same_project | 17751 | 小王庄民间吹打乐 | 天津市/不统计 | 16766 | 王庄民间吹打乐 | 天津市/不统计 | 0 | No standalone project row exactly matching the inheritor project name was found; both the inheritor row and linked project row use the same city/declaring-unit field value, so the roster does not distinguish Xiaowangzhuang from Wangzhuang. |
| 3649 | 3635 | same_project | 3650 | 苗族芦笙制作技艺 | 广西壮族自治区/柳州市 | 3636 | 苗族芦笙柱制作技艺 | 广西壮族自治区/柳州市 | 0 | No standalone project row exactly matching the broader inheritor project name was found in the same province/category; the linked project is the only lusheng-column project row and shares the same city/declaring-unit field. |

## Corrected Precision Estimate

- Reviewed audit sample size: **100** fuzzy-only links.
- Corrected false positives: **0/100**.
- Corrected false-positive rate: **0.000**.
- Exact binomial 95 percent upper bound: **0.036** (3.6%).

The upper bound uses the two-sided Clopper-Pearson exact interval upper limit; with 0 false positives in 100 reviewed links, this is approximately 3.6 percent.

## Files Written

- `tables/ticket13_fuzzy_precision_audit_sample.csv` (added `second_review`, `second_review_false_positive`, `second_review_note`, and `second_review_evidence`; original judgments retained)
- `docs/ticket17_resolve_flagged_links.md`
