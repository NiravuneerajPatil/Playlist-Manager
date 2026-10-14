class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next=None
        self.prev=None

    def __str__(self):
        return f"{self.title} by {self.artist}"
class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if not self.head:
            self.head = new_song
            self.tail = new_song
            self.current = new_song
        else:
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song
    def play_current(self):
        if self.current:
            print(f"Playing: {self.current}")
    def previous_song(self):
            if self.current and self.current.prev:
                self.current = self.current.prev
                self.play_current()
            else:
                print("No previous song.")
    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.play_current()
        else:
            print("No next song.")
    def display_playlist(self):
        current = self.head
        while current:
            print(current)
            current = current.next
    
def run():
    playlist = Playlist()
    while True:
        print("\nMenu:")
        print("1. Add Song")
        print("2. Play Current Song")
        print("3. Next Song")
        print("4. Previous Song")
        print("5. Display Playlist")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            playlist.add_song(title, artist)
        elif choice == '2':
            playlist.play_current()
        elif choice == '3':
            playlist.next_song()
        elif choice == '4':
            playlist.previous_song()
        elif choice == '5':
            playlist.display_playlist()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    run()
    
