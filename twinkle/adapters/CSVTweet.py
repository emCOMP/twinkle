#!/usr/bin/python
# -*- coding: utf-8 -*-

from TweetAdapterBase import TweetAdapterBase



class CSVTweet(TweetAdapterBase):

	def __init__(
			self, 
			row,
			has_retweet = False,
			max_hashtags = 1, 	
			max_mentions = 1,
			max_urls = 1, 
			max_media = 0):

		self.row = row
		self.has_retweet = has_retweet
		self.max_hashtags = max_hashtags
		self.max_mentions = max_mentions
		self.max_urls = max_urls
		self.max_media = max_media

	def safe_get_column(self, column):
		return self.row[column] if column in self.row else None


	def safe_get_int_column(self, column):
		return int(self.row[column]) if column in self.row else None


	@property
	def id(self):
		"""
		Tweet Id
		"""		
		return self.safe_get_int_column("id")


	@property
	def text(self):
		"""
		Tweet Text
		"""
		return self.safe_get_column("text")


	@property
	def source(self):
		"""
		Tweet source
		"""
		return self.safe_get_column("source")
	

	@property
	def in_reply_to_status_id(self):
		"""
		Tweet reply to status id
		"""
		return self.safe_get_int_column("in_reply_to_status_id")


	@property
	def in_reply_to_user_id(self):
		"""
		Tweet reply to user id
		"""
		return self.safe_get_int_column("in_reply_to_user_id")


	@property
	def in_reply_to_user_screen_name(self):
		"""
		Tweet reply to user screen name
		"""
		return self.safe_get_column("in_reply_to_screen_name")		


	@property
	def source(self):
		"""
		Tweet source
		"""
		return self.safe_get_column("source")
	

	@property
	def coordinates(self):
		"""
		Tweet tweet coordinates
		"""
		return (self.safe_get_column("coordinates.coordinates.0"),self.safe_get_column("coordinates.coordinates.1"))


	@property
	def created_at(self):
		"""
		Tweet creation date
		"""
		return self.safe_get_column("created_ts")



	@property
	def lang(self):
		"""
		Tweet lang
		"""
		return self.safe_get_column("lang")


	@property
	def retweet_count(self):
		"""
		Tweet retweet count
		"""
		return self.safe_get_int_column("retweet_count") if self.has_retweet else None


	@property
	def favorite_count(self):
		"""
		Tweet favorite count
		"""
		return self.safe_get_int_column("favorite_count")



	@property
	def retweet_of_id(self):
		"""
		if retweet, original tweet id
		"""
		return self.safe_get_int_column("retweeted_status.id") if self.has_retweet else None


	@property
	def retweet_of_user_screen_name(self):
		"""
		if retweet, original tweet user's screen name
		"""
		return self.safe_get_column("retweeted_status.user.screen_name") if self.has_retweet else None

	@property
	def retweet_of_user_id(self):
		"""
		if retweet, original tweet user's id
		"""
		return self.safe_get_int_column("retweeted_status.user.id") if self.has_retweet else None


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
		return self.safe_get_int_column("user.id")


	@property
	def user_name(self):
		"""
		Tweet user name
		"""
		return self.safe_get_column("user.name")


	@property
	def user_screen_name(self):
		"""
		Tweet user screen name
		"""
		return self.safe_get_column("user.screen_name")


	@property
	def user_created_at(self):
		"""
		User's creation date
		"""
		return self.safe_get_column("user.created_ts")

	@property
	def user_verified(self):
		"""
		User's verification status
		"""
		return self.safe_get_column("user.verified")


	@property
	def user_description(self):
		"""
		User's description
		"""
		return self.safe_get_column("user.description")


	@property
	def user_favorites_count(self):
		"""
		User's count of favorites
		"""
		return self.safe_get_int_column("user.favorites_count")



	@property
	def user_followers_count(self):
		"""
		User's count of followers
		"""
		return self.safe_get_int_column("user.followers_count")


	@property
	def user_friends_count(self):
		"""
		User's friends count
		"""
		return self.safe_get_int_column("user.friends_count")



	@property
	def user_listed_count(self):
		"""
		Number of lists the user is on 
		"""
		return self.safe_get_int_column("user.listed_count")


	@property
	def user_statuses_count(self):
		"""
		Number of status user has 
		"""
		return self.safe_get_int_column("user.statuses_count")


	@property
	def user_url(self):
		"""
		User's listed url
		"""
		return self.safe_get_column("user.url")


	@property
	def user_utf_offset(self):
		"""
		UTC offset of user's profile
		"""
		return self.safe_get_int_column("user.utc_offset")



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
		if self._hashtags:
			return self._hashtags
		else:
			self._hashtags = [self.row["entities.hashtags.%d.text"%i] for i in range(self.max_hashtags)]
			return self._hashtags



	@property
	def mentions(self):
		"""
		Tweet mentions
		"""
		if self._mentions:
			return self._mentions
		else:
			self._mentions = [self.row["entities.user_mentions.%d.text"%i] for i in range(self.max_mentions)]
			return self._mentions



	@property
	def urls(self):
		"""
		Tweet urls
		"""
		if self._urls:
			return self._urls
		else:
			self._urls = [self.row["entities.urls.%d.text"%i] for i in range(self.max_urls)]
			return self._urls



	@property
	def media(self):
		"""
		Tweet urls
		"""
		if self._media:
			return self._media
		else:
			self._media = [self.row["entities.media.%d.url"%i] for i in range(self.max_media)]
			return self._media






