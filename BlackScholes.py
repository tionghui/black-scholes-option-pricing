def Black_Scholes(S, E, t, r, sigma, option_type, delta=0):
    """Parameters:
    S : float : Current stock price
    E : float : Exercise price
    t : float : Time to expiration in years
    r : float : Risk-free interest rate (annualized)
    sigma : float : Volatility of the underlying stock (annualized)
    option_type : str : 'call' for Call option, 'put' for Put option
    delta : float : Dividend yield (annualized), default is 0
    """

    from math import log, sqrt, exp
    from scipy.stats import norm

    if delta != 0:
        d1 = (log(S / E) + (r - delta + 0.5 * sigma ** 2) * t) / (sigma * sqrt(t))
        d2 = d1 - sigma * sqrt(t)
    else:
        d1 = (log(S / E) + (r + 0.5 * sigma ** 2) * t) / (sigma * sqrt(t))
        d2 = d1 - sigma * sqrt(t)

    if option_type == 'call':
        price = S * exp(-delta * t) * norm.cdf(d1) - E * exp(-r * t) * norm.cdf(d2)
    else:
        price = E * exp(-r * t) * norm.cdf(-d2) - S * exp(-delta * t) * norm.cdf(-d1)

    return price

current_stock_price = 19.6
exercise_price = 20
time_to_expiration = 90 / 365
risk_free_rate = 0.08
volatility = 0.4
option_type = 'put'
delta = 0

print("Input Parameters:")
print(f"Current Stock Price: {current_stock_price}")
print(f"Exercise Price: {exercise_price}")
print(f"Time to Expiration (years): {time_to_expiration}")
print(f"Risk-Free Rate: {risk_free_rate}")
print(f"Volatility: {volatility}")
print(f"Option Type: {option_type}")
print(f"Dividend Yield (delta): {delta}")
print()

option_price = Black_Scholes(current_stock_price, exercise_price, time_to_expiration, risk_free_rate, volatility, option_type, delta)
print(f"The price of the {option_type} option is: {round(option_price, 4)}")