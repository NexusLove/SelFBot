from unittest import TestCase

from RequestParser import RequestParser, ResponseFlag


class TestRequestParser(TestCase):
    def test_parse_command(self):
        parser = RequestParser(';')

        self.assertEqual(parser.parse_command('test'), (None, None), "Parser found a command without prefix")
        self.assertEqual(parser.parse_command(';test'), ('test', ''), "Parser didn't found command with prefix")
        self.assertEqual(parser.parse_command(';test arg'), ('test', 'arg'),
                         "Parser didn't parsed command with args properly")

        self.assertEqual(parser.parse_command('ommit', True), ('ommit', ''),
                         "Parser couldn't find a command with omitted prefix")
        self.assertEqual(parser.parse_command('ommit test', True), ('ommit', 'test'),
                         "Parser didn't parsed command without prefix properly")

    def test_execute(self):
        parser = RequestParser(';')

        self.assertEqual(parser.execute('test'), (None, ResponseFlag.WRONG_REQUEST),
                         "Parser found a command without prefix")
        self.assertEqual(parser.execute(';this_command_does_not_exist'), (None, ResponseFlag.NOT_FOUND),
                         "Parser found non-existing command")
        self.assertEqual(parser.execute(';kys'), (None, ResponseFlag.KYS),
                         "Parser didn't found exit command")
        msg_list_prefixed, flag_list_prefixed = parser.execute(';list_cmd')
        self.assertEqual(flag_list_prefixed, ResponseFlag.OKAY, "Parser didn't found existing command")

        self.assertEqual(parser.execute('this_command_does_not_exist', True), (None, ResponseFlag.NOT_FOUND),
                         "Parser found non-existing command without prefix")
        self.assertEqual(parser.execute('kys', True), (None, ResponseFlag.KYS),
                         "Parser didn't found exit command without prefix")
        msg_list_not_prefixed, flag_list_not_prefixed = parser.execute('list_cmd', True)
        self.assertEqual(flag_list_not_prefixed, ResponseFlag.OKAY,
                         "Parser didn't found existing command without prefix")

        eval_data, eval_flag = parser.execute(";eval 2 + 2")
        self.assertEqual(eval_data, "4", "Wrong 'eval 2 + 2' return message!")
        self.assertEqual(eval_flag, ResponseFlag.OKAY, "Wrong 'eval 2 + 2' return flag!")
