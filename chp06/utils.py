import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve

def plot_learning_curve(estimater, title, X, y, ylim=None, cv=None,
                        n_jobs=-1, train_size=np.linspace(.1, 1.0, 5)):
    plt.figure()
    plt.title(title)
