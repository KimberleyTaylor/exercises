<h1 align="center">Day 2: Data Cleaning (Missings and Outliers)</h1>

## Exercises

### ❓ Missing values

#### 1. What is the missing datatype used in pandas?
* numpy.NaN
#### 2. How to replace all occurences of the value 9999 to missing in pandas?
* Use .replace(np.nan, 9999)
#### 3. How to get the absolute number of missings for each variable in pandas?
* Use df.isnull().sum()
#### 4. How to get the percentage of missings for each variable in pandas?
* Use df.isnull().sum()/len(df)
#### 5. How to drop rows with missing values?
* Use df.dropna(axis=0)
#### 6. How to drop variables with missing values?
* Use df.dropna(axis=1)
#### 7. What is the univariate imputation method in sklearn?
* impute.SimpleImputer - this replaces missing values with a constant value or a value realted to a feature. We can use the missing_values parameter to specify the missing value used in the dataset, and the strategy parameter for specifying how the missing value should be replaced.
#### 8. What is the multivariate imputation method in sklearn?
* impute.IterativeImputer - here is variable with missing values is calculated as a function of other variables. Then the missing values can be estimated through this function.
#### 9. What is the best univariate imputation method to categorical variables? (Explain why)
* Replacing with the mode value using SimpleImputer(strategy="most_frequent"), or replacing with a constant value using SimpleImputer(strategy="constant", fill_value=*insert string or numerical value*). These are best because it will give a more real-life estimation of the value, instead of creating a new value which would create a new category.
#### 10. What is the best univariate imputation method to numerical variables? (Explain why)
* Replacing with the mean or median value using IterativeImputer(initial_strategy="mean") or IterativeImputer(initial_strategy="median"). This will calculate a very accurate mean or median value using on estimator functions based on other variables. Therefore, instead of categorising, it will estimate a value specific to the general mean or median of other samples similar to itself.


### 🔎 Outliers

#### 1. What is an outlier?
* It is a point that is vastly different than the majority of other samples in the dataset. Therefore it creates a different distribution and effects the data in a bias way. To replace or remove an outlier is the best method to deal with this.
#### 2. What is a simple method to detect and deal with outliers of a numerical variable?
* To detect outliers of numerical variables, plot the data. If it is univariate, make a boxplot or splitplot. If it is bivariate, make a scatter plot. If it is multivariate, plot a dimentionality reduction such as TSNE or UMAP.
#### 3. What is novelty detection?
* It gives a confidence level of if **new** data added to a dataset is abnormal or regular or indistinguishable from other features in the original dataset. Therefore we can decide to keep the new data or not.
#### 4. Name 4 advanced methods of outlier detection in sklearn.
* Robust Covariance, One Class SVM, Isolation Forest, Local Outlier Factor. 


### 🖋 Typos

#### 1. What is a typo?
* A typographical error - (a spelling mistake)
#### 2. What is a good method of automatically detect typos?
* Use "fuzzywuzzy"


### Practical case

