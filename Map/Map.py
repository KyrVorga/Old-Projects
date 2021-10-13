import time
import random
from playsound import playsound

if __name__ == "__main__":
    
    flag = True
    while flag == True:
        time.sleep((random.random() * 10))
        playsound('audio\honk.mp3')

