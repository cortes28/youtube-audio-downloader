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


# convert a mp3 file to a wav file
def convert_to_wav(video, title="") -> bool:
    """
    input: video title which may contain .mp3 in string format, new title if given one
    """
    dest = ""
    video = video.strip()
    title = title.strip()

    if len(title) != 0:
        dest = str(title) + ".wav"
    elif video.includes(".mp3"):
        dest = video.replace(".mp3", ".wav")
    else:
        dest = video + ".wav"
        video = video + ".mp3"

    # convert now from mp3 to wav
    sound = AudioSegment.from_mp3(video)
    sound.export(dest, format="wav")


# does not take in user input other than the URL and title if given one by the user
def download_audio(video, title="", directory=".") -> None:
    """
    input: Youtube video URL (video URL enclosed with "<video URL>"), optional title for it, and optional directory
    """

    # convert into Youtube obj to get features
    yt = None
    try:
        yt = YouTube(video)
    except:
        print("Failure in converting video...")
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


# default function for the download
def download(video) -> str:
    """
    input: Youtube video URL (video)

    Asks user regarding the current video if they want to change the skip the download of the current video, change title,
    where they want to download it (directory/folder)
    """

    # convert into Youtube obj to get features
    yt = None
    try:
        yt = YouTube(video)
    except:
        print("Failure in converting current video...")
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
    return audio_download


def main(argv) -> None:
    # for each "URL" convert to audio file (mp3)
    for x in argv:
        download_audio(x)

    output = "a"
    if len(argv) > 0:
        output = "another"
        print("All the given videos have been downloaded!")

    decision = input(
        f"Would you like to download {output} video?\nEnter \033[1;31;40m Y \u001b[0m to do so. Otherwise press any key to exit: "
    )

    while decision.capitalize().strip() == "Y":
        url = input("Enter the URL of the video: ")
        download(url)
        decision = input(
            "Would you like to download another video?\nEnter \033[1;31;40m Y \u001b[0m to do so. Otherwise press any key to exit: "
        )

    print("\nExiting program...")


if __name__ == "__main__":
    main(sys.argv[1:])
