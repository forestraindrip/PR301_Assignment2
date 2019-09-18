import unittest


class ModelTest(unittest.TestCase):

    def test_model(self):
        #import drawer and parser we are testing
        from DrawerKieran import Drawer
        from ParserKC import Parser
        #open test file to read
        test = open('test.txt', "r+")
        to_draw = test.read()
        Parser(Drawer()).parse(to_draw)
        test.close()
        print(Drawer.model_capture)
        self.assertEqual(Drawer.model_capture, ['GOTO X=250', 'GOTO X=250', 'pen down', [250.0, 250.0, 50.0, 250.0], [50.0, 250.0, 50.0, 150.0], [50.0, 150.0, 250.0, 150.0], [250.0, 150.0, 250.0, 250.0], 'pen up'])


if __name__ == '__main__':
    unittest.main()
