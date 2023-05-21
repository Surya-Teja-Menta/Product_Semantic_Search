import sys,json
import pandas as pd
from utils.utils import *

if __name__ == '__main__':

    # Get the top 10 similar items
    similar_items = get_similar_items(sys.argv[1], 10)
    
    # Print the JSON data
    print(similar_items)
