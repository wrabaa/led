import RPi.GPIO as GPIO
import time

def simulate_relay(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    try:
        print("Turning relay on...")
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(5)

        print("Turning relay off...")
        GPIO.output(pin, GPIO.LOW)
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    pin = 18
    simulate_relay(pin)
