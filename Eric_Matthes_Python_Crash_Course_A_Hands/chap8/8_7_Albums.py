#  8-7. Album: Write a function called make_album() that builds a dictionary 
# describing a music album. The function should take in an artist name and an 
# album title, and it should return a dictionary containing these two pieces of 
# information. Use the function to make three dictionaries representing different 
# albums. Print each return value to show that the dictionaries are storing the 
# album information correctly.
#  Use None to add an optional parameter to make_album() that allows you to 
# store the number of songs on an album. If the calling line includes a value for 
# the number of songs, add that value to the album’s dictionary. Make at least 
# one new function call that includes the number of songs on an album.

def make_album(artist, title, number_of_songs=None):
    album = {'artist': artist, 'title': title}
    if number_of_songs is not None:
        album['songs'] = number_of_songs
    return album

album1 = make_album('Taylor Swift', '1989')
album2 = make_album('Adele', '25')
album3 = make_album('Coldplay', 'Parachutes', 10)  

print(album1)
print(album2)
print(album3)

