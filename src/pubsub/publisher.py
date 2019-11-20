# Program publisher untuk publish data random
# host redis server pada alamat 192.168.43.95
# data di publish setiap satu clock while


import redis
import time
import traceback
from random import seed
from random import random

if __name__ == '__main__':

    r = redis.StrictRedis(host='192.168.43.95', port=6379)                # Connect to local Redis instance
    p = r.pubsub()                                                    # See https://github.com/andymccurdy/redis-py/#publish--subscribe

    print("[PUBLISH] Start")

    # except Exception as e:
    #     print("Exception raised!.")
    #     print(str(e))
    #     print(traceback.format_exc())

    while(True):
        # seed(4)
        value = random() * 10
        r.publish('data/Sensor', value)                                # PUBLISH START message on startScripts channel

        # time.sleep(1) 

    print("Done")