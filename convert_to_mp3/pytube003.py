#!/usr/bin/env python
# PyTube - Small script to download, convert, and extract audio out of Youtube Videos.
# Written by Marcos Rodriguez - <marcosrdz@gmail.com> - License: GPLv3
import sys,time,platform,os

def op1():
	os.system('clear')
	print "Current Directory: " + os.path.abspath(os.path.curdir)
	changedirq=raw_input("Do you wish to change to another directory? Yes/No: ")
	changedirq=changedirq.lower()
	if changedirq=="yes":
        	wherechangeto=raw_input("Please type the full path of the folder you wish to access: ")
                if os.path.isdir(wherechangeto):
                        for f in wherechangeto:
                                os.chdir(wherechangeto)
                else:
                        print "The specified folder does not exist."
                        time.sleep(3)
                        op1()
        elif changedirq=="no":
                pass
	accountwant=raw_input("Do you wish to use your YouTube account? Yes/No: ")
	accountwant=accountwant.upper()
	if accountwant=="NO":
		itemdown=raw_input("Please type the full URL of the video you wish to download: ")
		os.system("youtube-dl -t " + itemdown)
		print "\n\nDone :-) "
		optionsexec()
	elif accountwant=="YES":
		userid=raw_input("Please type your username: ")
		while userid=="":
			userid=raw_input("Please type your username: ")
		password=raw_input("Please type your password: ")
		while password=="":
			 password=raw_input("Please type your password: ")
		itemdown=raw_input("Please type the full URL of the video you wish to download: ")
		while itemdown=="":
			 itemdown=raw_input("Please type the full URL of the video you wish to download: ")
		os.system("youtube-dl -t -u " + userid + " -p " + password + " " + itemdown)
		print "\n\nDone :-) "
		optionsexec()
	else:
		print "The answer you have given is incorrect. Please choose either Yes or No."
		time.sleep(2)
		op1()
	convertnow=raw_input("\n\nDo you wish to convert the video now? ")
	convertnow=convertnow.upper()
	if convertnow=="YES":
		op2()
	else:
		pass
	time.sleep(5)
	os.system('clear')
	optionsexec()

