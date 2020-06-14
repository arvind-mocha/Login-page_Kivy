import random

def random_numbers(bval,eval):
    ran = []
    sample = random.randint(bval,eval)

    #shuffle digits
    if sample not in ran:ran.append(sample)
    finalString = sample
    return finalString



