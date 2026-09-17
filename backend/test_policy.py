from services.policy_engine import (
    get_delay_policy,
    check_fare_difference
)


print("Arvind:")
print(get_delay_policy(4))

print("\nMeher:")
print(get_delay_policy(6))

print("\nFare difference ₹2000:")
print(check_fare_difference(2000))