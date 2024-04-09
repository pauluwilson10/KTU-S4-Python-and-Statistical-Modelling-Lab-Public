import math

def poisson_probability(poisson_d, k):

  probability = (math.exp(-poisson_d) * (poisson_d**k)) / math.factorial(k)
  return probability

# Example usage:
poisson_d=float(input("Enter the poisson distribution: "))
num=int(input("Enter the number of occurences: "))


# Calculate the probability
probability = poisson_probability(poisson_d, num)
print("Probability of", num, "occurrences:", probability)