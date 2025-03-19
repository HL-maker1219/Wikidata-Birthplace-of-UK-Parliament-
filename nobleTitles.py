import pandas as pd
import matplotlib.pyplot as plt

file_path = "parliament_simp.csv"  
df = pd.read_csv(file_path)

noble_titles = ['Viscount', 'Duke', 'Baron', 'Earl', 'Marquess', 'Lord', 'Sir',
                'Knight', 'Duchess', 'Marchioness', 'Countess', 'Viscountess', 
                'Baroness', 'Lady']

df['IsNoble'] = df['member'].astype(str).str.contains('|'.join(noble_titles), case=False, na=False)

# Count 
counts = df.groupby(['parliament', 'IsNoble']).size().unstack(fill_value=0)
counts.columns = ['Not Noble', 'Noble']

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(counts.index[:-1], counts['Noble'][:-1], marker='o', label='Noble')
plt.plot(counts.index[:-1], counts['Not Noble'][:-1], marker='s', label='Not Noble')

plt.xlabel('Number of Parliament')
plt.ylabel('Number of Member in Parliament')
plt.title('Number of Noble vs. Not Noble Member in Each Parliament')
plt.legend()
plt.grid(True)

plt.show()
