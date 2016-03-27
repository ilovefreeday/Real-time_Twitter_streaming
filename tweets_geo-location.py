# Tweets Geo-Location on World Map

import csv
import codecs
import gzip
import xml.etree.cElementTree as et
import os
from os.path import dirname, join
​
nan = float('NaN')
__file__ = os.getcwd()
​
data = {}
with gzip.open(join(dirname(__file__), '/data/World_Country_Boundaries.csv.gz')) as f:
    decoded = codecs.iterdecode(f, "utf-8")
    next(decoded)
    reader = csv.reader(decoded, delimiter=',', quotechar='"')
    for row in reader:
        geometry, code, name = row
        xml = et.fromstring(geometry)
        lats = []
        lons = []
        for i, poly in enumerate(xml.findall('.//outerBoundaryIs/LinearRing/coordinates')):
            if i > 0:
                lats.append(nan)
                lons.append(nan)
            coords = (c.split(',')[:2] for c in poly.text.split())
            lat, lon = list(zip(*[(float(lat), float(lon)) for lon, lat in
                coords]))
            lats.extend(lat)
            lons.extend(lon)
        data[code] = {
            'name'   : name,
            'lats'   : lats,
            'lons'   : lons,
        }


import pandas as pd
csv_in = '/Users/YeTian/../spark_tweets_20.csv'
t20_df = pd.read_csv(csv_in, index_col=None, header=0, sep=',', encoding='utf-8')
t20_geo = t20_df[['date', 'lat', 'lon', 'user_name', 'tweet_text']]
