__author__ = 'alberick'
# Basic Web service

# import libraries
import gdata.youtube
import gdata.youtube.service

# instantiate a new youtube object
yts = gdata.youtube.service.YouTubeService()

# get an user id
user = str(raw_input("What's the user ID: "))

# API data
url = "http://gdata.youtube.com/feeds/api/users/"
playlist_url = url + user + "/playlists"

# Get youtube playlist and video list
playlist_feed = yts.GetYouTubePlaylistVideoFeed(playlist_url)
print playlist_url

# display each playlist
for playlist in playlist_feed.entry:
    print playlist.title.text
    playlistid = playlist.id.text.split('/')[-1]
    video_feed = yts.GetYouTubePlaylistVideoFeed(playlist_id=playlistid)
    for video in video_feed.entry:
        print video.title.text