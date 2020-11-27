import random
from faker import Factory

def randomUserAgent():
    fc = Factory.create()
    return fc.user_agent()
