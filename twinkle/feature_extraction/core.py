#!/usr/bin/env python
# -*- coding: utf-8 -*-

import types
from twinkle.connectors.core import ConnectorRegistry


class FeatureExtractorBase(object):
	"""
	Base class for feature extractors
	"""

	def __init__(self):
		pass



class FeatureExtractorRegistry(object):
	"""
	Static class 
	"""

	registry = {}

	@classmethod
	def buildExtractor(cls, name, config_data):
		"""
		method for building 
		"""
		# make sure it exists
		if name not in cls.registry:
			raise Exception("Connector is not registered. ({})"%(name))

		extractor_class = cls.registry[name]

		extractor = extractor_class()
		extractor.configure(config_data)

		return extractor


	@classmethod
	def buildConnector(cls, name, config_data):
		"""
		method for building 
		"""
		# make sure it exists
		if name not in cls.registry:
			raise Exception("Connector is not registered. ({0})".format(name))

		connector_class = cls.registry[name]

		return connector_class(**config_data)

	@classmethod
	def register(cls, name, original_class):
		"""

		"""

		if name is None:
			raise Exception("Attempt to register class as name None")

		# make sure it's not already registered
		if name in ConnectorRegistry.registry:
			raise Exception("Class \"{0}\" has already been registered: ".format(name) )


		cls.registry[name] = original_class

	@classmethod
	def registerQualifiedName(cls, original_class):
		"""

		"""

		modulename = original_class.__module__ if original_class.__module__ != "__main__" else ""
		classname = original_class.__name__

		fullname = (modulename + "." + classname) if modulename else (classname)

		cls.register(fullname, original_class)

	@classmethod
	def registerAsGlobalClass(cls, original_class):
		"""

		"""

		classname = original_class.__name__
		cls.register(classname, original_class)


	@classmethod
	def dumpRegisteredConnectors(cls):
		"""

		"""
		if len(cls.registry) == 0:
			print "{0} has no registered connectors"
		else:
			for name, item in cls.registry.iteritems():
				print name




def register_connector(cls):
	ConnectorRegistry.registerQualifiedName(cls)
	ConnectorRegistry.registerAsGlobalClass(cls)

	return cls



def register_feature_extractor(cls):
	"""

	"""
	FeatureExtractorRegistry.registerQualifiedName(cls)
	FeatureExtractorRegistry.registerAsGlobalClass(cls)

	return cls




