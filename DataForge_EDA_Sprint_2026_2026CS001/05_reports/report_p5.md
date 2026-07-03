# Practical 5 Report
Student ID: 2026CS001
Name: Dakshini Anand Neel
Dataset: SuperStore Sale Dataset

## 1. Problem Statement
The objective was to enhance a raw dataset by implementing relational modeling and formulating advanced metrics. This involved creating a dedicated date dimension, establishing model relationships, and defining key analytical metrics (DAX) to enable deeper data exploration.

## 2. Concept Elaborated
* **Relational Modeling**: Organizing data into a star schema by separating transactional data from dimensional data (Dates) to enable time-intelligence filtering.
* **DAX (Data Analysis Expressions)**: A formula language used to create custom calculations that aggregate or transform data dynamically based on the report context.
* **Calculated Columns vs. Measures**: Calculated columns are static values computed at refresh time and stored in memory, whereas measures are dynamic calculations evaluated at query time based on user interactions.

## 3. Execution Steps
* **Model Setup**: Created a `DateTable` using `CALENDARAUTO()` and established a One-to-Many relationship between the `DateTable` and `Query1` via the `Order Date` field.
* **Feature Engineering**: Added a `Unique Order ID` and `Shipping Delay` as calculated columns to facilitate accurate row-level analysis.
* **Metric Formulation**: Developed DAX measures (`Total Sales`, `Order Count`, `Average Sales per Order`, `Transaction Volume`) to enable quantitative tracking.

## 4. Key Insights
- **Data Integrity**: Establishing unique keys (e.g., `Unique Order ID`) is essential when primary keys are composite or non-unique across the dataset.
- **Dynamic Analysis**: Using `DIVIDE` for ratio calculations provides built-in error handling for divide-by-zero scenarios.
- **Model Efficiency**: Moving calculations from columns to measures reduces memory footprint and improves overall report performance.

### Report Questions

1. **What is the difference between a column and a measure?**
   - **Calculated Column**: Evaluated at the row level during data refresh and stored in memory. They are ideal for filtering or grouping data.
   - **Measure**: Evaluated at query time based on the active filter context. They are calculated on-the-fly and are ideal for aggregations.

2. **Which KPI would you put on top of the dashboard and why?**
   - I would place **Total Sales** at the top. It is the primary financial indicator of business health, providing an immediate snapshot of revenue performance that guides all subsequent exploratory analysis.
