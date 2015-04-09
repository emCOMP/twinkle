#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import FeatureExtractorRegistry
from twinkle.connectors.core import ConnectorRegistry


class FeatureExtractorPipelineFactory(object):
	"""
	Factory object for creating a pipeline from a file

	"""

	def __init__(self):
		"""

		"""

		pass

	def buildInput(self, config_data):
		"""
		builds an input from the ConnectorRegistry
		"""

		input_name = config_data["name"]
		input_config = config_data["config"]

		return ConnectorRegistry.buildConnector(input_name, input_config)



	def buildOutput(self, config_data):
		"""
		builds na output from the connectorRegister
		"""
		output_name = config_data["name"]
		output_config = config_data["config"]

		return ConnectorRegistry.buildConnector(output_name, output_config)


	def buildExtractor(self, config_data):
		"""
		"""
		extractor_name = config_data["name"]
		extractor_config = config_data["config"]

		return FeatureExtractorRegistry.buildExtractor(extractor_name, extractor_config)


	def buildFromDictionary(self,config_data):
		"""

		"""
		if "input" not in config_data:
			raise Exception("No input source was specified in the configuration data")

		if "output" not in config_data:
			raise Exception("No output source was specified in the configuration data")

		#build input
		input_data = config_data["input"]
		input = self.buildInput(input_data)

		# build output
		output_data = config_data["output"]
		output = self.buildOutput(output_data)

		# create the pipeline
		pipeline = FeatureExtractorPipeline(input, output)

		# get feature extractors
		extractors = config_data["extractors"]

		# add each extractor
		for extractor_config in extractors:
			extractor = self.buildExtractor(extractor_config)
			pipeline.addExtractor(extractor)


		return pipeline





class FeatureExtractorPipeline(object):
	"""
	Simple feature extractor pipeline.

	Needs a lot of features in the future such as dependency graphs to resolve some of the intermediates
	and the ability to do second passes for items which need to be normalized. 
	"""

	def __init__(self, input, output):
		self.feature_extractors = []
		self.input = input
		self.output = output



	def addExtractor(self, extractor):
		"""
		add Extractor to the pipeline
		"""
		self.feature_extractors.append(extractor)


	def run(self):
		"""
		runs the pipeline
		"""

		processed_items = []

		# iterate through each item
		for item in self.input:
			item_cookie = { "tweet": item, "text": item.text}
			output = {}

			# first do preprossing
			for extractor in self.feature_extractors:
				extractor.extract(item, item_cookie, output)

			print output

			# write output
			self.output.write(output)



