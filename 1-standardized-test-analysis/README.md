# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Standardized Test Analysis

### Problem Statement

College Board who administers the SA, while ACT Inc. administers the ACT. Both often establish contracts with certain states in the US so that high school juniors within that state will be offered one SAT exam or ACT exam or both depending on which company they have contracted with. There are approximately 12 states that have contracted with the ACT ([*source*](https://blog.prepscholar.com/which-states-require-the-act-full-list-and-advice)) and 20 states that have contracted with College Board ([*source*](https://blog.prepscholar.com/which-states-require-the-sat)).  

Between the two tests, past data trends have suggested that the ACT is the more popular standardized exam to take when applying to college admissions.  However, in recent years its participation rate has started to decline, while the participation rate of the SAT has slowly risen.  This project aims to explore the national trends in ACT participation for the years 2017-2019 and seeks to identify states that have decreasing ACT participation rates.

The audience of my project will be ACT employees and C-suite or those in charge of making decisions at the company.  I will be an in-house Data Scientist analyzing the data of ACT participation rates collected between the years 2017 - 2019, and making recommendations on how to solve the problem of decreasing participation rates.   

---

### Datasets Chosen from Provided Data

* [`act_2017.csv`](./data/act_2017.csv): 2017 ACT Scores by State ([source](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows))
* [`act_2018.csv`](./data/act_2018.csv): 2018 ACT Scores by State ([source](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows))
* [`act_2019.csv`](./data/act_2019.csv): 2019 ACT Scores by State ([source](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows))
* [`act_2019_ca.csv`](./data/act_2019_ca.csv): 2019 ACT Scores in California by School ([source](https://www.cde.ca.gov/ds/sp/ai/) | [data dictionary](https://www.cde.ca.gov/ds/sp/ai/reclayoutact19.asp))
* [`sat_2017.csv`](./data/sat_2017.csv): 2017 SAT Scores by State ([source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/))
* [`sat_2018.csv`](./data/sat_2018.csv): 2018 SAT Scores by State ([source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/))
* [`sat_2019.csv`](./data/sat_2019.csv): 2019 SAT Scores by State ([source](https://blog.prepscholar.com/average-sat-scores-by-state-most-recent))


#### Additional Data

* [State abbreviations](https://www.infoplease.com/us/postal-information/state-abbreviations-and-state-postal-codes)
* [State latitudes and longitudes](https://inkplant.com/code/state-latitudes-longitudes)
* State contracts with either [College Board (SAT)](https://blog.prepscholar.com/which-states-require-the-sat) or [Act Inc. (ACT)](https://blog.prepscholar.com/which-states-require-the-act-full-list-and-advice)

---

### Data Dictionary of the Datasets Combined into 1 Master Dataset

|Feature|Type|Dataset|Description|
|---|---|---|---|
|state|object|ACT/SAT datasets|The state in which the test scores were collected| 
|participation|float|ACT/SAT datasets|The overall participation rate for in a particular state for a particular test and in a specified year| 
|total|float|ACT/SAT datasets|The average test score in the specified state for a particular test| 
|test|object|None, I manually added as a label|The test that data collected was for (either SAT or ACT)| 
|year|int|None, I manually entered as a label|The year the data for a test was collected| 
|ebrw|float|SAT datasets|The average Evidence-Based Reading and Writing score on the SAT for that year, and state| 
|math|float|SAT datasets|The average Math score on the SAT for that year, and state| 
|latitude|float|Scraped from html of List of Latitudes and Longitudes for Every State from Ink Plant website|The latitude coordinates for that state| 
|longitude|float|Scraped from html of List of Latitudes and Longitudes for Every State from Ink Plant website|The longitude coordinates for that state| 
|abbrev|object|Scraped from html of State Abbreviations from Infoplease website|The short state abbreviation| 
|contract_test|string|Collected from prepscholar.com|A categorical variable of what type of contract that a state has entered into with ACT or College Board (SAT) or either/both or neither| 




---

### Summary of Analysis

ACT scores have been decreasing in the years 2017-2019.  The number of states that have an ACT participation rate of around 50-60% has decreased in addition to the number of states that have participated in the ACT at 100%.  Focusing on the states whose participation decreased from 100% during these years, 4 states were identified as having declining participation rates within these years and these states were: Colorado, Minnesota, Missouri, and South Carolina.  Among these states it was shown that Colorado decreased most significantly due to them dropping the contract with ACT and taking a contract with College Board instead.  This lead to the discovery effect that the type of contract has on ACT paricipation rates.  It was seen that those states that had a contract with ACT, had very high parcticipation rates, with the mean rate being very close to 100%.  On the other hand, states that had a contract with the SAT test, had lower ACT participation rates.  This finding showed the effect the type of contract had on the ACT participation rates.

---

### Recommendations/Conclusions

Due to the effect the contracts have on ACT participation rates, 3 suggestions were made to address the decrease ACT participation over the past 3 years. 

For states that saw small decreases in participation rates:

- Increase marketing strategy to these states

- Increase online presence, social media, website analytics to understand who lands on the ACT website and how to market to these individuals. 

- Discuss partnering to cover funds or agree to aleviate some of the fee burdens

For states that have no contracts:

- Develop relationships with those states to discuss starting a contract to increase our market share

For states that have contracted with College Board only (i.e. Colorado):

- Improve relationships with these states. Send a liaison to discuss why they no longer contract with ACT Inc. 

---

