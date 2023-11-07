# Decision Tree for Predicting IT Job

The "Decision Tree for Predicting IT Job" project is a Jupyter Notebook that demonstrates the creation and implementation of a decision tree to predict whether you'll get a job in the IT field. This project is part of the Elements of Artificial Intelligence course and is created by Julia Baranowska, Aleksander Folfas, and Julia Głowa.

## Table of Contents

- [Introduction](#introduction)
- [Project Files](#project-files)
- [How it Works](#how-it-works)
- [Usage](#usage)
- [License](#license)

## Introduction

The project showcases the application of a decision tree algorithm to make predictions about job opportunities in the IT field based on specific criteria and attributes. Decision trees are a popular machine learning technique for classification tasks, and this project serves as an educational resource to understand how they work.

## Project Files

The project includes a Jupyter Notebook (`Decision_Tree_Prediction.ipynb`) that contains Python code for data preprocessing, decision tree construction, and prediction. The main libraries used are `pandas`, `numpy`, `networkx`, and `matplotlib`.

## How it Works

The project operates as follows:

1. **Import Necessary Libraries**: The necessary Python libraries are imported, including `pandas`, `numpy`, `networkx`, and `matplotlib`.

2. **Definition of Entropy and Information Gain Functions**: Functions are defined to calculate entropy and information gain, which are crucial for decision tree construction.

3. **Best Feature Selection**: A function selects the best feature to split the data based on the highest information gain.

4. **Decision Tree Construction**: A function builds the decision tree recursively, considering the features with the most information gain.

5. **Prediction**: A function is defined to make predictions based on the constructed decision tree.

6. **Loading Data**: The project loads training and test data from CSV files.

7. **Decision Tree Creation**: The decision tree is created using the training data.

8. **Making Predictions**: Predictions are made for the test data using the constructed decision tree.

## Usage

To run the project, follow these steps:

1. Ensure you have Jupyter Notebook installed on your system.

2. Open the Jupyter Notebook file `Decision_Tree_Prediction.ipynb`.

3. Execute the cells in the notebook sequentially to load the data, create the decision tree, and make predictions.

4. Review the predictions for the test data at the end of the notebook.

## License

This "Decision Tree for Predicting IT Job" project is available under the MIT License. For more details, please refer to the [LICENSE](LICENSE) file.

**Explore the world of decision trees and predict your potential IT job!**
