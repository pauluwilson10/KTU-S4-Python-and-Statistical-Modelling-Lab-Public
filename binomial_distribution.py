import math

def binomial_probability(trials, probability_of_success, successes):
  probability = (math.factorial(trials) / (math.factorial(successes) * math.factorial(trials - successes))) * (probability_of_success**successes) * ((1 - probability_of_success) ** (trials - successes))
  return probability

def probability_at_least_one_success(trials, probability_of_success):
  probability_no_success = binomial_probability(trials, probability_of_success, 0)
  probability_at_least_one_success = 1 - probability_no_success
  return probability_at_least_one_success

trials=int(input("Enter the nunmber of trials: "))

probability_of_success =float(input("Enter the probability of success: "))


success=int(input("Enter the number of success to find probability: "))
probability = binomial_probability(trials, probability_of_success, success)
print("Probability of", success, "successes in", trials, "trials:", probability)

# Calculate probability of at least 1 success
probability_at_least_one_success = probability_at_least_one_success(trials, probability_of_success)
print("Probability of at least 1 success in", trials, "trials:", probability_at_least_one_success)

