import random  # For shuffling the playlist

class SongNode:
    """Represents a node in the linked list for a song."""
    def __init__(self, title):
        self.title = title  # Song title
        self.next = None  # Pointer to the next song


class Playlist:
    """Manages a playlist of songs using a singly linked list."""

    def __init__(self):
        self.head = None  # First song in the playlist
        self.tail = None  # Last song in the playlist

    def add_song(self, title):
        """Adds a song to the end of the playlist."""
        if not title:
            print("Error: Song title cannot be empty.")
            return

        new_song = SongNode(title)  # Create a new song node
        if not self.head:  # If playlist is empty, set head and tail to new song
            self.head = self.tail = new_song
        else:  # Otherwise, attach new song to end of list
            self.tail.next = new_song
            self.tail = new_song
        print(f"Added: {title}")

    def display(self):
        """Prints the playlist in order."""
        current = self.head  # Start from the first song
        songs = []
        while current:  # Loop through linked list
            songs.append(current.title)  # Store song titles
            current = current.next
        print("Playlist:", " -> ".join(songs) if songs else "Empty")

    def randomize(self):
        """Shuffles the order of songs in the playlist."""
        # Convert linked list to array to make shuffling easier
        songs = []
        current = self.head
        while current:
            songs.append(current.title)
            current = current.next

        if len(songs) > 1:
            random.shuffle(songs)  # Shuffle list order

            # Rebuild the linked list in new order
            self.head = self.tail = SongNode(songs[0])
            for title in songs[1:]:
                new_song = SongNode(title)
                self.tail.next = new_song
                self.tail = new_song
        print("Playlist randomized!")
        self.display()  # Show new order

    def play_next(self):
        """Plays the first song and removes it from the playlist."""
        if not self.head:  # If playlist is empty, do nothing
            print("No songs left to play!")
            return
        print(f"Now playing: {self.head.title}")  # Show song being played
        self.head = self.head.next  # Move head to next song (remove current)
        if not self.head:  # If playlist is now empty, reset tail
            self.tail = None
        self.display()  # Show updated playlist

    def remove_song(self, title):
        """Removes a specific song from the playlist by title."""
        if not self.head:
            print("Playlist is empty.")
            return

        # If the song to remove is the head
        if self.head.title == title:
            print(f"Removed: {self.head.title}")
            self.head = self.head.next
            if not self.head:  # If playlist is now empty, reset tail
                self.tail = None
            return

        # Search for the song in the rest of the playlist
        current = self.head
        while current.next:
            if current.next.title == title:
                print(f"Removed: {current.next.title}")
                current.next = current.next.next
                if not current.next:  # If the removed song was the tail, update tail
                    self.tail = current
                return
            current = current.next

        print(f"Song '{title}' not found in the playlist.")
