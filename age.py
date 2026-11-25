def age(eligibility):
    if eligibility < 18:
        return "You are not eligible to vote."
    elif eligibility >= 18:
        return "You are eligible to vote."
    else:
        return "Invalid age."
print(age(eligibility=18))
print(age(eligibility=18))
print(age(eligibility=17))
print(age(eligibility=10))