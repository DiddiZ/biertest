from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from visualizations import visualize_ratings, visualize_ratings_per_person, visualize_ratings_per_price


def generate_plots(dataset, target, price=True):
    # Load data
    df = pd.read_csv(dataset, index_col=0)

    # Normalize ratings
    ratings = df.values[:, 2:]
    normalized_ratings = StandardScaler().fit_transform(ratings)
    average_ratings = np.mean(normalized_ratings, axis=1)

    # Plot ratings
    Path(target).mkdir(parents=True, exist_ok=True)
    visualize_ratings(target + 'ratings_average', normalized_ratings, df.index)
    visualize_ratings_per_person(target + 'ratings_per_person', normalized_ratings, df.index, df.columns[2:])
    if price:
        visualize_ratings_per_price(target + 'ratings_per_price', df['price'], average_ratings, df.index)


if __name__ == "__main__":
    generate_plots('data/ratings_2019-05-01.csv', 'plots/2019-05-01/')
    generate_plots('data/ratings_2020-06-06.csv', 'plots/2020-06-06/', price=False)
