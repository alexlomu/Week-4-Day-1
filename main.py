#Import all the necessary libraries here:
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#Import the Fitbit2 dataset and store it in a variable called fitbit. You can find the dataset in Ironhack's database:
fitbit = pd.read_csv("Fitbit2.csv")
#How the average number of steps change by month. Use the appropriate visualization to show the median steps by month. Is Fitbitter more active on weekend or workdays? 
print(fitbit.head())
print(fitbit.groupby(fitbit.Months).Steps.median())
print(fitbit.groupby(fitbit.Work_or_Weekend == 0).Steps.median())
ax = fitbit.groupby(fitbit.Months).Steps.median().plot(kind = "bar", color = ["r" , "g", "b"], grid = True, figsize = (12, 4), title = "Average steps in a month")
ax.set_xlabel("Month")
ax.set_ylabel("Median")
plt.savefig("images/average_steps.jpg")

ax = fitbit.groupby(fitbit.Work_or_Weekend == 0).Steps.median().plot(kind = "bar", color = ["r" , "g", "b"], grid = True, figsize = (12, 4), title = "Average steps in a month")
ax.set_xlabel("Month")
ax.set_ylabel("Median")
plt.savefig("images/steps_week_weekend.jpg")
#We conclude that there are more steps in the week
#Write a loop to plot 3 scatter plots of the following features:

#Import the titanic dataset and store it in a variable called titanic. You can find the dataset in Ironhack's database:
titanic = pd.read_csv("titanic.csv")
#Explore the titanic dataset using Pandas dtypes.
print(titanic.dtypes)
#What are your numerical variables? What are your categorical variables?
print(titanic.select_dtypes(include = ["int64", "float64"]))
print(titanic.select_dtypes(include = ["object"]))
#Set the plot style to classic and the figure size to (12,6).
plt.style.use("classic")
plt.figure(figsize = (12, 6))
#Use the right visulalization to show the distribution of column Age.
print(titanic.Age.describe())
#Since the minimum value is 0.17 and the maximum one is 80, we will use 40 as the bins value
plt.hist(titanic.Age, bins= 40)
#Use subplots and plot the distribution of the Age with bins equal to 10, 20 and 50.
bins10 = plt.hist(titanic.Age, bins= 10)
bins20 = plt.hist(titanic.Age, bins= 20)
bins50 = plt.hist(titanic.Age, bins= 50)

#How does the bin size affect your plot?
#As larger the bin number is the biggest the columns of the hitogram are

#Use seaborn to show the distribution of column Age.
sns.histplot(data = titanic.Age, element = "step", fill = False, stat = "count")
#Use the right plot to visualize column Gender. There are 2 ways of doing it. Do it both ways.
ax = titanic.Gender.value_counts().plot(kind = "bar", color = ["r" , "g"], grid = True, figsize = (12, 4), title = "Gendder")
sns.barplot(x = titanic.Gender.unique(), y = titanic.Gender.value_counts(), palette = sns.color_palette("bright"))
#Use the right plot to visualize the column Pclass.
sns.barplot(x = titanic.Pclass.unique(), y = titanic.Pclass.value_counts(), palette = sns.color_palette("bright"))
#We would like to have in one single plot the summary statistics of the feature Age. What kind of plot would you use? Plot it.
plt.boxplot(titanic.Age, showmeans = True)
plt.show()
#What does the last plot tell you about the feature Age?
#We have ages from 0 to 80 years, the mean is 30 year and the median is 28 years
#Now in addition to the summary statistics, we want to have in the same plot the distribution of Age. What kind of plot would you use? Plot it.

#What additional information does the last plot provide about feature Age?

#We suspect that there is a linear relationship between Fare and Age. Use the right plot to show the relationship between these 2 features. There are 2 ways, please do it both ways.

#Plot the correlation matrix using seaborn.

#What are the most correlated features?

#Use the most appropriate plot to display the summary statistics of Age depending on Pclass.
titanic.groupby(titanic.Pclass).Age.describe()["count"].plot(kind =  "bar", title = "Box plot Age", grid = True)
#Use seaborn to plot the distribution of Age based on the Gender.
sns.FacetGrid(data = titanic, col = "Gender").map(plt.hist, "Age")
