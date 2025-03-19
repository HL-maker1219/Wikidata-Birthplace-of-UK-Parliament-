import pandas as pd

df = pd.read_csv('parliament_list.csv')

#Remove wikidata links
df.drop(columns=['member'], inplace=True)
df.drop(columns=['parliament'], inplace=True)
df.drop(columns=['birthPlace'], inplace=True)
df.drop(columns=['party'], inplace= True)

#remove unnecessary text
df['parliamentLabel'] = df['parliamentLabel'].str.replace('member of the ', '', regex=True)
df['parliamentLabel'] = df['parliamentLabel'].str.replace(' Parliament of the United Kingdom', '', regex=True)
df['parliamentLabel'] = df['parliamentLabel'].str.replace('st', '', regex=True)
df['parliamentLabel'] = df['parliamentLabel'].str.replace('nd', '', regex=True)
df['parliamentLabel'] = df['parliamentLabel'].str.replace('rd', '', regex=True)
df['parliamentLabel'] = df['parliamentLabel'].str.replace('th', '', regex=True)
df['coordinates'] = df['coordinates'].str.replace('Point', '', regex=True)

#rename Column name
df.rename(columns={'memberLabel':'member'}, inplace=True)
df.rename(columns={'parliamentLabel':'parliament'}, inplace=True)
df.rename(columns={'birthPlaceLabel':'birthPlace'}, inplace=True)
df.rename(columns={'partyLabel':'party'}, inplace=True)

#remove start and end dates
df['start'] = pd.to_datetime(df['start']).dt.year
df['end'] = pd.to_datetime(df['end']).dt.year

#rearrange the order of the columns
columns = ['parliament','member','birthPlace','coordinates','start','end','party']
df = df[columns]

df.to_csv('parliament_simp.csv', index= False )

