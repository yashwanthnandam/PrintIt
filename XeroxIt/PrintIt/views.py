import os
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse    # ← new import
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
import pika
from PIL import Image
import socket

@csrf_exempt
def message(request):
    user = request.POST.get('From')
    message = request.POST.get('Body')
    media_url = request.POST.get('MediaUrl0')
    print(f'{user} sent {message}')

    response = MessagingResponse()
    if media_url:
        r = requests.get(media_url)
        content_type = r.headers['Content-Type']
        username = user.split(':')[1]  # remove the whatsapp: prefix from the number
        if content_type == 'image/jpeg':
            filename = f'uploads/{username}/{message}.jpg'
        elif content_type == 'image/png':
            filename = f'uploads/{username}/{message}.png'
        elif content_type == 'image/gif':
            filename = f'uploads/{username}/{message}.gif'
        else:
            filename = None
        if filename:
            if not os.path.exists(f'uploads/{username}'):
                os.mkdir(f'uploads/{username}')
            with open(filename, 'wb') as f:
                f.write(r.content)
            response.message('Thank you! Your image was received.')
        else:
            response.message('The file that you submitted is not a supported image type.')
    else:
        response.message('Please send an image!')
    return HttpResponse(str(response))

class Printer(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    @action(detail=False, methods=['post'])
    def find_printers_connected(self, request):
        TCP_IP = '192.168.29.117'
        TCP_PORT = 21
        BUFFER_SIZE = 1024
        data = {}
        try:
            img = Image.open('../docs/Costumer flow/PrintIT (1).jpg')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            data = s.recv(BUFFER_SIZE)
            s.send("hello")
            s.close()
        except:
             pass

        return Response(data)