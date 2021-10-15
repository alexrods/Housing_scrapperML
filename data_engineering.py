"""
This scrip is responsible for clean data collected
returns the house list as vectors
"""

import pandas as pd


def clean_data():
    try:
        df = pd.read_csv('data_houses.csv')
        df = df.reset_index()
        df.drop(['Superficie construida', 'Antigüedad', 'Orientación', 'Ambientes', 'Cuota mensual de mantenimiento',
                 'Cantidad de pisos', 'index'], axis=1, inplace=True)

        df['Superficie total'] = df['Superficie total'].str.replace('m²', '')
        df['Precio'] = df['Precio'].str.replace(',', '')

        df = df.fillna(0)

        df[['Baños', 'Estacionamientos', 'Precio', 'Recámaras', 'Superficie total']] = df[['Baños', 'Estacionamientos', 'Precio', 'Recámaras', 'Superficie total']].astype(float)

        houses_vector = []
        for i in df.index:
            if df.loc[i, 'Superficie total'] <= 75:
                df.loc[i, 'Superficie total'] = 1
            elif df.loc[i, 'Superficie total'] > 75 and df.loc[i, 'Superficie total'] <= 105:
                df.loc[i, 'Superficie total'] = 2
            elif df.loc[i, 'Superficie total'] > 105 and df.loc[i, 'Superficie total'] <= 135:
                df.loc[i, 'Superficie total'] = 3
            elif df.loc[i, 'Superficie total'] > 135 and df.loc[i, 'Superficie total'] <= 200:
                df.loc[i, 'Superficie total'] = 4
            elif df.loc[i, 'Superficie total'] > 200:
                df.loc[i, 'Superficie total'] = 5

            if df.loc[i, 'Precio'] <= 5000:
                df.loc[i, 'Precio'] = 1
            if df.loc[i, 'Precio'] > 5000 and df.loc[i, 'Precio'] <= 7000:
                df.loc[i, 'Precio'] = 2
            if df.loc[i, 'Precio'] > 7000 and df.loc[i, 'Precio'] <= 10000:
                df.loc[i, 'Precio'] = 3
            if df.loc[i, 'Precio'] > 10000 and df.loc[i, 'Precio'] <= 15000:
                df.loc[i, 'Precio'] = 4
            if df.loc[i, 'Precio'] > 15000:
                df.loc[i, 'Precio'] = 5

            x = [df.loc[i, 'Superficie total'], df.loc[i, 'Baños'], df.loc[i, 'Recámaras'],
                 df.loc[i, 'Estacionamientos'], df.loc[i, 'Precio']]
            houses_vector.append(x)

        return houses_vector

    except Exception as e:
        prin(e)
