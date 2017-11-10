"""File containing functions to execute"""
import os
import subprocess
import sys

from GCCHelper import GCCHelper

GCCRUNNER = GCCHelper()


def info(args):
    """Gets info about script"""
    if args is not None:
        docstring = getattr(sys.modules[__name__], str(args)).__doc__
        if docstring is not None:
            return docstring
    return """SelFBot v0.1 by SteelPh0enix\nPowered by Python {} on {}""".format(
        sys.version, sys.platform)


def runc(code):
    """Runs C code snippet and returns the human-readable verbose output"""
    data = GCCRUNNER.run_c_code(code)


def runcxx(code):
    """Runs C++ code snippet and returns the human-readable verbose output"""
    pass


def runfc(code):
    """Runs C code as whole file. Returns the human-readable verbose output"""
    pass


def runfcxx(code):
    """Runs C++ code as whole file. Returns the human-readable verbose output"""
    pass


def restart(arg):
    """Restarts the bot in mode sent by arguments"""
    if not arg:
        return "You have to enter restart mode!"
    subprocess.run(["python", os.path.join(
        os.path.split(os.path.realpath(__file__))[0], "Restart.py"), arg, str(os.getpid())])
