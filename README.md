# Movie Recommender System

A content-based movie recommendation system built with Python and Streamlit. It recommends five movies similar to a movie selected by the user and displays their posters using The Movie Database (TMDB) API.

## Features

- **Content-based recommendations:** Recommends movies using precomputed similarity scores.
- **Cosine similarity:** Uses similarity scores to rank movies by relevance.
- **Interactive interface:** Select a movie from a dropdown and view recommendations.
- **Movie posters:** Fetches poster images from the TMDB API.
- **Precomputed results:** Loads serialized movie data and a similarity matrix instead of recalculating similarities for every request.
- **Error handling:** Handles failed poster requests and unavailable poster images.

## Tech Stack

- **Language:** Python
- **Data Processing:** Pandas
- **Machine Learning:** Cosine Similarity
- **Web Interface:** Streamlit
- **API Integration:** TMDB API
- **Serialization:** Pickle

## Project Structure

```text
movie_recommender/
├── app.py
├── movierecommenderpr1 (2).ipynb
├── requirements.txt
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── movies.pkl
└── similarity.pkl
```

**Note:** `movies.pkl` and `similarity.pkl` are required by `app.py`. They must be generated using the notebook or supplied separately. They are shown here as required runtime artifacts, not as files guaranteed to be present in the public repository.

## How It Works

### 1. Data Preparation

The project includes the TMDB 5000 Movies and Credits datasets. The notebook is used for data preparation and building the recommendation data.

### 2. Similarity Calculation

The recommendation pipeline represents movies numerically and compares them using cosine similarity. The resulting similarity scores are saved in a matrix.

### 3. Loading Saved Data

The application loads two serialized Python objects:

- `movies.pkl`: Contains the processed movie information.
- `similarity.pkl`: Contains the precomputed movie-to-movie similarity scores.

### 4. Generating Recommendations

When a user selects a movie:

1. The application finds the movie's index in the dataset.
2. It retrieves that movie's similarity scores.
3. It sorts the scores in descending order.
4. It skips the selected movie and retrieves the next five results.
5. It returns the recommended movie titles and poster URLs.

### 5. Displaying Movie Posters

The application uses each recommended movie's TMDB ID to request its details from the TMDB API. It extracts the poster path and constructs the image URL for display in Streamlit.

## Installation and Setup

### Prerequisites

- Python 3.9 or a compatible version supported by your dependencies.
- pip
- A TMDB API key

### 1. Clone the Repository

```bash
git clone https://github.com/lucky4518/movie_recommender.git
cd movie_recommender
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the Required Artifacts

Run the notebook `movierecommenderpr1 (2).ipynb` to prepare the movie data and generate the serialized artifacts required by the application.

Ensure the following files exist in the project root:

```text
movies.pkl
similarity.pkl
```

The exact generation and export steps depend on the notebook implementation.

### 5. Configure the TMDB API Key

Obtain an API key from [TMDB](https://www.themoviedb.org/).

Store the key securely in an environment variable or Streamlit secrets. Update `app.py` to read the key from that configuration instead of hardcoding it in the request URL.

Never commit API credentials to a public repository.

### 6. Run the Application

```bash
streamlit run app.py
```

Open the local URL printed in the terminal by Streamlit.

## Usage

1. Launch the application.
2. Select a movie from the dropdown.
3. Click **Show Recommendation**.
4. View the five recommended movies and their posters.

## Limitations

- Recommendations depend on the quality of the movie features and similarity scores.
- The current interface recommends movies based on a selected movie rather than a learned user profile.
- The application depends on the precomputed pickle files being available.
- Poster retrieval depends on TMDB API availability and valid movie IDs.
- The current implementation does not demonstrate formal offline recommendation-quality evaluation.

## Future Improvements

- Add automated tests for movie lookup and recommendation ranking.
- Improve error handling for invalid titles, API failures and missing data.
- Cache poster requests to reduce repeated network calls.
- Evaluate recommendations using metrics such as Precision@K, Recall@K and NDCG@K when suitable relevance labels are available.
- Explore hybrid recommendations combining content features with user ratings or interaction history.
- Improve scalability by using an efficient nearest-neighbor search method instead of storing a dense similarity matrix for large catalogues.

## Author

**Ankit Kumar**

GitHub: [lucky4518](https://github.com/lucky4518)

## License

No license is specified here. Check the repository's licensing status before reusing or redistributing the project.
