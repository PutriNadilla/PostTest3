class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"{self.title} - {self.genre} ({self.rating})"

class Node:
    def __init__(self, movie):
        self.movie = movie
        self.next = None
        
class Playlist:
    def __init__(self):
        self.head = None
        
    def add_movie(self, movie):
        new_node = Node(movie)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            
    def remove_movie(self, movie_title):
        current_node = self.head
        previous_node = None
        while current_node is not None and current_node.movie.title != movie_title:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            print(f"movie {movie_title} not found!")
        elif previous_node is None:
            self.head = current_node.next
            print(f"movie {movie_title} has been removed from the playlist!")
        else:
            previous_node.next = current_node.next
            print(f"movie {movie_title} has been removed from the playlist!")
            
    def display_playlist(self):
        current_node = self.head
        if current_node is None:
            print("playlist is empty!")
        else:
            print("playlist:")
            while current_node is not None:
                print(current_node.movie)
                current_node = current_node.next

my_playlist = Playlist()

while True:
    print("""
        =================================
        |       Playlist Netflix        |
        |-------------------------------|     
        |       1. Add Movie            |      
        |       2. Remove Movie         |      
        |       3. Display Playlist     |                             
        |       4. Exit                 |  
        =================================     
        """)
    
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        title = input("Enter Movie Title: ")
        genre = input("Enter Genre Name: ")
        rating = input("Enter Movie Rating: ")
        movie = Movie(title, genre, rating)
        my_playlist.add_movie(movie)
        print(f"{title} has been added to the playlist!")
    elif choice == 2:
        title = input("Enter Movie Title to remove: ")
        my_playlist.remove_movie(title)
    elif choice == 3:
        my_playlist.display_playlist()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please choose again.")