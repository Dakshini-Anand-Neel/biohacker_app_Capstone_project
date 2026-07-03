# Practical 1 - SuperStore Sale Dataset Cleaning and Standardization
Student ID: 2026CS001
Name: Dakshini Anand Neel
Dataset: SuperStore Sale Dataset

## Problem Statement
The raw SuperStore sales dataset contained several structural integrity and data entry anomalies, including duplicate transaction entries, trailing whitespaces in text classifications, mismatched regional date formats, and empty or invalid metric values. If left untreated, these discrepancies break relational table joins, distort business intelligence metrics (such as inflating sales or miscalculating margins), and lead to incorrect forecasting. The objective was to transform this raw operational log into a validated, production-grade master workbook (`dataset_cleaned.xlsx`) to guarantee analytics accuracy.

## Procedure
1. **Ingestion & Dynamic Backup:** Imported the raw text asset `dataset_raw.csv` directly into Microsoft Excel and immediately isolated it by committing a copy as a structured workbook file named `dataset_cleaned.xlsx`.
2. **Primary Key Deduplication:** Highlighted the raw operational workspace matrix and executed the automated **Remove Duplicates** function across combined key identifiers (`Order ID` and `Product ID`) to drop redundant recurring records.
3. **String Trimming Manipulation:** Generated a temporary staging column applying the `=TRIM()` formula across text parameters like `Customer Name` and `Category` to completely scrub lingering trailing spaces.
4. **Hardcoding Computed Strings:** Extracted the cleaned, trimmed output strings and re-applied them back over the primary structural columns via **Paste Special > Values** to destroy active calculation dependencies before deleting the helper column.
5. **Date Uniformity Formatting:** Standardized irregular input strings (such as mixed `MM/DD/YYYY` and `YYYY-MM-DD` entries) by executing a column-wide explicit cell reset to **Short Date** structure matching universal system configurations.
6. **Logical Attribute Imputation:** Inspected empty attributes and imputed structural defaults (e.g., swapping missing client details with `"Unknown"`) to preserve complete row entries without skewing metrics.
7. **Mathematical Sign Inversion:** Corrected manual error flags under numerical columns—such as converting absolute absolute-value violations (negative sales parameters) into correct arithmetic positives.

## Outputs Created
* `dataset_raw.csv`: The initial unmodified, uncleaned comma-separated data dump.
* `dataset_cleaned.xlsx`: A multi-tab, fully formatted, polished enterprise Excel workbook complete with zebra-striped records, strict data validations, and active operational KPI evaluation cards.
* `data_dictionary.md`: A comprehensive metadata architecture registry clarifying field limits, constraints, and operational descriptions.

## Observations
* **Handling Web-Scraped Anomalies (Guide Question 1):** Excel's basic `=TRIM()` calculation string sweeps clean standard 7-bit ASCII space variants (value 32) but completely fails to acknowledge non-breaking spaces (`&nbsp;` or ASCII value 160) typical of web-extracted outputs. Cleaning these exceptions requires evaluating nested operations using `=TRIM(SUBSTITUTE(Cell, CHAR(160), " "))`.
* **Deduplication Validation Protocols (Guide Question 2):** Utilizing automated row deduplication sweeps without validating underlying primary keys introduces extreme structural liability. If valid recurring purchase actions occur within identical timestamp constraints and metadata blocks, blind algorithmic removal will discard legitimate revenue events. Unique entity validation must always precede global row purges.

## Conclusion
Standardizing the data using disciplined Excel validation workflows ensures that business decisions are based on accurate data, protecting the analytical environment from compounding downstream reporting errors.