def op2():
	os.system('clear')
	print "Current directory: " + os.path.abspath(os.path.curdir)
	changedirq=raw_input("Do you wish to change to another directory? Yes/No: ")
	changedirq=changedirq.lower()
	if changedirq=="yes":
		wherechangeto=raw_input("Please type the full path of the folder you wish to access: ")
		if os.path.isdir(wherechangeto):
			for f in wherechangeto:
				os.chdir(wherechangeto)
		else:
			print "The specified folder does not exist."
			time.sleep(3)
			op2()
	elif changedirq=="no":
		pass
	directory=os.path.abspath(os.path.curdir)+"/"
	print "\n\nThe .FLV files found on this directory are:\n===============================================\n"
	for f in os.listdir(directory):
		if f.endswith('.flv'):
			print f+"\n"
	print "\n===============================================\n"
	convfile=raw_input("Please specify the name of the .flv file you wish to convert? ")
	if not(convfile.endswith('.flv')):
		print "\nThe specified file is not a compatible file."
		time.sleep(2)
		op2()
	elif os.path.isfile(directory+convfile):
		print "\nConverting...Please Wait.."
		os.system("mencoder " + directory+convfile + "  -ofps 15 -vf scale=300:-2 -oac lavc -ovc lavc -lavcopts vcodec=msmpeg4v2:acodec=mp3:abitrate=64 -o " + directory+convfile+".avi > /dev/null 2>&1")
		print "\n\nConversion has finished :-). Your file will be locaed in the same folder as the original source."
		extfile=raw_input("\n\nDo you wish to extract audio of this video? Yes/No: ")
		extfile=extfile.upper()
		if extfile=="YES":
			finalfile=directory+convfile
			formatsound=raw_input("\n\nWich format do you wish to convert the extract audio into? mp3/ogg/wav: ")
			formatsound=formatsound.upper()
			if formatsound=="MP3":
				os.system("mplayer -dumpaudio " + finalfile + " -dumpfile " + finalfile + ".mp3 > /dev/null 2>&1")
				print "\n\nDone :-)"
				playnow=raw_input("Do you wish to listen to the extracted sound now? Yes/No: ")
				playnow=playnow.upper()
				if playnow=="NO":
					pass
				elif playnow=="YES":
					print "\nPress Enter if you wish to stop playing the file."
					os.system("mplayer " + finalfile + ".mp3 > /dev/null 2>&1")
				else:
					pass
				time.sleep(2)
			elif formatsound=="WAV":
				os.system('mplayer -ao pcm ' + finalfile + " > /dev/null 2>&1" )
				os.system("mv " + directory +"audiodump.wav " + finalfile + ".wav")
				print "\n\nDone :-)"
				playnow=raw_input("Do you wish to listen to the extracted sound now? Yes/No: ")
                                playnow=playnow.upper()
                                if playnow=="NO":
                                        pass
                                elif playnow=="YES":
                                        print "\nPress Enter if you wish to stop playing the file."
                                        os.system("mplayer " + finalfile + ".wav > /dev/null 2>&1")
                                else:
                                        pass
				time.sleep(2)
			elif formatsound=="OGG":
				os.system('mplayer -ao pcm ' + finalfile + " > /dev/null 2>&1")
				os.system('oggenc -q5 ' + directory+"audiodump.wav" + " -o " + finalfile + ".ogg > /dev/null 2>&1")
				os.system("rm " + directory+"audiodump.wav") 
				print "\n\nDone :-)"
				playnow=raw_input("Do you wish to listen to the extracted sound now? Yes/No: ")
                                playnow=playnow.upper()
                                if playnow=="NO":
                                        pass
                                elif playnow=="YES":
                                        print "\nPress Enter if you wish to stop playing the file."
                                        os.system("mplayer " + finalfile + ".ogg > /dev/null 2>&1")
                                else:
                                        pass
				time.sleep(2)
			else:
				print "\n\nThe answer you have given is incorrent, I will send you back to the main menu."
				time.sleep(2)
				optionsexec()
		if extfile=="NO":
			os.system('clear')
			optionsexec()
    	elif not(os.path.isfile(convfile)):
		print "\n\nThe specified file does not exist."
		time.sleep(1)
		op2()
	time.sleep(2)
	os.system('clear')
	optionsexec()

def op3():
	os.system('clear')
        print "Current directory: " + os.path.abspath(os.path.curdir)
        changedirq=raw_input("Do you wish to change to another directory? Yes/No: ")
        changedirq=changedirq.lower()
        if changedirq=="yes":
                wherechangeto=raw_input("Please type the full path of the folder you wish to access: ")
                if os.path.isdir(wherechangeto):
                        for f in wherechangeto:
                                os.chdir(wherechangeto)
                else:
                        print "The specified folder does not exist."
                        time.sleep(3)
                        op3()
        elif changedirq=="no":
                pass
	wichformat=raw_input("\n\nWich format you wish to convert the video into? iPod/3GP: ")
	wichformat=wichformat.upper()
	if wichformat=="IPOD":
		directory=os.path.abspath(os.path.curdir)+"/"
        	print "\n\nThe .FLV files found on this directory are:\n\n"
      		for f in os.listdir(directory):
                	if f.endswith('.flv'):
                        	print f+"\n"
        	convfile=raw_input("Please specify the name of the .flv file you wish to convert? ")
        	if os.path.isfile(directory+convfile):
                	os.system("ffmpeg -i " + directory+convfile + " -f mp4 -vcodec mpeg4 -maxrate 1000 -b 700 -qmin 3 -qmax 5 -bufsize 4096 -g 300 -acodec aac -ab 192 -s 320x240 -aspect 16:9")
                	print "\n\nConversion has finished :-). Your file will be locaed in the same folder as the original source."	
	elif wichformat=="3GP":
		directory=os.path.abspath(os.path.curdir)+"/"
                print "\n\nThe .FLV files found on this directory are:\n\n"
                for f in os.listdir(directory):
                        if f.endswith('.flv'):
                                print f+"\n"
			if f.endswith('.mpg'):
				print f+"\n"
			if f.endswith('.avi'):
				print f+"\n"
                convfile=raw_input("Please specify the name of the .flv file you wish to convert? ")
                if os.path.isfile(directory+convfile):
                        os.system("ffmpeg -i " + directory+convfile + " -s qcif -vcodec h263 -acodec mp3 -ac 1 -ar 8000 -ab 32 -y " + directory+convfile + ".3gp")
                        print "\n\nConversion has finished :-). Your file will be locaed in the same folder as the original source."
