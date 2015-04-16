#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simplejson as json

from twinkle.feature_extraction.core import FeatureExtractorBase, register_feature_extractor, FeatureExtractorRegistry
from twinkle.feature_extraction.pipelines import FeatureExtractorPipelineFactory
from twinkle.connectors.csv_connector import CSVReader, CSVTweetReader
from twinkle.connectors.json_connector import JSONReader, JSONTweetReader

from twinkle.connectors.core import ConnectorRegistry



@register_feature_extractor
class PropertyExtractor(object):

	def __init__(self):
		"""

		"""
		self.props = []


	def configure(self, config_data):
		"""
		configure the extractor from a dictionary
		"""
		if "properties" in config_data:
			self.props = config_data["properties"]
		

	def extract(self, data, cookie, output):
		"""
		configure extractor
		"""

		for prop in self.props:
			output[ prop["output_name"] ] = getattr(data, prop["property_name"])


@register_feature_extractor
class TweetLengthExtractor(object):

	def __init__(self):
		self.word_groups = []

	def configure(self, config_data):
		if "word_groups" in config_data:
			self.word_groups = config_data["word_groups"]

	def extract(self, data, cookie, output):
		"""
		extract
		"""

		output["tweet_length_with_spaces"] = len(data.text)
		output["tweet_length_no_spaces"] = len(data.text.replace(" ", ""))

@register_feature_extractor
class CharacterCountsExtractor(object):

	def __init__(self):
		self.word_groups = []

	def configure(self, config_data):
		if "word_groups" in config_data:
			self.word_groups = config_data["word_groups"]

	def extract(self, data, cookie, output):
		"""
		extract
		"""
		text_upper = data.text.upper()

		output["hashtags_counts"] = data.text.count('#')
		output["url_counts"] = text_upper.count('HTTP')
		output["exclamation_counts"] = data.text.count('!')



@register_feature_extractor
class WordFeaturesExtractor(object):

	def __init__(self):
		self.word_groups = []

	def configure(self, config_data):
		if "word_groups" in config_data:
			self.word_groups = config_data["word_groups"]

	def extract(self, data, cookie, output):

		#get a list of words
		word_list = data.text.split(" ")

		cum_word_length = 0
		max_word_length = 0

		#loop through the words in the list
		for word in word_list:
			#get length of the word
			word_length = len(word)
			cum_word_length += word_length

			#check if this word is longe than the longest so far
			if word_length>max_word_length:
				#set the new max length of the word if it is
				max_word_length = word_length

		output["word_count"] = len(word_list)
		output["average_word_length"] = cum_word_length/len(word_list)
		output["max_word_length"] = max_word_length


with open("pipeline.json") as f:
	pipeline_conf = json.load(f)

pfactory = FeatureExtractorPipelineFactory()

pipeline = pfactory.buildFromDictionary(pipeline_conf)

pipeline.run()

quit()



"""
print("building {}"%(pipeline_conf["input"]["name"]	))
reader = pfactory.buildInput(pipeline_conf["input"]["name"], pipeline_conf["input"]["config"])
print reader
for tweet in reader:
	print tweet.text

quit()


reader = CSVTweetReader.createFromDictionary(pipeline_conf["input"]["config"])
print reader
for tweet in reader:
	print tweet.text

quit()

csv_reader = CSVTweetReader("../../tests/data/test_tweet.csv", encoding="utf-8", max_hashtags=5, max_mentions=5, max_urls=5, max_media=5)


# prepare extractors
extractors = []

e = PropertyExtractor()
e.configure(prop_config)
extractors.append(e)

output_list = []

# run the pipeline
for tweet in csv_reader:
	cookie = { "tweet": tweet, "text": tweet.text }
	output = {}
	for ex in extractors:
		ex.extract( tweet, cookie, output )

	output_list.append(output)


print output_list
"""

