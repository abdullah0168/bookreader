# Function to save the current position to a bookmark file
import os
def save_bookmark(position, bookmark_file="bookmark.txt"):
    with open(bookmark_file, 'w') as file:
        file.write(str(position))

# Function to load the current position from a bookmark file
def load_bookmark(bookmark_file="bookmark.txt"):
    if os.path.exists(bookmark_file):
        with open(bookmark_file, 'r') as file:
            def callingfile(argumrnt):
                open_file = int(argumrnt.read())
                if open_file>=100:
                    open_file = 0
                with open(bookmark_file, 'w') as file:
                    file.write(str(open_file))
                
            callingfile(file)
            
with open("bookmark.txt", "r") as file:
    print(int(file.read()))
# Test the functions
save_bookmark(round(100.98832974982734))
load_bookmark()