# author: Hendrik Werner s4549775
import matplotlib.pyplot as plt
import numpy as np


# Plot the frequency of hashtag lengths
def plot_hashtag_freq_len(filename: str, title: str):
    hashtag_freq_len = np.loadtxt("../data/stats/{}.txt".format(filename))
    plt.plot(hashtag_freq_len[:, 1], hashtag_freq_len[:, 0])
    plt.title(title)
    plt.xlabel("Hashtag length")
    plt.ylabel("Frequency")
    plt.savefig("../plots/{}.pdf".format(filename))
    plt.show()


plot_hashtag_freq_len(
    "hashtagFrequencyLength"
    , title="Frequency of hashtag lengths"
)
plot_hashtag_freq_len(
    "hashtagFrequencyLengthNoDup"
    , title="Frequency of hashtag lengths (no duplicates)"
)