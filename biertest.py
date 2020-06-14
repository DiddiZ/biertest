import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from visualizations import visualize_ratings, visualize_ratings_per_person, visualize_ratings_per_price

# Load data
df = pd.read_csv('data/ratings_2019-05-01.csv', index_col=0)

# Normalize ratings
ratings = df.values[:, 2:]
normalized_ratings = StandardScaler().fit_transform(ratings)
average_ratings = np.mean(normalized_ratings, axis=1)

# Plot ratings
visualize_ratings('plots/ratings_average', normalized_ratings, df.index)
visualize_ratings_per_person('plots/ratings_per_person', normalized_ratings, df.index, df.columns[2:])
visualize_ratings_per_price('plots/ratings_per_price', df['price'], average_ratings, df.index)
