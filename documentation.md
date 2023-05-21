# Product Similarity Search

The goal of this project is to create a machine learning model capable of receiving text describing a clothing item and returning a ranked list of links to similar items from different websites. Your solution must be a function deployed on Google Cloud that accepts a text string and returns JSON responses with ranked suggestions.



## utils.py

This module contains two functions: `get_model()` and `get_similar_items()`.

### get_model()

This function returns a SentenceTransformer model. A SentenceTransformer model is a pre-trained model that can be used to encode text into a vector representation. This vector representation can then be used to calculate the similarity between two pieces of text.

### get_similar_items()

This function gets the top 10 similar items for the given item. The similarity between two items is calculated using the cosine similarity metric. The cosine similarity metric measures the similarity between two vectors by taking the dot product of the vectors and dividing by the product of their magnitudes.

The `get_similar_items()` function takes two arguments:

* `text`: The item to get similar items for.
* `n`: The number of similar items to get. Defaults to 10.

The `get_similar_items()` function returns a JSON string containing the top N most similar items. The JSON string has the following format:

```
[
  {
    "title": "Title of the first similar item",
    "link": "Link to the first similar item",
    "price": "Price of the first similar item"
  },
  {
    "title": "Title of the second similar item",
    "link": "Link to the second similar item",
    "price": "Price of the second similar item"
  },
  ...
]
```

## main.py

This module imports the `utils.py` module and calls the `get_similar_items()` function. The `get_similar_items()` function is called with the first argument from the command line as the `text` argument. The `get_similar_items()` function returns a JSON string containing the top 10 most similar items. The JSON string is then printed to the console.

## requirements.txt

This file contains a list of the Python packages that are required to run the code.

## Dockerfile

This file is used to build a Docker image that contains the code and all of the required Python packages. The Docker image can then be used to run the code on any machine that has Docker installed.

This file defines a Docker image that can be used to run the code. The Docker image is built using the following steps:

1. A Python 3.7-slim image is created.
2. The pip3 package manager is updated to the latest version.
3. The pandas package is installed.
4. The requirements.txt file is copied to the Docker image.
5. The torch and torchvision packages are installed.
6. The requirements.txt file is installed.
7. The contents of the current directory are copied to the Docker image.
8. The python command is used to run the main.py file.
Once the Docker image is built, it can be run using the following command:

```
docker run -it my_image
```
This will run the main.py file and print the JSON representation of the top 10 similar items to the console.

