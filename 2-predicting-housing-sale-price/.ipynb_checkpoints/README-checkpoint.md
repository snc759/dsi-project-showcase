# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2: Ames Housing Predictive Analytics Analysis

### Problem Statement

New prospective homeowners or those looking to buy a house, often want to know understand and evaluate the value of a house, based on its features and characteristics.  In order to value a house and to see how each of its features affects its value and therefore, its Sale Price, developing a predictive model that could predict the Sale Price of a house, as well as show the importance of certain house features to that Sale Price, would be beneficial for prospective homeowners.  

This project aims to give prospective homeowners an accurate valuation of a house based on its characteristics.  The goal will be accurately predict the Sale Price of a house, while still maintaining interpretability among the features to show the audience which features have a strong impace on the target variable (Sale Price).

The audience of my project will be prospective homeowners that have hired me as a data scientist to help them evaluate the sale price of a house, and what characteristics really drive up that price. I will be a Data Scientist consultant out for hire, analyzing the Ames Housing Data between the years 2006 and 2010.    

---

### Dataset Given from Kaggle

* https://www.kaggle.com/c/dsir-222-ames-competition/overview

---

### Data Dictionary of all the features used in modeling

|Feature|Type|Dataset|Description|
|---|---|---|---|
|ln_LotArea|float|Kaggle - Ames|natural log of the Lot Area in Square Feet| 
|ln_GrLivArea|float|Kaggle - Ames|natural log of the Above grade (ground) living area square feet| 
|GarageArea|float|Kaggle - Ames|The average test score in the specified state for a particular test| 
|OverallQual|int|Kaggle - Ames|Rates the overall material and finish of the house 
|TotalBsmtSF|float|Kaggle - Ames|Total square feet of basement area 
|BrDale|object|Kaggle - Ames|Briardale neighborhood within the Ames city limits| 
|BrkSide|object|Kaggle - Ames|Brookside neighborhood within the Ames city limits| 
|ClearCr|object|Kaggle - Ames|Clear Creek neighborhood within the Ames city limits| 
|CollegeCr|object|Kaggle - Ames|College Creek neighborhood within the Ames city limits| 
|Crawfor|object|Kaggle - Ames|Crawford neighborhood within the Ames city limits| 
|Edwards|object|Kaggle - Ames|Edwards neighborhood within the Ames city limits| 
|Gilbert|object|Kaggle - Ames|Gilbert neighborhood within the Ames city limits| 
|IDOTRR|object|Kaggle - Ames|Iowa DOT and Rail Road neighborhood within the Ames city limits| 
|MeadowV|object|Kaggle - Ames|Meadow Village neighborhood within the Ames city limits| 
|Mitchel|object|Kaggle - Ames|Mitchell neighborhood within the Ames city limits| 
|NAmes|object|Kaggle - Ames|North Ames neighborhood within the Ames city limits| 
|NPkVill|object|Kaggle - Ames|Northpark Villa neighborhood within the Ames city limits| 
|NWAmes|object|Kaggle - Ames|Northwest Ames neighborhood within the Ames city limits| 
|NoRidge|object|Kaggle - Ames|Northridge neighborhood within the Ames city limits| 
|NridgHt|object|Kaggle - Ames|Northridge Heights neighborhood within the Ames city limits| 
|OldTown|object|Kaggle - Ames|Old Town neighborhood within the Ames city limits| 
|Other_nhood|object|Kaggle - Ames|Other category for neighborhoods that had less than 10 observations| 
|SWISU|object|Kaggle - Ames|South & West of Iowa State University neighborhood within the Ames city limits| 
|Sawyer|object|Kaggle - Ames|Sawyer neighborhood within the Ames city limits| 
|Somerst|object|Kaggle - Ames|Somerset neighborhood within the Ames city limits| 
|StoneBr|object|Kaggle - Ames|Stone Brook neighborhood within the Ames city limits| 
|Timber|object|Kaggle - Ames|Timberland neighborhood within the Ames city limits|        
|Veenker|object|Kaggle - Ames|Veenker neighborhood within the Ames city limits|   
|YearBuilt_squ|float|Kaggle - Ames|Original construction date in years - squared| 
|YearRemod-Built|int|Kaggle - Ames|The Year the house was Remodeled minus the Year the House was Built| 
|ExterQual|int|Kaggle - Ames|Evaluates the quality of the material on the exterior|    
|BsmtQual|int|Kaggle - Ames|Evaluates the height of the basement| 
|BsmtFinType1|int|Kaggle - Ames|Rating of basement finished area| 
|BsmtFinSF1|float|Kaggle - Ames|Type 1 finished square feet| 
|BsmtFinType1\*BsmtFinSF1|object|Kaggle - Ames|Rating of basement finished area multiplied by Type 1 finished square feet| 
|1stFlrSF|float|Kaggle - Ames|First Floor square feet| 
|HeatingQC|int|Kaggle - Ames|Heating quality and condition| 
|BsmtFinType2|int|Kaggle - Ames|Rating of basement finished area (if multiple types)| 
|BsmtFinSF2|float|Kaggle - Ames|Type 2 finished square feet| 
|BsmtFinType2\*BsmtFinSF2|float|Kaggle - Ames|Rating of basement finished area if multiple types multiplied by Type 2 finished square feet| 
|BsmtUnfSF|float|Kaggle - Ames|Unfinished square feet of basement area| 
|TotalBsmtSF\*BsmtUnfSF|float|Kaggle - Ames|Total square feet of basement area multiplied by Unfinished square feet of basement area| 
|KitchenQual|int|Kaggle - Ames|Kitchen quality| 
|BedroomAbvGr|int|Kaggle - Ames|Bedrooms above grade (does NOT include basement bedrooms)| 
|FullBath|int|Kaggle - Ames|Basement full bathrooms| 
|BedroomAbvGr\*FullBath|float|Kaggle - Ames|Number of bedrooms on ground level multiplied by full bathrooms| 
|Fireplaces|int|Kaggle - Ames|Number of fireplaces| 
|FireplaceQu|int|Kaggle - Ames|Fireplace quality| 
|Hip|object|Kaggle - Ames|Hip type of roof| 
|Other_roof|object|Kaggle - Ames|Other category for roof types that are not Hip or Gable, and had a small number of observations|

