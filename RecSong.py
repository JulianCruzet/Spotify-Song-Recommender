import spotipy

# Function to fetch user's liked songs
def get_users_liked_songs(access_token):
    sp = spotipy.Spotify(auth=access_token)
    results = sp.current_user_saved_tracks()
    liked_songs_ids = []
    for idx, item in enumerate(results['items']):
        track = item['track']
        liked_songs_ids.append(track['id'])  # Append only the track ID
    return liked_songs_ids

# Function to recommend songs based on user's liked songs
def recommend_songs(access_token, based_on_songs_ids):
    sp = spotipy.Spotify(auth=access_token)
    seed_tracks_limited = based_on_songs_ids[:5]  # Limit the number of seed tracks
    recommendations = sp.recommendations(seed_tracks=seed_tracks_limited, limit=12)
    recommended_songs = []
    for track in recommendations['tracks']:
        # Include the album cover URL in the output
        song_info = {
            "name": track['name'],
            "artist": track['artists'][0]['name'],
            "album_cover_url": track['album']['images'][0]['url']  # The URL of the album cover
        }
        song_info['spotify_track_id'] = track['id']
        song_info['spotify_embed_url'] = f"https://open.spotify.com/embed/track/{track['id']}"
        recommended_songs.append(song_info)
    return recommended_songs
