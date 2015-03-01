#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import cStringIO
import codecs
import io
from twinkle.adapters.CSVTweet import CSVTweet


class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")



class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self



class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)



class CSVReader(object):
    """
    Simple CSVReader
    """


    def __init__(self, filename, encoding = "utf-8"):
        """

        """
        self.file = io.open(filename, mode="r", encoding=encoding )

        # utf-8 is forced on this line to encode the format so that DictReader can handle it
        self.csvreader = csv.DictReader(codecs.iterencode(self.file, "utf-8"), delimiter=',', quotechar='"')


    def close(self):
        # close the file if it's open
        if self.file is not None and not self.file.closed:
            self.file.close()
            self.csvreader = None
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
        if self.csvreader is not None:
            for line in self.csvreader:
                yield {k:v.decode('utf-8') for k,v in line.items()}



class CSVTweetReader(CSVReader):
    """
    """

    def __init__(self, filename, encoding = "utf-8", has_retweet = False, max_hashtags = 1, max_mentions = 1, max_urls = 1, max_media = 1):
        super(CSVTweetReader, self).__init__(filename, encoding=encoding)
        self.has_retweet = has_retweet
        self.max_hashtags = max_hashtags
        self.max_mentions = max_mentions
        self.max_urls = max_urls
        self.max_media = max_media

    def __iter__(self):
        """
        return a tweet instead
        """
        for row in super(CSVTweetReader, self).__iter__():
            yield CSVTweet(
                row,
                has_retweet = self.has_retweet,
                max_hashtags = self.max_hashtags,
                max_mentions = self.max_mentions,
                max_urls = self.max_urls,
                max_media = self.max_media
                 )


