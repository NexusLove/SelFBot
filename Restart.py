"""
Script (re)starting the bot.
Usage: python Restart.py [mode] (PID)
mode - mode in which bot will be started
PID - PID of process to kill
"""
import os
import signal
import subprocess
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            os.kill(int(sys.argv[2]), signal.SIGTERM)
        subprocess.run(["python", os.path.join(
            os.path.split(os.path.realpath(__file__))[0], '.'), str(sys.argv[1])])
