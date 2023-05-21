import sys,json
import pandas as pd
from utils.utils import *

if __name__ == '__main__':

    # Get the top 10 similar items
    inp = json.loads(sys.argv[1])
    similar_items = get_similar_items(inp['text'], inp['n'])
    
    # Print the JSON data
    print(similar_items)
