# ba_da_course_homeworks
# Main README (for root of repo)

## Overview

This repository contains several key directories related to data analysis, reporting, and visualization. Each folder includes its own README with details about the contents and their intended usage.

## Directory Structure

* **excel/** – Contains Excel workbooks used for analysis, reporting, and data preparation.
* **queries/** – Stores SQL queries used for data extraction and transformations.
* **tableau/** – Includes Tableau workbooks, dashboards, and related assets.
* **looker_studio/** – Contains Looker Studio dashboard resources, exports, and documentation.

## Purpose

This repo centralizes analytical assets to ensure consistency, collaboration, and version control across projects.

---

# excel/README.md

## Excel Folder

This folder contains all Excel-based data, including datasets, reports, calculations, and intermediate processing files.

### Typical Contents

* Raw and cleaned datasets
* KPI or metrics reports
* Pivot table models
* Data dictionary files

### Notes

* Large Excel files should be tracked with Git LFS.
* Use clear filenames with dates or version numbers.

---

# queries/README.md

## Queries Folder

This folder contains SQL queries used for reporting, dashboards, or data transformations.

### Typical Contents

* BigQuery SQL files
* Snowflake, Redshift, or PostgreSQL scripts
* ETL transformation queries

### Conventions

* Use descriptive filenames (e.g., `sales_summary.sql`, `customer_churn_query.sql`).
* Include comments inside SQL files explaining purpose and assumptions.

---

# tableau/README.md

## Tableau Folder

This folder contains all Tableau-related assets.

### Typical Contents

* Tableau Workbooks (`.twb`, `.twbx`)
* Data extracts (`.hyper`)
* Exported images or PDFs of dashboards

### Notes

* Avoid committing very large extract files unless necessary.
* Document data sources inside a README or within Tableau workbook notes.

---

# looker_studio/README.md

## Looker Studio Folder

This folder includes assets and documentation related to Looker Studio dashboards.

### Typical Contents

* Data source schemas
* Dashboard metadata
* Exported PDFs or images
* URL references (avoid storing sensitive links)

### Guidelines

* Document metric definitions.
* Include dates for dashboard updates.
