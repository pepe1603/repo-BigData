import psycopg2
import pandas as pd
import os

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    dbname="movies_database",
    user="postgres",
    password="unach2024",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Crear tabla en PostgreSQL
create_table_query = '''
CREATE TABLE IF NOT EXISTS FilmTv_USAMovies (
    color VARCHAR(50),
    director_name VARCHAR(50),
    num_critic_for_reviews FLOAT,
    duration FLOAT,
    director_facebook_likes FLOAT,
    actor_3_facebook_likes FLOAT,
    actor_2_name VARCHAR(50),
    actor_1_facebook_likes FLOAT,
    gross FLOAT,
    genres VARCHAR(255),
    actor_1_name VARCHAR(50),
    movie_title VARCHAR(255),
    num_voted_users FLOAT,
    cast_total_facebook_likes FLOAT,
    actor_3_name VARCHAR(50),
    facenumber_in_poster FLOAT,
    plot_keywords VARCHAR(255),
    movie_imdb_link VARCHAR(255),
    num_user_for_reviews FLOAT,
    language VARCHAR(50),
    country VARCHAR(50),
    content_rating VARCHAR(50),
    budget FLOAT,
    title_year FLOAT,
    actor_2_facebook_likes FLOAT,
    imdb_score FLOAT,
    aspect_ratio FLOAT,
    movie_facebook_likes FLOAT,
    TitleCode VARCHAR(50)
);
'''
cur.execute(create_table_query)
conn.commit()

# Cargar datos desde el CSV limpio
csv_file = 'data/FilmTV_USAMoviesClean.csv'

#imprimimos la ruta del archivo csv antes de la carga 
print("Ruta completa del archivo CSV:", os.path.abspath(csv_file))

movies_df = pd.read_csv(csv_file)

# Insertar datos en la tabla de PostgreSQL
for index, row in movies_df.iterrows():
    insert_query = """
    INSERT INTO FilmTv_USAMovies (color, director_name, num_critic_for_reviews, duration, director_facebook_likes,
                                   actor_3_facebook_likes, actor_2_name, actor_1_facebook_likes, gross, genres,
                                   actor_1_name, movie_title, num_voted_users, cast_total_facebook_likes,
                                   actor_3_name, facenumber_in_poster, plot_keywords, movie_imdb_link,
                                   num_user_for_reviews, language, country, content_rating, budget, title_year,
                                   actor_2_facebook_likes, imdb_score, aspect_ratio, movie_facebook_likes,
                                   TitleCode)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s)
    """
    cur.execute(insert_query, tuple(row))
    conn.commit()

# Imprimir las primeras 5 filas del DataFrame
print("Primeras 5 filas del DataFrame:")
print(movies_df.head())

# Cerrar conexión
cur.close()
conn.close()

