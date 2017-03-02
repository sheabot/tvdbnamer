import os
import shutil
import tempfile
from unittest import TestCase

import utils


class TVDBNamerTestCase(TestCase):

    dummy_files = []

    @classmethod
    def setUpClass(cls):
        """On inherited classes, run our `setUp` method"""
        # Inspired via http://stackoverflow.com/questions/1323455/python-unit-test-with-base-and-sub-class/17696807#17696807
        if cls is not TVDBNamerTestCase and cls.setUp is not TVDBNamerTestCase.setUp:
            orig_setUp = cls.setUp
            def setUpOverride(self, *args, **kwargs):
                TVDBNamerTestCase.setUp(self)
                return orig_setUp(self, *args, **kwargs)
            cls.setUp = setUpOverride

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        for filepath in self.dummy_files:
            # Fail out on absolute paths
            assert not os.path.isabs(filepath)
            dirname, filename = os.path.split(filepath)
            if dirname:
                dirpath = os.path.join(self.tmpdir, dirname)
                utils.mkdir_p(dirpath)
            open(os.path.join(self.tmpdir, filepath), 'a').close()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)
