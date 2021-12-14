import unittest
from src import delete_staff
import sys


class TestCharacters(unittest.TestCase):
    """test delete staff"""
    def setUp(self):
        self.stream_out = MyStream()
        self.out_stream = sys.stdout
        sys.stdout = self.stream_out
        pass

    def test_characters1(self):
        staff_list = ['John Smith', 'Jackie Jackson', 'Chris Jones', 'Amanda Cullen', 'Jeremy Goodwin']
        del_staff = 'Chris Jones'
        delete_staff.delete_staff(staff_list, del_staff)
        test=''
        test = test.join(self.stream_out.buff)
        self.assertEqual(test, 'There are 5 staff:\nJohn Smith\nJackie Jackson\n'
                               'Chris Jones\nAmanda Cullen\nJeremy Goodwin\n\nremove the staff: Chris Jones'
                               '\n\nThere are 4 staff:\nJohn Smith\nJackie Jackson\nAmanda Cullen\nJeremy Goodwin\n')

    def test_characters2(self):
        staff_list = ['Chris Jones']
        del_staff = 'Chris Jones'
        delete_staff.delete_staff(staff_list, del_staff)
        test = ''
        test = test.join(self.stream_out.buff)
        self.assertEqual(test, 'There are 1 staff:\nChris Jones\n\n'
                               'remove the staff: Chris Jones\n\nThere are 0 staff:\n')

    def test_characters3(self):
        staff_list = ['John Smith', 'Jackie Jackson', 'Chris Jones', 'Amanda Cullen', 'Jeremy Goodwin']
        del_staff = 'Jeremy Goodwin'
        delete_staff.delete_staff(staff_list, del_staff)
        test=''
        test = test.join(self.stream_out.buff)
        self.assertEqual(test, 'There are 5 staff:\nJohn Smith\nJackie Jackson\n'
                               'Chris Jones\nAmanda Cullen\nJeremy Goodwin\n\nremove the staff: Jeremy Goodwin'
                               '\n\nThere are 4 staff:\nJohn Smith\nJackie Jackson\n'
                               'Chris Jones\nAmanda Cullen\n')

    def test_characters4(self):
        staff_list = ['John Smith', 'Jackie Jackson', 'Chris Jones', 'Amanda Cullen', 'Jeremy Goodwin']
        del_staff = 'John Smith'
        delete_staff.delete_staff(staff_list, del_staff)
        test = ''
        test = test.join(self.stream_out.buff)
        self.assertEqual(test, 'There are 5 staff:\nJohn Smith\nJackie Jackson\n'
                               'Chris Jones\nAmanda Cullen\nJeremy Goodwin\n\nremove the staff: John Smith'
                               '\n\nThere are 4 staff:\nJackie Jackson\n'
                               'Chris Jones\nAmanda Cullen\nJeremy Goodwin\n')

    def tearDown(self):
        sys.stdout = self.out_stream
        pass


class MyStream:

    def __init__(self):
        self.buff = []

    def write(self, output_stream):
        self.buff.append(output_stream)

    def readline(self):
        if len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            return cur