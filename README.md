# IRCC-CRS-points-prediction
I became a permanent resident of Canada this year. In the past, I noticed that many people—including myself—constantly checked the IRCC invitation website to monitor the cutoff scores. We wanted to understand how far we were from the required score and what steps we could take to improve our chances.
Inspired by this experience, I am starting to build a program that analyzes historical IRCC invitation data and predicts future cutoff scores across different immigration categories.

## IRCC CRS Dashboard

An **interactive dashboard** that visualizes Canada Express Entry Invitation trends over time, by category (e.g., CEC, PNP, FSW). Built using **Python**, **Dash**, **Plotly**, and **Pandas**.


## Features

- Interactive line charts showing **minimum CRS score trends**.
- Displays **invitations issued** for each draw when hovering.
- Filter by **invitation category** (CEC, PNP, FSW, etc.).
- Fully interactive zooming, panning, and tooltips.

---

## How to Run Locally
```
1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Run `python dashboard.py`
5. Open http://127.0.0.1:8050
6.Select a category to view CRS trends. Hover over points to see detailed information.
```

## Technologies:

- **Python** (data processing & analysis)

- **Pandas** (interactive web framework)

- **Dash** (data visualization)

- **Plotly** (data manipulation)

---

## Program structure  
```
IRCC_Project/
│
├─ dashboard.py
├─ requirements.txt
├─ data/
│   └─ ircc_analyzer_data.csv
└─ src/
    ├─ data_loader.py
    ├─ analyzer.py
    └─ visualizer.py
```
## Data Source
Official IRCC Express Entry rounds:
```
https://www.canada.ca/en/immigration-refugees-citizenship/corporate/mandate/policies-operational-instructions-agreements/ministerial-instructions/express-entry-rounds.html
```
