import pandas as pd
import os
import openpyxl
path = os.getcwd()
contents = os.listdir(path)
files2 = [f for f in contents if f[-3:] == 'csv' and f[0] == 'C']
combine_path=files2[0]
print(combine_path)
with open(combine_path, 'r') as file:
    combine_data=pd.read_csv(file)
players=[]
for index, row in combine_data.iterrows():
    players.append(row["Player"])
with open("Madden_ratings.csv", 'r') as file:
    data = pd.read_csv(file)
ratings = []
speed=[]
acceleration=[]
agility=[]
strength=[]
df=data.groupby(['Full Name'], as_index=False).mean()
for i, player in enumerate(players):
    r=None
    spd=None
    acc=None
    agl=None
    str=None
    try: r=df.loc[df["Full Name"]==player, 'Overall Rating'].iloc[0]
    except: pass
    try: spd=df.loc[df["Full Name"]==player, 'Speed'].iloc[0]
    except: pass
    try: acc=df.loc[df["Full Name"]==player, 'Acceleration'].iloc[0]
    except: pass
    try: agl=df.loc[df["Full Name"]==player, 'Agility'].iloc[0]
    except: pass
    try: str=df.loc[df["Full Name"]==player, 'Strength'].iloc[0]
    except: pass

    ratings.append(r)
    speed.append(spd)
    acceleration.append(acc)
    agility.append(agl)
    strength.append(str)
combine_data["Ratings"]=ratings
combine_data["Speed"]=speed
combine_data["Acceleration"]=acceleration
combine_data["Agility"]=agility
combine_data["Strength"]=strength
with open("data.csv", 'w') as file:
    combine_data.to_csv(file, index=False)




