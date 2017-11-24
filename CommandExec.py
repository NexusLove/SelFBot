"""Module containing the command executing class"""
import Commands
from math import *

class CommandExec:
    """Class executing the command"""

    def __init__(self):
        function_list = [func for func in dir(Commands) if callable(
            getattr(Commands, func)) and not func.startswith("__")]

        self.cmd_list = {
            "eval":     eval,
            "exec":     exec,
            "list_cmd": self.get_cmd_list
        }

        for func in function_list:
            self.cmd_list[func] = getattr(Commands, func)

    def command_exists(self, cmd: str) -> bool:
        """Checks if command exists
        :param cmd: command to check
        :return: True if exists,
        :rtype: bool
        """
        return cmd in self.cmd_list

    def get_cmd_list(self) -> str:
        """Returns the commands list
        :rtype: str
        :return: String with list of commands
        """
        return str([key for key in self.cmd_list])

    def run(self, command: str, args: str) -> str:
        """Runs the command
        :param command: Command to run
        :param args: Arguments for this command
        :return: Command execution result or "" if it doesn't exists
        :rtype: str
        """
        if not self.command_exists(command):
            return ""

        if args:
            return self.cmd_list[command](args)
        return self.cmd_list[command]()
