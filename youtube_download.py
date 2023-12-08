import sys
import os
import time
import json

FRAME_RATE = 16000  # for speech recognition, with sampling rate of 1600 Hz 
CHANNELS = 1        # only will configure audio to single channel over L & R channels
model = None        # will load model in try
rec = None          # the recognizer

try:
    from pytube import YouTube
    from pydub import AudioSegment
    from vosk import Model, KaldiRecognizer
    # may delete this in the future as I found a new model 'vosk' to transcribe audio
    import speech_recognition as sr

    # unsure if to move this into mp3_to_text function
    model = Model(model_name="vosk-model-small-en-us-0.15")
    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)

except ImportError:
    print(ImportError.msg)
    print(
        "\033[1;31;40m Couldn't import |YouTube| from |pytube| OR |AudioSegment| from pydub OR speech recognition \u001b[0m "
    )
    print('The needed command for Python3 would be "pip3 install pytube/pydub"')
    print(
        "\n***NOTE*** \n\tIt may not work if there are issues with your pip3 OR other...\n"
    )
    print("Exiting program...")
    sys.exit()


def wav_to_text(filename: str) -> str:
    """
    (Outdated function - may be deleted)
    Converts up to 45 seconds of audio to text from a WAV audio file.

    Parameters
    ----------
        filename: str
            The name of the WAV file that will be transcribed to text.

    Returns
    -------
    str
        The transribed audio of up to 45 seconds. 
    """
    # use the source file .wav as the audio source to convert to text
    
    text = None
    video = filename.strip()

    # make sure if the file exists and if it doesn't it will create it IFF the video string is a valid youtube link
    file_exists = os.path.exists(path=video)

    if file_exists is False or ".mp3" in video:
        print(f"Converting {video} to .wav...")
        video = convert_to_wav(video=video)

    # initialize the recognizer
    r = sr.Recognizer()

    # open the file
    with sr.AudioFile(video) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)

    
    return text


def convert_to_wav(filename: str, title: str = "") -> str:
    """
    Converts an existing mp3 file to a wav file and returns the title of the .wav file created.
    
    Parameters
    ----------
    filename: str
        The video string that will be converted *NOTE* that it must be .mp3.
    title: str
        the name of the .wav if the user wants to rename it, otherwise it will use the name from the .mp3 file.

    Returns
    -------
    str
        Returns the name of the file that we just made with the .wav extension, 
    otherwise return nothing.

    """
    dest = ""
    video = filename.strip()
    title = title.strip()
    try:
        if len(title) != 0:
            dest = str(title) + ".wav"
        elif ".mp3" in video:
            dest = video.replace(".mp3", ".wav")
        else:
            dest = video + ".wav"
            video = video + ".mp3"
            

        # convert now from mp3 to wav
        sound = AudioSegment.from_file(video)
        sound.export(dest, format="wav")
        return dest
    except Exception as e:
        print(f"Error in converting INPUT:{video} to .wav file...\nNOTE it has to be an .mp3 file.")
        print(f"ERROR: {e}")
        return


def mp3_to_text(filename: str) -> list[str]:
    """
    Converts an existing mp3 file to a list of string containing all of the transcribed text of the video.

    Parameters
    ----------
    filename: str
        The existing .mp3 file that we will convert to text.

    Returns
    -------
    list[str]
        Returns a list of strings containing the transribed text of the video. 
    """
    mp3 = AudioSegment.from_file(filename)
    mp3 = mp3.set_channels(CHANNELS)
    mp3 = mp3.set_frame_rate(FRAME_RATE)

    # iterate over 45 seconds of audio
    step = 45000

    transcript = list()

    # transcribe pieces of audio (45 second intervals) to text
    for i in range(0, len(mp3), step):
        print(f"Progress: {i/len(mp3)}")
        segment = mp3[i:(i+step)]

        rec.AcceptWaveform(segment.raw_data)
        result = rec.Result()

        text = json.loads(result)["text"]
        transcript.append(text)

    print(transcript)

    return transcript

def summarize_text(text: list[str]) -> str:
    pass


