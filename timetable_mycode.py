# import numpy as np

# Sample data: topic scores (out of 100)
topic_scores = {
    'Math': 85,
    'Physics': 70,
    'History': 60,
    'Programming': 92,
    'Biology': 75
}

# Define revision timetable parameters
total_days = 30

no_of_topics = len(topic_scores)

# Function to generate a revision timetable based on scores
def generate_revision_timetable(topic_scores, total_days):
    sorted_topic_scores = dict(sorted(topic_scores.items(), key=lambda item: item[1], reverse=True))
    timetable = {}
    i = 0
    for topic, score in sorted_topic_scores.items():
        timetable[topic] = list(range(i+1, total_days + 1, int(total_days / (2 * no_of_topics - i))))
        i += 1
    return timetable

# Generate and print the revision timetable
revision_timetable = generate_revision_timetable(topic_scores, total_days)

print("Revision Timetable:")
for topic, days in revision_timetable.items():
    print(f"{topic}: Revise on days {days}")