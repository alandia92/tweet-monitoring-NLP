from flask import Flask, request, jsonify
import os
import pickle
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import pandas as pd
import sqlite3


os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return "Bienvenido twitter sentimental analysis"

#1

@app.route('/v2/predict', methods=['GET'])
def predict():
    model = pickle.load(open('./Entregas/model/sentiment_model', 'rb'))

    tweet = request.args.get('tweet', None)

    if tweet is None:
        return "Missing args, the tweet text is needed to predict"
    else:
        prediction = model.predict([tweet])
        return "The sentiment prediction for the tweet is: " + str(prediction[0])

    
#2


@app.route('/v2/ingest_data', methods=['POST'])
def ingest_data():
    connection = sqlite3.connect('tweets.db')
    cursor = connection.cursor()
    query = '''INSERT INTO tweets (tweet_text) VALUES (?)'''
    query_2 = '''SELECT * FROM tweets'''

    tweet_text = request.form.get('tweet_text', None)

    if tweet_text is None:
        return "Missing args, the tweet text is needed to ingest"

    cursor.execute(query, (tweet_text,))
    connection.commit()

    result = cursor.execute(query_2).fetchall()

    connection.close()
    return jsonify(result)

#3

@app.route('/v2/retrain', methods=['PUT'])
def retrain():
    connection = sqlite3.connect('tweets.db')
    cursor = connection.cursor()
    query = '''SELECT * FROM tweets'''
    result = cursor.execute(query).fetchall()

    columns = []
    for i in cursor.description:
        columns.append(i[0])

    df = pd.DataFrame(data=result, columns=columns)
    X = df.drop(columns='tweet_text')
    Y = df['tweet_text']

    model = pickle.load(open('./entregas/model/sentiment_model', 'rb'))
    model.fit(X, Y)
    pickle.dump(model, open('./entregas/model/sentiment_model', 'wb'))

    new_score = cross_val_score(model, X, Y, cv=10, scoring='accuracy').mean()

    
    return f'The score of your retrained model is: {new_score}'


    return result

    


app.run()