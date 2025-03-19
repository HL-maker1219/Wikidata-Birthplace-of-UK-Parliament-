import pandas as pd
import os

#This file is filter the parliament member list in terms of the number of the parliament they are in, 
# e.g. Devided the entire parliament history into 10 parliament in a file, 1st-10th, 11th-20th
#Also can be use to filter a specfic parliament out

file_path = 'parliament_simp.csv'  
output_folder = 'parliament_ranges'  
df = pd.read_csv(file_path)

os.makedirs(output_folder, exist_ok=True)

# Define range 
range_step = 1

#set the limmited of the parliament number 
min_parliament = df['parliament'].min()
max_parliament = df['parliament'].max()

# Loop through the ranges and filter the data
for start in range(min_parliament, max_parliament + 1, range_step):
    end = start + range_step - 1
    range_label = f"{start}-{end}"

    range_df = df[(df['parliament'] >= start) & (df['parliament'] <= end)]

    if range_df.empty:
        continue

    output_file = os.path.join(output_folder, f"parliament_{range_label}.csv")
    range_df = range_df.drop_duplicates(subset='member')
    range_df.to_csv(output_file, index=False)
    print(f"Saved range {range_label} to {output_file}")

print(f"All ranges saved in the folder: {output_folder}")
