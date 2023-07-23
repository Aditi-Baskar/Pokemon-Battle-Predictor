#Real time predictions

import os
import mysql.connector as database
import pandas as pd
import pickle
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import numpy as np
import warnings

warnings.filterwarnings('ignore') # setting ignore as a parameter

def add_data(pokemon1, pokemon2, winner):
    try:
        statement = "INSERT INTO battles VALUES (%s, %s, %s)"
        data = (pokemon1, pokemon2, winner)
        cursor.execute(statement, data)
        connection.commit()
        print("Successfully added entry to database")
    except database.Error as e:
        print(f"Error adding entry to database: {e}")

def check_data(pokemon1, pokemon2):
    statement1 = "SELECT * FROM battles WHERE Pokemon1 = %s and Pokemon2 = %s"
    data1 = (pokemon1, pokemon2)
    cursor.execute(statement1, data1)
    result1 = cursor.fetchall()

    statement2 = "SELECT * FROM battles WHERE Pokemon1 = %s and Pokemon2 = %s"
    data2 = (pokemon2, pokemon1)
    cursor.execute(statement2, data2)
    result2 = cursor.fetchall()

    if result1 == [] and result2 == []:
        return "None"
    else:
        if result1 != []:
            if result1[0][2] == 0:
                return pokemon1
            else:
                return pokemon2
        else:
            if result2[0][2] == 0:
                return pokemon2
            else:
                return pokemon1

    connection.commit()


connection = database.connect(
    user = "root",
    password = "aditi@3105",
    host = "localhost",
    database = "pokemon")

cursor = connection.cursor()

data = pd.read_csv("C:\\UMass\\Fall 2022\\Systems for DS\\Project\\poke_db_data.csv")
print("-----WHAT WILL ASH DO?-----")
print("Welcome trainer! Congratulations on taking up this challenge. Let us work together to ensure your victory!")
p_1 = input("Enter your first pokemon: ")
p_2 = input("Enter your second pokemon: ")
p_3 = input("Enter your third pokemon: ")
p_4 = input("Enter your fourth pokemon: ")
p_5 = input("Enter your fifth pokemon: ")
p_6 = input("Enter your sixth pokemon: ")
p2 = input("Enter your opponent pokemon: ")

#p1 = "Charmeleon"
#p2 = "Gastrodon"
final_list = []
P = [p_1, p_2, p_3, p_4, p_5, p_6]

for p1 in P:
    ch = check_data(p1, p2)
    print()
    print("-----" + p1 +" VS " + p2+"-----")
    if ch == "None":

        poke1 = data.query('Name == @p1')
        poke2 = data.query('Name == @p2')

        poke1 = poke1.drop(columns = ['Name'])
        poke2 = poke2.drop(columns = ['Name'])

        pokemon1 = poke1.iloc[0]
        pokemon2 = poke2.iloc[0]

        pokemon1_stat = []
        pokemon2_stat = []

        for i in pokemon1:
            pokemon1_stat.append(i)

        for i in pokemon2:
            pokemon2_stat.append(i)

        ip = []

        for i in pokemon1_stat:
            ip.append(i)

        for i in pokemon2_stat:
            ip.append(i)

        loaded_model = pickle.load(open("C:\\UMass\\Fall 2022\\Systems for DS\\Project\\finalized_model.sav", 'rb'))
        ip1 = np.array(ip)
        result = loaded_model.predict(ip1.reshape(1, -1))
        add_data(p1, p2, str(result[0]))
        print("MODEL PREDICTION")
        if result[0] == 1:
            print("Winner = "+p1)
            final_list.append(p1)
        else:
            print("Winner = "+p2)

    else:
        print("QUERYING DATABASE")
        print("Winner = "+ch)
        if ch == p1:
            final_list.append(ch)

print()
print("--------------------")
print("We suggest you play one of the following pokemon:")
for p in final_list:
    print(p)

'''
sql = "select * from battles"
cursor.execute(sql)
r = cursor.fetchall()
loaded_model = pickle.load(open("C:\\UMass\\Fall 2022\\Systems for DS\\Project\\finalized_model.sav", 'rb'))

for a in r:
    x = a[0]
    y = a[1]
    poke1 = data.query('Name == @x')
    poke2 = data.query('Name == @y')
    if not poke1.empty and not poke2.empty:
        poke1 = poke1.drop(columns=['Name'])
        poke2 = poke2.drop(columns=['Name'])

        pokemon1 = poke1.iloc[0]
        pokemon2 = poke2.iloc[0]

        pokemon1_stat = []
        pokemon2_stat = []

        for i in pokemon1:
            pokemon1_stat.append(i)

        for i in pokemon2:
            pokemon2_stat.append(i)

        ip = []

        for i in pokemon1_stat:
            ip.append(i)

        for i in pokemon2_stat:
            ip.append(i)

        res = loaded_model.predict([ip])
        if res == 0:
            print(x, y)
'''
