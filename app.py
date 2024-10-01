import os
import requests
from flask import Flask, request, redirect, session, render_template, url_for
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from RecSong import get_users_liked_songs, recommend_songs
from topsongartist import get_users_top_artists, get_users_top_songs

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.urandom(24)

# Spotify application credentials
CLIENT_ID = 'f974da21e2444e569517532cc1c99b3e'
CLIENT_SECRET = '71ded5b046e94b0482321c9b6fe4272f'
REDIRECT_URI = 'http://localhost:5000/callback'
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

@app.route('/login/')
def login():
    # Generate a random state token to protect against CSRF
    state = os.urandom(16).hex()
    session['state'] = state

    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': 'user-read-email user-library-read user-read-recently-played user-top-read',
        'state': state
    }

    auth_url = f"{SPOTIFY_AUTH_URL}?client_id={params['client_id']}&response_type={params['response_type']}&redirect_uri={params['redirect_uri']}&scope={params['scope']}&state={params['state']}"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    if request.args.get('state') != session['state']:
        return 'State token mismatch', 401

    code = request.args.get('code')
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(SPOTIFY_TOKEN_URL, data=token_data)
    token_json = response.json()

    access_token = token_json['access_token']
    refresh_token = token_json.get('refresh_token')

    # Store the access token in the session
    session['access_token'] = access_token
    session['refresh_token'] = refresh_token

    return redirect(url_for('home'))

@app.route('/home')
def home():
    if 'access_token' not in session:
        return redirect(url_for('login'))

    sp = spotipy.Spotify(auth=session['access_token'])
    user_data = sp.current_user()
    return render_template('home.html', user_data=user_data)

@app.route('/rec')
def rec():
    if 'access_token' not in session:
        return redirect(url_for('login'))

    liked_songs = get_users_liked_songs(session['access_token'])
    recommended_songs = recommend_songs(session['access_token'], liked_songs)
    return render_template('rec.html', songs=recommended_songs)


@app.route('/top')
def top():
    if 'access_token' not in session:
        return redirect(url_for('login'))

    # Fetch top songs and artists using the access token
    top_songs = get_users_top_songs(session['access_token'])
    top_artists = get_users_top_artists(session['access_token'])
    return render_template('top.html', top_songs=top_songs, top_artists=top_artists)

if __name__ == '__main__':
    app.run(debug=True)
