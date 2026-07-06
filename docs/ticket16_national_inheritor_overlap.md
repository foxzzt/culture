# Ticket 16 Summary: National Inheritor Overlap with Provincial Rosters

## Source and Anchor

- Official source page: `https://www.ihchina.cn/representative`.
- Official API used for extraction: `https://www.ihchina.cn/art/representative.html` with filters blank and paginated `limit=200`.
- The official page text states that six batches were named in 2007, 2008, 2009, 2012, 2018, and 2025 and that the national representative-inheritor total is **3,994** as of December 2025.
- The same official page's JSON API reports and returns **3,995** rows. The row-level analysis below uses the API-returned **3,995** rows because those are the records exposed by the official list endpoint. There are no duplicate `(name, project, province/unit)` records in the API extract.

## Batch Counts from Official API Extract

| batch | api_rows |
| --- | --- |
| 01(2007年（第一批）) | 226 |
| 02(2008年（第二批）) | 550 |
| 03(2009年（第三批）) | 705 |
| 04(2012年（第四批）) | 495 |
| 05(2018年（第五批）) | 1077 |
| 2025(2025年（第六批）) | 942 |

Rows mapped to the 31-province table: **3,881**. Rows not mapped to a mainland provincial unit: **114**. Province strings that begin with a provincial short name are mapped to the corresponding 31-province row; central-unit, Hong Kong, and Macau rows are left outside province rows.

## Main Result

The mean provincial roster overlap share is **0.121** with standard deviation **0.072**. The low-outlier threshold (`mean - 2 sd`) is **-0.024**.

- Minimum overlap share: **Jilin** = **0.028** (6 of 215 provincial roster rows).
- Maximum overlap share: **Beijing** = **0.364** (102 of 280 provincial roster rows).
- Provinces more than 2 SD below the mean: **0**.

## Guangdong Check

Guangdong has **494** provincial roster inheritor rows and **190** national representative-inheritor rows attributed to Guangdong. The match finds **33** provincial roster rows also appearing on the national list (**33** exact project-name matches and **0** fuzzy project-name matches), for an overlap share of **0.067**. Guangdong's share is **below** the 31-province mean by **-0.055**, and it is **not a >2 SD low outlier** under this diagnostic.

National rows attributed to Guangdong but not found in the 2005-2024 provincial roster: **157**.

## Lowest Shares

| province_name_english | provincial_roster_inheritors | national_attributed_to_province | overlap_total | overlap_share | national_not_on_provincial_roster |
| --- | --- | --- | --- | --- | --- |
| Jilin | 215 | 32 | 6 | 0.028 | 26 |
| Heilongjiang | 613 | 35 | 23 | 0.038 | 12 |
| Chongqing | 787 | 74 | 30 | 0.038 | 44 |
| Ningxia | 378 | 30 | 16 | 0.042 | 14 |
| Guangxi | 936 | 66 | 52 | 0.056 | 14 |
| Liaoning | 220 | 75 | 14 | 0.064 | 61 |
| Guangdong | 494 | 190 | 33 | 0.067 | 157 |
| Gansu | 746 | 84 | 55 | 0.074 | 29 |

## >2 SD Low-Outlier Rows

None.

## Files Written

- `tables/table_A15_national_overlap.csv`
- `tables/table_A15_national_overlap.tex`
- `docs/ticket16_national_inheritor_overlap.md`

Local-only, not for GitHub: `C:\Users\14706\Documents\culture\scratch_private\ticket16_provincial_national_match_detail_local.csv` and `C:\Users\14706\Documents\culture\scratch_private\national_inheritors_ihchina_raw.csv`.
