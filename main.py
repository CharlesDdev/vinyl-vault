import random # Import the random module

class Record:
    def __init__(self, title, artist, year, genre, condition, value): # Define the Record class
        self.title = title # Set the title attribute to the title parameter
        self.artist = artist # Set the artist attribute to the artist parameter
        self.year = year # Set the year attribute to the year parameter
        self.genre = genre # Set the genre attribute to the genre parameter
        self.condition = condition # Set the condition attribute to the condition parameter
        self.value = value # Set the value attribute to the value parameter
        
def __str__(self): # Define the __str__ method
    return f"{self.title} by {self.artist} ({self.year})" # Return a string representation of the object

class UserProfile:
    def __init__(self, username, email): # Define the UserProfile class
        self.username = username
        self.email = email
        self.favorite_genre = "Hip Hop" # Set the default genre to "Hip Hop"
        
class VinylVault:
    def __init__(self, username): # Define the VinylVault class
       self.collection = [] # Create an empty list to store records
       self.wishlist = [] # Create an empty list to store records
       self.user_profile = UserProfile(username, "default@example.com") # Create a new UserProfile object with the given username and a default email
       
class VinylVault:
    def __init__(self, username): # Define the VinylVault class
       self.collection = [] # Create an empty list to store records
       self.wishlist = [] # Create an empty list to store records
       self.user_profile = UserProfile(username, "default@example.com") # Create a new UserProfile object with the given username and a default email
       
    def scan_record(self, barcode): # simulating a barcodescan with random data
        artists = ("Kendrick Lamar", "J. Cole", "Drake", "Nas", "Jay-Z", "Boldy James")
        titles = ("Good Kid, M.A.A.D city", "2014 forest Hills Drive", "Take Care", "Illmatic", "Reasonable Doubt", "Permanent Ink")
        year = random.randint(1990, 2023)
        value = random.randint(10, 100)
        condition = ("Good", "Bad", "Mint")
        genre = ("R&B", "Hip Hop", "Soul", "Country", "Jazz", "Rock", "Blues")
        
        # Returns a new "Record" object that randomly returns details
        return Record(random.choice(titles), random.choice(artists), year, random.choice(genre), random.choice(condition), value)
                      
    def add_to_collection(self, record):
            self.collection.append(record)
            print(f"Added {record} to your collection.") # Adds record to collection

    def calculate_collection_value(self):
        return sum(record.value for record in self.collection) # Loops through all records, adds up their value and returns value
        
    def play_virtual_record(self, record):
        print(f"Now playing: {record}")
        print(f"*scratch* *scratch* Yo, check out this beat!") # Simulates playing a record by printing details
        
    def show_collection(self):
        if not self.collection:
            print("Your collection is empty. Time to dig in the crates!")
        else:
            print("Your Vinyl Vault")
            for i, record in enumerate(self.collection, 1):
                print(f"{i}. {record} - ${record.value}") # checks if collection is empty, otherwise loops through collection and prints index and value
    
if __name__ == "__main__":
    vault = VinylVault("DJ_Python") # creates an instance of "Vinyl Vault" with a username "DJ Python"
    
for _ in range(5):
    new_record = vault.scan_record("dummy_barcode")
    vault.add_to_collection(new_record) #simulates scanning 5 records and adds each to the collection
    
vault.show_collection() # calls the show_collection method to display the collection

total_value = vault.calculate_collection_value() # calculates the total value of the collection
print(f"\nTotal value of your collection: ${total_value}") # prints the total value of the collection
    
if vault.collection:
    vault.play_virtual_record(random.choice(vault.collection)) # plays a random record from the collection
    