def make_album(artis_name, album_title, songs_number = None):
    """Return a discografy of an artist in list"""
    if songs_number:
        list_artist = {'aName':artis_name,'albumTitle' : album_title,'songs_number':songs_number}
    else:
        list_artist = {'aName':artis_name,'albumTitle' : album_title}

    return list_artist

while True:
    print("\nWrite your favorite singer and its information")
    print("press 'q' and enter to quit")

    artistName = input('singer name: ')
    if artistName == 'q':
        break
    
    albumTitle = input('album singer: ')
    if albumTitle == 'q':
        break
    
    songsNumber = input('number of sings: ')
    if songsNumber == 'q':
        break
    elif songsNumber.isnumeric():
        songsNumber = int(songsNumber)
        artist_info = make_album(artistName,albumTitle,songsNumber)
    else:
        artist_info = make_album(artistName,albumTitle)

    print(artist_info)


    

