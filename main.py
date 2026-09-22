import random

prices = [random.randint(50, 75) for _ in range(100)]

print(prices)
returns = [((prices[i] - prices[i - 1]) / prices[i - 1]) * 100 for i in range(1, len(prices))]
print(returns)
import random
Market = [random.randint(-20, 12) for _ in range(len(returns))]
print(Market)
import statistics
market_variance = statistics.variance(Market)
print(market_variance)
statistics.covariance(returns, Market)
print(statistics.covariance(returns, Market))
Beta = statistics.covariance(returns, Market) / market_variance
print(Beta)
