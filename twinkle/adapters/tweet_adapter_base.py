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
		Tweet creation date
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
		User's creation date
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
	def user_favorites_count(self):
		"""
		User's count of favorites
		"""
		return None



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
	def user_utf_offset(self):
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
		Tweet hashtags
		"""
		return None



	@property
	def mentions(self):
		"""
		Tweet mentions
		"""
		return None


	@property
	def urls(self):
		"""
		Tweet urls
		"""
		return None


	@property
	def media(self):
		"""
		Tweet urls
		"""
		return None




