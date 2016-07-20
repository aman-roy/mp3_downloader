#!/usr/bin/env python
# A python to download a song or a list of songs.
# create by Aman Roy
# Creation Date : 18-Feb-2016
# Python version used : - Python 3.4.3+ (ported for python2)
# Please use right spelling to avoid errors
# All licence belongs to authour.

# import all the library used
import re, urllib, os, sys

# determine python version
version = sys.version_info[0]

# set user_input and import modules for correct version of python
if version == 2:  # python 2.x
    user_input = raw_input
    import urllib2
    urlopen = urllib2.urlopen  # open a url
    encode = urllib.urlencode  # encode a search line
    retrieve = urllib.urlretrieve  # retrieve url info
    cleanup = urllib.urlcleanup()  # cleanup url cache

else:  # python 3.x
    user_input = input
    import urllib.request
    import urllib.parse
    urlopen = urllib.request.urlopen
    encode = urllib.parse.urlencode
    retrieve = urllib.request.urlretrieve
    cleanup = urllib.request.urlcleanup()



# clear the terminal screen
def screen_clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# function to retrieve video title from provided link
def video_title(url):
    try:
        webpage = urlopen(url).read()
        title = str(webpage).split('<title>')[1].split('</title>')[0]
    except:
        title = 'Youtube Song'

    return title

# the intro to the script
def intro():
    print('''Created by Aman Roy
    FB:- amanroy007
    Email:- royaman8757@gmail.com''')


# find out what the user wants to do
def prompt():
    # userr prompt to ask mode
    print ('''\t\t\t Select A mode
    [1] Download from a list
    [2] Download from direct entry
    Press any other key from keyboard to exit''')

    choice = user_input('>>> ')
    return str(choice)


# download from a list of songs or links
def list_download():
    fileName = user_input('fileName(with extension): ')  # get the file name to be opened

    # find the file and set fhand as handler
    try:
        fhand = open(fileName, 'r')
    except IOError:
        print('File does not exist')
        exit(1)

    # Iterating over the lines in file
    for song in fhand:
        single_download(song)

    fhand.close()


# download directly with a song name or link
def single_download(song=None):
    if not(song):
        song = user_input('Enter the song name or youtube link: ')  # get the song name from user

        # try to get the search result and exit upon error
    try:
        query_string = encode({"search_query" : song})
        html_content = urlopen("http://www.youtube.com/results?" + query_string)

        if version == 3:  # if using python 3.x
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        else:  # if using python 2.x
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read())
    except:
        print('Network Error')
        return None

    # generate a download link that can be used to get the audio file using youtube2mp3 API
    downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video=' + 'http://www.youtube.com/watch?v=' + search_results[0]
    try:
        print('Downloading %s' % song)
        # code a progress bar for visuals? this way is more portable than wget
        retrieve(downloadLinkOnly, filename='%s.mp3' % song)
        cleanup  # clear the cache created by urlretrieve
    except:
        print('Error downloading %s' % song)
        return None

# program exit
def exit(code):
    print('\nExiting....')
    print('\nHave a good day.')
    sys.exit(code)


# main guts of the program
def main():
    try:
        screen_clear()
        intro()
        choice = prompt()

        try:
            if choice == '1':
                list_download()
            elif choice == '2':
                single_download()
        except NameError:
            exit(1)
    except KeyboardInterrupt:
        exit(1)
    exit(1)

if __name__ == '__main__':
    main()  # run the main program
    exit(0)  # exit the program
