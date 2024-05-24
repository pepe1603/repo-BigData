import pandas as pd

##carga de edatos
def load_data(filepath):
    return pd.read_csv(filepath)

##Limpieza de datos
def clean_data(df):
    for column in df.columns:
        if df[column].isnull().sum() > 0:
            df[column].fillna(df[column].mode()[0], inplace=True)
    return df

##guardar el datos limpios en un nuevo csv
def save_cleaned_data(df, filepath):
    df.to_csv(filepath, index=False)

if __name__ == "__main__":
    df = load_data('data/WallCityTap_Consumer.csv')
    df_clean = clean_data(df)
    save_cleaned_data(df_clean, 'data/cleaned_WallCityTap_Consumer.csv')
