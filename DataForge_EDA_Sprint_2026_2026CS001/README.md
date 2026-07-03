# The Biohacker Habit & Sleep Optimizer

Clinical-grade Streamlit dashboard for automated health telemetry analysis. The app helps users explore relationships between sleep, caffeine, screen time, activity, readiness, and circadian consistency through an interactive browser dashboard.

## Public App Link

Public demo link: **Not deployed yet**

After deployment, paste the real Streamlit link here:

```text
https://your-real-app-name.streamlit.app
```

Important: do not share a guessed Streamlit URL. It will show "You do not have access to this app or it does not exist" until the app is actually deployed and public.

## How The App Works

When the app opens, it automatically loads a sample patient dataset. This means reviewers can explore the dashboard immediately without uploading a file, downloading anything, or signing in.

The dashboard then cleans the telemetry data, fills missing numeric values with median values, detects outliers using the IQR method, calculates summary metrics, and generates charts and insights.

The main workflow is:

1. Open the public app link in a browser.
2. The sample patient dashboard loads by default.
3. Review the KPI cards for readiness, sleep, days analyzed, and circadian alignment.
4. Explore the tabs for clinical EDA, diagnostic charts, behavioral extremes, prediction simulation, and PDF export.
5. Optionally upload a patient CSV from the sidebar to analyze a custom dataset.

## Dashboard Tabs

### Clinical EDA

Shows the cleaned patient dataset, descriptive statistics, and detected outliers. This tab helps validate the data before interpreting results.

### Diagnostic Charts

Displays readiness trends, caffeine versus deep sleep analysis, and a habit correlation heatmap. It also includes statistical significance using Pearson correlation and p-values.

### Peak/Toxic Engine

Compares the best and worst readiness days. The app highlights top performance windows and clinical risk windows so users can see which behaviors may align with better or worse outcomes.

### What-If Simulator

Uses linear regression to estimate how changes in caffeine, screen time, and steps may affect predicted readiness and deep sleep. This is for educational exploration, not medical diagnosis.

### Export Report

Generates a one-page PDF summary with patient notes, telemetry averages, and key statistical findings. This can be used as a discussion aid with a doctor or sleep specialist.

## Data Input

The app works immediately with built-in sample patient data.

Optional CSV upload is supported from the sidebar. A custom CSV should include these columns:

```text
Date
Caffeine_mg
Screen_Time_Hours
Steps
Deep_Sleep_Hours
Daily_Readiness_Score
```

## Accessibility For Reviewers

After deployment, the app should open directly in a browser on Android, PC, or laptop. No download, installation, or sign-in is required for viewers.

The local URL below is only for the developer's network and should not be shared for public review:

```text
http://10.27.175.24:8501
```

## Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy Publicly

To make the app accessible to everyone:

1. Upload this project folder to a GitHub repository.
2. Go to Streamlit Community Cloud.
3. Create a new app from the GitHub repository.
4. Set the main file path to `streamlit_app.py`.
5. Keep the app visibility public.
6. Deploy the app.
7. Copy the generated `https://...streamlit.app` URL into the Public App Link section above.

## Project Files

- `streamlit_app.py` - Deployment entry point for Streamlit Cloud.
- `Biohacker_Habit_&_Sleep.py` - Main dashboard application.
- `requirements.txt` - Python dependencies needed to run the app.
- `.gitignore` - Excludes virtual environments and cache files from upload.

## Disclaimer

This project is an educational capstone dashboard. It provides statistical and exploratory insights, but it is not a medical device and should not replace professional medical advice.
