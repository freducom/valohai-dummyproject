import random
import time
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--iterations", help="how many iterations the algorithm will be run", type=int, default=7)
args = parser.parse_args()
n=args.iterations 

print("Fetching training images...")
time.sleep(1)
print("Fetching test images...")
time.sleep(1)
print("Fetching metadata from Spark...")
time.sleep(2)
print("Starting CNN training w/ TF")
time.sleep(1)
accuracy = 0
i=0
while i<n:
	increment = random.random()
	accuracy += increment/1000
	print("{\"step\":", i+1,", \"accuracy\":",accuracy," }")
	i+=1
	time.sleep(2*random.random())
