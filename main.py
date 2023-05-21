import sys,pickle
import pandas as pd
from utils.utils import *


# Get the top 5 similar items
similar_items = get_similar_items(sys.argv[1], 10)

print(similar_items.reset_index(drop=True).to_json(orient='records', indent=4))

