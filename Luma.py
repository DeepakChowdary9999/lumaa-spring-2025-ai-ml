import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_dataset():
    file_path = "C:/Users/deepa/Desktop/LUMA/dataset.csv"  # Update with the correct path
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset file not found at {file_path}")
    
    df = pd.read_csv(file_path)
    df.rename(columns={"Title": "title", "Plot": "description"}, inplace=True)
    required_columns = {'title', 'description'}
    if not required_columns.issubset(df.columns):
        raise KeyError(f"Dataset must contain {required_columns} columns, found: {df.columns}")
    
    df['description'] = df['description'].fillna("")
    print(" Dataset Loaded Successfully!")
    
    return df

def recommend_movies(user_input, top_n=15):
    df = load_dataset()
    documents = df['description'].tolist() + [user_input]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    if tfidf_matrix.shape[1] == 0:
        print(" No valid words found in descriptions or input!")
        return pd.DataFrame()  # Return an empty DataFrame
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    top_n = min(top_n, len(df))  # Prevent index errors
    top_indices = cosine_sim.argsort()[0][-top_n:][::-1]
    recommendations = df.iloc[top_indices]
    
    print("\n Recommended Movies:")
    for index, row in recommendations.iterrows():
        print(f" {row['title']} - {row['description'][:100]}...")
    
    return recommendations[['title', 'description']]

if __name__ == "__main__":
    user_query = input(" Enter your movie preference: ")
    recommended_movies = recommend_movies(user_query)

    print("\n Final Recommendations:")
    print(recommended_movies)
    
