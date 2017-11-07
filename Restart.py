"""Script restarting the bot"""
import subprocess
import sys
import os
import signal

if __name__ == "__main__":
    if len(sys.argv) > 2:
        os.kill(int(sys.argv[2]), signal.SIGTERM)
    subprocess.run(["python", os.path.join(
        os.path.split(os.path.realpath(__file__))[0], '.'), str(sys.argv[1])])
