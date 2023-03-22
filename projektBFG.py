import pandas as pd
import numpy as np
from math import log2

# Define a function to calculate entropy
def entropy(data):
    # Get the target column and its unique values
    target_col = data.iloc[:, -1]
    unique_vals = target_col.unique()
    
    # Calculate entropy for each unique value
    entropy_vals = []
    for val in unique_vals:
        p = (target_col == val).sum() / len(target_col)
        entropy_vals.append(-p * log2(p))
    
    # Return the sum of entropy values
    return sum(entropy_vals)

# Define a function to calculate information gain
def information_gain(data, feature):
    # Calculate entropy before splitting
    before_split = entropy(data)
    
    # Get unique values of the feature
    feature_vals = data[feature].unique()
    
    # Calculate entropy after splitting for each value of the feature
    after_split = 0
    for val in feature_vals:
        subset = data[data[feature] == val]
        after_split += len(subset) / len(data) * entropy(subset)
    
    # Calculate information gain
    return before_split - after_split

# Define a function to get the best split feature
def best_feature(data):
    # Get all feature names except the target column
    feature_cols = data.columns[:-1]
    
    # Calculate information gain for each feature
    info_gain = []
    for feature in feature_cols:
        info_gain.append(information_gain(data, feature))
    
    # Get the index of the feature with the highest information gain
    best_index = np.argmax(info_gain)
    
    # Return the name of the best feature
    return feature_cols[best_index]

# Define a function to build the decision tree
def build_tree(data):
    # Base case: if all instances have the same target value, return that value
    if len(data.iloc[:, -1].unique()) == 1:
        return data.iloc[0, -1]
    
    # Base case: if there are no more features to split on, return the most common target value
    if len(data.columns) == 1:
        return data.iloc[:, -1].mode()[0]
    
    # Get the best feature to split on
    best_feature_name = best_feature(data)
    
    # Create the tree
    tree = {best_feature_name: {}}
    for val in data[best_feature_name].unique():
        subset = data[data[best_feature_name] == val].drop(best_feature_name, axis=1)
        subtree = build_tree(subset)
        tree[best_feature_name][val] = subtree
    
    return tree

# Define a function to make predictions using the decision tree
def predict(tree, data):
    for feature in tree.keys():
        value = data[feature]
        subtree = tree[feature][value]
        if isinstance(subtree, dict):
            return predict(subtree, data)
        else:
            return subtree

# Load the CSV file into a Pandas dataframe
data = pd.read_csv('dane.csv', delimiter=';', index_col=False)

# Build the decision tree
tree = build_tree(data)

# Make predictions using the decision tree
predictions = []
for i in range(len(data)):
    instance = data.iloc[i, :-1]
    predictions.append(predict(tree, instance))

# Print the predictions
# print(predictions)
