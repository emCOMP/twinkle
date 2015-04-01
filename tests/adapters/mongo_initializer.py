#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import io
import simplejson
from pymongo import MongoClient



class MongoTestInitializer(object):
	"""
	"""

	def __init__(self, host="localhost", port=27017, db_name="twinkle_unittest_db", collection_name="tweets"):
		self.host = host
		self.port = port
		self.db_name = db_name
		self.collection_name = collection_name

		self.client = None
		self.db = None
		self.collection = None


	def connect(self):
		"""
		"""
		self.client = MongoClient(host, port)
		self.db = client[self.db_name]
		self.collection = self.db[self.collection_name]

	def disconnect(self):
		if self.client is not None:
			self.client.close()
			self.client = None
			self.db = None
			self.collection = None


	def setup(self, filename, encoding="UTF-8"):
		with io.open(filename, "r", encoding=encoding) as f:
			for l in f:
				o = simplejson.loads(l)
				self.collection.insert(o)

	def teardown(self):
		pass
