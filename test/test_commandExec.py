from unittest import TestCase

from CommandExec import CommandExec


class TestCommandExec(TestCase):
    def test_command_exists(self):
        executor = CommandExec()
        self.assertEqual(executor.command_exists('non_existing_command'), False, "Non-existing command exists")
        self.assertEqual(executor.command_exists('list_cmd'), True, "Existing command not exists")

    def test_run(self):
        executor = CommandExec()
        self.assertEqual(executor.run("eval", "2+2"), "4", "Executor couldn't run 'eval' properly")
        self.assertEqual(executor.run("non_existing_command", ""), "",
                         "Executor didn't returned empty string at non-existing command call")
