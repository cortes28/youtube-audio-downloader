Python 3 script based on downloading youtube videos and converting them to MP3 Files.

Note that there is a module import

`pytube import YouTube`

which may cause issues. you will need to pip3 install

`pip3 install pytube`

If there are any other issues with the pip3 install, it may be that your pip3 is broken or other.

The environment that this was run in was in a WSL2 Ubuntu. There are multiple ways to prompt the program

# Method 1

Simply pressing run. The program will prompt you to give it a YouTube URL.

# Method 2

Second way is to run it as given. It will then prompt you to give it a YouTube URL.

`python3 youtube_download.py`

# Method 3

The third way allows you to give it multiple arguments containing the proper YouTube URL encased in double quotations as shown

`python3 youtube_download.py "<YouTube URL #1>" "<YouTube URL #2>"`

Here is an example showing how it can be done

`python3 youtube_download.py "https://www.youtube.com/watch?v=ySO56zJxIns"`
