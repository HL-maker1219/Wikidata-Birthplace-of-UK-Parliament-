import pandas as pd
import folium

df = pd.read_csv("parliament_ranges\parliament_1801-1802.csv")

# Process coordinates into latitude and longitude
df[['longitude', 'latitude']] = df['coordinates'].str.extract(r'\(([-\d.]+) ([-\d.]+)\)')

# Convert latitude and longitude to numeric
df['latitude'] = pd.to_numeric(df['latitude'])
df['longitude'] = pd.to_numeric(df['longitude'])

# Create a Folium map centered on the average latitude and longitude
map_center = [df['latitude'].mean(), df['longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=6)

# Add markers to the map
for _, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row['member']} - {row['birthPlace']}",
        tooltip=row['member']
    ).add_to(m)


m.save("map.html")

print("Map saved as 'map.html")