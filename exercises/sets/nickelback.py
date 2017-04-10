# Define a set that contains tuples. Each tuple should contain two strings:

# The name of an artist
# A song by that artist
# Make sure that some of the songs are from the band Nickelback. You can see a list of their greatest hits on Amazon.

songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals'),
    ('Buddy Holly', 'Nickelback Sucks')
}

# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

better_songs = {song for song in songs if "Nickelback" != song[0]}
print(better_songs)

