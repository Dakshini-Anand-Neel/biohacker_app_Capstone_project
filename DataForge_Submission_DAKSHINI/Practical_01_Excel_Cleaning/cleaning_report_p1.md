# Practical 1 Report: SuperStore Dataset Cleaning
**Student ID:** 2026CS001 | **Name:** Dakshini Anand Neel | **Dataset:** SuperStore Sale Dataset

## 1. Problem Statement
The raw SuperStore transactional dataset contained data entry anomalies, including duplicate records, trailing spaces in categorical text, irregular date string formatting, and logical baseline errors (such as negative numbers in profit/sales metrics). If left untreated, these anomalies cause structural integrity issues, introduce computational inaccuracies into downstream data pipelines, and distort business intelligence dashboards. The objective of this practical was to clean, validate, and standardize these fields into a reliable database resource (`dataset_cleaned.xlsx`).

---

## 2. Concept Elaborated: Data Normalization & Cleaning Theory
* **Deduplication:** Multiple instances of identical primary transaction blocks skew basic statistical summaries, falsely inflating key metrics like total sales and unit volume counts. Systematic removal preserves unique entity occurrences.
* **Whitespace Trimming:** Extraneous leading or trailing spaces transform identical categories (e.g., `" Clothing "` vs. `"Clothing"`) into distinct unique entities during string evaluation. This fractures grouping filters and data aggregations.
* **Date Unification:** Database architectures require uniform ISO-compliant date types (`YYYY-MM-DD`). Inconsistent mix-and-match inputs prevent chronologically accurate sorting and break seasonal trend analysis.
* **Mathematical Boundary Enforcement:** Financial transaction metrics require strict mathematical domain compliance. Out-of-bounds metrics (like negative absolute sales figures) indicate system glitch points or data entry failures that must be logically inverted or flagged to preserve arithmetic continuity.

---

## 3. Execution Steps
1. **Environment Setup:** Opened Microsoft Excel and ingested the flat data resource `dataset_raw.csv`. Saved the active file instantly as an Excel Workbook structure named `dataset_cleaned.xlsx` to preserve standard features.
2. **Key Filtering Purge:** Marked the primary transaction array block and activated the native **Remove Duplicates** engine under the Data tab using the header structure.
3. **Text Vector Stripping:** Deployed a temporary staging column applying the `=TRIM()` formula across text fields like `Customer Name` and `Category`. Copied results and committed them as hardcoded string values using **Paste Special > Values**.
4. **Temporal Reconfiguration:** Converted mixed layout textual data entries within the date rows into uniform regional alignments by applying the native **Short Date** number-formatting wrapper.
5. **Sign Correction:** Corrected erroneous negative values in transaction metrics by replacing them with their absolute equivalents.

---

## 4. Key Insights
* **The `TRIM()` Limitation:** Standard Excel `=TRIM()` expressions fail to isolate or clear web-scraped non-breaking string space parameters (`CHAR(160)`). Removing these hidden blocks requires nesting operations via `=TRIM(SUBSTITUTE(A2, CHAR(160), " "))`.
* **Deduplication Liability Risks:** Executing a blanket automated duplicate purge across entire data rows without first checking underlying primary keys poses a major risk; it can inadvertently strip out separate, valid transactional purchases that happen to share identical metadata.
* **Downstream Alignment:** Standardizing text parameters and dates dramatically reduces system friction, turning broken, unparsed datasets into reliable inputs optimized for Pivot Table manipulation.