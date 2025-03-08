# Write a Python function that takes in a list of values and returns the probability distribution of those values. Assume the values are discrete.

# Input:
# data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1] 
# Output:
# {1: 0.3, 2: 0.2, 3: 0.2, 4: 0.2, 5: 0.1}


def probability_distribution(data):
    distribution = {}
    for i in data:
        if i in distribution:
            distribution[i] += 1
        else:
            distribution[i] = 1
    for i in distribution:
        distribution[i] /= len(data)
    return distribution

data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1]
print(probability_distribution(data))



# Write a Python function that calculates the conditional probability of event B given event A, given two lists of events A and B.

# Input:
# event_a = [1, 0, 1, 0, 1]
# event_b = [1, 1, 0, 0, 1]

# Output:
# 2/3

# B given A  = التقاطع / A

def conditional_probability(event_a, event_b):
    count_a = 0
    count_b = 0
    for i in range(len(event_a)):
        if event_a[i] == 1:
            count_a += 1
            if event_b[i] == 1:
                count_b += 1
    return count_b / count_a

event_a = [1, 0, 1, 0, 1]
event_b = [1, 1, 0, 0, 1]
print(conditional_probability(event_a, event_b))


# Write a Python function that implements Bayes' theorem to calculate the probability of event A given event B,
# given the prior probability of A and B, and the conditional probability of B given A.

# Input:
# prior_a = 0.3
# prior_b = 0.6
# conditional_b_given_a = 0.8

# Output:
# 0.4

# P(A|B) = P(B|A) * P(A) / P(B) من ملخص الكلية

def bayes_theorem(prior_a, prior_b, conditional_b_given_a):
    return (conditional_b_given_a * prior_a) / prior_b

prior_a = 0.3
prior_b = 0.6
conditional_b_given_a = 0.8
print(bayes_theorem(prior_a, prior_b, conditional_b_given_a))