from pytube import YouTube
from moviepy.editor import AudioFileClip

def download_as_mp3(youtube_url, output_path):
    # Download the video
    youtube = YouTube(youtube_url)
    video = youtube.streams.get_highest_resolution()
    video.download(output_path, filename="temp")

    # Convert the video to MP3
    video_clip = AudioFileClip(output_path + "/temp.mp4")
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path + "/" + youtube.title + ".mp3")

    # Clean up
    video_clip.close()
    audio_clip.close()

# Use the function
download_as_mp3("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "/home/youfi/Downloads")