# -*- coding: utf-8 -*-

import travis_test.app as app


def test_multiply():
    assert app.multiply(2, 3) == 6
