from unittest import TestCase

from GCCRunner import GCCRunner


class TestGCCHelper(TestCase):
    def test_run_c_code(self):
        runner = GCCRunner()
        ret = runner.run_c_code('puts("Hello, world!");')
        self.assertDictEqual(ret, {
            'compilation': {
                'stdout': "",
                'stderr': "",
                'retcode': 0
            },
            'execution': {
                'stdout': "Hello, world!\r\n",
                'stderr': "",
                'retcode': 0
            }
        })

    def test_run_cxx_code(self):
        runner = GCCRunner()
        ret = runner.run_cxx_code('std::cout << "Hello, world!\\n";')
        self.assertDictEqual(ret, {
            'compilation': {
                'stdout': "",
                'stderr': "",
                'retcode': 0
            },
            'execution': {
                'stdout': "Hello, world!\r\n",
                'stderr': "",
                'retcode': 0
            }
        })

    def test_compile_and_run_c(self):
        runner = GCCRunner()
        ret = runner.compile_and_run_c('#include <stdio.h>\n\nint main() {\n\tputs("Hello, world!");\n}\n')
        self.assertDictEqual(ret, {
            'compilation': {
                'stdout': "",
                'stderr': "",
                'retcode': 0
            },
            'execution': {
                'stdout': "Hello, world!\r\n",
                'stderr': "",
                'retcode': 0
            }
        })

    def test_compile_and_run_cxx(self):
        runner = GCCRunner()
        ret = runner.compile_and_run_cxx('#include <iostream>\n\nint main() {\n\tstd::cout << "Hello, world!\\n";\n}\n')
        self.assertDictEqual(ret, {
            'compilation': {
                'stdout': "",
                'stderr': "",
                'retcode': 0
            },
            'execution': {
                'stdout': "Hello, world!\r\n",
                'stderr': "",
                'retcode': 0
            }
        })
