"""Main module file"""
import sys

from SelFBFacebook import SelFB as SelfbotFacebook
from SelFBLocal import SelFB as SelfbotLocal


def run_local():
    """Runs the selfbot locally"""
    bot = SelfbotLocal()
    while True:
        bot.message_loop()


def run_facebook():
    """Runs the selfbot on FBChat"""
    bot = SelfbotFacebook()
    bot.listen()


def print_help():
    """Prints help message"""
    print("Usage:\n"
          "python [path_to_selfbot] [mode]\n"
          "mode - mode in which bot should run (local, fbchat)")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_help()
        exit(1)

    CURRENT_MODE = sys.argv[1]

    if CURRENT_MODE == "local":
        run_local()
    elif CURRENT_MODE == "fbchat":
        run_facebook()
    else:
        print_help()
        exit(2)
