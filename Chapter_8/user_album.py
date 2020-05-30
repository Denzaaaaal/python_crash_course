def make_album(name, title, no_of_songs=None):
    if no_of_songs:
        album = {
            'artist_name': name,
            'album_title': title,
            'number_of_songs': no_of_songs,
        }
    else:
        album = {
            'artist_name': name,
            'album_title': title,
        }
    return album

while True:
    print ("\n(Enter 'quit' to end the program)")
    entered_name = input("What is the artist name: ")
    if entered_name == 'quit':
        break
    entered_album = input("What is the albums title: ")
    if entered_album == 'quit':
        break

    print (make_album(entered_name, entered_album))