---

### File Directory
project-2
* README.md
* code
    * 00_functions.ipynb
    * 01_eda_cleaning.ipynb     
    * 02_linear_model.ipynb
    * 03_lasso_model.ipynb  
    * sample_submission.ipynb  
* data
    * train.csv
    * train_clean.csv
    * test.csv
    * submissions_final.csv
    * submissions_null.csv
* presentation
    * Ames Housing Sale Price Predictions.pdf
    * imgs
        * ExterQual_boxplot.jpg
        * heatmap_corr.jpg
        * heatmap_corr1.jpg
        * hist_GrLivArea.jpg
        * hist_ln_GrLivArea.jpg
        * hist_ln_LotArea.jpg
        * hist_LotArea.jpg
        * nhood_boxplot.jpg
        * ols_p_values_2.jpg
        * ols_p_values.jpg
        * YearBuilt_Price.jpg
        
---

### Conclusions 

To the prospective homeowner there are a few conclusions about what drives up the price of a house: 
- A house in College Creek neighborhood, then holding everything else constant, on average the sale price of the house will be \$20,080 less than a house bought in Bloomington Heights neighborhood
- A house bought in Meadow Village neighborhood, on average, has a sale price that is \$19,030 more than a house bought in the Bloomington Heights neighborhood
- An increase in a house’s exterior material quality from, ex: good, to excellent, on average will lead to an increase in the Sale Price by \$17,250. 
- An increase in the Heating Quality and Condition, ex: Fair to average, will lead to an increase in the sale price by \$2,012 dollars. 
- An increase in the ordinal category of the Kitchen Quality ex: Typical to good, will lead to an average increase in the sale price by \$11,330.
- An increase in the ordinal category of the Fireplace Quality ex: Good to excellent, will lead to an average increase in the sale price by \$1,961. 


### Areas for Further Study/Research 
- Would want to collect more data such as how much sq ft per bed
- Would want to collect more current data 
- Would want to take the top-down approach for a model and put all features into a model right away
