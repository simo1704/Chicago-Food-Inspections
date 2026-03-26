import pandas as pd
import numpy as np

df = pd.read_csv('food-inspections.csv', sep=',')
print(df.head())

# 1. Quali tipi di esercizi alimentari vengono ispezionati più spesso?
inspection_count = df['Facility Type'].value_counts()
print("Numero di ispezioni per tipo di esercizio alimentare:")
print(inspection_count)

# 2. Le attività ad alto rischio falliscono più spesso rispetto a quelle a basso rischio?
print("Distribuzione dei fallimenti per livello di rischio:")
print(df[df['Results'] == 'Fail'].groupby('Risk').size())

# 3. Come sono distribuiti gli esiti delle ispezioni tra le diverse categorie di rischio?
print(df.groupby(['Risk','Results'])['Inspection ID'].sum())

# 4. Il tasso di fallimento è cambiato nel tempo?
print(df[df['Results'] == 'Fail'].groupby('Inspection Date').size() / df.groupby('Inspection Date').size())