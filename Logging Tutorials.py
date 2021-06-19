#  Logging in Python is use  to log any type of error, information, status etc. for our understanding or reference. Logging runs along with the script, Infact it is a prst of script.

from logging import *
from datetime import datetime
import socket

hostname = socket.gethostname()
log_time = datetime.now().strftime("%d-%B-%Y_%A_%I-%m_%p")

# Levels of Log:
# Not Set  = 0
# Debug    = 10
# Info     = 20
# Warning  = 30  (default)
# Error    = 40
# Critical = 50

# Default level of logging is 30. Nothing befor level 30 will be logged if level is not specified. You have to manually specify the level,
# like 20 if you also wish to capture info logs.

# So here in the below log call function debug will not generate output but warning will because of the level criteria
# debug('This is debug')
# warning('This is Warning')

#  Here we create a basic configuraation for the logger. It is like settings that contains the following info:

#  filename=  is the name if the file you wish to create in .log format.
#  level=     as we know the default level is 30 (warning) so if you wish to start logging from debug use level. 
#  filemode=  the default filemode is append but you can use write mode if you wish to overwrite new logs.
#  style=     this is used in writing information in format. Default style is % but use of { makes the process easy.
#  format=    is used to provide the logger what all information a logger is suppose to log in a file like line no, name, message, time, etc

basicConfig(filename=f"SoftLogs__{log_time}.log", level=DEBUG, filemode='w', style='{', 
            format='\n==============================\nline: {lineno} -- {name} -- {asctime}{message}',datefmt="%d-%B-%Y - %A - %I:%m %p")

# Default user name is root os to get your custom username or ip address you can use getLogger and put it in a variable logger
logger = getLogger(hostname +"--"+socket.gethostbyname(hostname))

logger.debug('\nThis is debug\n'+("="*30))
logger.info("\nThis is Infromation\n"+("="*30))
logger.warning('\nThis is Warning\n'+("="*30))

# Now here we will try to capture the error thrown by the system without the code crashing using try and Except block.

def test(a,b):
    try:
        div = a/b
    except Exception as e:
        print ("Program Executed Successfully")
        logger.exception('\nError occurred during the process = '+str(e)+'\n'+("="*30))

test(20,0)

logger.warning('\nThis is Warning\n'+("="*30))

# This is almost everything needed in logs in Python.

