#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope="module")
def csvfixture(request):
	print "csvfixture"

	def fin():
		pass	

