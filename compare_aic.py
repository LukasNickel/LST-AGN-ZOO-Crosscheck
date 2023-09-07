import numpy as np
from gammapy.modeling.models import Models
from gammapy.datasets import Datasets
import matplotlib.pyplot as plt


def aic(stat_sums, n_parameters):
    return 2*n_parameters - 2*stat_sums


def relative_likelihood(aics):
    return np.exp((min(aics) - aics)/2)


def read_data(data_path, model_path):
    datasets = Datasets.read(data_path)
    models = Models.read(model_path)
    datasets.models = models

    stat_sum = datasets.stat_sum()
    n_params = len([x for x in models.parameters if not x.frozen])
    return stat_sum, n_params



def main(indirs, output):

    # fill for dir in indirs
    names = ["a", "b", "c", "d", "e"]
    stat_sums = np.array([12, 14, 19, 8, 44])
    n_params = np.array([2, 3, 3, 7, 1])

    aics = aic(stat_sums, n_params)
    rel_lls = relative_likelihood(aics)
    fig, [ax_aic, ax_rll] = plt.subplots(2)

    
    rects = ax_aic.bar(names, aics)
    for rect in rects:
        height = rect.get_height()
        ax_aic.text(rect.get_x() + rect.get_width()/2., 0.5*height,
                    '%.2f' % height,
                ha='center', va='top')
    ax_aic.set_title("AIC")

    rects2 = ax_rll.bar(names, rel_lls)
    ax_rll.set_title("Relative likelihood")
    ax_rll.set_yscale("log")
    for rect in rects2:
        height = rect.get_height()
        ax_rll.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%.2f' % height,
                ha='center', va='bottom')
    fig.savefig(output)

    return


if __name__ == "__main__":
    main(None, "test.pdf")


