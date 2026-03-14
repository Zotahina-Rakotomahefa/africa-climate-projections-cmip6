
import numpy as np
import matplotlib.pyplot as plt

def compute_taylor_metrics(reference, model):
    corr = np.corrcoef(reference.flatten(), model.flatten())[0,1]
    std_model = np.std(model)
    std_ref = np.std(reference)
    return corr, std_model, std_ref


def plot_taylor_diagram(metrics, reference_std):

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, polar=True)

    for label, (corr, std_model) in metrics.items():
        theta = np.arccos(corr)
        r = std_model
        ax.plot(theta, r, 'o', label=label)

    ax.set_title("Taylor Diagram")
    ax.set_rlabel_position(135)
    ax.legend()
    plt.show()
