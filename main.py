from spotify import Spotify
from youtube import Youtube

def main():
    sp = Spotify()
    yt = Youtube()
    
    yt_playlist_id = input("Your Youtube Playlist ID :: ")
    spotify_playlist_name = input("Suggest a name for your Spotify Playlist :: ")
    spotify_playlist_id = sp.create_playlist(spotify_playlist_name)
    songs = yt.get_songs_from_playlist(yt_playlist_id)

    for song in songs:
        song_uri = sp.get_song_uri(song.artist, song.title)

        if not song_uri:
            print(f"{song.artist} - {song.title} was not found!")
            continue
        
        was_added = sp.add_song_to_playlist(song_uri, spotify_playlist_id)

        if was_added:
            print(f'{song.artist} - {song.title} was added to playlist.')

    total_songs_added = sp._num_playlist_songs(spotify_playlist_id)
    print(f'Added {total_songs_added} songs out of {len(songs)}')

if __name__ == "__main__":
    main()
