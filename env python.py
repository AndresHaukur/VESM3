#!/usr/bin/env python
import gpiozero
from mfrc522 import SimpleMFRC522
import time
from Adafruit_IO import Client, Feed, RequestError
from datetime import datetime

ADAFRUIT_IO_KEY = "aio_FsKs25LTpX0JVsmTRA8JsVl4jiYX"
ADAFRUIT_IO_USERNAME = "addi11"
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
reader = SimpleMFRC522()

try: 
	digital = aio.feeds("digital")
except RequestError:
	feed = Feed(name="digital")
	digital = aio.create_feed(feed)

try:
	digital2 = aio.feeds("second")
except RequestError:
	feed2 = Feed(name="second")
	digital2 = aio.create_feed(feed2)

try: 
	digital3 = aio.feeds("third")
except RequestError:
	feed3 = Feed(name="third")
	digital3 = aio.create_feed(feed3)

teljari = 0
teljari2 = 0 

while True:
	aio.send(digital.key, 0)
	print("Vinsamlegast sláðu korti á til að skrá þig inn eða út")
	id, text = reader.read()
	print("Einkennisnúmer þitt er ", id)
	print("Velkomin/n ", text)
	if id == 253089264431 and teljari == 0:
		start = datetime.now()
		teljari = 1
		print("vaktin þín er hafin")
	elif id == 253089264431 and teljari == 1:
		end = datetime.now()
		teljari = 0
		print("Úlfur þú varst að vinna í ", end-start, " langan tíma")
		#aio.send(digital3.key, end-start)
		#time.sleep(5)


	if id == 238483593180 and teljari2 == 0:
		start2 = datetime.now()
		teljari = 1
	elif id == 238483593180 and teljari2 == 1:
		end2 = datetime.now()
		teljari = 0
		print("Andrés þú varst að vinna í ", end-start, "langann tíma")


	aio.send(digital.key, id)
	time.sleep(5)
	aio.send(digital2.key, text)
	time.sleep(5)
	print()
	time.sleep(5)

