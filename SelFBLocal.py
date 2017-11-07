"""Module containing local Selfbot runner"""
import json
import os

from RequestParser import RequestParser
from Flags import ResponseFlag


class SelFB():
    """Selfbot local runner"""

    def __init__(self):
        with open(os.path.join(os.path.split(os.path.realpath(__file__))[0],
                               'db/login.json')) as login_data:
            self.core_data = json.load(login_data)

        self.parser = RequestParser(self.core_data["prefix"])

    def kill(self):
        """Stops the bot"""
        print("Stopping the bot...")
        exit(0)

    def command_not_found(self):
        """Returns "command not found" message"""
        print("Command not found - use list_cmd to print list of commands")

    def message_loop(self):
        """Loop handling the messages input"""
        msg = input(self.core_data["prefix"])

        response, flag = self.parser.execute(msg, ommit_prefix=True)

        if ResponseFlag.KYS in flag:
            self.kill()
        elif ResponseFlag.NOT_FOUND in flag:
            self.command_not_found()
        elif ResponseFlag.WRONG_REQUEST in flag:
            return
        elif ResponseFlag.OKAY in flag:
            print(str(response))
