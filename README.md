# Number of disappearances in Mexico from 2008-2018

### Summary

From 2008 to 2018, nearly 40,000 disappearances were recorded in all 32 Mexican states. As a response, the federal government set up the National Registry of Information of Missing and Disappeared Persons. States that have higher presence of organized crime are those that have the most disappearances. Particularly, northern states present the highest numbers of disappearances even when adjusting to a rate per 100,000.

### Input Data 

datosnacionales.py and desaparecidos.csv

### Instructions

datosnacionales.py

1. Import pandas as pd

2. Import numpy as np

3. Set variable var_info to read CSV file: 'desaparecidos.csv'.

4. Set variable by_state  to call 'ENTIDAD' column of var_info. Then add value_counts() and to_frame('count') to arrange total number of disappearances per state. Finally, add sort_index() to order states alphabetically. 

5. Drop by_state['NO ESPECIFICADO'] to eliminate disappearances that were not registered in the 32 states.

6. Add column 'percent' to by_state and set it to get the percentage of disappearances per state by dividing it by the total number of national disappearances.

7. Create a list titled code and set it to the state of code corresponding to each individual state in Mexico.

8. Create column 'state code' in by_state and set it to variable code to include the codes for all 32 states.

9. Create column 'pop' in by_state which sets a list with the population of all 32 Mexican states.

10. Create column 'pop perc' in by_state to calculate the percentage each Mexican state has of the total population.

11. Create column 'des100k' in by_state and set it to calculate the rate of disappearances per state per 100,000.

12. Write out the above in a CSV file titled 'desap_por_estado.csv'

13. Print by_state

mexico.gpkg

1. Add the SHP file with the polygon containing border of Mexico.

2. Import the CSV file desap_por_estado.

3. Join layers from desap_por_estado with join field state code and target field CODE.

4. Create 3 different graduated layers that contain the following.

	a) Population percentages per state.
	
	b) Total disappearances per state.
	
	c) Disappearances per 100,000 per state.

5. Export PNG files of all the above maps.
