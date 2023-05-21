import pandas as pd,numpy as np,json
from sentence_transformers import SentenceTransformer,util
import pickle
from sklearn.metrics.pairwise import cosine_similarity

def get_model():
    """
    This function returns a SentenceTransformer model.
    """
    return SentenceTransformer('all-MiniLM-L6-v2')

def get_similar_items(text, n=10):
    """
    This function gets the top 10 similar items for the given item.

    Args:
        text (str): The item to get similar items for.
        n (int, optional): The number of similar items to get. Defaults to 10.

    Returns:
        str: A JSON string containing the top N most similar items.
    """
    text = text.lower()
    with open('utils/stopwords.pkl', 'rb') as file:
        stopwords = pickle.load(file)
        file.close()
    df = pd.DataFrame(np.load('data/df1.npy',allow_pickle = True),columns = ['title','link','price','embedding','score'])
    text = ' '.join([x for x in text.split() if x not in stopwords])
    model = get_model()
    embedds = model.encode(text)
    df["score"] = df.embedding.apply(lambda x: util.cos_sim(x, embedds))
    top_n =df.sort_values(["score"], ascending=False).head(n)

    similar_items =top_n[['title','link','price']]
    data = similar_items.reset_index(drop=True).values.tolist()

    # Create a list of dictionaries.
    result = []
    for item in data:
        title, link, price = item
        result.append({"titles": title, "link": link, "price": price})

    # Convert the list of dictionaries to JSON.
    return json.dumps(result)

    

