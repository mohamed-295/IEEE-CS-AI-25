# Comprehensive Summary: Probability Distributions, Conditional Probability, Bayes' Theorem, and Random Variables

## Introduction to Probability Distributions
A probability distribution describes how the values of a random variable are distributed. These distributions can be classified into **discrete** and **continuous** types.

### Key Characteristics of Probability Distributions:
- **Mean ($$\mu$$)**: The expected average value of the distribution.
- **Variance ($$\sigma^2$$)**: Measures the spread or dispersion of data around the mean.
- **Standard Deviation ($$\sigma$$)**: The square root of variance, offering an interpretable measure of dispersion.

## Discrete Probability Distributions
A discrete probability distribution applies to scenarios where the random variable takes **countable** values.

### Common Discrete Distributions:
1. **Bernoulli Distribution:**
   - Models a single trial with two outcomes: success (1) or failure (0).
   - *Example*: A light switch (ON = 1, OFF = 0).

2. **Binomial Distribution:**
   - Models the number of successes in $$n$$ independent Bernoulli trials.
   - *Example*: The number of defective items in a batch of 10 products.

3. **Geometric Distribution:**
   - Models the number of trials until the first success in Bernoulli trials.
   - *Example*: The number of times you roll a die until you get a 4.

4. **Poisson Distribution:**
   - Models the number of events occurring in a fixed interval of time or space when events happen at a constant rate.
   - *Example*: The number of website visitors per hour.

## Continuous Probability Distributions
A continuous probability distribution applies when the random variable can take **infinite** values within a given range.

### Common Continuous Distributions:
1. **Uniform Distribution:**
   - All values in an interval $$[a, b]$$ are equally likely.
   - *Example*: The time a bus arrives within a fixed 10-minute window.

2. **Normal (Gaussian) Distribution:**
   - A bell-shaped distribution commonly found in natural phenomena.
   - *Example*: Heights of students in a classroom.

3. **Exponential Distribution:**
   - Models the time between independent events occurring at a constant rate.
   - *Example*: The time between calls received in a call center.

4. **Gamma Distribution:**
   - Generalized form of the exponential distribution, modeling waiting times for multiple events.

5. **Chi-Squared Distribution:**
   - Arises from summing the squares of $$k$$ independent standard normal variables.
   - *Example*: Used in hypothesis testing and goodness-of-fit tests.

## Conditional Probability
Conditional probability determines the likelihood of an event $$A$$ occurring given that another event $$B$$ has already occurred. It is represented as:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

### Multiplication Rule:
Rearranging the formula:

$$
P(A \cap B) = P(A|B) \cdot P(B)
$$

### When to Use Conditional Probability?
- When events are dependent on each other.
- In Bayes' Theorem applications.
- Solving probability trees & real-world decision-making problems.

#### Example:
A box contains 5 red and 3 blue balls. If one ball is drawn randomly and not replaced, the probability that a second drawn ball is red depends on the first draw.

### Independent Events
Two events $$A$$ and $$B$$ are independent if the occurrence of one does not affect the probability of the other:

$$
P(A|B) = P(A) \quad \text{or} \quad P(B|A) = P(B)
$$

The probability of both occurring together:

$$
P(A \cap B) = P(A) \times P(B)
$$

#### Example:
Rolling two dice: The outcome of one die does not affect the outcome of the other.

## Total Probability Theorem
Finding the probability of an event $$A$$ by considering all possible ways it can happen through different mutually exclusive events:

$$
P(A) = \sum_{i=1}^{n} P(A|B_i) P(B_i)
$$

#### Example:
A company has three factories producing 50%, 30%, and 20% of its products. The probability of a defective product is different for each factory. The overall probability of a defective product can be found using the Total Probability Theorem.

## Bayes' Theorem
Bayes' Theorem helps in finding the probability of an event $$A$$, given that another event $$B$$ has already occurred:

$$
P(A|B) = \frac{P(B|A) P(A)}{P(B)}
$$

#### Example:
A medical test is 95% accurate in detecting a disease. If the general population has a 0.1% disease rate, Bayes' Theorem helps find the probability that a person actually has the disease given a positive test result.

## Random Variables
A random variable takes numerical values based on the outcome of a random experiment.

### Types of Random Variables:
1. **Discrete Random Variable (Countable Outcomes):**
   - Takes a finite or countable number of values.
   - *Example*: The number of students absent in a class on a given day.

2. **Continuous Random Variable (Uncountable Outcomes):**
   - Takes an infinite number of values within a range.
   - *Example*: The weight of randomly chosen apples.

### Probability Distributions:
- **Discrete Random Variable → Probability Mass Function (PMF)**  
  *Example*: Number of goals scored in a soccer match.
  
- **Continuous Random Variable → Probability Density Function (PDF)**  
  *Example*: Blood pressure levels in a group of adults.