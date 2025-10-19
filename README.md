# black-scholes-option-pricing
Personal project implementing the **Black-Scholes option pricing model** in Python.

## Introduction
The **Black–Scholes model** (F. Black & M. Scholes, 1973) provides a closed-form analytical solution for pricing European-style options.  
This project demonstrates the model’s implementation in Python and allows pricing of both **call** and **put** options.

## Assumptions
The model operates under the following key assumptions:  
1. The underlying asset price follows a **lognormal distribution**.
2. **No transaction costs** or taxes on trading the underlying asset.
3. **Frictionless** and efficient markets.
4. The option is **European-style** (exercisable only at expiration).
5. The **risk-free rate** and **volatility** remain constant over the option’s life.

## Parameters
$S$ = Current price of the underlying asset  
$E$ = Exercise (strike) price  
$t$ = Time to expiration in years  
$r$ = Risk-free interest rate (annualized)  
$N(.)$ = Cumulative distribution function (CDF) of the standard normal distribution  
$\sigma$ = Volatility of the underlying asset (annualized)  
$\delta$ = Dividend yield (optional, default = 0)

## Model Formulation
The equation for the **call** option is:
$C = Se^{-\delta t}N(d_1) - Ee^{-rt}N(d_2)$

The equation for the **put** option is:
$P = Ee^{-rt}N(-d_2) - Se^{-\delta t}N(-d_1)$

where  

$d_1 = \frac{\ln(S/E) + (r - \delta + 0.5\sigma^2)t}{\sigma \sqrt{t}}$

$d_2 = \frac{\ln(S/E) + (r - \delta - 0.5\sigma^2)t}{\sigma \sqrt{t}}$

or simply $d_2 = d_1 - \sigma \sqrt{t}$
