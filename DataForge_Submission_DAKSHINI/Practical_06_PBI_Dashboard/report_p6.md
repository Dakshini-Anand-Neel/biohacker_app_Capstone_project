# Practical 6 Report
**Author:** DAKSHINI
**Date:** 2026-07-01

# Practical 6: Power BI Executive Dashboard and Insight Story

## 1. Problem Statement
**Objective:** Design a single-page interactive report for the CEO. 
**Goal:** The dashboard must synthesize complex sales, profitability, and shipping data into a clean, easily digestible format that highlights overarching financial health and operational bottlenecks at a glance.

---

## 2. Concept Elaborated: Visual Hierarchy and Dashboard UX
**Why do we focus on layout and descriptive titles?** 
Visual hierarchy dictates how the human eye navigates information. By placing high-level KPI cards at the top, we immediately answer the most critical business questions (e.g., "What are our total sales?"). Detailed charts are positioned below for deeper exploration. Furthermore, using descriptive titles (e.g., "Technology Drives Top-Line Sales" instead of "Sales by Category") shifts the dashboard from merely *displaying* data to actively *communicating* insights, reducing the cognitive load on the executive.

---

## 3. Execution Steps
**IDE Setup & Workflow:**
1. **Data Preparation:** Imported the dataset into Power BI Desktop and verified table relationships in the Model view.
2. **Environment Configuration:** Set the canvas to a standard 16:9 ratio and enabled Map visuals within the Global Security Options.
3. **KPI Development:** Generated four Card visuals for Total Sales, Order Count, Order Size, and Shipping Delay, placing them in a horizontal row at the top of the canvas.
4. **Visual Construction:** Built four primary charts to address different analytical needs: a Line Chart (Trend over time), a Clustered Bar Chart (Category comparison), a Map (Geographic performance), and a Scatter Plot (Outlier analysis).
5. **Interactivity & Polish:** Inserted slicers for Date, Category, and Segment to enable user-driven filtering. Replaced default chart names with insight-driven titles.
6. **Export:** Saved the `.pbix` file and exported the final view to `dashboard_export.pdf`.

---

## 4. Key Insights
* **Seasonal Sales Dominance:** The trend line reveals distinct seasonal peaks, indicating that the bulk of annual revenue is concentrated in specific fiscal periods.
* **Category Discrepancies:** While top-level categories like Technology lead in total volume, the scatter plot highlights that performance and efficiency vary drastically when drilling down into specific sub-categories.
* **Geographic Bottlenecks:** The map, cross-referenced with shipping metrics, exposes specific regions that experience disproportionate shipping delays relative to their overall sales volume.

---

## 5. Report Questions

**What is the dashboard’s main business message?**
The dashboard tracks the correlation between sales volume and order size while actively monitoring shipping performance to identify geographic and categorical bottlenecks.

**Which filter changes the story most strongly?**
The **Time (Date) Slicer**. It possesses the strongest impact because it instantly shifts the narrative from a long-term historical growth view to a granular, short-term seasonal performance view.

**What would you improve if you had one more day?**
I would implement **Tooltips** on the scatter plot and map to reveal underlying metrics (like profit or distinct customer count) when hovering over data points, and I would configure a **Bookmark-driven "Reset Filters" button** to improve the user experience for the CEO.
