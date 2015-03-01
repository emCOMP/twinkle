#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import simplejson as json
from twinkle.adapters.JSONTweet import JSONTweet


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
            

