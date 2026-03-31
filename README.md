# 🍔 Tasky Bytes App – Sales Dashboard

## 📌 Overview

The **Tasky Bytes App** is an interactive data dashboard built using **Streamlit** and **Snowflake Snowpark**.
It provides insights into sales performance by allowing users to filter data by city and shift, and visualize trends through charts and maps.

---

## 🚀 Features

* 🔍 **Interactive Filters**

  * Filter data by **City** and **Shift**

* 💰 **Key Metrics**

  * Total Sales
  * Number of Locations
  * City Population

* 📈 **Data Visualization**

  * Sales trend (line chart)
  * Sales by day (bar chart)

* 🗺️ **Geospatial Map**

  * Displays store locations using latitude & longitude

* 📋 **Data Table**

  * Full dataset preview

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Snowflake Snowpark
* **Language:** Python
* **Database:** Snowflake

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Yoskie066/Tasky_Bytes_App.git
cd Tasky_Bytes_App
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file:

```env
SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ROLE=ACCOUNTADMIN
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_DATABASE=FROSTBYTE_TASTY_BYTES_DEV
SNOWFLAKE_SCHEMA=PUBLIC
```

---

### 4. Run the app

```bash
streamlit run streamlit_app.py
```

---

## 📊 Data Source

The data is retrieved from:

```
FROSTBYTE_TASTY_BYTES_DEV.PUBLIC.SHIFT_SALES_V
```

---

## ⚡ Performance Optimization

* Streamlit caching (`@st.cache_data`, `@st.cache_resource`)
* Query filtering in Snowflake
* Limited dataset (`LIMIT 1000`)

---

## 🔒 Security

* Sensitive credentials are stored in `.env`
* `.env` should NOT be pushed to GitHub

---

## ⭐ Notes

This project demonstrates:

* Real-time data fetching from Snowflake
* Dashboard development using Streamlit
* Data visualization and filtering
