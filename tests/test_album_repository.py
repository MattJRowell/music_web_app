from lib.album import Album
from lib.album_repository import AlbumRepository

""" 
When I call all()
I get a list of all of the albums in the album table
"""
def test_get_all(db_connection):
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, "We Are Not Your Kind", 2019, 1)
    ]

""" 
When I call create()
An album is created in the database and can be seen when all() is called
"""
def test_create(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "Test Title", 2000, 2)
    repository.create(album)
    assert repository.all() == [
        Album(1, "We Are Not Your Kind", 2019, 1),
        Album(2, "Test Title", 2000, 2)
    ]