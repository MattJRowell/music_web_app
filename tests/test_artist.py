from lib.artist import Artist

""" 
Artist constructed with an id, name, and genre
"""
def test_contrutcion():
    artist = Artist(1, "Test Name","Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Name"
    assert artist.genre == "Test Genre"


""" 
Artists with identical contents are equal
"""
def test_equal():
    artist_1 = Artist(1, "Test Name", "Test Genre")
    artist_2 = Artist(1, "Test Name", "Test Genre")
    assert artist_1 == artist_2


""" 
Artists can be represented as strings
"""
def test_stringifying():
    artist = Artist(1, "Test Name", "Test Genre")
    assert str(artist) == "Artist(1, Test Name, Test Genre)"