def op4():
	os.system('clear')
	print "Current directory: " + os.path.abspath(os.path.curdir)
	changedirq=raw_input("Do you wish to change to another directory? Yes/No: ")
	changedirq=changedirq.lower()
	if changedirq=="yes":
		wherechangeto=raw_input("Please type the full path of the folder you wish to access: ")
		if os.path.isdir(wherechangeto):
			for f in wherechangeto:
				os.chdir(wherechangeto)
		else:
			print "The specified folder does not exist."
			time.sleep(3)
			op4()
	elif changedirq=="no":
		pass
	directory=os.path.abspath(os.path.curdir)+"/"
	print "\n\nThe .FLV files found on this directory are:\n===============================================\n"
	for f in os.listdir(directory):
		if f.endswith('.flv'):
			print f+"\n"
	print "\n===============================================\n"
	convfile=raw_input("Please specify the name of the .flv file you extract audio from? ")
	if os.path.isfile(directory+convfile):
                finalfile=directory+convfile
                formatsound=raw_input("\n\nWich format do you wish to convert the extract audio into? mp3/ogg/wav: ")
                formatsound=formatsound.upper()
                if formatsound=="MP3":
                                os.system("mplayer -dumpaudio " + finalfile + " -dumpfile " + finalfile + ".mp3 > /dev/null 2>&1")
                                print "\n\nDone :-)"
                                playnow=raw_input("Do you wish to listen to the extracted sound now? Yes/No: ")
                                playnow=playnow.upper()
                                if playnow=="NO":
                                        pass
                                elif playnow=="YES":
                                        print "\nPress Enter if you wish to stop playing the file."
                                        os.system("mplayer " + finalfile + ".mp3 > /dev/null 2>&1")
                                else:
                                        pass
                                time.sleep(2)
        	elif formatsound=="WAV":
                                os.system('mplayer -ao pcm ' + finalfile + " > /dev/null 2>&1" )
                                os.system("mv " + directory +"audiodump.wav " + finalfile + ".wav")
                                print "\n\nDone :-)"
                                playnow=raw_input("Do you wish to listen to the extracted sound now? Yes/No: ")
                                playnow=playnow.upper()
                                if playnow=="NO":
                                        pass
                                elif playnow=="YES":
                                        print "\nPress Enter if you wish to stop playing the file."
                                        os.system("mplayer " + finalfile + ".wav > /dev/null 2>&1")
                                else:
                                        pass
                                time.sleep(2)
                elif formatsound=="OGG":
                                os.system('mplayer -ao pcm ' + finalfile + " > /dev/null 2>&1")
                                os.system('oggenc -q5 ' + directory+"audiodump.wav" + " -o " + finalfile + ".ogg > /dev/null 2>&1")
                                os.system("rm " + directory+"audiodump.wav")
                                print "\n\nDone :-)"
                                playnow=raw_input("Do you wish to listen to the extracted sound now? Yes/No: ")
                                playnow=playnow.upper()
                                if playnow=="NO":
                                        pass
                                elif playnow=="YES":
                                        print "\nPress Enter if you wish to stop playing the file."
                                        os.system("mplayer " + finalfile + ".ogg > /dev/null 2>&1")
                                else:
                                        pass

                        	time.sleep(2)
	        elif not(os.path.isfile(convfile)):
				print "\n\nThe specified file does not exist."
				time.sleep(1)
				op4()
	time.sleep(2)
	os.system('clear')
	optionsexec()
        
