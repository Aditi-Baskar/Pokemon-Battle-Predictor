# project-team_15
# What Will Ash Do?: Pokemon Battle Predictor


## Team Members:
1. Aditi Baskar: <abaskar@umass.edu>
2. Akshaya Mohan <akshayamohan@umass.edu>
3. Jaswanth Reddy Kommuru <jkommuru@umass.edu>

## Video
[Project Overview](https://youtu.be/eJlDpRutGw8)

## Datasets
Download the csv files [here](https://drive.google.com/drive/folders/1vFzug9NnXkSX_HPGmiL2BtcK3bLAWHMj?usp=share_link) and store in `data/`

### Original datasets
1. `pokedex.csv`
2. `pokemon.csv`
3. `combats.csv`
4. `tests.csv`

### Processed data
1. `final_data.csv`
2. `training_data.csv`
2. `encoded_data.csv`


## File Map
1. `dataproc.ipynb`: Joining the datasets to obtain a dataset with the statistics of each Pokemon in the battle and the winner of the battle. This is stored in `final_data.csv`. `training_data.csv` is generated for training classification models
2. `Pokemon_Stats_EDA.ipynb`: Exploratory data analysis of the Pokemon statistics dataset, including type, attack stats, defense stats, etc.
3. `Pokemon_Battle_EDA.ipynb`: Exploratory data analysis of the battles dataset, including win percentage, type performance, etc.
4. `train_pred.ipynb`: Encoding and preparing data for model training. Comparison of performance of feature selection techniques and classification models. 
5. `Pokemon_Data_Prep.ipynb`: Pre-processing the data for in-battle scenario predictions. The csv file `poke_db_data.csv` generated is used for this purpose.
6. `pokemon_db.py`: Read and load the battle matchup information into the MySQL database.
7. `inference.py`: Interactive interface for in-battle scenario predictions- The user inputs their 6 Pokémon and the opponent Pokémon. The best Pokémon for the user to play is given as the output.

