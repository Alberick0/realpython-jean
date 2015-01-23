__author__ = 'alberick'

# Basic web service example

# import libraries
import gdata.youtube
import gdata.youtube.service

# YouTubeService() generates the object we will use to communicate with the Youtube API
youtube_service = gdata.youtube.service.YouTubeService()

# Ask to type in the youtube user ID
playlist = raw_input("Please enter the user ID: ")

# setup the API data
url = "http://gdata.youtube.com/feeds/api/users/"
playlist_url = url + playlist + "/playlists"

# retrieve the playlist
video_feed = youtube_service.GetYouTubePlaylistVideoFeed(playlist_url)

print "\nPlaylist for " + str(playlist) + ":\n"

# display each playlist to the screen
for p in video_feed.entry:
    print p.title.text