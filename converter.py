import youtube_dl

def main():
    link = input("give link: ")
    output = "C:/something/somethin" # example path
    
    prepLink(link, output)


def downloadVideo(videoInfo ,path):
    try:
        filename = f"{path}/{videoInfo['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl': filename,
        }
        print(f"[script] downloading {videoInfo['title']}")

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([videoInfo['webpage_url']])
    except:
        print("error occured with one video")

def prepLink(link, path):
    video_url = link
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )

    try: 
        # trying it for a playlist
        for singleVideoInfo in video_info['entries']:
            downloadVideo(singleVideoInfo, path)
    except KeyError:
        # if the KeyError is raised it will be a  KeyError: 'entries'
        # it is a single video
        downloadVideo(video_info, path)
    print("download complete")

if __name__=='__main__':
    main()