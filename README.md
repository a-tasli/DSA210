# Investigating a Possible Correlation Between Daily Reported Mood and Dates of Academic Significance

In this project, I investigate if there is a correlation between my daily reported mood, and dates of academic importance (e.g. exams, homework submissions, etc.)

The datasets I worked with is a record of my self-reported mood taken every day, and dates of academic importance taken from SUCourse or in-class announcements.

The reported mood is a simple scale from 1-6, where 1 is the worst mood and 6 is the best. This is reported every day between 22:00 and 00:00 of the next day.

The average of daily reported mood in a certain number of days leading up to a date of academic significance is compared to the average of daily reported mood in other days will be compared to find evidence of a monotonic relationship using Spearman Correlation.

The Dates of Academic Importance (DAI's) and the mood values for each date are made into csv files and using pandas and scipy, t-tests, spearman correlation and p-values for the correlation are calculated for DAI's vs non-DAI's, dates just before DAI'S vs non-DAI's and both vs non-DAI's.

The result was: 

Average mood on DAI dates: 2.6

Average mood just before DAI dates: 3.1

Average mood on non-DAI dates: 2.80327868852459

Average mood on both DAI + Just Before DAI dates: 2.85

T-test for DAI vs Non-DAI: t-statistic = -0.659, p-value = 0.519

T-test for Just Before DAI vs Non-DAI: t-statistic = 0.935, p-value = 0.364

T-test for DAI + Just Before DAI vs Non-DAI: t-statistic = 0.187, p-value = 0.852

Spearman for DAI vs Non-DAI: correlation = -0.052, p-value = 0.666

Spearman for Just Before DAI vs Non-DAI: correlation = 0.118, p-value = 0.325

Spearman for DAI + Just Before DAI vs Non-DAI: correlation = 0.035, p-value = 0.771


So we can say the Investigation is inconclusive and i couldn't reject the H0 which was that there is no correlation between DAI's and reported mood.
The resulting graph is in the repository as result.png
