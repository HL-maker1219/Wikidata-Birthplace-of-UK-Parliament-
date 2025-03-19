import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('parliament_simp.csv')

# Count the number of MPs per parliament
mp_growth = df.groupby("parliament").size()

# Plot the line graph
plt.figure(figsize=(10, 5))
plt.plot(mp_growth.index[:-1], mp_growth.values[:-1], marker="o", linestyle="-", label="Number of MPs")

plt.xlabel("Parliament Number")
plt.ylabel("Number of Members of Parliament")
plt.title("Growth of Members of Parliament Over Time")
plt.legend()
plt.grid(True)

plt.show()