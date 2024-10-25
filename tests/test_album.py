from lib.album import Album

""" 
Album constructed with an id, title, release_year, and artist_id
"""
def test_contrutcion():
    album = Album(1, "Test Title", 2000, 2)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 2000
    assert album.artist_id == 2


""" 
Albums with identical contents are equal
"""
def test_equal():
    album_1 = Album(1, "Test Title", 2000, 2)
    album_2 = Album(1, "Test Title", 2000, 2)
    assert album_1 == album_2


""" 
Albums can be represented as strings
"""
def test_stringifying():
    album = Album(1, "Test Title", 2000, 2)
    assert str(album) == "Album(1, Test Title, 2000, 2)"