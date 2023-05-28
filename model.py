from cProfile import label
import sqlite3
from flask import Flask, request, jsonify
import pickle
import os
from flask import render_template
from sklearn.model_selection import cross_val_score
import pandas as pd

os.chdir(os.path.dirname(__file__))
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return "Bienvenido a Twitter Sentiment Analysis"

# Cargar el modelo pre-entrenado al iniciar la aplicación
model_path = './model/sentiment_model'
model = pickle.load(open(model_path, 'rb'))

# funcion que predice un nuevo texto y lo guarda en la base de datos
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        tweet_text = request.form['tweet']
        
        # Cargar el modelo pre-entrenado
        model = pickle.load(open('.model/sentiment_model', 'rb'))
        
        # Realizar la predicción
        prediction = model.predict([tweet_text])
        
        sentiment = "Sentimiento positivo" if prediction[0] == 1 else "Sentimiento negativo o nulo"
        
        # Insertar el texto del tweet en la base de datos
        connection = sqlite3.connect('tweets.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tweets (text) VALUES (?)", (tweet_text,))
        connection.commit()
        connection.close()
        
        return f'''
            <p>La predicción de sentimiento para el tweet '{tweet_text}' es: {sentiment}</p>
            <p>El texto del tweet se ha ingresado en la base de datos.</p>
            <p><a href="/predict">Ingresar otro texto</a></p>
        '''
    
    return '''
        <form method="post" action="/predict">
            <label for="tweet">Ingrese el texto del tweet:</label><br>
            <input type="text" id="tweet" name="tweet"><br><br>
            <input type="submit" value="Predecir">
        </form>
    '''
# seria interesante volver a entrenar el modelo con los neuvos datos, pero no hay información sobre el tratamiento de los datos par el modelo dado
if __name__ == '__main__':
    app.run()