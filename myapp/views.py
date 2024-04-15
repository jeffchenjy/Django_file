from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .tasks import listen_uart
import serial
# Create your views here.
SERIAL_PORT = '/dev/ttyAMA0'
BAUD_RATE = 9600
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

def GetCarCMD(request, command):
    ser.write(command.encode('utf-8'))
    return render(request, "Car_cmd.html", locals())

def Pi_camera(request):
    return render(request, "Pi_camera.html", locals())