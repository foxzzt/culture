# Ticket 19 Summary: Augmented IPR Bounds

Table A16 adds national representative inheritors who are attributed to each province but are not found on the corresponding provincial representative-inheritor roster. The fuzzy-overlap variant uses Table A15's exact-or-fuzzy overlap classification; the exact-only variant treats fuzzy project-name matches as missing, so it provides a larger add-back and brackets the correction.

Quality-gate anchors, fuzzy-overlap variant:

- Guangdong: (494 + 157) / 844 = 0.771
- Liaoning: (220 + 61) / 294 = 0.956
- Jilin: (215 + 26) / 442 = 0.545
- Jiangsu: (820 + 37) / 1,166 = 0.735

Under the fuzzy-overlap augmentation, 8 provinces remain below parity: Jilin, Guizhou, Jiangsu, Guangdong, Tianjin, Shandong, Shaanxi, Liaoning. The exact-only augmentation is weakly larger and leaves 8 provinces below parity: Jilin, Guizhou, Jiangsu, Guangdong, Tianjin, Shandong, Shaanxi, Liaoning.

The national source contains 3,995 rows; 3,881 are mapped to the 31 province rows used here, so the 114 non-provincial national rows are excluded. Because cross-level project-name mismatch can classify real overlaps as missing, the augmented numerator is an upper-bound correction rather than a replacement for the baseline roster IPR.

Files written:

- `tables/table_A16_augmented_ipr_bounds.csv`
- `tables/table_A16_augmented_ipr_bounds.tex`
- `docs/ticket19_augmented_ipr_bounds.md`
