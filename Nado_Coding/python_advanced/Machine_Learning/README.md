# Movie Recommendation System from Nado Coding YouTube


This project is based on the concepts of **demographic filtering**, **content-based filtering**, and **collaborative filtering**. I learned these techniques through the [Nado Coding YouTube lecture](https://youtu.be/TNcfJHajqJY?si=i_WjoBK3znwRx47S), and I applied them in this project to build a movie recommendation system.

## Learning Process

The recommendation techniques implemented in this project are as follows:

- **Demographic Filtering**: In this project, demographic filtering was implemented using a weighted rating formula based on vote count and rating scores. The formula used is:
  
  ```python
  def weighted_rating(x, m=m, C=C):
      v = x['vote_count']
      R = x['vote_average']
      return (v / (v + m) * R) + (m / (m + v) * C)
  ```
  This formula calculates a weighted average where higher vote counts are given more importance in the rating. The result is used to recommend items based on the number of votes and the average ratings.

- **Content-Based Filtering**: Recommending items based on the features or characteristics of the items themselves, such as movie genres, actors, or keywords.
  
- **Collaborative Filtering**: Recommending items based on the preferences and behaviors of similar users, leveraging data from users' interactions or ratings.

## Practical Implementation

For practice, I referred to this [**Kaggle Notebook**](https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system/notebook) that demonstrated the implementation of these techniques, which helped me understand the practical application of these methods.

## Movie Recommendation Web App

As part of this project, I built a simple **movie recommendation web app** using **Streamlit** and **tmdbv3api**. The app allows users to input their preferences or criteria, and it suggests movies based on their selection using collaborative filtering, content-based filtering, and demographic information.

## Technologies Used

- **Streamlit**: For building the web application interface.
- **tmdbv3api**: To access The Movie Database (TMDb) for movie data.
- **Pandas**, **Numpy**: For data manipulation and handling.

## How to Run the Web App

1. Install the required dependencies:
   ```bash
   pip install streamlit tmdbv3api pandas numpy
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

Enjoy exploring movie recommendations!