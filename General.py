import random

depressed = [
    "123",
    "123"
]

neutral = [
    "123",
    "123"
]

def chat(branch):
    if branch == 'depressed':
        return depressed[random.randint(0, len(depressed)-1)]
    else:
        return neutral[random.randint(0, len(depressed)-1)]