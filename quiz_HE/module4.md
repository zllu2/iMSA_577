A test loan dataset has 100 loans, 80 loans are paid off and 20 are default. Two classification models were already trained on the train dataset. When predicting on the test set, model A predicts all 80 paid off loans correctly as paid off, 10 out of 20 default loans correctly as default; Model B predicts all 20 default loans correctly as defualt and 40 out of 80 paid off loans correctly as paid off.

- Question 1: What is the accuracy score of model A?
 - 20%
 - 50%
 - 80%
 - * 90%

- Question 2: What is the accuracy score of model B?
 - 50%
 - * 60%
 - 80%
 - 90%

- Question 3: If you are investing on open loans, which model is likely to be the better model to use to help you pick up loans to invest?
- Model A
- * Model B
- Not enough information to determine

- Question 4: If you change class_weight of a logistic regression model from {0:0.5, 1:0.5} to {0:0.8, 1:0.2}, which class does the model more likely to predict as?
- * Class 0
- Class 1

- Question 5: True of False? R-squared can never be greater than 1.
- * True
- False

- Question 6: (Module 5 review question) What does model selection mean?
- Select the best model from different types of models like KNN and RandomForest.
- * Select the best combination of hyperparameter values for a particular model.

- Question 7: (Module 5 review question) The purpose of model training (fitting) is to determine a model's:
- parameter
- hyperparamter

- Question 8: (Final project review question) In the final project dataset (Lending Club loan data), mths_since_last_record means months since last public record (bankruptcy, foreclosure, lawsuit, etc.). About 94% of this column has missing value. What is the approximate paid off rate of all loans that have mths_since_last_record >= 0?
- 70%
- * 78%
- 85%
- 90%
