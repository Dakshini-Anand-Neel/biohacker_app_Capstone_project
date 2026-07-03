# Practical 10 Report

Student ID: 2026CS001
Name: Dakshini Anand Neel
Dataset: SuperStore Sale Dataset

# Practical 10: Python Visual EDA and Student-Built Automation App

## 1. Problem Statement
The objective was to generate publication-ready statistical plots to conduct Exploratory Data Analysis (EDA). This involved programmatically visualizing sales performance, profit margins, and dataset anomalies (such as missing values and outliers) using Python, ensuring all outputs were automatically saved to a structured directory hierarchy.

## 2. Concept Elaborated: Visual EDA and Statistical Plotting
Visual Exploratory Data Analysis is critical because it reveals underlying patterns, trends, and anomalies that summary statistics often hide. 
* **Why do we use Boxplots for outliers?** Boxplots mathematically isolate outliers using the Interquartile Range (IQR). Identifying these extreme values is crucial because they can skew predictive models or misrepresent average performance (e.g., a single massive loss masking an otherwise profitable month). 
* **Why use a Correlation Heatmap?** Heatmaps visually map the correlation matrix, allowing us to instantly spot multicollinearity or the lack of linear relationships (like between Sales and Discount) using color gradients, which is much faster to interpret than raw numeric tables. Applying a high "Data-Ink Ratio" ensures these visualizations remain uncluttered and focused purely on the data.

## 3. Execution Steps
1. **IDE Setup:** Configured VS Code with the required Python and Jupyter extensions, ensuring the correct Python kernel was selected to execute the `.ipynb` file.
2. **Environment Initialization:** Imported `pandas`, `matplotlib.pyplot`, and `seaborn`, and applied a global aesthetic using `sns.set_theme()`.
3. **Data Generation & Injection:** Created a mock dataset representing a retail environment and intentionally injected mathematical outliers and missing `NaN` values to test the visualizations.
4. **Plot Generation:** Executed specific Seaborn functions (`histplot`, `boxplot`, `heatmap`, `barplot`, `lineplot`, `scatterplot`) to analyze different dimensions of the data.
5. **Automated Export:** Utilized `os.makedirs()` to ensure the output directory existed, and appended `plt.savefig()` to every plotting step to systematically export all 8 charts as `.png` files directly to `04_python/outputs/plots/`.

## 4. Key Insights
* **Profitability is not strictly tied to volume:** The scatter plot and correlation heatmap revealed that high sales volume does not guarantee high profit, indicating that discounting or categorical costs play a heavier role.
* **Anomalies drastically distort averages:** The boxplot successfully isolated severe, specific instances of negative profit (losses) that would have otherwise skewed the general understanding of average transaction profitability.
* **Automation streamlines reporting:** Programmatically saving charts via `plt.savefig()` removes the friction of manual image exports, creating a highly reproducible EDA pipeline where updating the data automatically updates all publication-ready visuals.