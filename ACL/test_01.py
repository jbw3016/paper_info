import xml.etree.ElementTree as ET
import os
import numpy as np
import pandas as pd
from function import *

data_dir = r'C:\Users\원종복\Desktop\paper_list\acl\acl-anthology\data\xml'
year = 2023
conference_type = 'acl'
target_volume_id = 'long'

paper_info = load_paper_info(data_dir=data_dir, year=year,
                             conference_type=conference_type,
                             target_volume_id=target_volume_id)

print(paper_info.head())