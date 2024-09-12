import numpy as np

# User ratings data
X_train = np.array([
    [5, 3, 0, 2],  # User1
    [4, 0, 0, 5],  # User2
    [2, 5, 0, 3],  # User3
    [0, 3, 4, 0]   # User4
])

y_train = np.array([
    'User1',
    'User2',
    'User3',
    'User4'
])

# Ratings to be predicted for a new user (User1 in this case)
X_test = np.array([
    [5, 3, 0, 2]  # User1's ratings (used as a proxy for the new user)
])


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


def knn_recommend(X_train, y_train, X_test, k):

    predictions = []
    for test_point in X_test:

        # Calculate distances from the test point to all training points
        distances = [euclidean_distance(test_point, train_point) for train_point in X_train]

        # Find the indices of the k-nearest neighbors
        k_nearest_indices = np.argsort(distances)[:k]

        # Get the labels of the k-nearest neighbors
        k_nearest_users = y_train[k_nearest_indices]

        # Count the frequency of each user
        unique, counts = np.unique(k_nearest_users, return_counts=True)
        most_common_user = unique[np.argmax(counts)]

        predictions.append(most_common_user)

    return predictions


# Find the k-nearest neighbors for User1 with k=2
k = 2
predicted_users = knn_recommend(X_train, y_train, X_test, k)

print(f"Test User: {y_train[0]}")
print(f"Recommended Users based on KNN: {predicted_users}")
