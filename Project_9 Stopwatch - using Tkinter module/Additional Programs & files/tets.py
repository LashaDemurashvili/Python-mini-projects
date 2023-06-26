import time
from datetime import datetime
from time import *

x = 1
while x < 100:
    print(datetime.fromtimestamp(x).strftime("%M:%S"))
    sleep(0.10)
    x += 1
