# Psychological Testing Project
This is the README file of data processing code for Psychological testing.

## Requirement
- Python 3
- pandas
- numpy
- os

## Data Cleaning
### Description
It removes the responses whose questions are not answered, such as those whose age is out of range.

It removes the emails left to draw prizes, timestamps of the responses, and the "I agree" answered in the beginning.

It converts the 5-point Likert scale from text to numbers, including reversing reverse-scaled questions.

It removes the acquiescently answered responses.

It converts relationship status to dichotomous variable (0 for single and 1 otherwise), sex to dichotomous variable (0 for women and 1 for men).

It adds a column `Total` meaning the total score of a participant.

The output format the same as the input, in a csv file named `cleaned_data.csv`.
### Procedure
1. Rename the response file to `responses.csv`.
2. Run `python data_cleaning.py`.

## Item Information Table
### Description
It generates the count, mean, std, min, quartiles, max, skewness, kurtosis and **mean difference** (Nov. 7 update, high 1/3 minus low 1/3) of each item, including age, sex, and relationship status.

It computes the item-total correlation (with and without itself) and the item reliability index for each item, including age, sex, and relationship status. (Nov. 7 update, merge descriptive statistics and item-total correlation)

The output is in a csv file named `description.csv`, below is an example:

It prints out the Cronbach's alpha of the questionnaire to `stdout`.

### Procedure
1. Prepare the cleaned data from the previous step.
2. Run `python info.py`.

## Interitem Correlation
### Description
It computes the interitem correlation and saves the output file to `interitem_corr.csv`.

### Procedure
1. Prepare the cleaned data from the previous step.
2. Run `python interitem_corr.py`.

## Histogram
### Description
It generates histograms for each item in the directory named `histograms`. It will create the directory if it did not exist.

For example, histogram of item 1 will be `histograms/hist_1.png`.

### Procedure
1. Prepare the cleaned data from the previous step.
2. Run `python histogram.py`.