from __future__ import division

def fahrenheit(temp):
    return (temp - 32) * (5/9), temp

def celsius(temp):
    return (temp * 9/5) + 32, temp

fahrenheit = fahrenheit(72)
print '{0} degress F = {1} degress C'.format(fahrenheit[1], fahrenheit[0])

celsius = celsius(37)
print '{0} degress C = {1} degress F'.format(celsius[1], celsius[0])
