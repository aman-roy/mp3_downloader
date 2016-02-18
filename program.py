# A python to download a song or a list of songs.
# create by Aman Roy
# Creation Date : 18-Feb-2016
# Python version used : - Python 3.4.3+
# Please use right spelling to avoid errors
# All licence belongs to authour.

# import all the library used
import urllib.request
import urllib.parse
import re
import urllib
import wget
import os

#clear the screen
os.system('clear')
os.system('cls')

# Intro
print('''Created  by Aman Roy
FB:- amanroy007
Email:- royaman8757@gmail.com''')

#user prompt to ask mode
print ('''\t\t\t Select A mode  
[1] Download from a list
[2] Download from direct entry
[3] Download from the youtube link
[4] Download from a list of youtube links
Press any other key from keyboard to exit''')
AskAQuestion = input(">>>")


# Download from a list mode
if AskAQuestion == '1':

	fileName = input("fileName(with extention): ")  # get the file name to be opened
	
	# Find the file and set fhand as handler or show the error if can't find the file
	try:
		fhand = open(fileName)
	except:
		print("Enter valid file name. File must be in the working directory")
		quit()

	# loop through the all the songs in the list to download them.
	for songs in fhand:

		# try to get the search result if can't get the query return the error and quit the program
		try:
			query_string = urllib.parse.urlencode({"search_query" : songs})
			html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
			search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
		except:
			print("Check Internet connection or check the spelling")
			quit()

		# generate a Download link that can be get the audio file using youtube2mp3 APIs.
		DownloadLinkOnly = "http://www.youtubeinmp3.com/fetch/?video="+"http://www.youtube.com/watch?v=" + search_results[0]

		DownloadLink = songs + ":" + DownloadLinkOnly #Song name and link in a single file to save it in file safely
		print (songs)                                 #Print the songs name
		
		try:
			filename = wget.download(DownloadLinkOnly)    #download the file in working directory
		except:
			print('Error..!!!')


# Download directly mode
elif AskAQuestion == '2':

	song = input("Enter the song name: ")      # get the song name from user

	# try to get the search result if can't get the query return the error and quit the program
	try:
		query_string = urllib.parse.urlencode({"search_query" : song})
		html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
		search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	except:
		print("Network Error")
		quit()

	# generate a Download link that can be get the audio file using youtube2mp3 APIs.
	DownloadLinkOnly = "http://www.youtubeinmp3.com/fetch/?video="+"http://www.youtube.com/watch?v=" + search_results[0]
	print (song)
	try:
		filename = wget.download(DownloadLinkOnly)        # download the song in working directory	
	except:
		print('Error..!!')

# Download through the link directly...
elif AskAQuestion == '3':

	print("Enter full youtube link(case sensitive)")
	print("e.g.- https://www.youtube.com/watch?v=rYEDA3JcQqw")
	youtubeLink = input('>>>')
	DownloadLinkOnly = "http://www.youtubeinmp3.com/fetch/?video=" + youtubeLink
	try:
		filename = wget.download(DownloadLinkOnly) 
	except:
		print('Error..!!!') 

# Download through a list of links in a certain file
elif AskAQuestion == '4':
	fileName = input("fileName(with extention): ")  # get the file name to be opened
	
	# Find the file and set fhand as handler or show the error if can't find the file
	try:
		fhand = open(fileName)
	except:
		print("Enter valid file name. File must be in the working directory")
		quit()
	for link in fhand:
		DownloadLinkOnly = "http://www.youtubeinmp3.com/fetch/?video=" + link
		print (link)
		try:
			filename = wget.download(DownloadLinkOnly) 
		except:
			print('Error..!!!') 


# flush out.....
else:
	print("\nExiting.......")

print("\nHave a good day.")