Consider the following dataset: [San Francisco Building Permits](https://www.kaggle.com/aparnashastry/building-permit-applications-data). Look at the columns "Street Number Suffix" and "Zipcode". Both of these contain missing values.

- Which, if either, are missing because they don't exist? **(E)**
- Which, if either, are missing because they weren't recorded? **(R)**

Hint: Do all addresses generally have a street number suffix? Do all addresses generally have a zipcode?



| #  |  NaN % |    Var name                        |   Var Description                                                 | E/R?
|:--:|:------:|:----------------------------------:|:-----------------------------------------------------------------:|
| 1  |      0 | Permit Number                      | Number assigned while filing.                                     |  
| 2  |      0 | Permit Type                        | Type of the permit represented numerically.                       |
| 3  |      0 | Permit Type Definition             | Description of the Permit type, for example new construction or   |       |    |        |                                    | alterations.                                                      |
| 4  |      0 | Permit Creation Date               | Date on which permit created, later than or same as filing date.  |
| 5  |      0 | Block                              | Related to address.                                               |
| 6  |      0 | Lot                                | Related to address.                                               |
| 7  |      0 | Street Number                      | Related to address.                                               |
| 8  | 98.885 | Street Number Suffix               | Related to address.                                               |  E
| 9  |      0 | Street Name                        | Related to address.                                               |
| 10 |  1.391 | Street Name Suffix                 | Related to address.                                               |  E
| 11 | 85.178 | Unit                               | Unit of a building.                                               |  E
| 12 | 99.014 | Unit suffix                        | Suffix if any, for the unit.                                      |  E
| 13 |  0.145 | Description                        | Details about purpose of the permit. Example: reroofing, bathroom |  R     |    |        |                                    | renovation.                                                       | 
| 14 |      0 | Current Status                     | Current status of the permit application.                         |  
| 15 |      0 | Current Status Date                | Date at which current status was entered.                         |
| 16 |      0 | Filed Date                         | Filed date for the permit.                                        |
| 17 |  7.511 | Issued Date                        | Issued date for the permit.                                       |  R
| 18 | 51.135 | Completed Date                     | The date on which project was completed, applicable if Current    |  E     |    |        |                                    | Status = “completed”.                                             |  
| 19 |  7.514 | First Construction Document Date   | Date on which construction was documented.                        |  R
| 20 | 96.519 | Structural Notification            | Notification to meet some legal need, given or not.               |  E
| 21 | 21.510 | Number of Existing Stories         | Num of existing stories in the building. Not applicable for       |  E     |    |                                             | certain permit types.                                             |
| 22 | 21.552 | Number of Proposed Stories         | Number of proposed stories for the construction/alteration.       |  E
| 23 | 99.982 | Voluntary Soft-Story Retrofit      | Soft story to meet earth quake regulations.                       |  E
| 24 | 90.534 | Fire Only Permit                   | Fire hazard prevention related permit.                            |  E
| 25 | 26.083 | Permit Expiration Date             | Expiration date related to issued permit.                         |  R
| 26 | 19.138 | Estimated Cost                     | Initial estimation of the cost of the project.                    |  R
| 27 |  3.049 | Revised Cost                       | Revised estimation of the cost of the project.                    |  E
| 28 | 20.670 | Existing Use                       | Existing use of the building.                                     |  R
| 29 | 25.911 | Existing Units                     | Existing number of units.                                         |  E
| 30 | 21.336 | Proposed Use                       | Proposed use of the building.                                     |  R
| 31 | 25.596 | Proposed Units                     | Proposed number of units.                                         |  R
| 32 | 18.757 | Plansets                           | Plan representation indicating the general design intent of the   |  E    |    |                                             | foundation.                                                       |
| 33 | 99.998 | TIDF Compliance                    | TIDF compliant or not, this is a new legal requirement.           |  E
| 34 | 21.802 | Existing Construction Type         | Construction type, existing,as categories represented numerically.|  R
| 35 | 21.802 | Existing Construction Type Desc.   | Descr. of the above, eg: wood or other construction types.        |  R/E
| 36 | 21.700 | Proposed Construction Type         | Proposed construction type, as categories represented numerically.|  R
| 37 | 21.700 | Proposed Construction Type Desc.   | Description of the above.                                         |  R/E
| 38 | 97.305 | Site Permit                        | Permit for site.                                                  |  E
| 39 |  0.863 | Supervisor District                | Supervisor District to which the building location belongs to.    |  R
| 40 |  0.867 | Neighborhoods - Analysis Boundaries| Neighborhood to which the building location belongs to.           |  R
| 41 |  0.862 | Zipcode                            | Zipcode of building address.                                      |  R
| 42 |  0.854 | Location                           | Location in latitude, longitude pair.                             |  R
| 43 |      0 | Record ID                          | Some ID, not useful for this.                                     |


## Optional External Exercises:

From Kaggle [data cleaning mini course](https://www.kaggle.com/learn/data-cleaning) do:
- [Handling Missing Values](https://www.kaggle.com/alexisbcook/handling-missing-values) Data Cleaning: 1 of 5
- [Inconsistent Data Entry](https://www.kaggle.com/alexisbcook/inconsistent-data-entry) Data Cleaning: 5 of 5
