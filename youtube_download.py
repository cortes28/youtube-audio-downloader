# Audio downloader from YouTube URL

import sys
import os
import time

try:
    from pytube import YouTube
    from pydub import AudioSegment
except ImportError:
    print(ImportError.msg)
    print(
        "\033[1;31;40m Couldn't import |YouTube| from |pytube| OR |AudioSegment| from pydub \u001b[0m "
    )
    print('The needed command for Python3 would be "pip3 install pytube/pydub"')
    print(
        "\n***NOTE*** \n\tIt may not work if there are issues with your pip3 OR other...\n"
    )
    print("Exiting program...")
    sys.exit()


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


# does not take in user input other than the URL and title if given one by the user
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
        f"Do you want to download the audio for this video? -> {name} \nEnter \033[1;31;40m N \u001b[0m to \033[1;31;40m NOT \u001b[0m download it. Otherwise enter any key to continue: "
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


def prompter() -> None:
    """
    Prompts the user if they want to continue downloading audios from a YouTube URL.  

    Parameters
    ----------
    None

    Returns
    -------
    None 
    """
    
    decision = input(
        f"Would you like to download a video?\nEnter \033[1;31;40m Y \u001b[0m to do so. Otherwise press any key to exit: "
    )
    
    output = "another"

    while decision.capitalize().strip() == "Y":

        url = input("Enter the URL of the video: ")
        title = download(video=url)


        decision = input(
            f"Would you like to convert video to .wav?\nEnter \033[1;31;40m Y \u001b[0m to do so. Otherwise press any key to continue: "
        )

        if decision.capitalize().strip() == "Y":
            title = convert_to_wav(filename=title)
            

        decision = input(
            f"Would you like to download {output} video?\nEnter \033[1;31;40m Y \u001b[0m to do so. Otherwise press any key to exit: "
        )


def main(argv) -> None:
    """
    Our main function that will convert any hyperlink in string format (if given any) into audio. If argv did not receive any arguments, then we will move on to the prompter to 
    prompt the user to enter any videos they would like to download.

    Parameters
    ----------
    argv
        Our arguments in the command line that are strings containing URLs to YouTube videos to convert. 
    
    Returns
    -------
    None
    
    """
    for link in argv:
        download_audio(video=link)


    if len(argv) > 0:
        print("All the given videos have been downloaded!")


    prompter()

    print("exiting program...")


if __name__ == "__main__":
    main(sys.argv[1:])