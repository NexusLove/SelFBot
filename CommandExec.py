"""Module containing the command executing class"""
from math import *
from Commands import Commands


class CommandExec():
    """Class executing the command"""

    def __init__(self):
        function_list = [func for func in dir(Commands) if callable(
            getattr(Commands, func)) and not func.startswith("__")]

        self.cmd_list = {
            "eval": eval,
            "exec": exec,
            "list_cmd": self.get_cmd_list
        }

        for func in function_list:
            self.cmd_list[func] = getattr(Commands, func)

        # print("Function list: {}".format(self.cmd_list))

    def command_exists(self, cmd):
        """Checks if command exists"""
        return cmd in self.cmd_list

    def get_cmd_list(self, arg):
        """Returns the commands list"""
        return [key for key in self.cmd_list]

    def run(self, command, args):
        """Runs the command"""
        if not self.command_exists(command):
            return None

        return self.cmd_list[command](args)
