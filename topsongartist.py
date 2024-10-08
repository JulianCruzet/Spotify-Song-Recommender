import spotipy

# Function to fetch user's top songs
def get_users_top_songs(access_token, limit=10):
    sp = spotipy.Spotify(auth=access_token)
    results = sp.current_user_top_tracks(limit=limit)
    top_songs = []
    for idx, item in enumerate(results['items']):
        track_name = item['name']
        artists = ', '.join([artist['name'] for artist in item['artists']])
        album_name = item['album']['name']
        album_cover_url = item['album']['images'][0]['url']  # Get the URL of the first (largest) album cover image
        spotify_track_id = item['id']  # Spotify track ID
        spotify_embed_url = f"https://open.spotify.com/embed/track/{spotify_track_id}"  # Spotify embed URL
        top_songs.append({
            'name': track_name,
            'artists': artists,
            'album_name': album_name,
            'album_cover_url': album_cover_url,
            'spotify_embed_url': spotify_embed_url  # Add Spotify embed URL to the dictionary
        })
    return top_songs

# Function to fetch user's top 10 artists
def get_users_top_artists(access_token, limit=10):
    sp = spotipy.Spotify(auth=access_token)
    results = sp.current_user_top_artists(limit=limit)
    top_artists = []
    for artist in results['items']:
        artist_name = artist['name']
        artist_image_url = artist.get('images', [{'url': None}])[0]['url']  # Get the URL of the first (largest) artist image if available
        top_artists.append({
            'name': artist_name,
            'image_url': artist_image_url
        })
    return top_artists
