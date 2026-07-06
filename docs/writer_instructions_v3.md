# Writing Agent Instructions: Manuscript v3 Integration

Date: 2026-07-06 (v3.1, updated same day with Ticket 15 results)
From: Strategy/Referee agent, via Tony
Manuscript base: cultural_policy_revised_v2 (the version with all nine TODO[DATA] closed, 43 pages)
Repo inputs: fetch raw files from https://raw.githubusercontent.com/foxzzt/culture/main/

Scope: integrate the round-2 acceptance results and the M13 Part B policy findings. Two items remain HOLD (items 6 and 16); they wait on Codex Tickets 17 and 16 and will arrive as short summaries in docs/. Everything else can be executed now. Do not change the paper's descriptive framing, section order, or headline structure. Word budget is already near the 11,000 ceiling, so offset additions with trims in the sections named below.

## A. Appendix table integration

1. Replace the Table A10 input with tables/table_A10_composition_adjusted_ipr.tex (absolute Kitagawa contributions, Flag column). Delete any residual description of "share of gap" in the A10 discussion and table cross-references.
2. Add tables/table_A11_lagged_denominator_ipr.tex through table_A14_parity_flip_recount.tex to the appendix in numeric order. Update all in-text citations: lagged-denominator claims in Section 4.2 cite Table A11; exact-versus-fuzzy rates cite Table A12; category match rates cite Table A13; flip counts in Section 5.3 cite Table A14.
3. Transcribe the decomposition formula from docs/ticket12_methods_note.md into the paper, either at the end of the data section or as a short methods appendix. The required content is the additive identity, the definition of both contributions, the national benchmark value 1.073861, the 101 excluded non-standard records, and the degenerate-cell flag rule. Keep it under 200 words plus the displayed equation.

## B. Section 4.2, match rate paragraph

4. Report the exact-match-only national rate 0.500 alongside the fuzzy rate 0.511, with the sentence that the headline "roughly half of projects have no certified inheritor on record" survives the conservative linkage that uses exact name matches only.
5. Revise the lower-bound sentence. The current text treats reported rates as lower bounds without qualification. New logic: rates are lower bounds with respect to unlinked inheritor records (12.6 percent unmatched), and the false-positive risk of fuzzy links is bounded by an audit.
6. Audit sentence, two variants. HOLD until Ticket 17's summary arrives, then use exactly one.
   Variant A, if all three flagged links resolve as same_project: "All 100 sampled fuzzy links were reviewed by two independent automated semantic judgments; three initially uncertain links were resolved against the underlying registries and confirmed, implying an exact binomial 95 percent upper bound of roughly 3.6 percent on the false-positive rate."
   Variant B, if any link is a confirmed false positive: use the corrected count from the Ticket 17 summary and its reported upper bound, and soften the Section 4.2 lower-bound sentence accordingly.
   Do not use the words "manual" or "human" for this audit anywhere.

## C. Category and case material

7. Add one short paragraph to Section 7: the project-level linkage corroborates the category gradient. Performing categories show coverage between 0.55 and 0.65; craft, knowledge, and folk-practice categories between 0.35 and 0.50 (Table A13). Add one sentence noting that even traditional drama, the highest-IPR category, has project coverage of only 0.646, so above-parity certification coexists with substantial uncovered projects everywhere.
8. Add the Hainan illustration where Section 4.2 discusses the IPR-coverage distinction: Hainan holds the second-highest IPR (1.724) with a bottom-quartile match rate (0.402), the sharpest case that aggregate parity and thin project coverage coexist (Table A9).

## D. Flip counts and batch timing

9. Section 5.3: state the tie rule explicitly. Under strict-below, nine provinces flip in each symmetric window. Add a footnote that treating exact parity as below shifts the counts to eight and ten, and that Liaoning's 2010 value of exactly 1.000 is the boundary case (Table A14). Keep the asymmetric-design flips (ten and twelve) clearly labeled as national-relative parity, not literal parity, in both Section 5.3 and the policy section.
10. Attach Table A11 citations where Guangdong's and Jiangsu's recent-batch match shares are invoked (0.122 and 0.152 against a national 0.309), in Section 4.2 and Section 10.

## E. Referee-report prose fixes (carried from the round-2 report)

11. Abstract: fix the Jiangsu claim. Guangdong survives both composition and batch-timing adjustments; Jiangsu survives composition but rises above literal parity under lagged denominators, so its position is partly a timing story. The abstract must carry this asymmetry.
12. Section 5.1 and abstract: disclose the membership change in the below-parity twelve under adjustment. Beijing and Heilongjiang exit; Anhui and Hebei enter. "The count is unchanged" may stay only if immediately followed by the membership disclosure.
13. Conclusion: replace the "all sit above parity, while ... all sit below it" sentence with Section 7's gradient language, including the acrobatics knife-edge qualification.
14. Title page: remove course-paper artifacts (CNetID, course TA acknowledgments). Keep a standard acknowledgment footnote.

## F. Section 4.1, registry-boundary caveat (M13 Part B resolved)

15. Delete the sentence stating that the provincial-exit rule upon national promotion is unknown and unsignable. Replace with: "Official rules and empirical cross-checks do not support treating national recognition as removing a project from provincial registries. In Guangdong's current official list of provincial-and-above representative projects, Cantonese opera is recorded with both provincial and national batch identifiers. We therefore treat provincial and national recognition as cumulative registry layers." Footnote the sources: Ministry of Culture and Tourism Order No. 3 (adopted 2019, effective 2020), the Guangdong provincial inheritor measures (Yue Wen Lv Gui 2021 No. 2), the Jilin provincial inheritor measures (2020), and the Guangdong provincial-and-above project list page (2025-01-20), with URLs as provided in Tony's findings note. Do not cite Jiangsu; it was not verifiable during the check.
16. Add one inheritor-side footnote: "Some administrative evaluation reports use a provincial-only scope that excludes national-level inheritors; Guangdong's 2022 provincial evaluation covered 546 inheritors explicitly excluding national-level ones. Whether published provincial rosters themselves exclude nationally promoted inheritors is examined in [HOLD: one sentence from Ticket 16 summary]." If Ticket 16 finds Guangdong is a low outlier in roster overlap, flag it to the strategy agent before writing; the Guangdong narrative may need more than a footnote.

## G. Holds and sequencing

17. Ticket 15 numbers are confirmed and can be written now. In every place the text cites scenic-area Ginis, use the corrected values: 5A scenic areas 0.2643 (was 0.3161) and all A-level scenic areas 0.2806 (was 0.3332), both computed on N=30 provinces because Hainan is absent from the scenic registry snapshot; Xinjiang's counts were corrected from a join error. Non-scenic Ginis are unchanged (projects 0.2374, inheritors 0.2430, IPR 0.1722). Add half a sentence where scenic-area inequality is discussed noting the N=30 basis. The physical files (updated table_A3 TEX, cleaned table_A2 TEX, regenerated fig_3 PDF) are finished on Codex's machine but not yet pushed to GitHub due to a temporary client block. Before final compile, pull the latest tables/ and figures/ from the repo and swap them in. If they have not arrived by your final compile, edit the two Gini values and the N column of table_A3 directly in your local copy, delete the library_count and cultural_capacity_proxy rows from table_A2, and flag in your delivery note that fig_3 still needs the regenerated PDF.
18. Word budget: offset additions by trimming the abstract (currently about 260 words; target under 200) and compressing the Section 5.1 opening paragraph, which should also be split into at least three paragraphs.
19. After integration, recompile and confirm zero errors, zero undefined references, and report the new word count. Deliver main.tex plus the full source zip as usual.
