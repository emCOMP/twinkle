#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simplejson as json

from twinkle.feature_extraction.core import FeatureExtractorBase, register_feature_extractor, FeatureExtractorRegistry
from twinkle.feature_extraction.pipelines import FeatureExtractorPipelineFactory
from twinkle.connectors.csv_connector import CSVReader, CSVTweetReader
from twinkle.connectors.json_connector import JSONReader, JSONTweetReader
from twinkle.connectors.mongo_connector import MongoReader, MongoTweetReader

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
			value = getattr(data, prop["property_name"])
			output[ prop["output_name"] ] = value if value is not None else ""


@register_feature_extractor
class WordCountExtractor(object):

	def __init__(self):
		self.word_groups = []

	def configure(self, config_data):
		if "word_groups" in config_data:
			self.word_groups = config_data["word_groups"]

	def extract(self, data, cookie, output):
		"""
		extract
		"""

		output["word_count"] = len(data.text.split(" "))




ConnectorRegistry.dumpRegisteredConnectors()

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

