def make_album(artis_name, album_title, songs_number = None):
    """Return a discografy of an artist in list"""
    if songs_number:
        list_artist = {'aName':artis_name,'albumTitle' : album_title,'songs_number':songs_number}
    else:
        list_artist = {'aName':artis_name,'albumTitle' : album_title}

    return list_artist

print(make_album("canserbero","vida y muerte"))
print(make_album("nach","a traves de mi",15))