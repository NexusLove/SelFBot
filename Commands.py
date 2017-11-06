"""File containing functions to execute"""
import sys


class Commands():
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
        pass

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
