"""File containing functions to execute"""
import os
import subprocess
import sys

import GCCHelper


class Commands:
    """Class containing functionality of bot"""

    @staticmethod
    def info(args):
        """Gets info about script"""
        if args is not None:
            docstring = getattr(Commands, str(args)).__doc__
            if docstring is not None:
                return docstring
        return """SelFBot v0.1 by SteelPh0enix\nPowered by Python {} on {}""".format(
            sys.version, sys.platform)

    @staticmethod
    def runc(args):
        """Runs C code snippet and returns the human-readable verbose output"""
        data = GCCHelper.run_c_code(args)

    @staticmethod
    def runcxx(args):
        """Runs C++ code snippet and returns the human-readable verbose output"""
        pass

    @staticmethod
    def runfc(args):
        """Runs C code as whole file.
 Returns the human-readable verbose output"""
        pass

    @staticmethod
    def runfcxx(args):
        """Runs C++ code as whole file.
 Returns the human-readable verbose output"""
        pass

    @staticmethod
    def restart(args):
        """Restarts the bot in mode sent by arguments"""
        if args is None or args == "":
            return "You have to enter restart mode!"
        subprocess.run(["python", os.path.join(
            os.path.split(os.path.realpath(__file__))[0], "Restart.py"), args, str(os.getpid())])