def op5():
	os.system('clear')
	print "\n\n\n"
	print "======================================================================================================="
	print "PyTube is a small script to download, convert and extract audio out of YouTube videos.\nThis script was written by Marcos Rodriguez \
and it is licensed under the GPLv3.\n\nEmail: marcosrdz@gmail.com\nHomepage: http://www.bashterritory.com/pytube\n\n"
	print "Your Operating System: " + platform.system()
	print "Your System Architecture: " + platform.machine() + "\n" 
	if os.path.isfile("/usr/bin/ffmpeg"):
		print "FFMPEG found: Yes"
	else:
		print "FFMPEG found: No"
	if os.path.isfile("/usr/bin/mplayer"):
                print "Mplayer found: Yes"
        else:
                print "Mplayer found: No"
	if os.path.isfile("/usr/bin/mencoder"):
		print "Mencoder found: Yes"
	else:
		print "Mencoder found: No"
	if os.path.isfile("/usr/bin/oggenc"):
                print "OGGEnc found: Yes"
        else:
                print "OGGEnc found: No"
	if os.path.isfile("/usr/bin/youtube-dl"):
        	print "Youtube-DL found: Yes"
	else:
       		print "Youtube-DL found: No"
	print \
"======================================================================================================="
	time.sleep(10)
	os.system('clear')
	optionsexec()

def optionsexec():
	os.system('clear')
        print "==============================================================\n            PyTube - Version \
0.0.3 - BETA\n=============================================================="
        print "Select wich task you wish to execute:\n\n"
	opcion1='1) Download Videos'
	opcion2='2) Convert a Downloaded Video to MPG'
	opcion3='3) Convert a Downloaded Video to iPod/3GP format'
	opcion4='4) Extract audio'
	opcion5='5) About'	
	opcion6='6) Quit'
	print "%s\n%s\n%s\n%s\n%s\n%s\n" %(opcion1,opcion2,opcion3,opcion4,opcion5,opcion6)
	optionsask()
def optionsask():
	escoger=raw_input("Choose the task you wish to execute by typing the number next to it: ")
	if escoger=="6":
		print "Good bye :-)"
		time.sleep(1)
		os.system('clear')
		sys.exit()
	if escoger=="5":
		op5()
	if escoger=="4":
		op4()
	if escoger=="2":
		op2()
	if escoger=="1":
		op1()
	if escoger=="3":
		op3()
	else:
		optionsask()
os.system('clear')
if platform.system()=="Windows":
	print "THIS VERSION IS OPTIMIZED ONLY FOR LINUX! THIS APPLICATION FAILS COMPLETELY UNDER WINDOWS!"
	time.sleep(5)
if not(os.path.isfile("/usr/bin/oggenc")) and not(os.path.isfile("/usr/bin/mplayer")) and not(os.path.isfile("/usr/bin/ffmpeg")) and not(os.path.isfile("/usr/bin/youtube-dl")) and not(os.path.isfile("/usr/bin/mencoder")):
        print """You have none of the needed tools installed. In order to obtain these visit their respective websites:
====================================================================================================================
FFMPEG: http://ffmpeg.mplayerhq.hu

Mplayer: http://www.mplayerhq.hu

OGGEnc: http://www.vorbis.com

Youtube-DL: http://www.arrakis.es/~rggi3/youtube-dl/

Mencoder: http://www.mplayerhq.hu/
====================================================================================================================
"""

	time.sleep(5)
	optionsexec()
if os.path.isfile("/usr/bin/ffmpeg"):
	print "FFMPEG found: Yes"
else:
        print "FFMPEG found: No\nYou can obtain FFMPEG from http://ffmpeg.mplayerhq.hu"
	time.sleep(5)
if os.path.isfile("/usr/bin/mplayer"):
        print "Mplayer found: Yes"
else:
        print "Mplayer found: No\nYou can obtain Mplayer from http://www.mplayerhq.hu"
	time.sleep(5)
if os.path.isfile("/usr/bin/mencoder"):
        print "Mencoder found: Yes"
else:
        print "Mencoder found: No\nYou can obtain Mencoder from http://www.mplayerhq.hu"
        time.sleep(5)
if os.path.isfile("/usr/bin/oggenc"):
        print "OGGEnc found: Yes"
else:
        print "OGGEnc found: No\nYou can obtain OGGEnc from http://www.vorbis.com"
	time.sleep(5)
if os.path.isfile("/usr/bin/youtube-dl"):
	print "Youtube-DL found: Yes"
else:
	print "Youtube-DL found: No\nYou can obtain Youtube-DL from http://www.arrakis.es/~rggi3/youtube-dl"
	time.sleep(5)
optionsexec()
