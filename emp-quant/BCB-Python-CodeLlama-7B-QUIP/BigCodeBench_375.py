
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(l):
    pca = PCA(n_components=2)
    pca.fit(l)
    ax = plt.figure()
    ax.set_title("PCA Result")
    ax.set_xlabel("First Principal Component")
    ax.set_ylabel("Second Principal Component")
    ax.plot(pca.components_[0], pca.components_[1])
    return ax