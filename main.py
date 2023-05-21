import sys,json
import pandas as pd
from utils.utils import *

print(sys.argv[1])
# Get the top 5 similar items
similar_items = get_similar_items(sys.argv[1], 10)

data = similar_items.reset_index(drop=True).values.tolist()
result = []
for item in data:
    title, link, price = item
    result.append({"titles": title, "link": link, "price": price})

# Convert dictionary to JSON
json_data = json.dumps(result)

# Print the JSON data
print(json_data)
