from base64 import encode
from django.shortcuts import render
from email.mime import image
from importlib.resources import path
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import date 
from . models import *
from django.views.decorators.csrf import csrf_exempt
import imagehash
from PIL import Image
import cv2
import face_recognition


# vending machine function
@csrf_exempt
def CheckExist(request):
    if request.method == 'POST':
        # getting fingerprint and image
        received_fingerprint = request.FILES['fingerprint']
        received_photo = request.FILES['photo']

        hash_received_fingerprint = imagehash.average_hash(
            Image.open(received_fingerprint))

        
        open_received_photo=face_recognition.load_image_file(received_photo)
        encode_received_photo=face_recognition.face_encodings(open_received_photo)[0]


        print('hashed fingerprint', hash_received_fingerprint)

        existing_fingerprints = UserDetails.objects.all()

        for finger in existing_fingerprints:
            hash_finger = imagehash.average_hash(
                Image.open(finger.fingerprint))
            if hash_finger == hash_received_fingerprint:
                print('**old user**')
                print('old user tb finger path', finger.fingerprint)

                transaction = Transaction.objects.get(user__id=finger.id)
                old_photo= UserDetails.objects.get(id=finger.id)

                open_exist_photo=face_recognition.load_image_file(old_photo.photo)
                encode_exist_photo=face_recognition.face_encodings(open_exist_photo)[0]

                check_photo=face_recognition.compare_faces([encode_received_photo],encode_exist_photo)

                if not check_photo[0]:
                    return JsonResponse({'Access':'photo not matching'})
                print(check_photo[0])
                print('fayis')
                todayDate = date.today()
                d0 = transaction.LastAccessedDate
                d1 = todayDate
                delta = d1 - d0

                print(finger.id)
                if transaction.status < 3:
                    transaction.status = transaction.status+1
                    transaction.LastAccessedDate = date.today()
                    transaction.save()
                    return JsonResponse({'Access': 'Allowed'})
                    
                elif delta.days>30:
                    transaction.status=1
                    transaction.LastAccessedDate=date.today()
                    transaction.save()
                    return JsonResponse({'Access':'Allowed'})
                else:
                    return JsonResponse({'Access':'Denied'})  
                break                  
        else:
            print("**New user**")
            user1=UserDetails(fingerprint=received_fingerprint,photo=received_photo)
            user1.save()
            print(user1)
            print(user1.id)
            Transaction(user=user1, LastAccessedDate=date.today(), status=1).save()
            return JsonResponse({'Access':'Allowed'})
    else:
        return HttpResponse("Need post request")




