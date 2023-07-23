#Write the battles results into the DB

import os
import mysql.connector as database
import pandas as pd

def add_data(pokemon1, pokemon2, winner):
    try:
        statement = "INSERT INTO battles VALUES (%s, %s, %s)"
        data = (pokemon1, pokemon2, winner)
        cursor.execute(statement, data)
        connection.commit()
        print("Successfully added entry to database")
    except database.Error as e:
        print(f"Error adding entry to database: {e}")

connection = database.connect(
    user = "root",
    password = "aditi@3105",
    host = "localhost",
    database = "pokemon")

cursor = connection.cursor()

data = pd.read_csv("C:\\UMass\\Fall 2022\\Systems for DS\\Project\\final_data.csv")
battle_data = d = data.loc[:,["name", "name_2", "Winner"]]

for i in battle_data.index:
    print(i)
    n1 = battle_data['name'][i]
    n2 = battle_data['name_2'][i]
    poke1 = ""
    poke2 = ""
    for k in n1:
        if (k >= 'a' and k <= 'z') or (k >= 'A' and k <= 'Z'):
            poke1 += k
    for k in n2:
        if (k >= 'a' and k <= 'z') or (k >= 'A' and k <= 'Z'):
            poke2 += k
    add_data(poke1, poke2, str(battle_data['Winner'][i]))
