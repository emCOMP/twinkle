#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ConnectorRegistry(object):
	"""
	Static class 
	"""

	registry = {}

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


"""
def register_connector(shortname = None, as_global_class = False):

	def register(cls):
		ConnectorRegistry.registerQualifiedName(cls)
		if shortname is not None:
			ConnectorRegistry.register(shortname, cls)

		if as_global_class == True:
			ConnectorRegistry.registerAsGlobalClass(cls)

		return cls
	return register
"""
