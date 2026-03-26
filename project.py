import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    'C:\\Users\\simom\\OneDrive - Università degli Studi di Milano-Bicocca\\3° anno\\Data Processing\\Chicago Food Inspections\\dataset\\food-inspections.csv', sep=',')
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

# 15. Alcune violazioni sono fortemente associate a specifici tipi di struttura?
data = df.select_dtypes(include='number').dropna(axis=1, how='all') # Seleziona solo le colonne numeriche e rimuove quelle con tutti i valori NaN

f, ax = plt.subplots(figsize=(9, 6)) # Crea una figura e un asse per il grafico
# Crea una heatmap della matrice di correlazione dei dati numerici, con annotazioni e formattazione dei numeri
sns.heatmap(data.corr() , annot=True, fmt=".2f", linewidths=.5, ax=ax) 
plt.tight_layout() # Regola automaticamente i parametri del layout per evitare sovrapposizioni
plt.show() # Mostra il grafico
# Salva il grafico come file PNG in una posizione specifica
f.savefig('C:\\Users\\simom\\OneDrive - Università degli Studi di Milano-Bicocca\\3° anno\\Data Processing\\Chicago Food Inspections\\correlation_heatmap.png') 