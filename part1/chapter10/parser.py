import argparse

parser = argparse.ArgumentParser(prog='myprogram', usage='%(prog)s [options]', description='A foo that bars', epilog="And that's how you'd foo a bar")
parser.add_argument('--foo', help='foo help', nargs='?')
parser.add_argument('bar', nargs='+', help='bar help')
parser.print_help()




'''
parser = argparse.ArgumentParser(prog='test', description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum integers (default:find the max)')

args = parser.parse_args()
print args.accumulate(args.integers)
'''




'''
import argparse

parser = argparse.ArgumentParser(prog='csv splitter',description='Splits a csv file into numerous files')


'''
