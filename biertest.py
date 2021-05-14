from pathlib import Path
import numpy as np
import pandas as pd
from visualizations import visualize_ratings, visualize_ratings_per_person, visualize_ratings_per_price, visualize_alcohol_per_beer


def generate_plots(dataset, target):
    # Load data
    df = pd.read_csv(dataset)

    persons = [c for c in df.columns if c not in ["beer", "vol", "price", "origin"]]

    # Normalize ratings
    for person in persons:
        df[person] = (df[person] - np.mean(df[person])) / np.std(df[person])

    # Melt dataframe
    df = df.melt(id_vars=[c for c in df.columns if c not in persons], var_name='person', value_name='normalized rating')

    # Plot ratings
    Path(target).mkdir(parents=True, exist_ok=True)

    visualize_ratings(target + 'ratings_average.png', df)
    visualize_ratings_per_person(target + 'ratings_per_person.png', df)
    if 'vol' in df.columns:
        visualize_alcohol_per_beer(target + 'ratings_per_vol.png', df)
    if 'price' in df.columns:
        visualize_ratings_per_price(target + 'ratings_per_price.png', df)
    if 'origin' in df.columns:
        visualize_ratings(target + 'ratings_by_origin.png', df, x='origin')


if __name__ == "__main__":
    generate_plots('data/ratings_2019-05-01.csv', 'plots/2019-05-01/')
    generate_plots('data/ratings_2020-06-06.csv', 'plots/2020-06-06/')
    generate_plots('data/ratings_2021-05-13.csv', 'plots/2021-05-13/')
