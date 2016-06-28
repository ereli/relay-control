from serial import *
import time

def main():
	conn = Manager('/dev/cu.wchusbserial1410',9600)
	conn.toggle()
	# Make a Serial object

class Manager:
	def __init__(self, comport, rate):
		self.comport = comport
		self.rate = rate

		self.ser = Serial( self.comport, self.rate, timeout=0, writeTimeout=0 )

	def __exit__(self, exc_type, exc_value, traceback):
		self.ser.close()

	def toggle(self):
		self.ser.write('1\n'.encode('ASCII'))
		time.sleep(1)


if __name__ == "__main__":
	main()
