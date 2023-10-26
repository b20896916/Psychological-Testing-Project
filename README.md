# Psychological Testing Project
This is the README file of data processing code for Psychological testing.

## Requirement
- Python 3
- pandas
- numpy

## Data Cleaning
### Description
It removes the responses whose questions are not answered, such as those whose age is out of range.

It removes the emails left to draw prizes, timestamps of the responses, and the "I agree" answered in the beginning.

It converts the 5-point Likert scale from text to numbers, including reversing reverse-scaled questions.

It converts relationship status to dichotomous variable (0 for single and 1 otherwise), sex to dichotomous variable (0 for women and 1 for men).

It adds a column `Total` meaning the total score of a participant.

The output format the same as the input, in a csv file named `cleaned_data.csv`.
### Procedure
1. Rename the response file to `responses.csv`.
2. Run `python data_cleaning.py`.

## Descriptive Statistics
### Description
It generates the count, mean, std, min, quartiles, max, skewness, and kurtosis of each item, including age, sex, and relationship status.

The output is in a csv file named `descriptive_stat.csv`, below is an example:
```
                 Sex         Age  Relationship_Status          1.  ...         44.         45.         46.       Total
count     364.000000  364.000000           364.000000  364.000000  ...  364.000000  364.000000  364.000000  364.000000
mean        0.326923   21.043956             0.230769    2.475275  ...    2.442308    1.950549    2.774725  112.219780
std         0.469735    1.665810             0.421905    1.131538  ...    1.135198    1.032675    1.245960   35.242506
min         0.000000   17.000000             0.000000    1.000000  ...    1.000000    1.000000    1.000000   49.000000
25%         0.000000   20.000000             0.000000    2.000000  ...    2.000000    1.000000    2.000000   85.750000
50%         0.000000   21.000000             0.000000    2.000000  ...    2.000000    2.000000    3.000000  111.000000
75%         1.000000   22.000000             0.000000    3.000000  ...    3.000000    2.000000    4.000000  137.000000
max         1.000000   25.000000             1.000000    5.000000  ...    5.000000    5.000000    5.000000  214.000000
skew        0.740985    0.379410             1.283314    0.377097  ...    0.421847    1.201000    0.064454    0.391697
kurtosis   -1.458988   -0.071162            -0.355087   -0.907278  ...   -0.714761    0.956695   -1.121351   -0.254629
```

### Procedure
1. Prepare the cleaned data from the previous step.
2. Run `python descriptive_stat.py`.

## Item Reliability
### Descriptive
It computes the item-total correlation and the item reliability index for each item, including age, sex, and relationship status.

It prints out the Cronbach's alpha of the questionnaire.

The output, excluding Cronbach's alpha, is in a csv file named `item_reli.csv`.

### Procedure
1. Prepare the cleaned data from the previous step.
2. Run `python item_reliability.py`.