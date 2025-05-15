#  8-8. User Albums: Start with your program from Exercise 8-7. Write a while 
# loop that allows users to enter an album’s artist and title. Once you have that 
# information, call make_album() with the user’s input and print the dictionary 
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist, title, number_of_songs=None):
    album = {'artist': artist, 'title': title}
    if number_of_songs is not None:
        album['songs'] = number_of_songs
    return album

while True:
    artist = input("Enter artist name: ")
    title = input("Enter album title: ")
    album = make_album(artist,title)
    print(album)
    quit = input("If you want to exit, enter q or any other word to continue: ")
    if quit == 'q':
        break