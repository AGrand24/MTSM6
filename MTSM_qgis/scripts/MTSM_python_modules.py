import traceback

# try:
import pandas as pd
import geopandas as gpd
import numpy as np
import os
import shutil
import warnings
from lxml import etree
from tabulate import tabulate
import re
from datetime import datetime,timedelta,time
import time
import errno, stat
import ppigrf
from shapely import Point,Polygon,LineString,MultiPolygon,MultiLineString
from pathlib import Path

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore', 'GeoSeries.notna', UserWarning)
pd.set_option('mode.chained_assignment', None)
# except Exception as error:
# 	traceback.print_exc()
# 	input('Press ENTER to continue!')

