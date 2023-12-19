from bs4 import BeautifulSoup
import psycopg2
import pandas as pd
import requests
from sqlalchemy import create_engine,text

class MovieDb:
    def __init__(self):
        self.conn = psycopg2.connect(database="MoviesDB", user="postgres", password="postgres", host="localhost", port="5432")
        self.cur = self.conn.cursor()
        self.conn.set_session(autocommit=True)

    def CreateDB(self):
        engine = create_engine('postgresql://postgres:postgres@localhost/MoviesDB')
        df=pd.read_csv('csv_movies.csv')
        df.to_sql('Movies',engine,if_exists='replace',index=False)
        self.conn.commit()

    def find_rating_by_title(self, title):
        self.cur.execute('SELECT "Rating" FROM "Movies" WHERE "Title" = %s', (title,))
        result = self.cur.fetchone()
        if result:
            return result[0]
        else:
            return None
        
    def find_title_by_actor(self, actor):
        self.cur.execute('SELECT "Title" FROM "Movies" WHERE "Cast" LIKE %s', ('%' + actor + '%',))
        result = self.cur.fetchall()
        if result:
            tmp = '\n'.join([row[0] for row in result[:5]])
            return tmp
        else:
            return "Actor not found"
    

# Database connection


