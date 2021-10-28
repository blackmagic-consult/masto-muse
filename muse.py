#!/usr/bin/python3
from mastodon import Mastodon
import musicpd

port = 6600
host = 'localhost'
instance = 'https://cybre.space'
lang = eng

client = musicpd.MPDClient()
client.connect(host, port)
now = client.currentsong()
client.close()
client.disconnect()

if lang == "eng":
  nowp = ("Now Playing: %s - %s" % (now['title'], now['artist']))
  print(nowp)
else:
  nowp = ("現在再生中： %s - %s" % (now['title'], now['artist']))
  print(nowp)

mast = Mastodon(client_id='/home/USER/.ncmpcpp/masto-muse_appcred.secret', access_token='/home/USER/.ncmpcpp/masto-muse_usercred.secret', api_base_url=instance)
mast.account_update_credentials(note=nowp)
