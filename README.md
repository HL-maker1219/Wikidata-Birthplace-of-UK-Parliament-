
# COMP3517 Coursework
Title:
The Birthplaces Distributions of Members in British Parliament From 1801 to 2024 Based on Wikidata  
Name: Keyin Lin





## Operate Enviroment

#### Operate Enviroment: Python 3.9
#### Required Libaries: Pandas, Mataplotlib, Numpy, Folium 

| Libary Name | Fuction   |
| :-------- | :------- | 
| `Pandas` | `Process data` |
| `Numpy` | `Plot graph` |
| `Mataplotlib` | `Produced line graph` |
| `Folium` | `Produced heat map` |

## Process Detail
All data that are being used in this assignment are the dataset tretrive from Wikidata Query Service with SPARQL:

```http
SELECT ?member ?memberLabel ?parliament ?parliamentLabel ?birthPlace ?birthPlaceLabel ?coordinates ?start ?end ?party ?partyLabel  
	WHERE {  
	  ?member p:P39 ?statement.                   
	  ?statement ps:P39 ?parliament;           # which parliament MP belongs   
	             pq:P580 ?start;               # Parliament memnerships starts  
	             pq:P582 ?end.                 # Parliament memberships ends  
	  ?parliament wdt:P279 wd:Q16707842.       # MP Subcalss  
	  ?member wdt:P19 ?birthPlace.             # MP Birthplace  
	  
	  OPTIONAL {  
	    ?birthPlace wdt:P625 ?coordinates.     #  Birthplace geographical coordinates  
	  }  
	  
	  OPTIONAL {  
	    ?member wdt:P102 ?party.               # Political party  
	    ?party rdfs:label ?partyLabel.           
	    FILTER(LANG(?partyLabel) = "en").        
	  }  
	  
	  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }  

```
The retrieved dataset named **parliament_list.csv**
#### Python Program
| Name |Function      | Produced |
| :-------- | :------- | :------- | 
| `clearData.py`      | Clearing the data retrieved from wikidata Query Service| `parliament_simp.csv`|
| `parliamentExtract.py`      | Extract MPs list in certain parliaments(stored in *parliament_ranges* folder)| `parliament_(start parliament)-(end parliament).csv`|
| `yearExtract.py`      | Extract MPs list in certain years(stored in *parliament_ranges* folder)| `parliament_(start year)-(end year).csv`|
| `londonBorn.py`      | Produced MPs who born in Lodon line graph| `Figure_2.jpg`|
| `nobleTitles.py`      | Produced MPs who owns noble titles line graph| `Figure_1.jpg`|
| `parliamentGrowth.py`      | Produced graph to show MPs number growth line graph| `Figure_3.jpg`|
| `plotMap.py`      | Produced plot map| `map.html`|
| `heatMap.py`      | Produced heatMap map| `heatmap(start period)-(end period).html`|

All the data (apart from `parliament_list` and `parliament_simp`) are stored in **parliament_ranges** folder

All the images  are stored in **images** folder

