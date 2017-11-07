"""Selfbot's request parser"""
from Flags import ResponseFlag
from CommandExec import CommandExec


class RequestParser():
    """Class validating the command, checking it for existence and running it"""

    def __init__(self, prefix):
        self.prefix = prefix
        self.executor = CommandExec()

        self.exit_cmds = ['kys', 'exit']

    def parse_command(self, message, ommit_prefix):
        """
            Returns the command
            (command, args) if the command has arguments
            (command, None) if it doesn't
            (None, None) if this is not a command
        """
        if ommit_prefix or message.startswith(self.prefix):
            message = message[len(self.prefix):] if not ommit_prefix else message
            arg_split = message.split(' ', 1)
            if (len(arg_split)) == 1:
                return (arg_split[0], None)
            return (arg_split[0], arg_split[1])
        return (None, None)

    def execute(self, message, ommit_prefix=False):
        """Executes the command and returns result"""
        command, args = self.parse_command(message, ommit_prefix)

        if command is None:
            return (None, ResponseFlag.WRONG_REQUEST)

        if command in self.exit_cmds:
            return (None, ResponseFlag.KYS)

        if not self.executor.command_exists(command):
            return (None, ResponseFlag.NOT_FOUND)

        return self.executor.run(command, args), ResponseFlag.OKAY
