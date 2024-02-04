import numpy as np
from sklearn.tree import DecisionTreeRegressor

# Sample data: topic scores (out of 100)
# get a dictionary of results from Maia code
topic_scores = {
    'Math': 85,
    'Physics': 70,
    'History': 60,
    'Programming': 92,
    'Biology': 75
}

# Generate random revision days for each topic
revision_days = {topic: sorted(np.random.choice(range(1, 31), size=5, replace=False)) for topic in topic_scores}

# Prepare data for machine learning
X_train = []
y_train = []

for topic, score in topic_scores.items():
    for day in range(1, 31):
        X_train.append([score, day])
        y_train.append(1 if day in revision_days[topic] else 0)

X_train = np.array(X_train)
y_train = np.array(y_train)

# Train a decision tree regression model
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Generate predictions for the entire month
X_predict = np.array([[score, day] for score in topic_scores.values() for day in range(1, 31)])
y_predict = model.predict(X_predict)

# Extract the optimized schedule based on predictions
optimized_schedule = {topic: [day for day, prediction in zip(range(1, 31), y_predict) if prediction > 0.5] for topic in topic_scores}

# Print the optimized revision schedule
print("Optimized Revision Schedule:")
for topic, days in optimized_schedule.items():
    print(f"{topic}: Revise on days {days}")