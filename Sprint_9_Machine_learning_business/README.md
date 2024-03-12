# OilyGiant

You work at the oil extraction company OilyGiant. Your task is to find the best locations to open 200 new oil wells.

To complete this task, you will need to perform the following steps:

- Read the files with parameters collected from oil wells in the selected region: crude oil quality and reserve volume.
- Create a model to predict the reserve volume in new wells.
- Choose the oil wells with the highest estimated values.
- Select the region with the highest total profit for the selected oil wells.
- You have data on crude oil samples from three regions. The parameters of each oil well in the region are already known. Create a model to help choose the region with the highest profit margin. Analyze potential benefits and risks using bootstrapping technique.

**Conditions:**

- Only linear regression should be used for model training.
- When exploring the region, a study of 500 points is conducted with the selection of the best 200 points for profit calculation.
- The budget for the development of 200 oil wells is 100 million dollars.
- A barrel of raw materials generates 4.5 USD in revenue. The income from one unit of product is 4500 dollars (the reserve volume is expressed in thousands of barrels).
- After risk assessment, only regions with a loss risk below 2.5% should be kept. From those that meet the criteria, the region with the highest average profit should be selected.
- The data is synthetic: contract details and well characteristics are not published.

**Data Description**

Geological exploration data from the three regions are stored in files:

- geo_data_0.csv. Download dataset
- geo_data_1.csv. Download dataset
- geo_data_2.csv. Download dataset
- id — unique identifier of oil well
- f0, f1, f2 — three features of the points (specific meaning is not important, but the features themselves are significant)
- product — reserve volume in the oil well (thousands of barrels).
