import pandas as pd


mood_df = pd.read_csv("mood.csv", header=None, names=["date", "mood"])
mood_df["date"] = pd.to_datetime(mood_df["date"], format="%Y.%m.%d")  # Convert date to datetime

dai_df = pd.read_csv("dai.csv", header=None)

dai_dates = pd.DataFrame(dai_df.values.flatten(), columns=["date"])
dai_dates = dai_dates.dropna()  # Drop any empty cells
dai_dates["date"] = pd.to_datetime(dai_dates["date"], format="%Y.%m.%d")  # Convert to datetime
