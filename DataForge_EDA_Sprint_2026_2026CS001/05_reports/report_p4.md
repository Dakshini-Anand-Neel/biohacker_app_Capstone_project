# Practical 4 Report
Student ID: 2026CS001
Name: Dakshini Anand Neel
Dataset: SuperStore Sale Dataset

# Practical 4: Power Query ETL Engine

### 1. Problem Statement
Automate the data transformation steps so that when new data arrives, cleaning is instantaneous. The goal is to build a reusable ETL (Extract, Transform, Load) pipeline that eliminates manual data wrangling.

### 2. Concept Elaborated: ETL Pipelines
**ETL (Extract, Transform, Load)** is the process of pulling data from a source (Extract), cleaning and structuring it (Transform), and placing it into a visualization tool (Load). In this practical, Power Query acts as the ETL engine, recording our cleaning steps sequentially without altering the original raw data.

### 3. Execution Steps / Procedure
**IDE Setup:** Power BI Desktop (Power Query Editor).

**Workflow:**
1. Connect Power BI to your raw CSV (`dataset_raw.csv`).
2. Open Power Query Editor.
3. Promote Headers, replace errors, extract the 'Year' from 'Order Date', and split the 'Order ID' column by delimiter.
4. Create a Conditional Column ("Order Size" -> If Sales > 500 then "Large Order" else "Standard Order").
5. Copy the Advanced Editor M code to a text file, then click Close & Apply.

### 4. Report Questions & Answers

**Q1: How is Power Query different from manual Excel cleaning?**
**Answer:** Power Query creates an automated, repeatable ETL pipeline rather than performing one-off manual changes. Unlike manual Excel cleaning where you alter the source cells directly (which is prone to human error), Power Query records a sequential list of transformation steps without changing the underlying raw data. It can also handle millions of rows smoothly, whereas Excel slows down.

**Q2: Which transformation would save time when new CSV data arrives?**
**Answer:** The structural transformations like "Split Column by Delimiter" and the "Conditional Column" logic save the most time. In Excel, splitting an ID or writing nested IF statements requires writing formulas and dragging them down thousands of rows every time new data arrives. In Power Query, simply hitting "Refresh" applies all these complex rules instantaneously.

### 5. Key Insights
* **Automation beats repetition:** Complex structural rules (like splitting columns and conditional logic) are saved in the backend, meaning new data is cleaned instantly with a single refresh.
* **Data Types Matter:** Conditional math logic will fail if numeric columns contain text or symbols. Cleaning out rogue characters (like `$`, `,`, or `?`) and enforcing strict data types is a mandatory first step.
* **Non-Destructive Process:** Power Query applies steps chronologically without destroying the original CSV file, preserving data integrity and making it easy to troubleshoot errors.