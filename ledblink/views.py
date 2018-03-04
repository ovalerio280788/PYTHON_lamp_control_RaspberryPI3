from django.shortcuts import render
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)


def blinker(request):
    status = "pending"
    if 'on' in request.POST:
        print("Turning on")
        GPIO.output(18, 0)
        status = 'on'
    elif 'off' in request.POST:
        print("Turning off")
        GPIO.output(18, 1)
        status = 'off'

    context = {
        'status': status,
    }

    return render(request, 'control_page.html', context)
