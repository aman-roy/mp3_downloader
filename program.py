#!/usr/bin/env python3
# A python to download a song or a list of songs.
# create by Aman Roy
# Creation Date : 18-Feb-2016
# Python version used : - Python 3.4.3+ (ported for python2)
# Please use right spelling to avoid errors
# All licence belongs to authour.

# import all the library used
import re
import urllib
import os
import sys


# determine python version
version = sys.version_info[0]


# set user_input for correct version
if version == 2:
    user_input = raw_input
    import urllib2
else:
    user_input = input
    import urllib.request
    import urllib.parse


# clear the terminal screen
def screen_clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# function to retrieve video title from provided link
def video_title(url):
    if version == 3:  # if using python 3.x
        try:
            webpage = urllib.request.urlopen(url).read()
            title = str(webpage).split('<title>')[1].split('</title>')[0]
        except:
            title = 'Youtube Song'
    else:
        try:
            webpage = urllib2.urlopen(url).read()
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
    [3] Download from the youtube link
    [4] Download from a list of youtube links
    Press any other key from keyboard to exit''')
    
    choice = user_input('>>> ')
    return str(choice)


# download from a list
def name_list_download():
    fileName = user_input('fileName(with extension): ')  # get the file name to be opened
    
    # find the file and set fhand as handler
    try:
        fhand = open(fileName, 'r')
    except IOError:
        print('File does not exist')
        exit(1)

    if version == 3:  # if using python 3.x
        for songs in fhand:
            query_string = urllib.parse.urlencode({'search_query' : songs})
            html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                    
            # generate a download link that can grab the audio file using youtube2mp3 API
            downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video=' + 'http://www.youtube.com/watch?v=' + search_results[0]
            # why do we have this variable being created?
            downloadLink = songs + ':' + downloadLinkOnly  # song name and link in a single file to save it in the file safely
                     
            try:
                print('Downloading %s' % songs) 
                # code a progress bar for visuals?? this way is more portable than wget
                urllib.request.urlretrieve(downloadLinkOnly, filename='%s.mp3' % songs)  # download the file in the working directory
                urllib.request.urlcleanup()  # clear the cache created by urlretrieve
            except:
                print('Error downloading %s' % songs)
        fhand.close()

    else:  # if using python 2.x
        for songs in fhand:
            query_string = urllib.urlencode({'search_query': songs})
            html_content = urllib2.urlopen('http://www.youtube.com/results?' + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read())

            # generate a download link that can grab the audio file using youtube2mp3 API
            downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video=' + 'http://www.youtube.com/watch?v=' + search_results[0]
            # why do we have this variable being created?
            downloadLink = songs + ':' + downloadLinkOnly  # song name and link in a single file to save it in the file safely

            try:
                print('Downloading %s' % songs)
                # code a progress bar for visuals??
                urllib.urlretrieve(downloadLinkOnly, filename='%s.mp3' % songs)  # download the file in the working directory
                urllib.urlcleanup() # clear the cache created by urlretrieve
            except:
                print('Error downloading %s' % songs)
        fhand.close()


# download directly with a song name
def name_download():
    song = user_input('Enter the song name: ')  # get the song name from user
    
    if version == 3:  # if using python 3.x
        # try to get the search result and exit upon error
        try:
            query_string = urllib.parse.urlencode({"search_query" : song})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        except:
            print('Network Error')
            exit(1)

        # generate a download link that can be used to get the audio file using youtube2mp3 API
        downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video=' + 'http://www.youtube.com/watch?v=' + search_results[0]
        try:
            print('Downloading %s' % song)
            # code a progress bar for visuals? this way is more portable than wget
            urllib.request.urlretrieve(downloadLinkOnly, filename='%s.mp3' % song)
            urllib.request.urlcleanup()  # clear the cache created by urlretrieve
        except:
            print('Error downloading %s' % song)
            exit(1)

    else:  # if using python 2.x
        
        try:
            query_string = urllib.urlencode({'search_query': song})
            html_content = urllib2.urlopen('http://www.youtube.com/results?' + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read())
        except:
            print('Network Error')
            exit(1)

        # generate a download link that can grab the audio file using youtube2mp3 API
        downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video=' + 'http://www.youtube.com/watch?v=' + search_results[0]
        try:
            print('Downloading %s' % song)
            # code a progress bar for visuals?
            urllib.urlretrieve(downloadLinkOnly, filename='%s.mp3' % song)
            urllib.urlcleanup() # clear the cache created by urlretrieve
        except:
            print('Error downloading %s' % song)
            exit(1)


# download directly with a youtube link
def link_download():
    print('Enter full youtube link (case sensitive)')
    print('e.g. - https://www.youtube.com/watch?v=rYEDA3JcQqw')
    youtubeLink = user_input('>>> ')
    downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video=' + youtubeLink

    if version == 3:  # if using python 3.x    
        try:
            song = video_title(youtubeLink)
            print('Downloading %s' % song)
            # code a progress bar for visuals? this way is more portable than wget
            urllib.request.urlretrieve(downloadLinkOnly, filename='%s.mp3' % song)
            urllib.request.urlcleanup()  # clear the cache created by urlretrieve
        except:
            print('Error downloading %s' % song)
            exit(1)
    else:  # if using python 2.x
        try:
            song = video_title(youtubeLink)
            print('Downloading %s' % song)
            # code a progress bar for visuals?
            urllib.urlretrieve(downloadLinkOnly, filename='%s.mp3' % song)
            urllib.urlcleanup() # clear the cache created by urlretrieve
        except:
            print('Error downloading %s' % song)
            exit(1)


# download songs with a list of youtube links
def link_list_download():
    fileName = user_input('fileName(with exension): ')  # get the file name to be opened
    
    # find the file and set fhand as handler
    try:
        fhand = open(fileName, 'r')
    except IOError:
        print('File does not exist')
        exit(1)
    
    if version == 3:
        for links in fhand:
            try:
                downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video=' + links
                song = video_title(links)
                print('Downloading %s' % song)
                # code a progress bar for visuals? this way is more portable than wget
                urllib.request.urlretrieve(downloadLinkOnly, filename='%s.mp3' % song)
                urllib.request.urlcleanup()  # clear the cache created by urlretrieve
            except:
                print('Error downloading %s' % song)
        fhand.close()
    
    else:  # if using python 2.x
        for links in fhand:
            try:
                downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video=' + links
                song = video_title(links)
                print('Downloading %s' % song)
                # code a progress bar for visuals?
                urllib.urlretrieve(downloadLinkOnly, filename='%s.mp3' % song)
                urllib.urlcleanup()  # clear the cache created by urlretrieve
            except:
                print('Error downloading %s' % song)
        fhand.close()


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
                name_list_download()
            elif choice == '2':
                single_name_download()
            elif choice == '3':
                link_download()
            elif choice == '4':
                link_list_download()
        except NameError:
            exit(1)
    except KeyboardInterrupt:
        exit(1)

if __name__ == '__main__':
    main()  # run the main program
    exit(0)  # exit the program
