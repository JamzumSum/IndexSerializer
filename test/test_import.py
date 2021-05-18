import unittest


class TestImport(unittest.TestCase):
    def testInit(self):
        import indexserial
        self.assertIsNotNone(indexserial)

    def testLoader(self):
        from indexserial import IndexLoader
        self.assertIsNotNone(IndexLoader)

    def testDumper(self):
        from indexserial import IndexDumper
        self.assertIsNotNone(IndexDumper)
