#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TwitterTextRemover(object):
	"""
	Class that removes elements other than plain text and emoticons (urls, mentions, retweet, urls, punctuation )
	"""

	re_strip_rt = re.compile(u'(RT|Via|MT|\(?from\s?\)?|) @\w+\:?\s', flags=re.IGNORECASE)
	re_strip_mention = re.compile(u'(via\s)?@\w+', flags=re.IGNORECASE)
	re_strip_cc = re.compile(u'-CC', flags=re.IGNORECASE)
	re_strip_url = re.compile(u'(?i)\b((?:https?:?//|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', flags=re.IGNORECASE)
	re_strip_tco_url = re.compile(u'https?:?//[\w\-\.]*(/[\w\-\%]*)*( via)?', flags=re.IGNORECASE)
	re_strip_punct = re.compile(u'[\.,;\:\-\!\[\]\"\?\(\)\|@\/]', flags=re.IGNORECASE)
	re_strip_newline = re.compile(u'[\r\n\t]+')
	re_strip_ending_http = re.compile(u'(\s)ht?t?t?p?:?/?/?([\w\-\.]*)?\s?$', flags=re.IGNORECASE)



	def __init__( self, strip_retweets = True, strip_mentions = True, strip_cc = True, strip_url = True, strip_tco_urls = True, strip_punct = True, strip_newline = True, strip_ending_http = True ):
		"""
		initializes the text remover
		"""
		self.regex_list = []
		if strip_retweets:
			self.regex_list.append(self.re_strip_rt)
		if strip_mentions:
			self.regex_list.append(self.re_strip_mention)
		if strip_cc:
			self.regex_list.append(self.re_strip_cc)
		if strip_url:
			self.regex_list.append(self.re_strip_url)
		if strip_tco_urls:
			self.regex_list.append(self.re_strip_tco_url)
		if strip_punct:
			self.regex_list.append(self.re_strip_punct)
		if strip_newline:
			self.regex_list.append(self.re_strip_newline)
		if strip_ending_http:
			self.regex_list.append(self.re_strip_ending_http)


	def strip(self, text):
		"""
		function to actually strip text
		"""
		if text is None:
			return None

		for regex in self.regex_list:
			text = regex.sub(' ', text)
		return text
