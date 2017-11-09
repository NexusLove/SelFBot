"""
    Selfbot for facebook
"""
import json
import os

from fbchat import models, Client

from Flags import ResponseFlag
from RequestParser import RequestParser


class SelFB(Client):
    """Main class of the selfbot"""

    def __init__(self):
        with open(os.path.join(os.path.split(os.path.realpath(__file__))[0],
                               'db/login.json')) as login_data:
            self.core_data = json.load(login_data)

        self.parser = RequestParser(self.core_data["prefix"])
        super().__init__(self.core_data["email"], self.core_data["pwd"])

    def kill(self, thread_id, thread_type):
        """Stop the selfbot, with message"""
        exit_msg = models.Message("[Stopping the selfbot]")
        self.send(exit_msg, thread_id, thread_type)
        self.stopListening()

    def command_not_found(self, thread_id, thread_type):
        """Sends a "command not found" message"""
        info_msg = models.Message(
            "[Command not found! Use "
            + self.core_data["prefix"] + "list_cmd to show available commands]")
        self.send(info_msg, thread_id, thread_type)

    def onMessage(self, mid=None, author_id=None, message=None, message_object=None,
                  thread_id=None, thread_type=models.ThreadType.USER, ts=None, metadata=None,
                  msg=None):
        if message_object.author != self.core_data["owner"] or message_object.text.startswith('['):
            return

        response, flag = self.parser.execute(message_object.text)

        if ResponseFlag.KYS in flag:
            self.kill(thread_id, thread_type)
        elif ResponseFlag.NOT_FOUND in flag:
            self.command_not_found(thread_id, thread_type)
        elif ResponseFlag.WRONG_REQUEST in flag:
            return
        elif ResponseFlag.OKAY in flag:
            send_msg = models.Message('[' + str(response) + ']')
            self.send(send_msg, thread_id, thread_type)
