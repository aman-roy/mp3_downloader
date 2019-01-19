# Mp3_Downloader
---
A simple python script from which you can download the songs by just entering the name. You can also download by entering a list of name, youtube link or list of youtube links.

You can try that online. Here is the link ->  http://mp3.amanroy.me


[![asciicast](https://asciinema.org/a/222455.svg)](https://asciinema.org/a/222455)

# Usage

> Make sure you have python and youtube-dl installed.

### Install youtube-dl for UBUNTU
```bash
$ sudo apt-get install youtube-dl
```
### Install youtube-dl for windows
> For windows download [youtube-dl.exe](https://yt-dl.org/latest/youtube-dl.exe) file and copy it in the directory.
### For other operating systems
> [See this](https://rg3.github.io/youtube-dl/download.html) 


### Install ffprobe ubuntu
```bash
$ sudo add-apt-repository ppa:mc3man/trusty-media
$ sudo apt-get install ffmpeg
```


### Run program
```bash
$ ./program.py 
```

### passing arguments

##### Single song download
```bash
$ ./program.py -s "<song_name>"
```
```bash
$ ./program.py --single "<song_name>"
```

##### List of songs download 

```bash
$ ./program.py -l <filename_with_extension>
```
```bash
$ ./program.py --list <filename_with_extension>
```

# Contributors

[Check Here](https://github.com/aman-roy/mp3_downloader/graphs/contributors)

# Note:

> This program is tested on Ubuntu 16.04/18.04 LTS

# Disclaimer

Downloading copyrighted material may be illegal in your country. Use at your own risk.
