# import the Flask class from the flask library
from flask import Flask, g, render_template, jsonify, request
import sqlite3
# import chatbot here and do not import app.py into chatbot or circular import error
from chatbot import get_synonyms
import nltk
nltk.download('wordnet')


# object inheriting from Flask
app = Flask(__name__)

# this function gets a random word, the correct definiton of it, and the incorrect defintion
def get_word():
    # connecting to SQlite database
    conn = sqlite3.connect('word_definition.db')
    c = conn.cursor()
    # selecting a random word with definition 
    c.execute('SELECT word, definition FROM words ORDER BY RANDOM() LIMIT 1')
    # gets one as opposed to fetchmany
    word = c.fetchone()
    # gets a random incorrect definition
    c.execute('SELECT definition FROM words WHERE definition != ? ORDER BY RANDOM() LIMIT 1', (word[1],))
    incorrect_definition = c.fetchone()
    # closes database connection
    conn.close()
    # word 0 is the correct word to be asked
    # word 1 is the correct definition
    # incorrect_definition[0] is 0 as it is the only element we got, no word selected here
    return word[0], word[1], incorrect_definition[0]

# gets to home page
@app.route('/')
def index():
    # finds .html file in templates and sends rendered html to be opened on browser
    return render_template('web-front.html')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('word_definition.db')
        g.db.row_factory = sqlite3.Row
    return g.db

# gets random word and its defintion
# only handles GET requests
@app.route('/get_word', methods=['GET'])
def get_word_route():
    difficulty = request.args.get('difficulty', 'easy')
    c = get_db().cursor()
    c.execute('SELECT word, definition FROM words WHERE difficulty = ? ORDER BY RANDOM() LIMIT 1', (difficulty,))
    word = c.fetchone()
    c.execute('SELECT definition FROM words WHERE definition != ? AND difficulty = ? ORDER BY RANDOM() LIMIT 1', (word[1], difficulty))
    incorrect_definition = c.fetchone()
    # returning as json response
    return jsonify({'word': word[0], 'definition': word[1], 'incorrect_definition': incorrect_definition[0]})

# using flask to define a route for the synonyms
# only handles GET requests
@app.route('/get_synonyms', methods=['GET'])
def get_synonyms_route():
    # accesses word 
    word = request.args.get('word')
    # initalise a set as set ensures all values are unique
    synonyms = set()
    # if we got a word
    if word:
        # call synonyms function which returns a set of synonyms
        synonyms = get_synonyms(word)
        # convert set to a list then use json
    return jsonify({'word': word, 'synonyms': list(synonyms)})

# runs script in debug mode
if __name__ == '__main__':
    app.run(debug=True)
