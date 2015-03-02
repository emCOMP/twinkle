#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tweet_adapter_base import TweetAdapterBase
from datetime import datetime
import email.utils

def convertRFC822ToDateTime(rfc822string):
	"""
		convert an RFC822 date to a datetime
	"""
	return datetime.utcfromtimestamp(email.utils.mktime_tz(email.utils.parsedate_tz(rfc822string)))


class JSONTweet(TweetAdapterBase):

	def __init__(
			self, 
			obj):

		self.obj = obj



	@property
	def id(self):
		"""
		Tweet Id
		"""		
		return self.obj["id"]


	@property
	def text(self):
		"""
		Tweet Text
		"""
		return self.obj["text"]


	@property
	def source(self):
		"""
		Tweet source
		"""
		return self.obj["source"]
	

	@property
	def in_reply_to_status_id(self):
		"""
		Tweet reply to status id
		"""
		return self.obj["in_reply_to_status_id"]


	@property
	def in_reply_to_user_id(self):
		"""
		Tweet reply to user id
		"""
		return self.obj["in_reply_to_user_id"]


	@property
	def in_reply_to_user_screen_name(self):
		"""
		Tweet reply to user screen name
		"""
		return self.obj["in_reply_to_screen_name"]		


	@property
	def source(self):
		"""
		Tweet source
		"""
		return self.obj["source"]
	

	@property
	def coordinates(self):
		"""
		Tweet tweet coordinates
		"""
		if "coordinates" in self.obj["coordinates"] and self.obj["coordinates"]["coordinates"]:
			return (self.obj["coordinates"]["coordinates"][0],self.obj["coordinates"]["coordinates"][1])
		return None


	@property
	def created_at(self):
		"""
		Tweet creation date in twitter formatted string
		"""
		return self.obj["created_at"]


	@property
	def created_ts(self):
		"""
		Tweet creation date as timestamp
		"""
		if "created_ts" in self.obj:
			return self.obj["created_ts"]
		else:
			return convertRFC822ToDateTime(self.obj["created_at"])


	@property
	def lang(self):
		"""
		Tweet lang
		"""
		return self.obj["lang"]


	@property
	def retweet_count(self):
		"""
		Tweet retweet count
		"""
		return self.obj["retweet_count"]


	@property
	def favorite_count(self):
		"""
		Tweet favorite count
		"""
		return self.obj["favorite_count"]



	@property
	def retweet_of_id(self):
		"""
		if retweet, original tweet id
		"""
		if "retweeted_status" in self.obj:
			return self.obj["retweeted_status"]["id"]
		return None



	@property
	def retweet_of_user_screen_name(self):
		"""
		if retweet, original tweet user's screen name
		"""
		if "retweeted_status" in self.obj:
			return self.obj["retweeted_status"]["user"]["screen_name"]
		return None

	@property
	def retweet_of_user_id(self):
		"""
		if retweet, original tweet user's id
		"""
		if "retweeted_status" in self.obj:
			return self.obj["retweeted_status"]["user"]["id"]
		return None


	#
	#
	# User Attributes
	#
	#

	@property
	def user_id(self):
		"""
		Tweet user id
		"""
		return self.obj["user"]["id"]


	@property
	def user_name(self):
		"""
		Tweet user name
		"""
		return self.obj["user"]["name"]


	@property
	def user_screen_name(self):
		"""
		Tweet user screen name
		"""
		return self.obj["user"]["screen_name"]


	@property
	def user_created_at(self):
		"""
		User's creation date as a twitter formatted string
		"""
		return self.obj["user"]["created_at"]

	@property
	def user_created_ts(self):
		"""
		User's creation date as a timestamp
		"""
		if "created_ts" in self.obj["user"]:
			return self.obj["user"]["created_ts"]
		else:
			return convertRFC822ToDateTime(self.obj["user"]["created_at"])



	@property
	def user_verified(self):
		"""
		User's verification status
		"""
		return self.obj["user"]["verified"]


	@property
	def user_description(self):
		"""
		User's description
		"""
		return self.obj["user"]["description"]


	@property
	def user_favourites_count(self):
		"""
		User's count of favorites
		"""
		return self.obj["user"]["favourites_count"]



	@property
	def user_followers_count(self):
		"""
		User's count of followers
		"""
		return self.obj["user"]["followers_count"]


	@property
	def user_friends_count(self):
		"""
		User's friends count
		"""
		return self.obj["user"]["friends_count"]



	@property
	def user_listed_count(self):
		"""
		Number of lists the user is on 
		"""
		return self.obj["user"]["listed_count"]


	@property
	def user_statuses_count(self):
		"""
		Number of status user has 
		"""
		return self.obj["user"]["statuses_count"]


	@property
	def user_url(self):
		"""
		User's listed url
		"""
		return self.obj["user"]["url"]


	@property
	def user_utc_offset(self):
		"""
		UTC offset of user's profile
		"""
		return self.obj["user"]["utc_offset"]



	#
	#
	# entities
	#
	#



	@property
	def hashtags(self):
		"""
		Tweet hashtags
		"""
		return self.obj["entities"]["hashtags"]

	@property
	def hashtags_text_list(self):
		"""
		returns a list of only the hashtag text for each hashtag
		"""
		return [h['text'] for h in self.obj["entities"]["hashtags"]]

	@property
	def mentions(self):
		"""
		Tweet mentions
		"""
		return self.obj["entities"]["user_mentions"]

	@property
	def mentions_text_list(self):
		"""
		returns a list of only the mention screen names
		"""
		return [m['screen_name'] for m in self.obj["entities"]["user_mentions"]]

	@property
	def mentions_id_and_screen_name(self):
		"""
		returns a list of mentions with the mentioned user's id and their screen_name
		"""
		return [(m['id'], m['screen_name']) for m in self.obj["entities"]["user_mentions"]]		

	@property
	def urls(self):
		"""
		Tweet urls
		"""
		return self.obj["entities"]["urls"]

	@property
	def urls_simple_list(self):
		"""
		returns a list of pairs of urls (url, expanded_url)
		"""
		return None		


	@property
	def media(self):
		"""
		Tweet urls
		"""
		return self.obj["entities"]["media"]


	@property
	def media_simple_list(self):
		"""
		returns a list of pairs of urls (url, expanded_url)
		"""

		return [(m['url'], m['media_url']) for m in self.obj["entities"]["media"]]



