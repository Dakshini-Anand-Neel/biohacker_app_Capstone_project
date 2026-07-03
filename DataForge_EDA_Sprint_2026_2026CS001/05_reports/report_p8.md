# Execution Report: Practical 8 - Python Cleaning, Type Conversion & Feature Engineering

# Practical 8 Report
Student ID: 2026CS001
Name: Dakshini Anand Neel
Dataset: SuperStore Sale Dataset


## 1. Problem Statement
The objective of this practical was to clean, transform, and reshape raw dataset files using a programmatic, reproducible approach. The core challenge involved handling dirty data (missing values, duplicates, and incorrect data types) and transforming raw inputs into business-ready metrics by engineering new features and aggregating regional data, completely bypassing manual spreadsheet manipulation.

## 2. Concept Elaborated
**Programmatic Data Imputation & Feature Engineering**
Data in its raw form is rarely ready for analysis. We clean data programmatically (using Python scripts rather than Excel clicks) to ensure **absolute reproducibility**—meaning the exact same pipeline can be applied to new data tomorrow without manual effort. 
* **Imputation:** Replacing missing numerical values with the `.median()` rather than the mean is a deliberate choice, as the median is robust against extreme outliers that could artificially inflate or deflate the dataset's average. 
* **Feature Engineering:** We extract specific components from data (like `month` and `year` from a `datetime` object) or mathematically combine columns (like calculating `profit_margin`) because machine learning models and business dashboards require explicit, standardized signals to detect trends and seasonality.

## 3. Execution Steps
1. **IDE & Workspace Setup:** Utilized VS Code as the primary IDE. Established a strict, modular folder structure (`04_python/notebooks`, `04_python/scripts`, and `01_data/processed`) to separate raw data, reusable code, and exploratory analysis.
2. **Reusable Script Creation:** Developed a standalone Python file (`clean_dataset.py`) containing a master cleaning function. This function handled duplicate removal, dynamic threshold-based column dropping (>50% missing), numeric imputation, and categorical filling.
3. **Data Transformation:** Applied type conversions (parsing strings to `datetime`) and generated new columns for temporal tracking (Month/Year) and financial metrics (Profit/Profit Margin).
4. **Notebook Execution & Aggregation:** Imported the custom cleaning script into a Jupyter Notebook (`08_wrangling.ipynb`) running in VS Code. Applied `.groupby()` to the cleaned dataset to calculate average sales per region.
5. **Exporting Assets:** Saved the final preprocessed dataframe to `dataforge_cleaned.csv` and the aggregated metrics to `region_sales_aggregated.csv`.

## 4. Key Insights

**Discoveries:**
* **Modularity is crucial:** Abstracting the cleaning logic into a separate `.py` script keeps the Jupyter notebook clean and allows the same cleaning pipeline to be imported into other projects easily.
* **Preserving Categorical Data:** Filling missing categorical values with the string `"Unknown"` prevents massive data loss (which would occur if we simply dropped rows) while remaining highly transparent to downstream analysts.
* **The Power of Aggregation:** Using `.groupby()` instantly transformed hundreds of individual transactions into a clear, high-level overview of regional performance, demonstrating how raw data is summarized for executive decision-making.

**Report Questions:**
* **What cleaning decision could affect business conclusions?**
Replacing missing numerical values with the median alters the data's natural variance. While it protects against outliers, heavily relying on median imputation can skew overall totals and artificially smooth out underlying trends or localized anomalies in specific regions or demographics.
* **Which engineered feature is most useful and why?**
The `profit_margin` feature is the most useful because it normalizes profitability relative to revenue. Absolute sales numbers can be misleading if costs are also high; profit margin allows for a standardized, fair performance comparison across completely different products or regions regardless of their total sales volume.