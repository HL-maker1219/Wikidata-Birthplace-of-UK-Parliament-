import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('parliament_simp.csv')

# FIlter if birthplace in London
df["is_london"] = df["birthPlace"].str.contains("London", case=False, na=False)

#divided in group
london_counts = df[df["is_london"]].groupby("parliament").size()
outside_london_counts = df[~df["is_london"]].groupby("parliament").size()

parliament_numbers = np.union1d(london_counts.index, outside_london_counts.index)

# Align counts with all parliament numbers, if value is missing then set as 0
london_counts = london_counts.reindex(parliament_numbers, fill_value=0)
outside_london_counts = outside_london_counts.reindex(parliament_numbers, fill_value=0)

# Plot the line graph
plt.figure(figsize=(10, 5))
plt.plot(parliament_numbers[:-1], london_counts[:-1], marker="o", linestyle="-", label="London")
plt.plot(parliament_numbers[:-1], outside_london_counts[:-1], marker="s", linestyle="-", label="Outside London", alpha=0.7)

plt.xlabel("Parliament Number")
plt.ylabel("Number of Members")
plt.title("Number of Members Born in London vs Outside London per Parliament")
plt.legend()
plt.grid(True)

plt.show()

# Count for London MPs 
num_london_mps = df["is_london"].sum()

total_mps = len(df)

print (num_london_mps, total_mps)


