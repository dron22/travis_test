# -*- coding: utf-8 -*-

import os
import sys

# SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
# REPO_DIR = SCRIPT_DIR + '/..'
# sys.path.append(REPO_DIR)

import app


def test_multiply():
    assert app.multiply(2, 3) == 6
