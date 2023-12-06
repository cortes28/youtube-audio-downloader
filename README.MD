Python 3 script based on downloading YouTube videos and converting them to MP3 Files to convert them to text! With the option to convert them to .wav if needed. I will have a section below of upcoming updates for this program and future goals. 


Note that there are specific module imports
=======
Python 3 script based on downloading YouTube videos and converting them to MP3 Files. 
Notes at the bottom are notices to be considered as the program could have issues. Namely, the audio-to-speech is not working.

Note that there are modules to import

`pytube import YouTube`
`from vosk import Model, KaldiRecognizer`
`from pydub import AudioSegment` 

which may cause issues. you will need to pip3 install

`pip3 install pytube`
`pip3 install vosk`
`pip3 install pydub`

Second module

`pip3 install pydub`

The third module is still not being fully utilized but may be used for future features

`pip3 install SpeechRecognition`

There may be other methods towards installing such modules depending on your environment.
If there are any other issues with the pip3 install, it may be that your pip3 is broken.

The environment that this was run in was in a WSL2 Ubuntu. There are multiple ways to prompt the program.

## Method 1

Press run. The program will prompt you to give it a YouTube URL.

## Method 2

The second way is to run it as given. It will then prompt you to give it a YouTube URL.

`python3 youtube_download.py`

## Method 3

The third way allows you to give it multiple arguments containing the proper YouTube URL encased in double quotations as shown during execution.

`python3 youtube_download.py "<YouTube URL #1>" "<YouTube URL #2>"`

Here is an example showing how it can be done

`python3 youtube_download.py "https://www.youtube.com/watch?v=ySO56zJxIns"`

## Method 4

The fourth method is a direct function that accepts multiple parameters into arguments using the following function.

`def download_audio(video, title = "", directory = ".") -> None:`

* video - the string containing a YouTube URL
* title - if empty, it will use the given YouTube title
* directory - if you want to store it in a specific directory, otherwise it will download it into the current folder/directory

# Future Updates

I am looking forward to further advancing this program and currently am looking for a model that would summarize the piece of text from the video. The next biggest update will be to bring this program into a website with Django to allow users to use. However, first I will try to continue working on this code until it seems viable to bring onto Django. So it will be a little while longer before it comes to life!
=======
## Current Bugs/Errors

* Have not run into any bugs/errors, but that does not mean there might not be any! Let me know if there is an error!

## Other

If you have any other questions please let me know!

