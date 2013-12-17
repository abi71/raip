#####################
## READ ME FIRST ! ##
#####################

Why ? 
    Confusing with Public IP always changed?, RaIP is alternative solution such as dyndns 
    (remote access) but without domain, just reporting current public ip address to your email. 

How ? 
    Don't need root, just give executable permissions. 
    Execute via commandline (ex: python raip.py or ./raip.py)
    or running as cron job.

Description Configuration ?
 
1.A. BOT_SERVER_HOST
    
    Desc:
      SMTP host 
    Example:
      BOT_SERVER_HOST = "smtp.gmail.com"
 
1.B. BOT_SERVER_PORT
    
    Desc:
      SMTP port number
    Example:
      BOT_SERVER_HOST = "587"
 
1.C. BOT_SERVER_USER
    
    Desc:
      specify the username account, doesn't need the domain mail server
    Example:
      BOT_SERVER_USER = "rndc"
 
1.D. BOT_SERVER_PASSWD
    
    Desc:
      specify the password account
    Example:
      BOT_SERVER_PASSWD = "rndcpass"
 
2.A. MSG_DST
    
    Desc:
      specify the destination mails, you can specify multiple destination separated by comma
    Example:
      MSG_DST = "me@mail.com" or MSG_DST = "me@mail.com,l0g.bima@gmail.com"
 
2.B. MSG_SUBJECT
    
    Desc:
      fill the message subject
    Example:
      MSG_SUBJECT = "[IPCHECK] router.rndc.or.id"
 
2.C. MSG_CONTENT
    
    Desc:
      fill the message content
    Example:
      MSG_CONTENT = "router.rndc.or.id assigned to"
 
3.A. LOG_FILE_PATH
    
    Desc:
      specify the log files path
    Example:
      LOG_FILE_PATH = "" or LOG_FILE_PATH = "/tmp"
 
3.B. LOG_FILE_NAME
    
    Desc:
      specify the log file name, all activity of bot written to this file
    Example:
      LOG_FILE_NAME = "raip.log"

3.C. LOG_FILE_IPTEMP
    
    Desc:
      specify the temporary file name, this file is used to store temporary ip address
    Example:
      LOG_FILE_NAME = "raip.log"

