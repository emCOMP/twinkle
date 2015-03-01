#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pymongo import MongoClient

from twinkle.connectors.csv_connector import CSVReader, CSVTweetReader
from twinkle.connectors.json_connector import JSONReader, JSONTweetReader
from twinkle.connectors.mongo_connector import MongoReader, MongoTweetReader





class BaseTestAdapter:

	def test_id(self, tweet):
		assert tweet.id == 567827122539999200

	def test_text(self, tweet):
		assert tweet.text == u"@geosoco $GOOG @soco_research  test #MNMMNN43 more testing #mas #test $MSFT test http://t.co/P7T85U0IwG   💃🎄🌈✨✨ http://t.co/rpLcXaI1Lr"

	def test_source(self, tweet):
		assert tweet.source == 	u"<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>"




class TestCSVAdapter(BaseTestAdapter):

	@pytest.fixture
	def tweet(self, request):

		csv_reader = CSVTweetReader("tests/data/test_tweet.csv", encoding="utf-8")

		def fin():
			csv_reader.close()

		request.addfinalizer(fin)

		return list(csv_reader)[0]


class TestJSONAdapter(BaseTestAdapter):

	@pytest.fixture
	def tweet(self, request):
		json_reader = JSONTweetReader("tests/data/test_tweet.json", encoding="utf-8")

		def fin():
			json_reader.close()

		request.addfinalizer(fin)

		return list(json_reader)[0]