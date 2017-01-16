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

# Plot hashtag repetition frequencies
hashtag_rep_count = np.loadtxt("../data/stats/hashtagRepetitionsCount.txt")

plt.plot(hashtag_rep_count[:, 0], hashtag_rep_count[:, 1])
plt.title("Hashtag repetition frequencies")
plt.xlabel("Hashtag repetitions")
plt.ylabel("Frequency")
plt.savefig("../plots/hashtagRepetitionsCount.pdf")
plt.show()

# Plot hashtag count frequencies
hashtag_freq_count = np.loadtxt("../data/stats/hashtagFrequenciesCount.txt")

plt.plot(hashtag_freq_count[:, 0], hashtag_freq_count[:, 1])
plt.title("Hashtag count frequencies")
plt.xlabel("Hashtag count")
plt.ylabel("Frequency")
plt.savefig("../plots/hashtagFrequenciesCount.pdf")
plt.show()
