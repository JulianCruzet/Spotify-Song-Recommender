import spotipy
from spotipy.exceptions import SpotifyException

# Fetch user's liked songs
def get_users_liked_songs(access_token):
    sp = spotipy.Spotify(auth=access_token)
    results = sp.current_user_saved_tracks(limit=50)
    liked_songs_ids = [
        item['track']['id']
        for item in results['items']
        if item['track']['type'] == 'track'
    ]
    return liked_songs_ids


# Debug helper to check each track ID
def debug_track_ids(sp, track_ids):
    print("🎧 Checking individual seed tracks:")
    for tid in track_ids:
        try:
            track = sp.track(tid)
            print(f"✅ {tid}: {track['name']} by {track['artists'][0]['name']}")
        except SpotifyException as e:
            print(f"❌ {tid} is invalid or unavailable - {e}")


# Validate track IDs
def validate_tracks(sp, track_ids):
    valid_ids = []
    for tid in track_ids:
        try:
            sp.track(tid)
            valid_ids.append(tid)
        except SpotifyException:
            print(f"⚠️ Skipping invalid track ID: {tid}")
    return valid_ids


# Fallback search-based "recommendations"
def fallback_search_recommendations(sp, artist_name, track_name):
    query = f"{artist_name} {track_name}"
    print(f"🌀 Fallback search for: {query}")
    results = sp.search(q=query, type='track', limit=10)

    recommended_songs = []
    for track in results['tracks']['items'][1:]:  # Skip first match
        song_info = {
            "name": track['name'],
            "artist": track['artists'][0]['name'],
            "album_cover_url": track['album']['images'][0]['url'],
            "spotify_track_id": track['id'],
            "spotify_embed_url": f"https://open.spotify.com/embed/track/{track['id']}"
        }
        recommended_songs.append(song_info)
    return recommended_songs


# Main recommendation function
def recommend_songs(access_token, based_on_songs_ids):
    sp = spotipy.Spotify(auth=access_token)

    seed_tracks_raw = based_on_songs_ids[:5]
    debug_track_ids(sp, seed_tracks_raw)
    seed_tracks_valid = validate_tracks(sp, seed_tracks_raw)

    if not seed_tracks_valid:
        print("⚠️ No valid seed tracks available.")
        return []

    try:
        recommendations = sp.recommendations(seed_tracks=seed_tracks_valid[:3], limit=12)
        if not recommendations['tracks']:
            raise SpotifyException(404, -1, "No recommendations returned")
    except SpotifyException as e:
        print("❌ Spotify API Error:", e)

        # Use fallback search
        try:
            original_track = sp.track(seed_tracks_valid[0])
            artist = original_track['artists'][0]['name']
            title = original_track['name']
            return fallback_search_recommendations(sp, artist, title)
        except Exception as fallback_error:
            print("❌ Fallback search also failed:", fallback_error)
            return []

    recommended_songs = []
    for track in recommendations['tracks']:
        song_info = {
            "name": track['name'],
            "artist": track['artists'][0]['name'],
            "album_cover_url": track['album']['images'][0]['url'],
            "spotify_track_id": track['id'],
            "spotify_embed_url": f"https://open.spotify.com/embed/track/{track['id']}"
        }
        recommended_songs.append(song_info)

    return recommended_songs
