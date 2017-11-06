"""GCC executing library"""
import os
import requests
import subprocess


class GCCHelper():
    """Class with functions for executing C/C++ code"""

    def __init__(self):
        self.c_compiler = "gcc"
        self.cxx_compiler = "g++"

        self.c_flags = ["-Wall",  "-Wextra", "-Wpedantic", "-std=c11"]
        self.cxx_flags = ["-Wall", "-Wextra", "-Wpedantic", "-std=c++1z"]

        self.file_path = os.path.join(os.path.split(
            os.path.realpath(__file__))[0], "tmp")
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path)
        self.c_file_path = os.path.join(self.file_path, "tmp.c")
        self.cxx_file_path = os.path.join(self.file_path, "tmp.cpp")
        self.output_file = os.path.join(self.file_path, "tmp.exe")

        self.c_headers = ["stdio.h", "time.h", "stdlib.h", "string.h"]
        self.cxx_headers = ["iostream", "array", "vector",
                            "algorithm", "string", "chrono", "random"]

    def run_c_code(self, code):
        """Runs C code in main() function"""
        # Prepare the boilerplate code
        runcode = "// Generated using GCCHelper by SteelPh0enix\n"
        for header in self.c_headers:
            runcode += "#include <" + header + ">\n"

        runcode += "\nint main() {\n" + code + "\n}\n"
        return self.compile_and_run_c(runcode)

    def run_cxx_code(self, code):
        """Runs C++ code in main() function"""
        runcode = "// Generated using GCCHelper by SteelPh0enix\n"
        for header in self.cxx_headers:
            runcode += "#include <" + header + ">\n"

        runcode += "\nint main() {\n" + code + "\n}\n"
        return self.compile_and_run_cxx(runcode)

    def compile_and_run_c(self, code):
        """Executes the C code. Returns dict with keys 'compilation',
        and (if compilation was sucessfull) 'execution'.
        Both keys contain keys 'stdout', 'stderr' and 'retcode'."""
        # print("Code: {}\n".format(code))

        with open(self.c_file_path, mode="w") as c_file:
            c_file.write(code)

        comp_stdout, comp_stderr, comp_code = self.run_and_get_output(
            [self.c_compiler] + self.c_flags + ["-o", self.output_file, self.c_file_path])

        ret_dict = {
            'compilation':
                {'stdout': comp_stdout, 'stderr': comp_stderr, 'retcode': comp_code}
        }

        if comp_code != 0:
            return ret_dict

        exec_stdout, exec_stderr, exec_code = self.run_and_get_output(
            [self.output_file])

        ret_dict['execution'] = {
            'stdout': exec_stdout, 'stderr': exec_stderr, 'retcode': exec_code
        }

        return ret_dict

    def compile_and_run_cxx(self, code):
        """Executes the C++ code. Returns dict with keys 'compilation',
        and (if compilation was sucessfull) 'execution'.
        Both keys contain keys 'stdout', 'stderr' and 'retcode'."""
        # print("Code: {}\n".format(code))

        with open(self.cxx_file_path, mode="w") as cxx_file:
            cxx_file.write(code)

        comp_stdout, comp_stderr, comp_code = self.run_and_get_output(
            [self.cxx_compiler] + self.cxx_flags + ["-o", self.output_file, self.cxx_file_path])

        ret_dict = {
            'compilation':
                {'stdout': comp_stdout, 'stderr': comp_stderr, 'retcode': comp_code}
        }

        if comp_code != 0:
            return ret_dict

        exec_stdout, exec_stderr, exec_code = self.run_and_get_output(
            [self.output_file])

        ret_dict['execution'] = {
            'stdout': exec_stdout, 'stderr': exec_stderr, 'retcode': exec_code
        }

        return ret_dict

    def run_and_get_output(self, arguments):
        "Runs the program and returns (stdout, stderr, return_code) tuple"
        proc = subprocess.Popen(
            arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        # print("Arguments: {}\nProc: {}\n Out: {}\n Err: {}\n Return code: {}\n".format(
        #     arguments, proc, out, err, proc.returncode
        # ))
        return out.decode('utf-8'), err.decode('utf-8'), proc.returncode

    def post_on_hastebin(self, content):
        """Helper funciton.
        Posts the stuff on Hastebin, returns URL.
        Yea, this is copy&paste from hastebin.py
        https://github.com/LyricLy/hastebin.py/blob/master/hastebin/hastebin.py"""
        post = requests.post("https://hastebin.com/documents", data=content)
        return "https://hastebin.com/" + post.json()["key"]


if __name__ == "__main__":
    HELPER = GCCHelper()
    print(HELPER.run_c_code(r'puts("Hello, world!");'))
    print(HELPER.run_cxx_code(r'std::cout << "Hello, world from C++!\n";'))
    print(HELPER.run_c_code(r'test'))
    print(HELPER.run_cxx_code(r'std::cout << '))
    print(HELPER.compile_and_run_c(r'''#include <stdio.h>
    int main() { puts("Hi there (C)!"); }'''))
    print(HELPER.compile_and_run_cxx(r'''#include <iostream>
    int main() { std::cout << "Hello there from C++!\n"; }'''))
