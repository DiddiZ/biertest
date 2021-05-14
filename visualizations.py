import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns


def __add_name_labels(ax, xs, ys):
    last_y_pos = 9999
    for i, name in enumerate(xs):
        y_pos = ys[i] - 0.1
        if np.abs(y_pos - last_y_pos) < 0.1:
            y_pos = last_y_pos - 0.1
        last_y_pos = y_pos
        ax.text(
            i, y_pos, name, ha="center", va="center", bbox=dict(
                boxstyle="round",
                ec=(1, 1, 1, 0),
                fc=(1, 1, 1, 0.7),
            )
        )

    # Remove original ticks
    ax.set_xticks([])
    ax.set_xticks([], minor=True)


def visualize_ratings(file_name, df, x='beer', plot_type="box", show=False, figsize=(16, 9)):
    fig = plt.figure(figsize=figsize)

    # Plot ratings

    if plot_type == "box":
        ax = sns.boxplot(data=df, x=x, y='normalized rating', whis=[0, 100])
    elif plot_type == "violin":
        ax = sns.violinplot(data=df, x=x, y='normalized rating', inner="point", bw=0.15, scale="count")
    ax.grid(linestyle=':')

    # Add nice name labels
    __add_name_labels(ax, xs=df[x].unique(), ys=df.groupby(x, sort=False)['normalized rating'].min())

    plt.tight_layout()
    if file_name is not None:
        fig.savefig(file_name)
    if show:
        plt.show()
    plt.close(fig)


def visualize_ratings_per_person(file_name, df, show=False, figsize=(16, 9)):
    fig = plt.figure(figsize=figsize)

    ax = sns.scatterplot(data=df, x='beer', y='normalized rating', hue='person', s=50, edgecolor=(0, 0, 0, 0))
    ax.grid(linestyle=':')

    # Add nice name labels
    __add_name_labels(ax, xs=df['beer'].unique(), ys=df.groupby('beer', sort=False)['normalized rating'].min())

    plt.tight_layout()
    if file_name is not None:
        fig.savefig(file_name)
    if show:
        plt.show()
    plt.close(fig)


def visualize_ratings_per_price(file_name, df, show=False, figsize=(16, 9)):
    fig = plt.figure(figsize=figsize)

    data = df.groupby('beer').agg(
        price=pd.NamedAgg(column='price', aggfunc="first"),
        rating=pd.NamedAgg(column='normalized rating', aggfunc="mean"),
        beer=pd.NamedAgg(column='beer', aggfunc="first"),
    )

    # Plot ratings
    ax = sns.scatterplot(data=data, x='price', y='rating', s=50, color="black", edgecolor=(0, 0, 0, 0))
    ax.set_xlabel('€ / l')
    ax.set_ylabel('normalized rating')
    ax.grid(linestyle=':')

    for _, price, rating, beer in data.itertuples():
        ax.annotate(
            beer,
            xytext=(8, -5),
            textcoords='offset pixels',
            xy=(price, rating),
        )

    ax.set_xlim(right=2)

    ax.imshow(
        [[1, 0.5], [0.5, 0]],
        cmap=plt.cm.RdYlGn,
        interpolation='bicubic',
        extent=plt.xlim() + plt.ylim(),
        aspect="auto"
    )

    plt.tight_layout()
    if file_name is not None:
        fig.savefig(file_name)
    if show:
        plt.show()
    plt.close(fig)


def visualize_alcohol_per_beer(file_name, df, show=False, figsize=(16, 9)):
    fig = plt.figure(figsize=figsize)

    data = df.sort_values(['vol', 'beer']).groupby('beer', sort=False).agg(
        beer=pd.NamedAgg(column='beer', aggfunc="first"),
        rating=pd.NamedAgg(column='normalized rating', aggfunc="mean"),
        vol=pd.NamedAgg(column='vol', aggfunc="first"),
    )

    # Plot ratings
    ax = sns.scatterplot(data=data, x='vol', y='rating', s=50, color="black", edgecolor=(0, 0, 0, 0))
    ax.grid(linestyle=':')
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())

    # Plot trend fit
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression().fit(data['vol'].values.reshape(-1, 1), data['rating'])
    plt.plot(
        plt.xlim(),
        reg.predict(np.array(plt.xlim()).reshape(-1, 1)),
        linewidth=1,
        color="black",
        linestyle="dashed",
        label="Trend"
    )
    plt.legend()

    for _, beer, rating, vol in data.itertuples():
        ax.annotate(
            beer,
            xytext=(8, -5),
            textcoords='offset pixels',
            xy=(vol, rating),
            bbox=dict(
                boxstyle="round",
                ec=(1, 1, 1, 0),
                fc=(1, 1, 1, 0.7),
            ),
        )

    plt.tight_layout()
    if file_name is not None:
        fig.savefig(file_name)
    if show:
        plt.show()
    plt.close(fig)
