import os
from sys import platform

def run_fresco():
	if platform == "linux" or platform == "linux2" or platform == "darwin":
		os.system("fresco < 19F_dd.fin > 19F_dd.fro")
	elif platform == "win32":
		os.system("fresco < 19F_dd.fin > 19F_dd.fro")
		print("Fresco run completed!")


def run_sfresco():
	if platform == "linux" or platform == "linux2" or platform == "darwin":
		os.system("sfresco < 19F_dd.min")
	elif platform == "win32":
		os.system("sfresco < 19F_dd.min")


if __name__ == "__main__":
	# run_fresco()
	run_sfresco()
	os.system("python ../scripts/parse_dfcs.py")