#!/usr/bin/python3

# initialize variables
n = 3
θ = 1
φ = 0
ξ = 0

deltaξ = 0.001

# table header
print("\tθ", "\t\t\tξ", "\t\t\tφ")
print("----------------------------------------------------------------------")

while θ > 0:
    # avoid divide by zero case
    if ξ == 0:
        deltaθ = 0
        deltaφ = 0
    else:
        deltaθ = φ / (ξ**2) * deltaξ
        deltaφ = -(ξ**2) * (θ**n) * deltaξ

    θ += deltaθ
    φ += deltaφ
    ξ += deltaξ

    # avoid outputting way too many lines
    if θ % 0.1 < 0.0002:
        print(θ, "\t", ξ, "\t", φ) 

print("ξ1:", ξ)
