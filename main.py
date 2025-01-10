import pandas as pd
from scipy.stats import ttest_ind, spearmanr
import matplotlib.pyplot as plt

mood_df = pd.read_csv("./mood.csv", header=None, names=["date", "mood"])
mood_df["date"] = pd.to_datetime(mood_df["date"], format="%Y.%m.%d")

dai_df = pd.read_csv("./dai.csv", header=None)
dai_dates = pd.DataFrame(dai_df.values.flatten(), columns=["date"])
dai_dates = dai_dates.dropna()
dai_dates["date"] = pd.to_datetime(dai_dates["date"], format="%Y.%m.%d")

mood_df["is_dai"] = mood_df["date"].isin(dai_dates["date"])

just_before_dai_dates = dai_dates["date"] - pd.Timedelta(days=1)

just_before_dai_moods = mood_df[mood_df["date"].isin(just_before_dai_dates)]["mood"]

dai_moods = mood_df[mood_df["is_dai"]]["mood"]
non_dai_moods = mood_df[~mood_df["is_dai"]]["mood"]
both_moods = pd.concat([dai_moods, just_before_dai_moods])

print("Average mood on DAI dates:", dai_moods.mean())
print("Average mood just before DAI dates:", just_before_dai_moods.mean())
print("Average mood on non-DAI dates:", non_dai_moods.mean())
print("Average mood on both DAI + Just Before DAI dates:", both_moods.mean())

t_stat_dai_non_dai, p_value_dai_non_dai = ttest_ind(dai_moods, non_dai_moods, equal_var=False)
t_stat_before_non_dai, p_value_before_non_dai = ttest_ind(just_before_dai_moods, non_dai_moods, equal_var=False)
t_stat_both_non_dai, p_value_both_non_dai = ttest_ind(both_moods, non_dai_moods, equal_var=False)

print(f"T-test for DAI vs Non-DAI: t-statistic = {t_stat_dai_non_dai:.3f}, p-value = {p_value_dai_non_dai:.3f}")
print(f"T-test for Just Before DAI vs Non-DAI: t-statistic = {t_stat_before_non_dai:.3f}, p-value = {p_value_before_non_dai:.3f}")
print(f"T-test for DAI + Just Before DAI vs Non-DAI: t-statistic = {t_stat_both_non_dai:.3f}, p-value = {p_value_both_non_dai:.3f}")


correlation_dai_non_dai, corr_p_value_dai_non_dai = spearmanr(mood_df["is_dai"], mood_df["mood"])
correlation_before_non_dai, corr_p_value_before_non_dai = spearmanr(mood_df["date"].isin(just_before_dai_dates), mood_df["mood"])
correlation_both_non_dai, corr_p_value_both_non_dai = spearmanr(mood_df["is_dai"] | mood_df["date"].isin(just_before_dai_dates), mood_df["mood"])

print(f"Spearman for DAI vs Non-DAI: correlation = {correlation_dai_non_dai:.3f}, p-value = {corr_p_value_dai_non_dai:.3f}")
print(f"Spearman for Just Before DAI vs Non-DAI: correlation = {correlation_before_non_dai:.3f}, p-value = {corr_p_value_before_non_dai:.3f}")
print(f"Spearman for DAI + Just Before DAI vs Non-DAI: correlation = {correlation_both_non_dai:.3f}, p-value = {corr_p_value_both_non_dai:.3f}")

plt.figure(figsize=(12, 6))

# dai
plt.scatter(
    mood_df[mood_df["is_dai"]]["date"],
    mood_df[mood_df["is_dai"]]["mood"],
    color="red",
    label="DAI Dates",
    zorder=5,
)

# jb nondai
plt.scatter(
    mood_df[mood_df["date"].isin(just_before_dai_dates) & ~mood_df["is_dai"]]["date"],
    mood_df[mood_df["date"].isin(just_before_dai_dates) & ~mood_df["is_dai"]]["mood"],
    color="orange",
    label="Just Before DAI Dates (Non-DAI)",
    zorder=5,
)

# nondai
plt.scatter(
    mood_df[~mood_df["is_dai"] & ~mood_df["date"].isin(just_before_dai_dates)]["date"],
    mood_df[~mood_df["is_dai"] & ~mood_df["date"].isin(just_before_dai_dates)]["mood"],
    color="green",
    label="Non-DAI Dates",
    zorder=5,
)

# lines
plt.plot(mood_df["date"], mood_df["mood"], color="gray", linestyle='-', alpha=0.5)

plt.axhline(dai_moods.mean(), color="red", linestyle="--", label="Mean DAI Mood")
plt.axhline(just_before_dai_moods.mean(), color="orange", linestyle="--", label="Mean Just Before DAI Mood")
plt.axhline(non_dai_moods.mean(), color="green", linestyle="--", label="Mean Non-DAI Mood")
plt.axhline(both_moods.mean(), color="purple", linestyle="--", label="Mean DAI + Just Before DAI Mood")
plt.yticks(range(int(mood_df["mood"].min()), int(mood_df["mood"].max()) + 1))

plt.xlabel("Date")
plt.ylabel("Mood")
plt.title("Mood Analysis: DAI Dates, Just Before DAI, and Non-DAI")

plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.35), ncol=3)

plt.grid()
plt.show()
