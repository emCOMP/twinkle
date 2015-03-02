#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TweetAdapterBase(object):

	def __init__(self):
		pass


	@property
	def id(self):
		"""
		Tweet Id
		"""		
		return None


	@property
	def text(self):
		"""
		Tweet Text
		"""
		return None


	@property
	def source(self):
		"""
		Tweet source
		"""
		return None
	

	@property
	def in_reply_to_status_id(self):
		"""
		Tweet reply to status id
		"""
		return None


	@property
	def in_reply_to_user_id(self):
		"""
		Tweet reply to user id
		"""
		return None


	@property
	def in_reply_to_user_screen_name(self):
		"""
		Tweet reply to user screen name
		"""
		return None		

	

	@property
	def coordinates(self):
		"""
		Tweet tweet coordinates
		"""
		return None


	@property
	def created_at(self):
		"""
		Tweet creation date in Twitter format as a string
		"""
		return None

	@property
	def created_ts(self):
		"""
		Tweet creation date as a datetime object
		"""
		return None

	@property
	def lang(self):
		"""
		Tweet lang
		"""
		return None


	@property
	def retweet_count(self):
		"""
		Tweet retweet count
		"""
		return None


	@property
	def favorite_count(self):
		"""
		Tweet favorite count
		"""
		return None

	@property
	def favourite_count(self):
		"""
		alias for favorite_count
		"""
		return self.favorite_count


	@property
	def retweet_of_id(self):
		"""
		if retweet, original tweet id
		"""
		return None


	@property
	def retweet_of_user_screen_name(self):
		"""
		if retweet, original tweet user's screen name
		"""
		return None

	@property
	def retweet_of_user_id(self):
		"""
		if retweet, original tweet user's id
		"""
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
		return None


	@property
	def user_name(self):
		"""
		Tweet user name
		"""
		return None


	@property
	def user_screen_name(self):
		"""
		Tweet user screen name
		"""
		return None


	@property
	def user_created_at(self):
		"""
		User's creation date as original twitter string
		"""
		return None

	def user_created_ts(self):
		"""
		User's creation date as a timestamp
		"""
		return None

	@property
	def user_verified(self):
		"""
		User's verification status
		"""
		return None


	@property
	def user_description(self):
		"""
		User's description
		"""
		return None


	@property
	def user_favourites_count(self):
		"""
		User's count of favourites
		"""
		return None

	@property
	def user_favorites_count(self):
		"""
		alias for favourites count
		"""
		return self.user_favourites_count



	@property
	def user_followers_count(self):
		"""
		User's count of followers
		"""
		return None


	@property
	def user_friends_count(self):
		"""
		User's friends count
		"""
		return None


	@property
	def user_listed_count(self):
		"""
		Number of lists the user is on 
		"""
		return None


	@property
	def user_statuses_count(self):
		"""
		Number of status user has 
		"""
		return None


	@property
	def user_url(self):
		"""
		User's listed url
		"""
		return None


	@property
	def user_utc_offset(self):
		"""
		UTC offset of user's profile
		"""
		return None



	#
	#
	# entities
	#
	#



	@property
	def hashtags(self):
		"""
		Tweet hashtags in its raw format
		"""
		return None

	@property
	def hashtags_text_list(self):
		"""
		returns a list of only the hashtag text for each hashtag
		"""
		return None

	@property
	def mentions(self):
		"""
		Tweet mentions
		"""
		return None

	@property
	def mentions_text_list(self):
		"""
		returns a list of only the mention screen names
		"""
		return None

	@property
	def mentions_id_and_screen_name(self):
		"""
		returns a list of mentions with the mentioned user's id and their screen_name
		"""
		return None


	@property
	def urls(self):
		"""
		Tweet urls
		"""
		return None

	@property
	def urls_simple_list(self):
		"""
		returns a list of pairs of urls (url, expanded_url)
		"""
		return None


	@property
	def media(self):
		"""
		Tweet urls objects in raw format
		"""
		return None

	@property
	def media_simple_list(self):
		"""
		returns a list of pairs of urls (url, expanded_url)
		"""

		return None




