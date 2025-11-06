"""
MACHINE LEARNING CLASSIFICATION - Beginner Starter Code
========================================================

This starter code provides the foundation for building and training a simple
machine learning model. It loads a dataset and displays basic information
about it, so you can see the data immediately.

BEFORE RUNNING: Install the required libraries:
    pip install scikit-learn pandas matplotlib

YOUR TASKS:
1. Split the data into training and testing sets
2. Train a simple classifier on the training data
3. Make predictions on the test data
4. Evaluate the model's accuracy
5. Visualize the results

RUN THIS FILE FIRST to see what you're starting with:
    python ml_beginner.py

Then work with Claude Code to build a machine learning pipeline step by step.
"""

from sklearn.datasets import load_iris
import pandas as pd


def load_dataset():
    """
    Loads the Iris dataset, a classic dataset for classification.

    The Iris dataset contains measurements of iris flowers from three species.
    Given measurements of a flower, we can train a model to predict its species.

    Returns:
        tuple: (features, labels, feature_names, target_names)
    """
    iris = load_iris()

    # Features are the measurements (sepal length, sepal width, etc.)
    features = iris.data

    # Labels are the species (0, 1, or 2 representing different iris species)
    labels = iris.target

    # Names of the features and target classes
    feature_names = iris.feature_names
    target_names = iris.target_names

    return features, labels, feature_names, target_names


def display_dataset_info(features, labels, feature_names, target_names):
    """
    Displays information about the dataset.

    Parameters:
        features: The feature data (measurements)
        labels: The target labels (species)
        feature_names: Names of the features
        target_names: Names of the target classes
    """
    print("Dataset Information:")
    print(f"Number of samples: {len(features)}")
    print(f"Number of features: {len(feature_names)}")
    print(f"\nFeature names: {feature_names}")
    print(f"\nTarget classes: {target_names}")
    print(f"Target distribution: {pd.Series(labels).value_counts().to_dict()}")

    print("\nFirst 5 samples:")
    df = pd.DataFrame(features, columns=feature_names)
    df['species'] = [target_names[label] for label in labels]
    print(df.head())


def main():
    """
    Main function demonstrating dataset loading and exploration.

    You'll expand this to include model training, prediction, and evaluation.
    """
    print("=" * 60)
    print("  MACHINE LEARNING: Classification Project")
    print("=" * 60)
    print("\nThis starter code loads and displays a dataset.")
    print("Your task is to train a model to classify the data.\n")

    # Load the dataset
    features, labels, feature_names, target_names = load_dataset()

    # Display information about it
    display_dataset_info(features, labels, feature_names, target_names)

    print("\n" + "=" * 60)
    print("This is your starting point!")
    print("Next step: Split the data into training and testing sets.")
    print("=" * 60)


if __name__ == "__main__":
    main()


"""
SUGGESTED PROMPTS FOR CLAUDE CODE:
===================================

After running this starter code, try these prompts one at a time:

1. "Import train_test_split from sklearn.model_selection and split the
   features and labels into training and testing sets with 80% for training
   and 20% for testing. Use random_state=42 for reproducibility."

2. "Import DecisionTreeClassifier from sklearn.tree and create a classifier.
   Train it on the training data using the fit method."

3. "Use the trained model to make predictions on the test data. Display
   the predicted labels alongside the actual labels for the first 10 samples."

4. "Import accuracy_score from sklearn.metrics and calculate how accurate
   the model's predictions are. Display the accuracy as a percentage."

5. "Create a confusion matrix using confusion_matrix from sklearn.metrics
   to see which classes the model confuses most often. Display it in a
   readable format."

6. "Use matplotlib to create a simple visualization showing the model's
   accuracy or the confusion matrix as a heatmap."

Remember: Test after each change! Machine learning involves experimentation.
"""
