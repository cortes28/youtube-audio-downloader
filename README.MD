

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

