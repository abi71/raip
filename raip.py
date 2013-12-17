#!/usr/bin/python
#
# raip.py 1.0 - Report Associate IP
# By abi <l0g.bima@gmail.com> (http://rndc.or.id, http://gxrg.org, http://abi71.wordpress.com) 
#
# Public License aja bro... :D
#

#####################
## READ ME FIRST ! ##
#####################
#
# Why ? 
#    Confusing with Public IP always changed?, RaIP is alternative solution such as dyndns 
#    (remote access) but without domain, just reporting current public ip address to your email. 
#
# How ? 
#    Don't need root, just give executable permissions. 
#    Execute via commandline (ex: python raip.py or ./raip.py)
#    or running as cron job.
#
# Description Configuration ?
# 
# 1.A. BOT_SERVER_HOST
#    
#    Desc:
#      SMTP host 
#    Example:
#      BOT_SERVER_HOST = "smtp.gmail.com"
# 
# 1.B. BOT_SERVER_PORT
#    
#    Desc:
#      SMTP port number
#    Example:
#      BOT_SERVER_HOST = "587"
# 
# 1.C. BOT_SERVER_USER
#    
#    Desc:
#      specify the username account, doesn't need the domain mail server
#    Example:
#      BOT_SERVER_USER = "rndc"
# 
# 1.D. BOT_SERVER_PASSWD
#    
#    Desc:
#      specify the password account
#    Example:
#      BOT_SERVER_PASSWD = "rndcpass"
# 
# 2.A. MSG_DST
#    
#    Desc:
#      specify the destination mails, you can specify multiple destination separated by comma
#    Example:
#      MSG_DST = "me@mail.com" or MSG_DST = "me@mail.com,l0g.bima@gmail.com"
# 
# 2.B. MSG_SUBJECT
#    
#    Desc:
#      fill the message subject
#    Example:
#      MSG_SUBJECT = "[IPCHECK] router.rndc.or.id"
# 
# 2.C. MSG_CONTENT
#    
#    Desc:
#      fill the message content
#    Example:
#      MSG_CONTENT = "router.rndc.or.id assigned to"
# 
# 3.A. LOG_FILE_PATH
#    
#    Desc:
#      specify the log files path
#    Example:
#      LOG_FILE_PATH = "" or LOG_FILE_PATH = "/tmp"
# 
# 3.B. LOG_FILE_NAME
#    
#    Desc:
#      specify the log file name, all activity of bot written to this file
#    Example:
#      LOG_FILE_NAME = "raip.log"
#
# 3.C. LOG_FILE_IPTEMP
#    
#    Desc:
#      specify the temporary file name, this file is used to store temporary ip address
#    Example:
#      LOG_FILE_NAME = "raip.log"
#



###############
## LIBRARIES ##
###############

import os
import re
import sys
import socket
import smtplib
import urllib
import datetime
import HTMLParser
HTParse = HTMLParser.HTMLParser()

################### 
## SERVER CONFIG ##
###################

BOT_SERVER_HOST   = "?"
BOT_SERVER_PORT   = "?"
BOT_SERVER_USER   = "?"
BOT_SERVER_PASSWD = "?"


####################
## MESSAGE CONFIG ##
####################

MSG_DST     = "?"
MSG_SUBJECT = "?"
MSG_CONTENT = "?"

################
## LOG CONFIG ##
################

LOG_FILE_PATH = ""
LOG_FILE_NAME = "raip.log"
LOG_FILE_IPTEMP = "raip.tmp" 

##############
## THE CODE ##
##############

def checkMyIp():
	try:
		gotIP = False
		result = urllib.urlopen("http://bot.whatismyipaddress.com/")
		result = result.readlines()

		for i in result:
			return ("%s" % (i))
			gotIP = True
			break
	
		if not gotIP:
			return None
	except IOError:
		return None

# current time
currenttime = ("%s " % datetime.datetime.now())
			
# open log & temporary files
if os.path.exists("%s%s" % (LOG_FILE_PATH,LOG_FILE_NAME)):
	LOPEN = open("%s%s" % (LOG_FILE_PATH,LOG_FILE_NAME), "a+")
else:
	LOPEN = open("%s%s" % (LOG_FILE_PATH,LOG_FILE_NAME), "w+")

if os.path.exists("%s%s" % (LOG_FILE_PATH,LOG_FILE_IPTEMP)):
	TOPEN = open("%s%s" % (LOG_FILE_PATH,LOG_FILE_IPTEMP), "r")
else:
	TOPEN = open("%s%s" % (LOG_FILE_PATH,LOG_FILE_IPTEMP), "w+")


# current & old ip's	
ipcurrent = checkMyIp()
ipold = TOPEN.read().strip()

if ipcurrent:	
	# compare curent & old ip's
	if ipcurrent != ipold:
		# put the current ip to message content
		MSG_CONTENT = ("%s %s" % (MSG_CONTENT,ipcurrent))
		# reopen old ip, set flag to w+
		TOPEN = open("%s%s" % (LOG_FILE_PATH,LOG_FILE_IPTEMP), "w+")
	
		try:
			server = smtplib.SMTP(BOT_SERVER_HOST,BOT_SERVER_PORT) 
			server.ehlo()
			server.starttls()
			server.login(BOT_SERVER_USER,BOT_SERVER_PASSWD)
			for msgdst in MSG_DST.split(","):
				mimetxt = 'From: ' + BOT_SERVER_USER + '\nSubject: ' + MSG_SUBJECT + '\n' + 'Message:\n'+ MSG_CONTENT
				server.sendmail(BOT_SERVER_USER,msgdst,mimetxt)
				LOPEN.write(mimetxt)
				LOPEN.write("\nInfo: Message has been delivered at %s\n\n" % (currenttime))
			TOPEN.write(ipcurrent)
			LOPEN.close()
			TOPEN.close()
			server.quit()
		except KeyboardInterrupt:
			sys.exit()
		except smtplib.SMTPAuthenticationError:
			LOPEN.write("%s ERROR: The username or password your entered is incorrect\n\n" % (currenttime))
			LOPEN.close()
		except socket.error:
			LOPEN.write("%s ERROR: Network is unreachable\n\n" % (currenttime))
			LOPEN.close()
	else:
		LOPEN.write("%s INFO: Congrats, IP isn't changed!\n\n" % (currenttime))
		LOPEN.close()
else:
	LOPEN.write("%s ERROR: IP check is failed\n\n" % (currenttime))
	LOPEN.close()
	

### EOF ###
