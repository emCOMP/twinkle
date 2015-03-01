#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import simplejson as json
from twinkle.adapters.JSONTweet import JSONTweet
from pymongo import MongoClient


class MongoReader(object):
    """
    Mongo Reader
    """


    def __init__(self, host, database, collection, port=27017, query=None):
        """
        initialize the mongodb reader
        """
        self.client = MongoClient(host, port)
        self.db = self.client[database]
        self.collection = self.db[collection]

        if query is not None:
            self.cursor = self.collection.find(query)
        else:
            self.cursor = self.collection.find()


    def close(self):
        """
        Close the connection
        """

        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None

        if self.client is not None:
            self.client.close()
            self.client = None


    def __enter__(self):
        """
        """
        return(self)


    def __exit__(self, exception_type, exception_value, traceback):
        """
        """
        try:
            self.close()

        finally:
            pass


    def __iter__(self):
        """
        make it iterable
        """
        for tweet in self.cursor:
            yield tweet





class MongoTweetReader(MongoReader):
    """
    """

    def __init__(self, host, database, collection, port=27017, query=None):
        super(MongoTweetReader, self).__init__(host, database, collection, port=port, query=query)


    def __iter__(self):
        """
        return a tweet instead
        """
        for tweet in super(MongoTweetReader, self).__iter__():
            yield JSONTweet(tweet)
            

