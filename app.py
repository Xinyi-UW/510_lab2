import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Load your dataset
@st.cache_data
def load_data():
    data_path = 'BostonHousing.csv'
    df = pd.read_csv(data_path)
    return df

df = load_data()


# Title and overview
st.title('Boston Housing Dataset Visualization')
st.markdown("""
This application showcases the Boston Housing dataset which contains data about various housing attributes in the Boston area. Here are the key factors we'll explore:
- `dis`: Weighted distances to five Boston employment centers.
- `crim`: Per capita crime rate by town.
- `rm`: Average number of rooms per dwelling.
- `medv`: Median value of owner-occupied homes.

**Use the widgets to filter data and explore how these factors influence housing in Boston.**
""")

# Widgets for filtering
dis_range = st.slider("Select distance to employment centres", float(df['dis'].min()), float(df['dis'].max()), (float(df['dis'].min()), float(df['dis'].max())))
crim_range = st.slider("Select crime rate", float(df['crim'].min()), float(df['crim'].max()), (float(df['crim'].min()), float(df['crim'].max())))
rm_range = st.slider("Select number of rooms", float(df['rm'].min()), float(df['rm'].max()), (float(df['rm'].min()), float(df['rm'].max())))
medv_range = st.slider("Select median value of homes", float(df['medv'].min()), float(df['medv'].max()), (float(df['medv'].min()), float(df['medv'].max())))

# Filtering data
filtered_data = df[(df['dis'] >= dis_range[0]) & (df['dis'] <= dis_range[1]) &
                   (df['crim'] >= crim_range[0]) & (df['crim'] <= crim_range[1]) &
                   (df['rm'] >= rm_range[0]) & (df['rm'] <= rm_range[1]) &
                   (df['medv'] >= medv_range[0]) & (df['medv'] <= medv_range[1])]

# Visualization with Plotly Express
fig = px.scatter(filtered_data, x='rm', y='crim', size='dis', color='medv',
                 hover_name='dis', size_max=60,
                 title="Housing Data Visualization: Rooms vs. Crime Rate (Size by Distance, Color by Median Value)")
st.plotly_chart(fig, use_container_width=True)

# Generating latitude and longitude for demonstration (replace with real data for accurate mapping)
np.random.seed(42)
filtered_data['lat'] = np.random.uniform(low=42.23, high=42.40, size=len(filtered_data))
filtered_data['lon'] = np.random.uniform(low=-71.16, high=-70.92, size=len(filtered_data))

# Mapping
map_fig = px.scatter_mapbox(filtered_data, lat="lat", lon="lon", color="medv", size="dis",
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                            mapbox_style="carto-positron",
                            title="Map of Housing: Color by Median Value, Size by Distance to Employment")
st.plotly_chart(map_fig, use_container_width=True)
