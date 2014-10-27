from __future__ import division

def fahrenheit(temp):
    return (temp - 32) * (5/9), temp

def celsius(temp):
    return (temp * 9/5) + 32, temp

fahrenheit = fahrenheit(72)
print fahrenheit[1], "degrees F =", fahrenheit[0], "degrees C"

celsius = celsius(37)
print celsius[1], "degrees C =", celsius[0], "degrees F"
