from Bot import Bot
import Confings
from Confings import IDENT
import socket
from Command import command


class HiveMind:
    CHANNEL = "sn0wyowl"
    RAIDCHANNEL = ""

    oauth_token = ""
    commands_list = []
    commands_queue = []
    admin_users = []
    phrases_list = []
    bots_list = []
    bad_phrases = []

    def __init__(self):
        self.sock = None
        self.admin_users.append("sn0wyowl")
        self.init_commands()
        print("set command channel")
        # self.CHANNEL = input()

    def add_bot(self, username, passwrd):
        file = open("twitch_accounts.txt", 'r')
        message = file.readline()
        for line in file:
            login, passwrd, oauth = line.split()
            bot = Bot(username, passwrd)
            self.bots_list.append(bot)
            print("bot successfuly added")

    def print_avaible_commands(self):
        self.send_single_message(message="Avaible commands: \n")
        for i in self.commands_list:
            self.send_single_message(message=i.value)


    def openSocket(self):
        s = socket.socket()
        s.connect(("irc.twitch.tv", 6667))
        s.send(("PASS " + self.oauth_token + "\r\n").encode())
        s.send(("NICK " + IDENT + "\r\n").encode())
        s.send(("JOIN #" + self.CHANNEL + "\r\n").encode())
        print("socket opened!")
        self.sock = s
        return s

    def join_room(self, s=None):
        if s == None:
            s = self.sock
        readBuffer = " "
        loading = True
        while loading:
            temp = self.get_response(readBuffer, s)
            for line in temp:
                print(line)
                loading = self.loadingComplete(line)

        self.send_single_message(s, "Successfuly joined chat!")

    def get_response(self, readBuffer = " ", s = None):
        if s == None:
            s = self.sock

        readBuffer = readBuffer + s.recv(1024).decode()
        temp = readBuffer.split("\n")
        readBuffer = temp.pop()
        return temp

    def loadingComplete(self, line):
        if ("End of /NAMES list" in line):
            return False
        else:
            return True

    def check_access(self, user):
        if user in self.admin_users:
            return True
        else:
            self.send_single_message(message="Sorry, but you have no rights to use me(")
            return False

    def send_single_message(self, s = None, message = "default"):
        if s == None:
            s = self.sock
        message.encode()
        messageTemp = ("PRIVMSG #" + self.CHANNEL + " :" + message)
        s.send((messageTemp + "\r\n").encode())
        print("Sent: " + messageTemp)


    def remove_dead_bots(self):
        for bot in self.bots_list:
            if bot.isDead:
                self.bots_list.remove(bot)

    def add_command_to_queue(self, command):
        self.commands_queue.append(command)


    def init_commands(self):
        c = command(val="help")
        self.commands_list.append(c)
        pass

    def get_message(self):
        pass

    def get_user(self):
        pass

    def execute_command(self, command, user):
        access = self.check_access(user)
        if not access:
            return

        if (command == "help"):
            self.print_avaible_commands()

    def check_command(self, command):
        if command in self.commands_list:
            return True
        else:
            self.send_single_message(message="Sorry, i dont have this command")

    def set_raid_chanel(self, raid_chanel):
        self.RAIDCHANNEL = raid_chanel

    def set_admin_channel(self, admin_chanel):
        self.CHANNEL = admin_chanel

    def prepare_to_raid(self):
        pass

    def start_raid(self):
        pass

    def stop_raid(self):
        pass

    def add_phrase_to_list(self, phrase):
        if phrase not in self.bad_phrases:
            self.phrases_list.append(phrase)
            self.send_single_message(message="Phrase: %a successfuly added!" % phrase)
        else:
            self.send_single_message(message="Sorry, but you pharse is too bad for Raid")

    def clear_pharses_list(self):
        self.phrases_list.clear()
