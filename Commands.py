"""File containing functions to execute"""
import sys


class Commands():
    """Class containing functionality of bot"""

    @staticmethod
    def info(args):
        """Gets info about script"""
        return """SelFBot by SteelPh0enix
            Powered by Python {} on {}""".format(sys.version, sys.platform)

    @staticmethod
    def run_c_snippet(args):
        """Runs C code snippet and returns the human-readable verbose output"""
        pass

    @staticmethod
    def run_cxx_snippet(args):
        """Runs C++ code snippet and returns the human-readable verbose output"""
        pass
