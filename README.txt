Hello! This program has a few key features that sets it apart from others.
While this is a working jukebox, it also has music downloading methods which has requirments (oooooh! scary!)
(Ichidaiji is a banger though.)

Install the requirments!
pip install youtube-dl (We use this to download youtube videos)
pip install youtube-search (Youtube API is heavy rate limited, and also kinda sucks, here we just have a web scraper do it for us.)
pip install pygame (This is so we can actually play music files.)

we also have to move files! AHHH! I know!
After youtube-dl has be downloaded find its .exe should be in the Python-3.8 install directiory under the \Scripts\ folder you need to
add the 3 .exes from this folder into that folder. These executables convert the youtube-dl default format of WebM to mp3 so we can play
them in the pygame-mixer

If you happen to want the source code or the original build for ffmpeg you can find it at ffmpeg.org, but my files are just the same as theirs.
