#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pset_1` package."""

import os
import pandas as pd
from pandas.util.testing import assert_frame_equal
from tempfile import TemporaryDirectory
from tempfile import NamedTemporaryFile
from unittest import TestCase, mock


from final_project_face_recognition.utils.hash import *
from final_project_face_recognition.utils.io import *


class FakeFileFailure(IOError):
    pass


class HashTests(TestCase):
    def test_basic(self):
        """Ensure provided string is hashed successfully"""
        self.assertEqual(hash_str("world!", salt="hello, ").hex()[:6], "68e656")

    def test_characters(self):
        """Ensure provided string of symbols/characters is hashed successfully"""
        self.assertEqual(hash_str("@#$%^").hex()[:6], "7af7d6")


class AtomicWriteTests(TestCase):
    def test_atomic_write(self):
        """Ensure file exists after being written successfully"""

        with TemporaryDirectory() as tmp:
            fp = os.path.join(tmp, "asdf.txt")

            with atomic_write(fp, "w") as f:
                assert not os.path.exists(fp)
                tmpfile = f.name
                f.write("asdf")

            assert not os.path.exists(tmpfile)
            assert os.path.exists(fp)

            with open(fp) as f:
                self.assertEqual(f.read(), "asdf")

    def test_atomic_failure(self):
        """Ensure that file does not exist after failure during write"""

        with TemporaryDirectory() as tmp:
            fp = os.path.join(tmp, "asdf.txt")

            with self.assertRaises(FakeFileFailure):
                with atomic_write(fp, "w") as f:
                    tmpfile = f.name
                    assert os.path.exists(tmpfile)
                    raise FakeFileFailure()

            assert not os.path.exists(tmpfile)
            assert not os.path.exists(fp)

    def test_file_exists(self):
        """Ensure an error is raised when a file exists"""
        check_returned_error = False
        try:
            with NamedTemporaryFile() as fp:
                tmpfile = fp.name
                with atomic_write(tmpfile, "w") as f:
                    f.write("asdf")
        except FileExistsError:
            check_returned_error = True
        if check_returned_error:
            assert True
        else:
            assert False

    def test_same_extension(self):
        """Ensure the temporary file has the same extension(s) as the target"""

        with TemporaryDirectory() as tmp:
            fp = os.path.join(tmp, "test.parquet")

            with atomic_write(fp, "w") as f:
                assert not os.path.exists(fp)
                tmpfile = f.name
                f.write("asdf")
                filename, file_extension = os.path.splitext(f.name)
                self.assertEqual(file_extension, ".parquet")


class MainTests(TestCase):
    def test_excel_to_parquet(self):
        """Ensure parquet file can be written successfully based on original excel file"""

        # Remove test files if they exist
        if os.path.exists("test.xlsx"):
            os.remove("test.xlsx")
        if os.path.exists("test.parquet"):
            os.remove("test.parquet")

    def test_get_user_hash(self):
        """Ensure when string and optional salt parameter is provided, outcome is as expected"""
        self.assertEqual(get_user_hash("world!", salt="hello, ").hex()[:6], "68e656")
