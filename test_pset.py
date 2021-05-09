#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{cookiecutter.project_slug}}` package."""

import os
from tempfile import TemporaryDirectory, NamedTemporaryFile
from unittest import TestCase, main, mock

class FakeFileFailure(IOError):
    pass
