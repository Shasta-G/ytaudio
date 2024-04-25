from pytube import YouTube

def extract_audio(video_url):
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    return stream.download()

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    extract_audio(video_url)
