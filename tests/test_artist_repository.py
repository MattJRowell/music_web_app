from lib.artist import Artist
from lib.artist_repository import ArtistRepository

""" 
When I call all()
I get a list of all of the artists in the artists table
"""
def test_get_all(db_connection):
    repository = ArtistRepository(db_connection)
    assert repository.all() == [
        Artist(1, "Slipknot", "Metal")
    ]

""" 
When I call create()
An artist is created in the database and can be seen when all() is called
"""
def test_create(db_connection):
    db_connection.seed("seeds/artists_table.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, "Test Name", "Test Genre")
    repository.create(artist)
    assert repository.all() == [
        Artist(1, "Slipknot", "Metal"),
        Artist(2, "Test Name", "Test Genre")
    ]