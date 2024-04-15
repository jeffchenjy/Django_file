from celery import shared_task
from time import sleep
import serial
SERIAL_PORT = '/dev/ttyAMA0'
BAUD_RATE = 9600
@shared_task
def listen_uart():
    # 打開UART
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    try:
        while True:
            if ser.in_waiting > 0:
                # 讀取數據
                data = ser.readline().decode('utf-8').strip()
                print("Received data:", data)
            else:
                sleep(0.1)
    except:
        print("Error")
    finally:
        print("End")