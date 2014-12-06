import os
import re

with open ('sloppy_data.txt', 'rb') as input_file:
    for line in input_file.readlines():
        line = re.sub('^\s*\n', '', line)
        line = re.sub('^\s+', '', line)
        line = re.sub('\[\d+\]', ' ', line)
        line = re.sub('^\d+\s+', ' ', line)
        line = re.sub('(,* |,)(Incorporated|Inc\.*)', '', line)
        line = re.sub('(\(\d{3}\))(\s)(\d{3}-\d{4})', '$1$3', line)
        with open ('output.txt', 'wb') as output_file:
            output_file.write(line)
