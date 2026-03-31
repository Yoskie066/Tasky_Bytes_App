import streamlit as st
from snowflake.snowpark import Session
import os
from dotenv import load_dotenv

# =======================
# LOAD ENV VARIABLES
# =======================
load_dotenv()

connection_parameters = {
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "role": os.getenv("SNOWFLAKE_ROLE"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA")
}

# =======================
# CACHE SESSION (IMPORTANT 🚀)
# =======================
@st.cache_resource
def create_session():
    return Session.builder.configs(connection_parameters).create()

session = create_session()

# =======================
# STREAMLIT CONFIG
# =======================
st.set_page_config(layout="wide")
st.title("🍔 Tasty Bytes Sales Dashboard")

# =======================
# LOAD FILTER OPTIONS (LIGHT QUERY)
# =======================
@st.cache_data
def load_filter_options():
    query = """
    SELECT DISTINCT CITY, SHIFT
    FROM FROSTBYTE_TASTY_BYTES_DEV.PUBLIC.SHIFT_SALES_V
    """
    return session.sql(query).to_pandas()

filter_df = load_filter_options()

# =======================
# SIDEBAR FILTERS
# =======================
st.sidebar.header("🔍 Filters")

city = st.sidebar.selectbox(
    "Select City", sorted(filter_df["CITY"].dropna().unique())
)

shift = st.sidebar.selectbox(
    "Select Shift", sorted(filter_df["SHIFT"].dropna().unique())
)

# =======================
# LOAD FILTERED DATA (FAST QUERY 🔥)
# =======================
@st.cache_data
def load_data(city, shift):
    query = f"""
    SELECT 
        CITY,
        SHIFT,
        SHIFT_SALES,
        LOCATION_ID,
        CITY_POPULATION,
        DAY_OF_WEEK,
        LATITUDE,
        LONGITUDE
    FROM FROSTBYTE_TASTY_BYTES_DEV.PUBLIC.SHIFT_SALES_V
    WHERE CITY = '{city}'
    AND SHIFT = '{shift}'
    LIMIT 1000
    """
    return session.sql(query).to_pandas()

with st.spinner("Loading data..."):
    df = load_data(city, shift)

# =======================
# HANDLE EMPTY DATA
# =======================
if df.empty:
    st.warning("No data available for selected filters")
    st.stop()

# =======================
# METRICS
# =======================
col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", round(df["SHIFT_SALES"].sum(), 2))
col2.metric("📍 Locations", df["LOCATION_ID"].nunique())
col3.metric("👥 Population", int(df["CITY_POPULATION"].mean()))

# =======================
# CHARTS
# =======================
col4, col5 = st.columns(2)

with col4:
    st.subheader("📈 Sales Trend")
    st.line_chart(df["SHIFT_SALES"])

with col5:
    st.subheader("📊 Sales by Day")
    day_sales = df.groupby("DAY_OF_WEEK")["SHIFT_SALES"].sum()
    st.bar_chart(day_sales)

# =======================
# MAP
# =======================
st.subheader("🗺️ Location Map")

map_data = df[["LATITUDE", "LONGITUDE"]].dropna()

if not map_data.empty:
    st.map(map_data)
else:
    st.info("No map data available")

# =======================
# DATA TABLE
# =======================
st.subheader("📋 Detailed Data")
st.dataframe(df)

