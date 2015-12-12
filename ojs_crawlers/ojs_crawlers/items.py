# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Problem(scrapy.Item):
    # its remote_id on the online judge
    remote_id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    # the problem description
    statement = scrapy.Field()
    # the date of creation on the online judge
    creation_date = scrapy.Field()
    # indicating its categories (dynamic programming, graph theory, .. etc)
    tags = scrapy.Field()
    # online judge official name
    online_judge = scrapy.Field()
    # some online judges explicitly define each problem difficulty
    difficulty = scrapy.Field()
    # number of users who solved the problem
    solved_count = scrapy.Field()
    # number of wrong tries
    wrong_tries = scrapy.Field()
    # problem level (in case the online judge explicitly specifying it difficulty level)
    # it might be the problems point
    level = scrapy.Field()

