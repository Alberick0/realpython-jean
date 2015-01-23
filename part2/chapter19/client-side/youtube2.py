__author__ = 'alberick'
# Basic web service

# import libraries
import gdata.youtube
import gdata.youtube.service

# YouTubeService() generates an object that we use to communicate with youtube
youtube_service = gdata.youtube.service.YouTubeService()

# type in a youtube id
playlist = str(raw_input('Type in the youtube ID: '))

# API data
url = "http://gdata.youtube.com/feeds/api/users/"
playlist_url = url + playlist + "/playlists"

# get youtube playlist
video_feed = youtube_service.GetYouTubePlaylistVideoFeed(playlist_url)

print video_feed