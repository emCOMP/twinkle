#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pymongo import MongoClient
from datetime import datetime

from twinkle.connectors.csv_connector import CSVReader, CSVTweetReader
from twinkle.connectors.json_connector import JSONReader, JSONTweetReader
from twinkle.connectors.mongo_connector import MongoReader, MongoTweetReader





class BaseTestAdapter:

	def test_core_values(self, tweet):
		assert tweet.id == 567827122539999200
		assert tweet.text == u"@geosoco $GOOG @soco_research  test #MNMMNN43 more testing #mas #test $MSFT test http://t.co/P7T85U0IwG   💃🎄🌈✨✨ http://t.co/rpLcXaI1Lr"
		assert tweet.source == 	u"<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>"
		assert tweet.in_reply_to_status_id == 567826248212193300
		assert tweet.in_reply_to_user_id == 2891731229
		assert tweet.in_reply_to_user_screen_name == u"soco_research"
		assert tweet.created_at == u"Tue Feb 17 23:25:10 +0000 2015"
		assert tweet.created_ts == datetime(2015, 2, 17, 23, 25, 10)
		assert tweet.lang == u"en"
		print tweet.retweet_count
		print tweet.favourite_count
		assert tweet.retweet_count == 37
		assert tweet.favorite_count == 65
		assert tweet.retweet_of_id == None
		assert tweet.retweet_of_user_screen_name == None
		assert tweet.retweet_of_user_id == None

	def test_user_values(self, tweet):
		assert tweet.user_id == 2891731229
		assert tweet.user_name == u"Soco"
		assert tweet.user_screen_name == u"soco_research"
		assert tweet.user_created_at == u"Tue Nov 25 06:59:06 +0000 2014"
		assert tweet.user_created_ts == datetime(2014, 11, 25, 06, 59, 06)
		assert tweet.user_verified == False
		assert tweet.user_description == u"Student at http://t.co/ClglXIOunF and http://t.co/CDe8EQ72jl $GOOG $ MSFT #hcde #test"
		assert tweet.user_favourites_count == 0
		assert tweet.user_followers_count == 2
		assert tweet.user_friends_count == 0
		assert tweet.user_listed_count == 0
		assert tweet.user_statuses_count == 4
		assert tweet.user_url == u"http://t.co/wxWJj3vC5E"
		assert tweet.user_utc_offset == None

	def test_alias_values(self, tweet):
		assert tweet.favorite_count == tweet.favourite_count
		assert tweet.user_favourites_count == tweet.user_favorites_count

	def test_hashtags_text_list(self, tweet):
		hashtags = tweet.hashtags_text_list
		assert len(hashtags) == 3
		assert hashtags[0] == u'MNMMNN43'
		assert hashtags[1] == u'mas'
		assert hashtags[2] == u'test'

	def test_mentions_text_list(self, tweet):
		mentions = tweet.mentions_text_list
		assert len(mentions) == 2
		assert mentions[0] == u'geosoco'
		assert mentions[1] == u'soco_research'


	def test_mention_id_and_screen_names(self, tweet):
		mentions = tweet.mentions_id_and_screen_name
		assert len(mentions) == 2
		assert mentions[0][0] == 90497936
		assert mentions[0][1] == u'geosoco'
		assert mentions[1][0] == 2891731229
		assert mentions[1][1] == u'soco_research'


	def test_media_text_list(self, tweet):
		media = tweet.media_text_list
		assert len(media) == 2
		assert media[0][0] == u"http://t.co/rpLcXaI1Lr"
		assert media[0][1] == u"http://pbs.twimg.com/media/B-FTwk-CIAEOHqk.jpg"
		assert media[1][0] == u"http://t.co/P7T85U0Iw"
		assert media[1][1] == u"http://pbs.twimg.com/media/B-FKCj5CEAAE6F7.png"


class TestCSVAdapter(BaseTestAdapter):

	@pytest.fixture
	def tweet(self, request):

		csv_reader = CSVTweetReader("tests/data/test_tweet.csv", encoding="utf-8", max_hashtags=5, max_mentions=5, max_urls=5, max_media=5)

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


class TestMongoAdapter(BaseTestAdapter):

	@pytest.fixture
	def tweet(self, request):

		mongo_reader = MongoTweetReader("localhost", "twinkle_unittest_db", "tweets")

		def fin():
			mongo_reader.close()

		request.addfinalizer(fin)

		return list(mongo_reader)[0]

