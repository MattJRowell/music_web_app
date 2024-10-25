# Tests for your routes go here

""" 
When I call GET /albums
I get a list of all albums back
"""
def test_get_albums(db_connection, web_client):
    # Seed the database with the initial data
    db_connection.seed("seeds/albums_table.sql")
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, We Are Not Your Kind, 2019, 1)"

""" 
When I call POST /albums with album info
that album is added to the list in GET /albums
"""
def test_post_album(db_connection, web_client):
    # Seed the database with the initial data
    db_connection.seed("seeds/albums_table.sql")
    post_response = web_client.post("/albums", data={
        'title': 'Voyage',
        'release_year': '2022',
        'artist_id': '2'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""
    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, We Are Not Your Kind, 2019, 1)\n" \
        "Album(2, Voyage, 2022, 2)"


def test_post_albums_with_no_data(db_connection, web_client):
    # Seed the database with the initial data
    db_connection.seed("seeds/albums_table.sql")
    post_response = web_client.post("/albums")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "" \
        "You need to submit a title, release_year, and artist_id"
    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, We Are Not Your Kind, 2019, 1)"

""" 
When I call GET /artists
I get a list of all artists back
"""
def test_get_artists(db_connection, web_client):
    # Seed the database with the initial data
    db_connection.seed("seeds/artists_table.sql")
    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Artist(1, Slipknot, Metal)"