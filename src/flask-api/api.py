# save this  as API.py 

from flask import Flask, jsonify
import mysql.connector
import json

app = Flask(__name__)

@app.route('/data')
def get_data():
    try:
        conn = mysql.connector.connect(
            user="root",
            password="dahmanim",
            host="localhost",
            port=3306,
            database="identity"
        )
        conn2 = mysql.connector.connect(
            user="root",
            password="dahmanim",
            host="localhost",
            port=3306,
            database="config_generator"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM utilisateur")
        rows = cursor.fetchall()

        cursor1 = conn2.cursor()
        cursor1.execute("SELECT * FROM load_balancer")
        rows1 = cursor1.fetchall()

        cursor2 = conn2.cursor()
        cursor2.execute("SELECT * FROM proxy")
        rows2 = cursor2.fetchall()

        cursor3 = conn2.cursor()
        cursor3.execute("SELECT * FROM webserver")
        rows3 = cursor3.fetchall()

        # Convertir les données en JSON
        data = []
        for row in rows:
            d = {
                "id": row[0],
                "name": row[1],
                "prenom": row[2],
                "date" : row[3]
            }
            data.append(d)

        for row in rows1:
            d1 = {
                "id": row[0],
                "serveur1": row[1],
                "location": row[2],
                #"serv": row[3],
            }
            data.append(d1)

        for row in rows2:
            d2 = {
                "id": row[0],
                "serv1": row[1],
                "serv2": row[2],
                "proxy_pass": row[3],
            }
            data.append(d2)
        
        for row in rows3:
            d3 = {
                "id": row[0],
                "root": row[1],
                "location": row[2],
                "error_page": row[3],
                "location_error": row[4],
                "root_error": row[5]
            }
            data.append(d3)

        # Fermer la connexion à la base de données
        cursor.close()
        conn.close()

        cursor1.close()
        conn2.close()

        cursor2.close()
        conn2.close()

        cursor3.close()
        conn2.close()
        # Renvoyer les données sous forme de JSON
        return jsonify(data)

    except mysql.connector.Error as error:
        print(error)
        return "Error connecting to databasealex"

if __name__ == '__main__':
    app.run(debug=True)