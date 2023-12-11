import psycopg2

# Database connection
conn = psycopg2.connect(host="localhost", database="MoviesDB", user="postgres", password="postgres")
cur = conn.cursor()