![social_preview](https://user-images.githubusercontent.com/6128978/130181938-e9df8403-a3e2-455a-86f1-58261b148c01.jpg)

![MADE-IN-INDIA](https://img.shields.io/badge/MADE%20WITH%20%E2%9D%A4%20IN-INDIA-orange?style=for-the-badge) [![DOWNLOAD](https://img.shields.io/badge/CLICK%20HERE%20TO-DOWNLOAD-blue?style=for-the-badge)](https://github.com/pranjal-joshi/GifSaver/releases/latest) ![GitHub](https://img.shields.io/github/license/pranjal-joshi/GifSaver?style=for-the-badge) [![BADGE](https://img.shields.io/badge/OPEN-SOURCE-red?style=for-the-badge)](https://github.com/pranjal-joshi/GifSaver/blob/main/GifSaver.py)

## What's GifSaver?

Only an Ubuntu user knows the true pain of not able set a Live Screensaver. So the GifSaver came to save ya'all! 🎊

## How to Use it?

Firstly, Install the dependency by executing following command:

`sudo apt-get install xprintidle`

You can either run GifSaver with Python or use a pre-compiled binary!

The script takes 2 inputs from the user as follow:
```
usage: GifSaver.py or GifSaver.bin [-h] -f FOLDER [-t TIMEOUT] [-c CHANGE]

optional arguments:
  -h, --help            show this help message and exit
  -f FOLDER, --folder FOLDER
                        Path to GIF Folder
  -t TIMEOUT, --timeout TIMEOUT
                        Idle Timeout to Start Screensaver
  -c CHANGE, --change CHANGE
                        Change Image/GIF after seconds (0 = shuffle disable)

```
For example
```
python3 path/to/GifSaver.py -f path/to/folder/where/GIFs/are/stored -t 120 -c 60

or

./path/to/GifSaver.bin -f path/to/folder/where/GIFs/are/stored -t 60 -c 300
```

## Adding to Start-up

In ubuntu, You can execute any command on start-up, so we can run our GifSaver on every boot without manually running it!
Just enter above command as a new startup application!

**Note: Make sure to give full path for startup command and test the command in terminal before adding!**

## Bonus :tada:

Here are some Good GIFs made by **[adi1090x](https://github.com/adi1090x/plymouth-themes)**, Just to Get Started!

## Contributing:
* Please feel free to Suggest improvements bugs by creating an issue.
* PRs are always welcome

## Brought to You by:
* Pranjal Joshi