import socket

class Bot:

    id = 0
    oauth_token = ""
    username = ""
    password = ""
    isDead = False
    sock = None

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def open_bot_socket(self, CHANNEL):
        s = socket.socket()
        s.connect(("irc.twitch.tv", 6667))
        s.send(("PASS " + self.oauth_token + "\r\n").encode())
        s.send(("NICK " + self.username + "\r\n").encode())
        s.send(("JOIN #" + CHANNEL + "\r\n").encode())
        print("Bot # " + self.id + " is connected")
        sock = s