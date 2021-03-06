<div align=center><h1>Lynx</h1></div>
<div align=center><h2>A Linux Keylogger with great features :)</h2></div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-this-tool">About this tool</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#limitations">Limitations</a></li>
    <li>
      <a href="#getting-Started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#generating-RSA-Keys">Generating RSA Keys</a></li>
        <li><a href="#configuration">Configuration</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About this tool
Lynx is a Linux Keylogger with many great features, described in the [Features](#Features) section.

Version: 2.0

_DISCLAIMER : This tool was made only for educational purposes. I strongly advise against using it on machines you don't own or in any other way that is forbidden in your country/region. I am not responsible for your actions._



## Features
- Works on Windows and Linux
- Sends logs by email or FTP
- Sends system information 
- Hybrid Encryption
- Takes screenshots and sends them
- Logs are sent every 60 seconds by default
- No X dependency
- File shredder integrated
- Persistence

## Limitations
- Needs to be run with root (Admin on Windows) permissions
- Not so stealthy

## Getting Started
### Prerequisites

You must install the dependencies before running the program:

```bash
pip3 install -r requirements.txt
```
_Note: If you are using Windows, you will need to install an additional dependency:_
```bash
pip3 install pywin32
```

### Generating RSA keys
Generate the RSA keys that will be used for encryption later on:
```bash
python3 generate_keys.py
```
By default, the keys are written to the current directory

### Configuration
1. Replace the value of "RSA_PUBLIC_KEY" in [lynx.py](lynx.py) with the content of "public_key.pem" 
2. Replace the value of "RSA_PRIVATE_KEY" in [decryptor.py](decryptor.py) with the content of "private_key.pem". You can also just set the value of the same variable to an empty string ("").
#### If you want to receive logs by email, follow these steps:
1. Set the value of "EMAIL_ADDRESS" in [lynx.py](lynx.py) to your email address.
2. Set the value of "EMAIL_PASSWORD" in [lynx.py](lynx.py) to your password.
3. If you using Gmail, just skip this step. Otherwise, change "SMTP_SERVER" in [lynx.py](lynx.py) to the SMTP server of your email provider, also change "SMTP_PORT" in the same file as needed. 
#### If you want to receive logs on your FTP server, follow these steps:
1. Set the value of "HOST" in [lynx.py](lynx.py) to your FTP server's IP Address.
2. Set the value of "PORT" in [lynx.py](lynx.py) to your FTP server's port.
3. Set the value of "USERNAME" in [lynx.py](lynx.py) to your FTP username.
4. Set the value of "PASSWORD" in in [lynx.py](lynx.py) to your FTP password.
#### That's it. Lynx is ready to go.

### Usage
Run it with Python3:
```bash
python3 lynx.py
```
Note: [decryptor.py](decryptor.py) will be decrypting your messages. Put your message in the [message.txt](message.txt) file or paste it as the value of "CIPHERTEXT", then run it; the plaintext will be printed to the screen.

## Roadmap
- [x] Replace RSA encryption with hybrid encryption 
- [x] Add Cross-platform support
- [x] Better keylogging
- [ ] Stealthier keylogging
- [x] Persistence
- [ ] Record webcam and microphone
- [ ] Take screenshots when interesting web pages open
- [ ] Record mouse and log mouseclicks
- [x] Add FTP support

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License
This project is licensed under the [GNU GPLv3](LICENSE.md) license.
<p align="right">(<a href="#top">back to top</a>)</p>
