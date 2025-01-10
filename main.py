import pandas as pd
from scipy.stats import ttest_ind, spearmanr
import matplotlib.pyplot as plt

mood_df = pd.read_csv("./mood.csv", header=None, names=["date", "mood"])
mood_df["date"] = pd.to_datetime(mood_df["date"], format="%Y.%m.%d")  # Convert date to datetime

dai_df = pd.read_csv("./dai.csv", header=None)

dai_dates = pd.DataFrame(dai_df.values.flatten(), columns=["date"])
dai_dates = dai_dates.dropna()  # Drop any empty cells
dai_dates["date"] = pd.to_datetime(dai_dates["date"], format="%Y.%m.%d")  # Convert to datetime

mood_df["is_dai"] = mood_df["date"].isin(dai_dates["date"])

dai_moods = mood_df[mood_df["is_dai"]]["mood"]
non_dai_moods = mood_df[~mood_df["is_dai"]]["mood"]

print("average mood on dai:", dai_moods.mean())
print("average mood normal:", non_dai_moods.mean())

t_stat, p_value = ttest_ind(dai_moods, non_dai_moods, equal_var=False)
print(f"t-test: t-statistic = {t_stat:.3f}, p-value = {p_value:.3f}")

correlation, corr_p_value = spearmanr(mood_df["is_dai"], mood_df["mood"])
print(f"spearman: correlation = {correlation:.3f}, p-value = {corr_p_value:.3f}")

plt.figure(figsize=(10, 6))
plt.plot(mood_df["date"], mood_df["mood"], label="Mood", marker="o", color="blue")
plt.scatter(
    mood_df[mood_df["is_dai"]]["date"],
    mood_df[mood_df["is_dai"]]["mood"],
    color="red",
    label="dai",
    zorder=5,
)
plt.axhline(dai_moods.mean(), color="red", linestyle="--", label="mean dai")
plt.axhline(non_dai_moods.mean(), color="blue", linestyle="--", label="mean non-dai")
plt.xlabel("date")
plt.ylabel("mood")
plt.title("test")
plt.legend()
plt.grid()
plt.show()