from sys import stdin
def sumstr(s):
	return sum(int(i) for i in s.split())
print(" ".join(str(i)) for i in stdin.readlines()[1:])
