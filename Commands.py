"""File containing functions to execute"""
import os
import subprocess
import sys

from GCCRunner import GCCRunner as __GCCRunner
from GCCRunner import prepare_message as __prepare_message
from GCCRunner import post_on_hastebin

from Flags import MessageEventFlag

_GCCRUNNER = __GCCRunner()
# Following stuff is just for the sake of this script. I preferred to keep it inside GCCRunner object,
# instead of making new variable
_GCCRUNNER.max_output_len = 50


def info(args=None):
    """Gets info about script"""
    if args is not None:
        docstring = getattr(sys.modules[__name__], str(args)).__doc__
        if docstring is not None:
            return docstring
    return """SelFBot v0.1 by SteelPh0enix\nPowered by Python {} on {}""".format(
        sys.version, sys.platform)


def runc(code):
    """Runs C code snippet and returns the human-readable verbose output"""
    data = _GCCRUNNER.run_c_code(code)
    return __prepare_message(data)


def runcxx(code):
    """Runs C++ code snippet and returns the human-readable verbose output"""
    data = _GCCRUNNER.run_cxx_code(code)
    return __prepare_message(data)


def runfc(code):
    """Runs C code as whole file. Returns the human-readable verbose output"""
    data = _GCCRUNNER.compile_and_run_c(code)
    return __prepare_message(data)


def runfcxx(code):
    """Runs C++ code as whole file. Returns the human-readable verbose output"""
    data = _GCCRUNNER.compile_and_run_cxx(code)
    return __prepare_message(data)


def restart(arg):
    """Restarts the bot in mode sent by arguments"""
    if not arg:
        return "You have to enter restart mode!"
    subprocess.run(["python", os.path.join(
        os.path.split(os.path.realpath(__file__))[0], "Restart.py"), arg, str(os.getpid())])


def angery():
    """Turns angery on"""
    return MessageEventFlag.ANGERY


def calm():
    """Turns angery off"""
    return MessageEventFlag.NONE
