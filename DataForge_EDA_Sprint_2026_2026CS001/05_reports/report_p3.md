# Practical 3: Excel EDA & Interactive Pivot Dashboards

Student ID: 2026CS001
Name: Dakshini Anand Neel
Dataset: SuperStore Sale Dataset

## Problem Statement
Stakeholders require quick, dynamic summaries of performance metrics (Sales, Profit, Trends) without having to manually filter or read through thousands of rows of raw data. 

## Concept Elaborated
**Multi-dimensional Data Aggregation:** Pivot tables allow us to instantly group and summarize large datasets across multiple dimensions (like time, geography, and product category). By layering Slicers on top, we create an interactive data model where filtering one dimension automatically updates all related aggregations, providing instant answers to complex business questions.

## Execution Steps
1. Calculated baseline KPIs (Count, Sum, Average) on a dedicated summary sheet.
2. Built three distinct Pivot Tables to analyze Sales by Region, Profit by Category, and Sales Trend over time.
3. Generated Pivot Charts for visual representation and migrated them to a clean, gridless Dashboard sheet.
4. Implemented 'Year' and 'Country' Slicers, using "Report Connections" to link them across all pivot tables for unified interactivity.

## Key Insights & Evaluation
* **Which pivot table gave the most useful insight?**
  [Insert your answer. E.g., "The Profit by Category table was most useful because it instantly highlighted which product lines are actually driving revenue vs. causing losses."]
* **What changed when you used slicers?**
  [Insert your answer. E.g., "The slicers transformed static charts into a dynamic tool. Filtering by 'Year' revealed that regional performance drastically shifted between 2022 and 2023, a trend hidden in the overall aggregates."]
* **What is one limitation of doing this only in Excel?**
  [Insert your answer. E.g., "Excel struggles with massive datasets (over 1 million rows) and lacks automated data-refresh pipelines. If new data arrives, the dashboard requires manual updates and file sharing, whereas a tool like Power BI connects directly to live databases."]

## Step-by-Step Instructions to Create the Dashboard

This dashboard was generated using your provided dataset (`p2_excel_cleaning.xlsx`). Here are the steps to create interactive Slicers and PivotTables manually:

1. **Format as Table:** Open your raw data sheet, select all data (`Ctrl + A`), and press `Ctrl + T` to convert it to an Excel Table. This makes data updates dynamic.
2. **Insert Pivot Tables:**
   - Go to `Insert > PivotTable`. Place it in a new sheet.
   - **Pivot 1 (Performance by Category):** Drag `Category` to Rows, and `Sales` to Values.
   - **Pivot 2 (Performance by Region):** Create a new PivotTable. Drag `Region` to Rows, and `Sales` to Values.
   - **Pivot 3 (Orders by Month):** Create a new PivotTable. Drag `Order Date` to Rows (group by Month/Year), and `Sales` or Count of Orders to Values.
3. **Insert Pivot Charts:** Click anywhere inside each PivotTable, go to `Insert > PivotChart`, and choose the appropriate chart (Bar, Pie, Line). Cut and paste these charts onto a new "Dashboard" sheet.
4. **Add Slicers:**
   - Click on any PivotChart. Go to the `PivotChart Analyze` tab and click `Insert Slicer`.
   - Select `Year` and `Country`.
   - Right-click each Slicer, choose `Report Connections`, and check the boxes for all three Pivot Tables. Now, clicking the slicer updates the entire dashboard!
5. **Dashboard Polish:** Hide gridlines (`View > Gridlines`), align your charts, and add KPI text boxes for Total Sales, Unique Orders, and Total Customers.

---

## Report Questions

### 1. Which pivot table gave the most useful insight?
The **Performance by Category/Segment** pivot table provided the most actionable insight. It quickly identifies which product categories are driving the most revenue across different consumer segments, allowing for targeted marketing and inventory decisions.

### 2. What changed when you used slicers?
Slicers transformed the static charts into a **dynamic, interactive experience**. By clicking on a specific `Year` or `Country`, all connected Pivot Tables and Charts immediately filtered to show data *only* for that selection. This allows stakeholders to drill down into specific dimensions without needing separate reports.

### 3. What is one limitation of doing this only in Excel?
One major limitation is **scalability and automation with large datasets**. While Excel is great for quick EDA and dashboards on manageable datasets (like this one), its performance degrades significantly when handling millions of rows or connecting to complex, real-time data pipelines. For enterprise-scale dynamic dashboards, tools like Power BI, Tableau, or programmatic approaches (Python/Pandas/Dash) are far more robust and reproducible.
