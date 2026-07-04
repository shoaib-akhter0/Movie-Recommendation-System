# Movie Recommendation System

A Streamlit-based movie recommendation app that suggests similar movies based on a selected title using cosine similarity on movie metadata.

## Features

- Select any movie from the dataset
- Get 5 similar movie recommendations
- Display posters for each recommended movie
- Built with Streamlit, pandas, scikit-learn, and requests

## Project Structure

- app.py - Streamlit app entry point
- poster.py - Helper to fetch movie posters from TMDb
- movies.pkl - Serialized movie dataset
- similarity.pkl - Precomputed similarity matrix
- requirements.txt - Python dependencies

## Installation

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```

## Environment Variable

To fetch posters from TMDb, set your API key:

```bash
export TMDB_API_KEY="your_tmdb_api_key"
```

On Windows PowerShell:

```powershell
$env:TMDB_API_KEY="your_tmdb_api_key"
```

## Demo

The app opens in your browser and lets you pick a movie, then shows five related recommendations with poster images.