def download_audio(video: str, title: str="", directory: str=".") -> None:
    """
    Converts a YouTube video into an .mp3 file.

    Parameters
    ----------
    video: str
        A YouTube hyperlink or URL in string format that the function will convert to an audio file (MP3).
    title: str
        A new title for the MP3 file if the user wants to change the name of it, otherwise it will default to the title of the video.
    directory: str
        The directory or folder that we want to place the MP3 file in, otherwise it will default to the same folder. 

    Returns
    -------
    None
    """

    # convert into Youtube obj to get features
    yt = None
    try:
        yt = YouTube(video)
    except Exception as e:
        print("Failure in converting video...")
        print(f"ERROR: {e}")
        return

    if len(title) > 0:
        yt.title = title

    name = f"\033[1;35;40m {yt.title} \u001b[0m"

    # convert to an audio file
    audio = yt.streams.filter(only_audio=True).first()

    # download the audio
    download = audio.download(output_path=directory)

    # save the audio
    base, ext = os.path.splitext(download)
    audio_download = base + ".mp3"
    os.rename(download, audio_download)

    print(f"{name} has been downloaded\n")
    time.sleep(0.5)



def download(video: str) -> str:
    """
    (Default function) Converts a YouTube video into an MP3 file. Here the user will be asked more information regarding their download.

    Parameters
    ----------
    video: str
        A YouTube hyperlink or URL in string format that the function will convert to an audio file (MP3).

    Returns
    -------
    str
        Title of the video downloaded.
    """

    # convert into Youtube obj to get features
    yt = None
    try:
        yt = YouTube(video)
    except Exception as e:
        print("Failure in converting current video...")
        print("ERROR: {e}")
        return

    name = yt.title
    title = name
    name = f"\033[1;35;40m {name} \u001b[0m"

    print("\n")
    # ask if the user wants to download the audio for the given video
    decision = input(
        f"Do you want to download the audio for this video? -> {name} \nEnter \033[1;31;40m N \u001b[0m Otherwise enter any key to continue: "
    )

    if decision.capitalize().strip() == "N":
        print("\n")
        return

    # determine whether the user wants to change the title of the mp3 audio
    decision = input(
        f"the current title name is {name}. \nDo you wish to change it? Enter \033[1;31;40m Y \u001b[0m to do so. Otherwise enter any key to continue: "
    )

    while decision.capitalize().strip() == "Y":
        title = input("Enter the new title for the mp3: ")

        name = f"\033[1;35;40m {title} \u001b[0m"
        yt.title = title

        decision = input(
            f"\nThe current title is {name}.\nDo you wish to change it? Enter \033[1;31;40m Y \u001b[0m to do so. Otherwise enter any key to continue: "
        )

    # convert to an audio file
    audio = yt.streams.filter(only_audio=True).first()
    directory = ""
    decision = "Y"

    while decision.capitalize().strip() == "Y":
        print("\n")
        print(
            "Give a folder/directory to place the mp3 file or leave blank to leave it in current folder/directory"
        )
        directory = str(input(" >> "))

        if len(directory) == 0:
            directory = "."

        print(
            f"\nThe given directory for the song {name} is \033[1;35;40m '{directory}' \u001b[0m"
        )
        decision = input(
            "Do you wish to change it?\nEnter \033[1;31;40m Y \u001b[0m to do so. Otherwise enter any key to continue: "
        )

    # download the audio
    download = audio.download(output_path=directory)

    # save the audio
    base, ext = os.path.splitext(download)
    audio_download = base + ".mp3"
    os.rename(download, audio_download)

    print(f"{name} has been downloaded\n")

    # returns the title name with the 'mp3' appended to it
    title = title + ".mp3"
    return title


def main(argv) -> None:
    # for each "URL" convert to audio file (mp3)
    for link in argv:
        download_audio(video=link)

    output = "a"
    if len(argv) > 0:
        output = "another"
        print("All the given videos have been downloaded!")

    decision = input(
        f"Would you like to download {output} video?\nEnter \033[1;31;40m Y \u001b[0m to do so. Otherwise press any key to exit: "
    )
    
    output = "another"

    while decision.capitalize().strip() == "Y":
        url = input("Enter the URL of the video: ")
        title = download(video=url)


        decision = input(
            f"Would you like to convert video to text?\nEnter \033[1;31;40m Y \u001b[0m to do so. Otherwise press any key to continue: "
        )

        if decision.capitalize().strip() == "Y":
            text = mp3_to_text(filename=title)

            for segment in text:
                print(text)
            
            # TODO: Summarizer right after of converting to text
            # decision = input(
            #     f"Would you like to summarize the next?\nEnter \033[1;31;40m Y \u001b[0m to do so. Otherwise press any key to continue: "
            # )

            # if decision.capitalize().strip() == "Y":
            #     print(summarize_text(text=text))
          


        decision = input(
            f"Would you like to convert video to .wav?\nEnter \033[1;31;40m Y \u001b[0m to do so. Otherwise press any key to continue: "
        )

        if decision.capitalize().strip() == "Y":
            title = convert_to_wav(video=title)
            
   


if __name__ == "__main__":
    main(sys.argv[1:])


