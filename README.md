# lol-encyclopedia-lakehouse

## :open_book: Project Overview

The goal of this web app is to provide the following information of the League of Legends ecosystem:

- Display every champion statistics (cf. base stats, mana/energy/HP costs, etc...)
- Update these stats on every new patch.
- Display more advanced information (cf. champion % pick rate)

### :hammer_and_wrench: Tools

- Docker
- GitHub Actions
- Pytest
- Terraform
- Airflow
- Python + PySpark
- AWS + Databricks
- Streamlit

### :building_construction: Data Architecture

The data architecture for this project follows Medallion Architecture Bronze, Silver, and Gold layers:

1. Bronze Layer: Stores raw data as-is from the source systems.
2. Silver Layer: This layer includes data cleansing, standardization, and normalization processes to prepare data for analysis.
3. Gold Layer: Houses business-ready data modeled into a star schema required for reporting and analytics.
