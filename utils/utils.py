import pandas as pd
from sentence_transformers import SentenceTransformer
import pickle
from sklearn.metrics.pairwise import cosine_similarity

def get_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def get_similar_items(text, n=10):
    """
    Get top 10 similar items for the given item
    """
    text = text.lower()
    with open('utils/stopwords.pkl', 'rb') as file:
        stopwords = pickle.load(file)
        file.close()
    df = pd.read_pickle('data/final_myntra3.pkl')
    text = ' '.join([x for x in text.split() if x not in stopwords])
    model = get_model()
    embedds = model.encode(text)
    df["score"] = df.embedding.apply(lambda x: cosine_similarity(x, embedds))
    top_n =df.sort_values(["score"], ascending=False).head(n)
    return top_n[['title','link-href','price']]

    

