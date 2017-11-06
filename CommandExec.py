"""Module containing the command executing class"""
from Commands import Commands
from math import *


class CommandExec():
    """Class executing the command"""

    def __init__(self):
        self.cmd_list = {
            "info": Commands.info,
            "eval": eval,
            "exec": exec
        }

    def command_exists(self, cmd):
        """Checks if command exists"""
        if cmd in self.cmd_list:
            return True
        else:
            return False

    def run(self, command, args):
        if not self.command_exists(command):
            return None

        return self.cmd_list[command](args)
