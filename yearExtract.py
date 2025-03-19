import pandas as pd
import os

#This file is used to filter the list of parliament member overlaps terms of years, e.g. the parliament member from 2000 to 2010

output_folder = 'parliament_ranges'
df = pd.read_csv('parliament_simp.csv')

os.makedirs(output_folder, exist_ok= True)

#Set period here 
start_year = 1900
end_year = 1920

filtered = df[
    (df['start'] <= end_year)&
    (df['end'] >= start_year)
]

filtered = filtered.drop_duplicates(subset='member')

output_file = os.path.join(output_folder, f'parliament_{start_year}-{end_year}.csv')

filtered.to_csv (output_file, index=False)
print(f"parliament{start_year}-{end_year}.csv pocessed complete")


