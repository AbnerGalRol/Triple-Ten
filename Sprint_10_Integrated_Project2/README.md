# Zyfra

Prepare a prototype of a machine learning model for Zyfra. The company develops efficiency solutions for heavy industry.

The model should predict the amount of gold extracted from the gold ore. You have data on extraction and purification.

The model will help optimize production and eliminate unprofitable parameters.

You will need to:

1. Prepare the data;
2. Perform data analysis;
3. Develop and train a model.

To complete the project, you can use the documentation of pandas, matplotlib, and sklearn.
The next lesson covers the process of ore refining.
You will need to select the important information for the model development.

**How is gold extracted from the ore?**

Let's look at the stages of this process.
The extracted ore undergoes primary treatment to obtain the mineral mixture, or rougher feed, which is the raw material used for flotation (also known as the rougher process). After flotation, the material undergoes purification process in two stages.


Let's examine the process step by step:

**Flotation**

The gold ore mixture is introduced into flotation plants to obtain a rougher gold concentrate and rougher tails (i.e., product residues with low concentration of valuable metals).

The stability of this process is affected by the volatility and unfavorable physico-chemical state of the flotation pulp (a mixture of solid particles and liquid).

**Purification**
The rougher concentrate undergoes two stages of purification. After this, we have the final concentrate and the new tails.

## Data Description

**Technological process**

- Rougher feed: raw material

- Rougher additions (or reagent additions) - flotation reagents: xanthate, sulfate, depressant

    - Xanthate: flotation promoter or activator

    - Sulfate: sodium sulfide for this particular process

    - Depressant: sodium silicate

- Rougher process: flotation

- Rougher tails: product residues

- Float banks: flotation installation

- Cleaner process: purification

- Rougher Au: rougher gold concentrate

- Final Au: final gold concentrate

**Parameters of the stages**

- air amount: volume of air

- fluid levels

- feed size: particle size of the feed

- feed rate

## Naming of characteristics

Here's how the characteristics are named:

[stage].[parameter_type].[parameter_name]

Example: rougher.input.feed_ag

**Possible values for [stage]:**

- rougher: flotation

- primary_cleaner: primary purification

- secondary_cleaner: secondary purification

- final: final characteristics

**Possible values for [parameter_type]:**

- input: parameters of the raw material

- output: product parameters

- state: parameters characterizing the current state of the stage

- calculation: calculation features













