#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import simplejson as json
from twinkle.adapters.json_tweet import JSONTweet
from core import register_connector

@register_connector
class JSONReader(object):
    """
    Simple JSON Reader
    """


    def __init__(self, filename, encoding = "utf-8"):
        """

        """
        self.file = io.open(filename, mode="r", encoding=encoding )


    def close(self):
        # close the file if it's open
        if self.file is not None and not self.file.closed:
            self.file.close()
            self.file = None


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
        for line in self.file:
            yield json.loads(line)


@register_connector
class JSONTweetReader(JSONReader):
    """
    """

    def __init__(self, filename, encoding = "utf-8"):
        super(JSONTweetReader, self).__init__(filename, encoding=encoding)


    def __iter__(self):
        """
        return a tweet instead
        """
        for tweet in super(JSONTweetReader, self).__iter__():
            yield JSONTweet(tweet)
            


@register_connector
class JSONWriter(object):
    """
    """

    def __init__(self, filename, encoding="utf-8"):
        self.file = io.open(filename, encoding=encoding)


    def write(self, data_dictionary):
        self.file.write(json.dumps(data_dictionary) + "\n")

    def __del__(self):
        self.file.close()

