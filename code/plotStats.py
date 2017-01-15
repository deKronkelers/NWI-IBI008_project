# author: Hendrik Werner s4549775
import matplotlib.pyplot as plt
import numpy as np

# Plot the frequency of hashtag lengths
hashtag_freq_len = np.loadtxt("../data/stats/hashtagFrequencyLength.txt")

plt.plot(hashtag_freq_len[:, 1], hashtag_freq_len[:, 0])
plt.title("Frequency of hashtag lengths")
plt.xlabel("Hashtag length")
plt.ylabel("Frequency")
plt.savefig("../plots/hashtagFrequencyLength.pdf")
plt.show()
