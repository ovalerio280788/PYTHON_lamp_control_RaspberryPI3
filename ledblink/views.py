from django.shortcuts import render
from django.http import HttpResponse
# import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(18, GPIO.OUT)


def blinker(request):
    status = "pending"
    if 'on' in request.POST:
        # GPIO.output(18, 1)
        print("It will be on")
        status = 'on'
    elif 'off' in request.POST:
        # GPIO.output(18, 0)
        print("It will be off")
        status = 'off'

    context = {
        'status': status,
    }

    return render(request, 'control_page.html', context)
