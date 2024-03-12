# Crankshaft
Hundreds of free vehicle listings are posted on your website every day. You need to study the data collected over the past years and determine which factors influence the price of a vehicle.

## Perform exploratory data analysis following these instructions:
- Study the following parameters: price, vehicle years when the ad was placed, mileage, number of cylinders, and condition. Plot histograms for each of the parameters. Study how outliers affect the shape and legitimacy of the histograms.
- Determine the upper limits of the outliers, remove those values, and store them in a separate DataFrame, then continue your work with the filtered data.
- Use the filtered data to create new histograms. Compare them with the previous histograms (those with the outliers included). Draw conclusions from each histogram.
- Study how many days the ads were listed (days_listed). Plot a histogram. Calculate the mean and median. Describe the typical lifespan of an ad. Determine when ads are quickly removed and when they are posted for an abnormally long time.
- Analyze the number of ads and the average price for each type of vehicle. Plot a graph showing the dependency of the number of ads on each type of vehicle. Select the two types with the highest number of ads.
- Which factors impact price the most? Take each of the most popular types you identified in the previous phase and study if the price depends on age, mileage, condition, transmission type, and color. For categorical variables (transmission type and color), plot box and whisker plots, and create scatter plots for the rest. When analyzing categorical variables, note that categories should have at least 50 ads; otherwise, their parameters will not be valid for analysis.

## Data Description
The dataset contains the following data:

price
model_year
model
condition
cylinders
fuel — gasoline, diesel, etc.
odometer — vehicle mileage when the ad was posted
transmission
paint_color
is_4wd — if the vehicle has 4-wheel drive (Boolean type)
date_posted — the date the ad was posted
days_listed — from posting until it is removed