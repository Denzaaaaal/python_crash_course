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

album_0 = make_album('vybz kartel', 'dancehall')
album_1 = make_album('alkaline', 'showcase raw', 16)
album_2 = make_album('i-octane', 'my life')

print (album_0)
print (album_1)
print (album_2)