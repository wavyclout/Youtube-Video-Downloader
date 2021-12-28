from pytube import YouTube

url = '' # Paste youtube video URL
my_video = YouTube(url)

print("Video Title: ")

print(my_video.title)

print("Thumbnail Image: ")

print(my_video.thumbnail_url)

print("Download Video: ")
#get all the stream resolution for the 
for stream in my_video.streams:
    print(stream)


my_video = my_video.streams.get_highest_resolution()





my_video.download()
