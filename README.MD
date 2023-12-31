2 Python scripts
================
 `youtube_download.py`
the original file now ONLY contains code to convert a YouTube URL to an MP3/WAV file.
`youtube_summarizer.py`
is a new file containing code to convert a YouTube URL to an MP3 to summarize (using the 'Extractive Summarization' method) the video using spaCy. 

NOTES:

There are modules to import

`pytube import YouTube`
`from vosk import Model, KaldiRecognizer`
`from pydub import AudioSegment` 
and more...

which may cause issues. you will need to pip3 install

`pip3 install pytube`
`pip3 install vosk`
`pip3 install pydub`
`pip3 install -U spacy`
`python3 -m spacy download en_core_web_sm`


The fourth module was previously used. However, future advancements in the code have made it redundant. It will only convert a WAV file up to 45 seconds. Using the MP3-to-text method is more applicable. 

`import speech_recognition as sr`

`pip3 install SpeechRecognition`

There may be other methods towards installing such modules depending on your environment.
If there are any other issues with the pip3 install, it may be that your pip3 is broken.

The environment that this was run in was in a WSL2 Ubuntu. There are multiple ways to prompt both scripts. If you only want to convert a YouTube URL to an MP3/WAV file. use the `youtube_download.py` script in place of the `youtube_summarizer.py` script. 

## Method 1

Press run. The program will prompt you to give it a YouTube URL.

## Method 2

The second way is to run it as given. It will then prompt you to give it a YouTube URL.

`python3 youtube_summarizer.py`

## Method 3

The third way allows you to give it multiple arguments containing the proper YouTube URL encased in double quotations as shown during execution.

`python3 youtube_summarizer.py "<YouTube URL #1>" "<YouTube URL #2>"`

Here is an example showing how it can be done

`python3 youtube_summarizer.py "https://www.youtube.com/watch?v=ySO56zJxIns"`

## Method 4

The fourth method is a direct function that accepts multiple parameters into arguments using the following function.

`def download_audio(video, title = "", directory = ".") -> None:`

* video - the string containing a YouTube URL
* title - if empty, it will use the given YouTube title
* directory - if you want to store it in a specific directory, otherwise it will download it into the current folder/directory

# Future Updates

I believe I will make small patches, I am already looking forward to moving this into a more applicable environment. Either using Flask or Django. I am experimenting with which is better as I have hopes of publishing this as a website with the main focus being a YouTube summarizer! 

## Current Bugs/Errors

* Have not run into any bugs/errors, but that does not mean there might not be any! Let me know if there is an error!

## Other

If you have any other questions please let me know!

