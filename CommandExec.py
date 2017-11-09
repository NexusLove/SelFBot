"""Module containing the command executing class"""
from Commands import Commands


class CommandExec:
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

    def command_exists(self, cmd: str) -> bool:
        """Checks if command exists
        :param cmd: command to check
        :return: True if exists,
        :rtype: bool
        """
        return cmd in self.cmd_list

    def get_cmd_list(self, arg: None) -> str:
        """Returns the commands list
        :rtype: str
        :param arg: Not used, required for bot call
        :return: String with list of commands
        """
        return str([key for key in self.cmd_list])

    def run(self, command: str, args: str) -> str:
        """Runs the command"""
        if not self.command_exists(command):
            return ""

        return self.cmd_list[command](args)
