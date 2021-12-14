import unittest
import sys
from src import string_task


class Test(unittest.TestCase):

    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test1(self):
        input_str = 'Codeforces\n'
        output_str = '.c.d.f.r.c.s\n'
        self.stream_in.write(input_str)
        string_task.get_string()
        result = str(self.stream_out.readline())
        self.assertEqual(result, output_str)

    def test2(self):
        input_str = 'aBAcAba\n'
        output_str = '.b.c.b\n'
        self.stream_in.write(input_str)
        string_task.get_string()
        result = str(self.stream_out.readline())
        self.assertEqual(result, output_str)

    def test3(self):
        input_str = 'transmiSSioNbt\n'
        output_str = '.t.r.n.s.m.s.s.n.b.t\n'
        self.stream_in.write(input_str)
        string_task.get_string()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test4(self):
        input_str = 'eMbeDdeDsystemSandHeadLessUse\n'
        output_str = '.m.b.d.d.d.s.y.s.t.m.s.n.d.h.d.l.s.s.s\n'
        self.stream_in.write(input_str)
        string_task.get_string()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test5(self):
        input_str = 'wsxvbnjkyhgtfzzxCVB\n'
        output_str = '.w.s.x.v.b.n.j.k.y.h.g.t.f.z.z.x.c.v.b\n'
        self.stream_in.write(input_str)
        string_task.get_string()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def tearDown(self):
        sys.stdout = self.out_stream
        sys.stdin = self.in_stream
        pass


class MyStream:

    def __init__(self):
        self.buff = []

    def write(self, output_stream):
        self.buff.append(output_stream)

    def readline(self):
        result = ''
        while len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            result = result + cur
            if result.endswith('\n'):
                return result
        return result
