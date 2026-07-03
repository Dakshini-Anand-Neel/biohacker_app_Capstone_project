# Practical 9 Report

Student ID: 2026CS001
Name: Dakshini Anand Neel
Dataset: SuperStore Sale Dataset

# Practical 9: Statistical EDA & Correlation Analysis Report

## 1. Problem Statement
The objective of this analysis was to uncover hidden mathematical relationships between numerical variables within the dataset and rigorously summarize the data’s structural integrity. By quantifying missing data, establishing statistical summaries, and identifying correlated features, the goal was to transform raw data into a mathematically validated foundation for future predictive modeling and strategic decision-making.

## 2. Concept Elaborated
Statistical Exploratory Data Analysis (EDA) goes beyond simple visual observation by applying mathematical frameworks to quantify data behavior. 
* **Correlation Analysis:** Generating a correlation matrix allows us to measure the strength and direction of linear relationships between numerical variables. Identifying highly correlated pairs is crucial for predictive modeling, as it highlights key drivers and helps detect multicollinearity (where redundant variables skew model accuracy).
* **Data Distributions & Skewness:** Real-world data rarely follows a perfect bell curve. Measuring skewness (e.g., using `scipy.stats`) tells us if our data is symmetrical or skewed by heavy tails. For instance, right-skewed financial data often requires mathematical transformation (like a logarithmic scale) before being fed into machine learning algorithms that assume normal distribution.
* **Aggregation:** Grouping and ranking data summarizes granular records into macro-level trends, allowing us to benchmark performance across different categories.

## 3. Execution Steps
1. **Environment Setup:** Activated a Python virtual environment via PowerShell and installed necessary analytical dependencies (`pandas`, `scipy.stats`).
2. **Directory Initialization:** Configured a structured project workspace within the IDE, creating `04_python/notebooks/09_python_eda_tables.ipynb` and corresponding output folders.
3. **Data Summarization:** Loaded the dataset using `pandas`, executing `describe().T` for descriptive statistics and calculating the percentage of missing values per column. Exported results to `.csv`.
4. **Correlation & Shape:** Filtered the DataFrame for numerical columns to compute a correlation matrix (`df.corr()`). Extracted the highest positive correlation pair and calculated the skewness of the primary target metric.
5. **Categorical Analysis:** Utilized `groupby()`, `nlargest()`, and `nsmallest()` to engineer subset tables, isolating the top and bottom 10 performing records across specific categorical dimensions.

## 4. Key Insights
* **Primary Drivers Identified:** The correlation matrix revealed the strongest positive relationship between the top two numerical variables, indicating that they scale together and one could potentially be used to predict the other.
* **Distribution Asymmetry:** The target metric distribution exhibited notable skewness, suggesting a concentration of standard values disrupted by a long tail of extreme high or low outliers that pull the average away from the median.
* **Categorical Discrepancies:** The aggregated grouped tables demonstrated that the categories with the highest overall transaction count are not necessarily the ones yielding the highest maximum individual metrics, indicating distinct operational behaviors across segments.
