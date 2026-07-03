# DataForge Internship Folder Structure Guide

Use this guide to create both required master folders inside one internship folder.

Replace `YOURID` with your own name, roll number, or student ID before running the commands.

Recommended final layout:

```text
DataForge_Internship_YOURID/
|-- DataForge_Submission_YOURID/
`-- DataForge_EDA_Sprint_2026_YOURID/
```

## Option 1: Windows PowerShell

Open PowerShell in the drive or folder where you want to create the internship folder.

Example for E drive:

```powershell
E:
```

### 1. Create the Internship Master Folder

```powershell
New-Item -ItemType Directory -Force -Path "DataForge_Internship_YOURID"
Set-Location "DataForge_Internship_YOURID"
```

### 2. Create Submission Master Folder

```powershell
New-Item -ItemType Directory -Force -Path `
"DataForge_Submission_YOURID\Practical_01_Excel_Cleaning", `
"DataForge_Submission_YOURID\Practical_02_Excel_Stats", `
"DataForge_Submission_YOURID\Practical_03_Excel_Pivot", `
"DataForge_Submission_YOURID\Practical_04_PBI_PowerQuery", `
"DataForge_Submission_YOURID\Practical_05_PBI_DAX", `
"DataForge_Submission_YOURID\Practical_06_PBI_Dashboard", `
"DataForge_Submission_YOURID\Practical_07_Python_Pandas", `
"DataForge_Submission_YOURID\Practical_08_Python_Wrangling", `
"DataForge_Submission_YOURID\Practical_09_Python_Stats", `
"DataForge_Submission_YOURID\Practical_10_Python_Visuals", `
"DataForge_Submission_YOURID\Capstone_WebApp_Deployment"
```

### 3. Create EDA Sprint Master Folder

```powershell
New-Item -ItemType Directory -Force -Path `
"DataForge_EDA_Sprint_2026_YOURID\00_admin", `
"DataForge_EDA_Sprint_2026_YOURID\01_data\raw", `
"DataForge_EDA_Sprint_2026_YOURID\01_data\interim", `
"DataForge_EDA_Sprint_2026_YOURID\01_data\processed", `
"DataForge_EDA_Sprint_2026_YOURID\02_excel", `
"DataForge_EDA_Sprint_2026_YOURID\03_powerbi", `
"DataForge_EDA_Sprint_2026_YOURID\04_python\notebooks", `
"DataForge_EDA_Sprint_2026_YOURID\04_python\scripts", `
"DataForge_EDA_Sprint_2026_YOURID\04_python\outputs\tables", `
"DataForge_EDA_Sprint_2026_YOURID\04_python\outputs\plots", `
"DataForge_EDA_Sprint_2026_YOURID\05_reports", `
"DataForge_EDA_Sprint_2026_YOURID\06_app", `
"DataForge_EDA_Sprint_2026_YOURID\07_submission"

New-Item -ItemType File -Force -Path `
"DataForge_EDA_Sprint_2026_YOURID\README.md", `
"DataForge_EDA_Sprint_2026_YOURID\05_reports\final_reflection.md"
```

### 4. Check the Created Structure

```powershell
Get-ChildItem -Recurse
```

## Option 2: Git Bash / Linux / macOS Terminal

Open Git Bash, Linux terminal, or macOS terminal in the location where you want to create the internship folder.

### 1. Create the Internship Master Folder

```bash
mkdir -p DataForge_Internship_YOURID
cd DataForge_Internship_YOURID
```

### 2. Create Submission Master Folder

```bash
mkdir -p DataForge_Submission_YOURID/{Practical_01_Excel_Cleaning,Practical_02_Excel_Stats,Practical_03_Excel_Pivot,Practical_04_PBI_PowerQuery,Practical_05_PBI_DAX,Practical_06_PBI_Dashboard,Practical_07_Python_Pandas,Practical_08_Python_Wrangling,Practical_09_Python_Stats,Practical_10_Python_Visuals,Capstone_WebApp_Deployment}
```

### 3. Create EDA Sprint Master Folder

```bash
mkdir -p DataForge_EDA_Sprint_2026_YOURID/{00_admin,01_data/{raw,interim,processed},02_excel,03_powerbi,04_python/{notebooks,scripts,outputs/{tables,plots}},05_reports,06_app,07_submission}
touch DataForge_EDA_Sprint_2026_YOURID/README.md DataForge_EDA_Sprint_2026_YOURID/05_reports/final_reflection.md
```

### 4. Check the Created Structure

```bash
find . -maxdepth 4 -type d | sort
```
