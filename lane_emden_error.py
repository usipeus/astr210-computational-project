#!/usr/bin/python3
import math

# initialize variables
n = 1
θ = 1
φ = 0
ξ = 0

deltaξ = 0.1

# table header
print("\tθ", "\t\t\tξ", "\t\t\tθ - θactual")
print("----------------------------------------------------------------------")

while θ > 0:
    # avoid divide by zero case
    if ξ == 0:
        deltaθ = 0
        deltaφ = 0
        θactual = 1
    else:
        deltaθ = φ / (ξ**2) * deltaξ
        deltaφ = -(ξ**2) * (θ**n) * deltaξ
        θactual = math.sin(ξ) / ξ

    θ += deltaθ
    φ += deltaφ
    ξ += deltaξ

    print(θ, "\t", ξ, "\t", θ - θactual) 

print("ξ1:", ξ)
