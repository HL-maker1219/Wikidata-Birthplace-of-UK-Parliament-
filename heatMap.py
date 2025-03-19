import pandas as pd
import folium
from folium.plugins import HeatMap
import os

output_folder = 'heat_map'
df = pd.read_csv(r"parliament_ranges\\parliament_1900-1920.csv")
range = '1-1'
# Process coordinates 
df[['longitude', 'latitude']] = df['coordinates'].str.extract(r'\(([-\d.]+) ([-\d.]+)\)')

# Convert latitude and longitude to numeric
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')  
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

#In case NaN
df.dropna(subset=['latitude', 'longitude'], inplace=True)


if df.empty:
    print("No valid coordinate")
else:
    # Create a Folium map 
    map_center = [df['latitude'].mean(), df['longitude'].mean()]
    m = folium.Map(location=map_center, zoom_start=6)

    # Prepare data for the heatmap list of [latitude, longitude]
    heat_data = df[['latitude', 'longitude']].values.tolist()
    
    #heat map radius adjust
    HeatMap(heat_data, radius=10, blur=5).add_to(m)

    m.save('heatMap.html')
    print("heat map complete")
    
