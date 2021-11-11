# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import os
import unittest
import tempfile
import platform


class Helper(unittest.TestCase):

    DATA = """
    """

    def setUp(self):
        super(Helper, self).setUp()
        fd, self._path = tempfile.mkstemp(dir="/tmp")

        self._file = os.fdopen(fd, "w")
        self._file.write(self.DATA)
        self._file.flush()

        self._fds = self._builder_fix()

    def _builder_fix(self):
        raise NotImplementedError

    def get_temporary_dir(self):
        system = platform.system()
        if "Linux" in system:
            return "/tmp"
        elif "Darwin" in system:
            return "/tmp"  # "/var/folders"

    def tearDown(self):
        self._file.close()
        for fd in self._fds:
            fd.close()
