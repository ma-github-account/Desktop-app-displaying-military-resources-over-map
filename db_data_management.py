
import pyodbc

server = "server"
database = "database"
username = "username"
password = "password"

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

def select_all_coordinates_list_from_db():

    cursor.execute("SELECT * FROM [Test1].[dbo].[Strategic_resources]")
    
    list_of_results = []

    for row in cursor:
        list_of_results.append([row[1],row[2]])

    return list_of_results
