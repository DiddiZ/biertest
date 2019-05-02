import matplotlib.pyplot as plt


def visualize_ratings(file_name, ratings, labels, show=False, figsize=(16, 9)):
    fig = plt.figure(figsize=figsize)
    ax1 = fig.add_subplot(111)
    ax1.set_ylabel('normalized rating')
    ax1.grid(linestyle=':')

    # Plot ratings
    ax1.boxplot(ratings.T, whis='range', labels=labels)

    if file_name is not None:
        #fig.savefig(file_name + ".pdf", bbox_inches='tight', pad_inches=0)
        fig.savefig(file_name + ".png", bbox_inches='tight', pad_inches=0)
    if show:
        plt.show()
    plt.close(fig)


def visualize_ratings_per_person(file_name, ratings, labels1, labels2, show=False, figsize=(16, 9)):
    fig = plt.figure(figsize=figsize)
    ax1 = fig.add_subplot(111)
    ax1.set_ylabel('normalized rating')
    ax1.grid(linestyle=':')

    # Plot ratings
    for i in range(ratings.shape[1]):
        ax1.scatter(labels1, ratings[:, i], label=labels2[i])

    ax1.legend()

    if file_name is not None:
        #fig.savefig(file_name + ".pdf", bbox_inches='tight', pad_inches=0)
        fig.savefig(file_name + ".png", bbox_inches='tight', pad_inches=0)
    if show:
        plt.show()
    plt.close(fig)


def visualize_ratings_per_price(file_name, prices, ratings, labels, show=False, figsize=(16, 9)):
    fig = plt.figure(figsize=figsize)
    ax1 = fig.add_subplot(111)
    ax1.set_xlabel('€ / l')
    ax1.set_ylabel('normalized rating')
    ax1.grid(linestyle=':')

    # Plot ratings
    ax1.scatter(prices, ratings)
    for i, label in enumerate(labels):
        ax1.annotate(
            label,
            xytext=(8, -5),
            textcoords='offset pixels',
            xy=(prices[i], ratings[i]),
        )

    ax1.set_xlim(right=2)

    if file_name is not None:
        #fig.savefig(file_name + ".pdf", bbox_inches='tight', pad_inches=0)
        fig.savefig(file_name + ".png", bbox_inches='tight', pad_inches=0)
    if show:
        plt.show()
    plt.close(fig)
