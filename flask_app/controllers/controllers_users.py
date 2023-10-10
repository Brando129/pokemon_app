# Imports
from flask_app import app
from flask import render_template, redirect, request, session
import requests
from pprint import pprint


# Get routes
# Render index page
@app.get('/')
def index():
    return render_template('index.html')

# Render show pokemon page
@app.get('/display/pokemon/info')
def display_pokemon():
    return render_template('display_pokemon.html')


# Post routes
# Search pokemon
@app.post('/search/pokemon')
def search_pokemon():

    name = request.form['name']
    url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
    response = requests.get(url)

    session['id'] = response.json()['id']
    session['name'] = response.json()['name']
    session['image'] = response.json()['sprites']['other']['official-artwork']['front_default']
    session['height'] = response.json()['height']
    session['weight'] = response.json()['weight']
    session['ability'] = response.json()['abilities'][0]['ability']['name']

    return redirect('/display/pokemon/info')