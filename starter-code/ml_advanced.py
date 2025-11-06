"""
MACHINE LEARNING CLASSIFICATION - Advanced Starter Code
========================================================

This starter code provides dataset loading, train/test splitting, and a
basic training pipeline. Your focus will be on model evaluation, comparison,
and understanding what makes models perform well.

BEFORE RUNNING: Install the required libraries:
    pip install scikit-learn pandas matplotlib seaborn

RUN THIS FILE FIRST to see what you're starting with:
    python ml_advanced.py

The program demonstrates basic model training and evaluation.

YOUR TASKS:
1. Compare multiple classification algorithms
2. Implement cross-validation for more robust evaluation
3. Visualize model performance and decision boundaries
4. Experiment with feature importance and selection
5. Understand when models work well vs. poorly
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np


def load_and_split_data():
    """
    Loads the Iris dataset and splits it into training and testing sets.

    Returns:
        tuple: (X_train, X_test, y_train, y_test, feature_names, target_names)
    """
    # Load data
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test, iris.feature_names, iris.target_names


def train_model(X_train, y_train):
    """
    Trains a decision tree classifier.

    Parameters:
        X_train: Training features
        y_train: Training labels

    Returns:
        The trained model
    """
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test, target_names):
    """
    Evaluates the model on test data and displays metrics.

    Parameters:
        model: The trained model
        X_test: Test features
        y_test: Test labels
        target_names: Names of the target classes
    """
    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    # Detailed classification report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=target_names))

    # Show some predictions
    print("\nSample Predictions vs. Actual:")
    comparison = pd.DataFrame({
        'Actual': [target_names[i] for i in y_test[:10]],
        'Predicted': [target_names[i] for i in y_pred[:10]]
    })
    print(comparison)


def main():
    """
    Main function demonstrating the complete ML pipeline.

    You'll expand this to compare models, visualize results, and
    gain deeper understanding of how ML models work.
    """
    print("=" * 60)
    print("  MACHINE LEARNING: Classification - Advanced Starter")
    print("=" * 60)

    # Load and split data
    print("\n[1] Loading and splitting data...")
    X_train, X_test, y_train, y_test, feature_names, target_names = load_and_split_data()
    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")

    # Train model
    print("\n[2] Training Decision Tree classifier...")
    model = train_model(X_train, y_train)
    print("Training complete!")

    # Evaluate model
    print("\n[3] Evaluating model performance...")
    evaluate_model(model, X_test, y_test, target_names)

    print("\n" + "=" * 60)
    print("Demo complete! Now expand your ML knowledge:")
    print("  - Compare multiple algorithms (KNN, SVM, Random Forest)")
    print("  - Use cross-validation for better evaluation")
    print("  - Visualize decision boundaries")
    print("  - Explore feature importance")
    print("  - Try different datasets")
    print("=" * 60)


if __name__ == "__main__":
    main()


"""
SUGGESTED PROMPTS FOR CLAUDE CODE:
===================================

After running this starter code, work on these features:

1. "Create a function that trains and compares three different classifiers:
   DecisionTreeClassifier, KNeighborsClassifier, and RandomForestClassifier.
   Display the accuracy of each."

2. "Implement cross-validation using cross_val_score to get a more robust
   estimate of model performance. Use 5-fold cross-validation and display
   the mean and standard deviation of scores."

3. "Create a confusion matrix visualization using seaborn's heatmap to show
   where the model makes mistakes."

4. "For the DecisionTreeClassifier, extract and visualize feature importance
   to understand which measurements are most useful for classification."

5. "Create a function that visualizes the decision boundary of a classifier
   using two features at a time. Use a 2D plot with different colors for
   different predicted regions."

6. "Load a different dataset (like the wine or breast cancer dataset from
   sklearn) and apply the same pipeline. Compare performance across datasets."

7. For deeper exploration, consider:
   - Hyperparameter tuning with GridSearchCV
   - Feature scaling and normalization
   - Handling imbalanced datasets
   - Learning curves to detect overfitting/underfitting
   - ROC curves and AUC for model comparison
   - Ensemble methods and voting classifiers
   - Feature engineering and selection
   - Explaining model predictions

Remember: Machine learning is experimental! Try different approaches and see
what works best.
"""
