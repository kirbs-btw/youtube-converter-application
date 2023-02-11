import youtube_dl

def main():
    output = input("output folder path: ")
    output = sub(output, "\\", "/")
    link = input("give link: ")
    
    converter(link, output)


# my re.sub does not work 
# don't have the time to fix it
def sub(text, pattern, replace) -> str:
    newText = ""

    for char in text:
        if char == pattern:
            newText += replace
        else:
            newText += char

    return newText


def downloadVideo(videoInfo ,path):
    nameSave = ""

    try:
        filename = f"{path}/{videoInfo['title']}.wav"
        nameSave = filename
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl': filename,
        }
        print(f"[script] downloading {videoInfo['title']}")

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([videoInfo['webpage_url']])
    except:
        print("Error occured with the video {}".format(nameSave))


def converter(link, path):
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