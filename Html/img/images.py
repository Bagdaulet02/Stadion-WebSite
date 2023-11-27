import glob
import os
import mysql.connector

db = mysql.connector.connect( 
        host="localhost",
        user="stadioner",
        password="stadionpass",
        database="Stadion"
)

db_cursor = db.cursor()

folder = ""

