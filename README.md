# 🛍️ E-Commerce Data Insights

An interactive data analytics project built with **Python**, **pandas**, **SQLite**, **Streamlit**, and **Plotly**, consuming real product data from the [Fake Store API](https://fakestoreapi.com/).

This project demonstrates a full **data pipeline** — from API integration and database storage to data processing, visualization, and business insights.

---

## 🚀 Features

✅ Real API data consumption (Fake Store API)  
✅ Data cleaning and transformation with `pandas`  
✅ Local storage with `SQLite`  
✅ Interactive dashboard built with `Streamlit`  
✅ Visual insights using `Plotly` charts  
✅ CSV export for use in Power BI or other BI tools  
✅ Type-safe and fully annotated Python code

---

## 🧠 Tech Stack

| Layer           | Technology              | Purpose                        |
| --------------- | ----------------------- | ------------------------------ |
| Database        | **SQLite**              | Lightweight local database     |
| Data Processing | **pandas**              | ETL (Extract, Transform, Load) |
| Visualization   | **Streamlit + Plotly**  | Interactive dashboards         |
| BI Tool         | **Power BI (optional)** | Executive reporting            |
| Language        | **Python 3.11+**        | Main language                  |

---

## 📂 Project Structure

ecommerce-insights/  
├── backend/  
│ ├── db.py # Database connection and table creation  
│ ├── fetch_data.py # Fetches and saves API data into SQLite  
│  
├── data_processing/  
│ └── process_data.py # Cleans and exports data using pandas  
│  
├── dashboard/  
│ └── app.py # Streamlit dashboard (interactive visuals)  
│  
├── exports/  
│ └── clean_data.csv # Processed data exported for Power BI  
│  
├── requirements.txt  
└── README.md  
  
---

## ⚙️ Installation

## 1️⃣ Clone the repository

git clone https://github.com/kevincamussi/e-commerce-data-insights.git  
cd ecommerce-data-insights

## 2️⃣ (Optional) Create a virtual environment

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)

## 3️⃣ Install dependencies

pip install -r requirements.txt

## 🧩 Usage  
## 1️⃣ Create the database and populate it

python backend/db.py
python backend/fetch_data.py

## 2️⃣ Process and clean the data

python data_processing/process_data.py

## 3️⃣ Launch the dashboard

streamlit run dashboard/app.py
Then open the link provided (usually http://localhost:8501) to view the interactive dashboard.

## 📊 Dashboard Overview  
Streamlit Dashboard Features:

Filter by category

KPIs: Total Products, Average Price, Total Profit

Bar chart: Price × Profit per Product

Scatter chart: Price × Rating per Category

**Example visuals:**

## 📈 Power BI Integration (Optional)
You can import the exported file exports/clean_data.csv into Power BI for advanced BI dashboards and executive reports.

Steps:

Open Power BI Desktop

Go to Get Data → CSV

Select exports/clean_data.csv

Build visuals and insights

