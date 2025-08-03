import json

def add(song, playlist):
    """Add song to playlist"""
    playlist.append(song)


def remove(song, playlist):
    """Remove song from playlist (if there)"""
    playlist.remove(song)


def play(playlist):
    """Print the first song in the playlist (if any) and remove"""
    print(playlist)


def show_all(playlist):
    """Print all contents in the playlist"""
    print(playlist)


def save(playlist, filepath):
    """Save current playlist to filepath"""
    with open(filepath, "w") as file:
        json.dump(playlist, file, indent=4)

def load(filepath):
    """Load a new playlist from filepath and return it"""
    with open(filepath, "r") as file:
        data = json.load(file)
        return data

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

        elif user_choice == "save":
            save_file = input("Where to save: ")
            save(playlist, save_file)

        elif user_choice == "load":
            load_file = input("What file to load: ")
            playlist = load_file
            load(playlist)

        if user_choice == "exit":
            end = True


playlist_app()