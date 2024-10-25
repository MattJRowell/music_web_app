Test-drive a route `POST /albums` to create a new album:

```
# Request:
POST /albums

# With body paramters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK):
(no content) 
```

Your test should assert that the new album is present in the list of records returned by `GET /a;bums'.

# SINGLE TABLE DESIGN RECIPE

## 1. Extract nouns from the user stories or specification

```
Nouns:

album, title, release year, artist id.
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                         |
| --------------------- | ---------------------------------- |
| album                 | id, title, release_year, artist_id |

Name of the table (always plural): `albums`

Column names: `id`, `title`, `release_year`, `artist_id`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
id: SERIAL
title: text
release_year: int
artist_id: int
```

## 4. Write the SQL

```sql
-- file: albums_table.sql

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 music_db < albums_table.sql
```





# PLAIN ROUTE DESIGN RECIPE

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# POST /albums
# With body parameters:
#   - title: string
#   - release_year: int
#   - artist_id: int

# GET /albums
# No parameters (just return all)
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# Scenario 1 - Add an album to albums then see it reflected in the list

#   POST /albums
# Body:
# title=Voyage
# release_year=2022
# artist_id=2
#   Expected Response (200 OK):
"""
(No content)
"""

#   GET /albums
#   Expected Resposne (200 OK):
"""
Album(1, We Are Not Your Kind, 2019, 1)
Album(2, Voyage, 2022, 2)
"""

def test_post_album(db_connection, web_client):
    # Seed the database with the initial data
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.post("/albums", data={
        'title': 'We Are Not Your Kind',
        'release_year': '2019',
        'artist_id': '1'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""

# Scenario 2 - Don't write anything in the POST request then show existing albums

#   POST /albums
#   Expected Response (400 Bad Request):
"""
You need to submit a title, release_year, and artist_id
"""

#   GET /albums
# Expected Response (200 OK):
"""
Album(1, We Are Not Your Kind, 2019, 1)
"""


```