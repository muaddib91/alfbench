#!/bin/env python2

# import section
import math
import random
import argparse
from appy.pod.renderer import Renderer

# create argument parser
parser = argparse.ArgumentParser(description='Generates content for benchmark')

parser.add_argument('-n', '--number', metavar='num', help='number of files to generate', required=True)
parser.add_argument('-d', '--dictionary', metavar='words', help='path to file that contains word list', required=True)
parser.add_argument('-m', '--mean', metavar='mean', help='mean size of generating files', required=True)
parser.add_argument('-a', '--alpha', metavar='alpha', help='distribution parameter', required=True)
parser.add_argument('-o', '--output', metavar='path', help='distribution parameter', required=True)
parser.add_argument('-t', '--template', metavar='template', help='path to odt template', required=True)
parser.add_argument('-v', '--verbose', action='store_true', help='be verbose')

# parse arguments
args = parser.parse_args()

# load word list
words = [line.strip() for line in open(args.dictionary)]
wc = len(words)
alpha = float(args.alpha)
mean = int(args.mean)
# generate files
for i in range(int(args.number)):
	# generate content
	k = math.trunc(mean-alpha*math.tan((1-2*random.random())*math.atan(mean/alpha)))
	TextToReplace = ''
	for j in range(k):
		TextToReplace += words[math.trunc(wc*random.random())]+' '
	outputFile = args.output+"/"+str(i)
	if args.verbose:
		print '\rGenerating file: '+str(i+1)+'/'+args.number
	if random.random() > 0.5:
		outputFile = outputFile + '.pdf'
	else:		
		outputFile = outputFile + '.doc'
	renderer = Renderer(args.template, globals(), outputFile)
	renderer.run()
