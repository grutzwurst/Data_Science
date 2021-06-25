if __name__ == '__main__':
    import os
    from sklearn.cluster import KMeans
    from sklearn.decomposition import PCA
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import glob

    N = 5
    PATH_SOURCE_DATA = '/home/simon/HiDrive/Dokumente/Archiv/TH_Luebeck/Semester_2/Data_Science/Eindendeaufgaben/EA_12'
    PATH_RESULT = os.path.join(
        '/home/simon/HiDrive/Dokumente/Archiv/TH_Luebeck/Semester_2/Data_Science/Eindendeaufgaben/EA_12/Images')
    SEED = 1234
    data = pd.read_csv(os.path.join(PATH_SOURCE_DATA, 'edlich-kmeans-A0.csv'))
    dataT = data.transpose()
    print(dataT)

    kmeans = KMeans(n_clusters=N, init='random', random_state=SEED)
    kmeans.fit(data)
    print('Cluster centers:', kmeans.cluster_centers_)
    print('Labels:', kmeans.labels_)
    print(data.columns)
    result = pd.DataFrame([dataT.columns, kmeans.labels_]).transpose()
    result.columns = ['Item', 'KMeans-Kategorie']
    result['KMeans-Kategorie'] += 1
    out = result.sort_values(by=['KMeans-Kategorie', 'Item'])
    centers = kmeans.cluster_centers_

    #
    # Plot 3D
    #
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(data.iloc[:, 0], data.iloc[:, 1], data.iloc[:, 2], c=kmeans.labels_)
    ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], marker='x', s=1000)
    #plt.show()

    #
    # PCA
    # Reduce dimensions
    # https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html?highlight=sklearn%20decomposition%20pca
    reduced_data = PCA(n_components=2).fit_transform(data)
    kmeans = KMeans(n_clusters=N)
    kmeans.fit(reduced_data)

    # Step size of the mesh. Decrease to increase the quality of the VQ.
    h = .002  # point in the mesh [x_min, x_max]x[y_min, y_max].

    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh. Use last trained model.
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1)
    plt.clf()
    plt.imshow(Z, interpolation="nearest",
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired, aspect="auto", origin="lower")

    plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
    # Plot the centroids as a white X
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=169, linewidths=3,
                color="w", zorder=10)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()
