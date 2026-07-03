# Practical 2: Descriptive Statistics & Outlier Detection

## 1. Problem Statement
The objective of this practical was to understand the numerical spread of our core sales data, establish a statistical baseline, and visually identify structural or operational anomalies (such as hidden text-format errors and negative profit margins) without altering the raw data structure.

## 2. Concept Elaborated
**Measures of Central Tendency and Dispersion:** Descriptive statistics (Mean, Median, Quartiles) allow us to summarize massive, complex datasets into a few understandable metrics. However, we actively look for and isolate outliers (extreme highs or lows) because they heavily skew metrics like the Mean. In business terms, identifying outliers—like negative profit margins—allows stakeholders to instantly spot critical revenue leaks that require immediate action, rather than letting those losses hide inside a "good" overall average.

## 3. Execution Steps
* **Data Validation Setup:** Executed Excel's `Text to Columns` feature on the Sales and Profit columns to strip hidden string characters (`?`) and force the system to recognize the data as calculable numbers.
* **Statistical Modeling:** Built a dedicated "Stats Summary" sheet using cross-sheet references to calculate `=AVERAGE()`, `=MEDIAN()`, `=STDEV.P()`, and `=QUARTILE()` without duplicating the raw data.
* **Visual Anomaly Detection:** Applied a Green-Yellow-Red color scale to the 'Sales' column to map variance, and built a custom Conditional Formatting rule (`Value < 0`) on the 'Profit' column to instantly highlight operational losses in red.

## 4. Key Insights
* **Format Dictates Function:** Hidden string characters completely block statistical formulas (triggering `#DIV/0!` and `#NUM!` errors), proving that data typing is a mandatory first step before any analysis.
* **Visual Masking is Highly Efficient:** By using custom conditional formatting, we isolated negative profit margins instantly, turning a dense matrix of numbers into an executive-ready visual dashboard.
* **Separation of Concerns:** By building the statistical calculations on a completely separate sheet from the data table, we maintained a clean, non-destructive analytical environment.

---

## 5. Evaluation Questions

**Which column had the highest data quality risk?**
The `Profit` column presented the highest data quality risk. It contained hidden text-formatting errors (such as the `?` symbol mapping issues) which caused the system to treat the numbers as strings. Additionally, it contained extreme negative outliers (operational losses) that would severely skew central tendency metrics if left unidentified.

**What cleaning decision did you take and why?**
1. **Schema Correction:** I used `Text to Columns` to force the system to recognize the data as calculable numbers so statistical formulas could execute. 
2. **Visual Masking over Deletion:** Instead of deleting the negative profit outliers, I applied a custom Conditional Formatting rule to highlight them in red. I made this decision because negative profit is a valid, critical business metric (a loss), and highlighting it allows stakeholders to see the anomalies instantly without destroying the integrity of the total dataset. 

**Why should raw data and cleaned data be kept separately?**
Keeping raw and cleaned data separated is a fundamental principle of data governance. The raw data acts as an immutable "Single Source of Truth." If a mistake is made during the cleaning pipeline, or if valid rows are accidentally deleted, keeping the files separate ensures we can safely roll back to the pristine raw data and start over, preserving the data lineage for auditing.