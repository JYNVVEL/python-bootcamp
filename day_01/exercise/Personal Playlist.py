import json

def add(song, playlist):
    """Add song to playlist"""
    song.append(playlist)


def remove(song, playlist):
    """Remove song from playlist (if there)"""
    song.remove(playlist)


def play(playlist):
    """Print the first song in the playlist (if any) and remove"""
    print(playlist[0])


def show_all(playlist):
    """Print all contents in the playlist"""
    print(playlist)


def save(playlist, filepath):
    """Save current playlist to filepath"""
    with open(filepath, "w") as file:
        json.dump(playlist, file, indent=4)

def load(filepath):
    """Load a new playlist from filepath and return it"""


def playlist_app():
    """
    While user doesn’t want to stop, keep asking for command
        then do the task requested
    """

    playlist = []
    end = False

    while not end:
        user_choice = input("Select command: ")

        # Ask all inputs in the playlist_app() function to make functions simple
        if user_choice == "add":
            new_song = input("Enter song name: ")
            add(new_song, playlist)

        elif user_choice == "remove":
            remove_song = input("Enter a song to remove: ")
            remove(remove_song, playlist)

        elif user_choice == "show":
            show_all(playlist)



        elif user_choice == "play":
            play_song = input("Enter a song to play: ")
            play(play_song)

        if user_choice == "exit":
            end = True


playlist_app()