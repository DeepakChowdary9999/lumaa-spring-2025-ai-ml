# Movie Recommendation System

## Overview
This is a **content-based movie recommendation system** that suggests movies based on a user's input query. The system compares the user's input description with a dataset of movies using **TF-IDF vectorization** and **cosine similarity** to find the most relevant matches.

## Dataset
- The dataset should be stored in **`dataset.csv`**.
- Ensure that the dataset has the following **columns**:
  - `Title` → Renamed to `title`
  - `Plot` → Renamed to `description`
- The dataset must be placed in the **same directory** as the script.
- If the dataset is missing or incorrectly formatted, an error will be raised.

## Setup Instructions

### **Install Dependencies**
Make sure you have **Python 3.10+** installed. Then, install the required libraries:
```sh
pip install pandas scikit-learn
```

### **Place Dataset**
Ensure the `dataset.csv` file is in the project folder:
```
C:/Users/deepa/Desktop/LUMA/
```

### **Run the Script**
Navigate to the project folder in the terminal and execute:
```sh
python Luma.py
```

---

## How to Use
1. The system will **prompt you to enter a movie preference**:
    Enter your movie preference: I love thrilling sci-fi adventures with deep storylines.
2. Then, you **choose how many recommendations you want (10–20)**:
    How many recommendations do you want? (10-20): 15
3. The system will process your query and **display the top movies** matching your preference!

## Example Output
Enter your movie preference: I love sci-fi adventures with deep character development.
How many recommendations do you want? (10-20): 15
Dataset Loaded Successfully!

Recommended Movies (15 results):
Interstellar - A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival...
The Martian - An astronaut becomes stranded on Mars and must rely on his ingenuity to survive...
Blade Runner 2049 - A young blade runner discovers a long-buried secret that could unravel society...


## Customization
- **Change the number of recommendations**: Modify the `top_n` parameter in the function `recommend_movies(user_input, top_n=10)`.
- **Use a different dataset**: Replace `dataset.csv` with a new dataset, ensuring it has `title` and `description` columns.

---
** Author:** Deepak's Movie Recommender System

