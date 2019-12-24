import socket
from Confings import *
import string
from HiveMind import HiveMind


def main():

    bot_mind = HiveMind()
    bot_mind.openSocket()
    bot_mind.join_room()

    while True:
        temp = bot_mind.get_response()

        for line in temp:
            print(temp)
            if "!hive" in line:
                commands = line.split()
                if len(commands) > 5:
                    bot_mind.send_single_message(message="Sorry, i cant recognise you command")
                elif len(commands) == 5:
                    print(commands[2][1:])
                    print(commands[4])
                    bot_mind.execute_command(commands[4], commands[2][1:])
                elif len(commands) == 4:
                    bot_mind.send_single_message(message="Hive is here, my lord")


if __name__ == "__main__":
    main()