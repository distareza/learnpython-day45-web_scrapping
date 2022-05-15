import configparser

config = configparser.RawConfigParser()
config.read(filenames="../config.properties")

spotify_client_id = config.get("spotify.com", "spotify.client.id")
spotify_client_secret = config.get("spotify.com", "spotify.client.secret")