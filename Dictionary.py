"""
Find the key with the Maximum Value
"""

scores = {'Alice': 85, 'Bob': 92,'Charlie' : 88}

max_key = max(scores, key=scores.get)
print("Person with highest score:", max_key)