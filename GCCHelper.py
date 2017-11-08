"""GCC executing library"""
import os
import subprocess
import requests

C_COMPILER = "gcc"
CXX_COMPILER = "g++"

C_FLAGS = ["-Wall", "-Wextra", "-Wpedantic", "-std=c11"]
CXX_FLAGS = ["-Wall", "-Wextra", "-Wpedantic", "-std=c++1z"]

FILE_PATH = os.path.join(os.path.split(
    os.path.realpath(__file__))[0], "tmp")
if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)
C_FILE_PATH = os.path.join(FILE_PATH, "tmp.c")
CXX_FILE_PATH = os.path.join(FILE_PATH, "tmp.cpp")
OUTPUT_FILE = os.path.join(FILE_PATH, "tmp.exe")

C_HEADERS = ["stdio.h", "time.h", "stdlib.h", "string.h"]
CXX_HEADERS = ["iostream", "array", "vector",
               "algorithm", "string", "chrono", "random"]


def run_c_code(code):
    """Runs C code in main() function"""
    # Prepare the boilerplate code
    runcode = "// Generated using GCCHelper by SteelPh0enix\n"
    for header in C_HEADERS:
        runcode += "#include <" + header + ">\n"

    runcode += "\nint main() {\n" + code + "\n}\n"
    return compile_and_run_c(runcode)


def run_cxx_code(code):
    """Runs C++ code in main() function"""
    runcode = "// Generated using GCCHelper by SteelPh0enix\n"
    for header in CXX_HEADERS:
        runcode += "#include <" + header + ">\n"

    runcode += "\nint main() {\n" + code + "\n}\n"
    return compile_and_run_cxx(runcode)


def compile_and_run_c(code):
    """Executes the C code. Returns dict with keys 'compilation',
    and (if compilation was sucessfull) 'execution'.
    Both keys contain keys 'stdout', 'stderr' and 'retcode'."""
    # print("Code: {}\n".format(code))

    with open(C_FILE_PATH, mode="w") as c_file:
        c_file.write(code)

    comp_stdout, comp_stderr, comp_code = run_and_get_output(
        [C_COMPILER] + C_FLAGS + ["-o", OUTPUT_FILE, C_FILE_PATH])

    ret_dict = {
        'compilation':
        {'stdout': comp_stdout, 'stderr': comp_stderr, 'retcode': comp_code}
    }

    if comp_code != 0:
        return ret_dict

    exec_stdout, exec_stderr, exec_code = run_and_get_output(
        [OUTPUT_FILE])

    ret_dict['execution'] = {
        'stdout': exec_stdout, 'stderr': exec_stderr, 'retcode': exec_code
    }

    return ret_dict


def compile_and_run_cxx(code):
    """Executes the C++ code. Returns dict with keys 'compilation',
    and (if compilation was sucessfull) 'execution'.
    Both keys contain keys 'stdout', 'stderr' and 'retcode'."""
    # print("Code: {}\n".format(code))

    with open(CXX_FILE_PATH, mode="w") as cxx_file:
        cxx_file.write(code)

    comp_stdout, comp_stderr, comp_code = run_and_get_output(
        [CXX_COMPILER] + CXX_FLAGS + ["-o", OUTPUT_FILE, CXX_FILE_PATH])

    ret_dict = {
        'compilation':
        {'stdout': comp_stdout, 'stderr': comp_stderr, 'retcode': comp_code}
    }

    if comp_code != 0:
        return ret_dict

    exec_stdout, exec_stderr, exec_code = run_and_get_output(
        [OUTPUT_FILE])

    ret_dict['execution'] = {
        'stdout': exec_stdout, 'stderr': exec_stderr, 'retcode': exec_code
    }

    return ret_dict


def run_and_get_output(arguments):
    "Runs the program and returns (stdout, stderr, return_code) tuple"
    proc = subprocess.Popen(
        arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    # print("Arguments: {}\nProc: {}\n Out: {}\n Err: {}\n Return code: {}\n".format(
    #     arguments, proc, out, err, proc.returncode
    # ))
    return out.decode('utf-8'), err.decode('utf-8'), proc.returncode


def post_on_hastebin(content):
    """Helper funciton.
    Posts the stuff on Hastebin, returns URL.
    Yea, this is copy&paste from hastebin.py
    https://github.com/LyricLy/hastebin.py/blob/master/hastebin/hastebin.py"""
    post = requests.post("https://hastebin.com/documents", data=content)
    return "https://hastebin.com/" + post.json()["key"]
