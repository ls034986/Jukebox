from pygame import mixer
import os
from youtube_search import YoutubeSearch
import youtube_dl
import time

currentFolder = os.path.dirname(__file__)
songFolder = os.path.join(currentFolder, "songs")
fileList = []

mixer.init()

def clear():
    os.system('cls')

def run():
    while True:
        mixer.music.stop()
        mixer.music.unload()
        clear()
        for file in os.listdir("./songs"):
            if file.endswith(".mp3"):
                fileList.append(file)

        print('############################')
        print('#  Welcome to the Jukebox  #')
        print('#     Here you can play    #')
        print('# any pre-downloaded music #')
        print('#    Please input a song   #')
        print('#         you like         #')
        print('############################')
        userChoice = input('>> ')


        userFile = userChoice+'.mp3'

        ydl_opts = {
            'outtmpl' : 'songs/'+userChoice+'.webm',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }


        if userFile in fileList:
            print('Playing your song.')
            mixer.music.load(os.path.join(songFolder, userFile))
            mixer.music.set_volume(0.5)
            mixer.music.play()
        else:
            print('We could not find your song. Would you like us to download it? y/n')
            if input('>> ') == 'y':
                results = YoutubeSearch(f'{userChoice} song', max_results=1).to_dict()
                firstResult = results[0]
                print(f'We found {firstResult["title"]} by {firstResult["channel"]}. Is this correct? y/n')
                if input('>> ') == 'y':
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([f'http://www.youtube.com{firstResult["url_suffix"]}'])
                        print('Clearing screen in 5 seconds')
                        time.sleep(5)
                        clear()
                else:
                    print('We can\'t automatically download the file.')
        input('Press enter when ready to try again.')

run()