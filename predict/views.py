import pickle
from django.shortcuts import render
from django.http import JsonResponse
from predict.models import PredictionResults
from django.contrib.auth.decorators import login_required
import os

app_name = 'predict'


def encoding(breathing_problem, sore_throat, Fever, dry_cough):
    x_test = [0] * 12
    if breathing_problem.lower() == 'no':
        x_test[2] = 1
    elif breathing_problem.lower() == 'mild':
        x_test[0] = 1
    elif breathing_problem.lower() == 'moderate':
        x_test[1] = 1
    if sore_throat.lower() == 'no':
        x_test[5] = 1
    elif sore_throat.lower() == 'mild':
        x_test[3] = 1
    elif sore_throat.lower() == 'moderate':
        x_test[4] = 1
    if Fever.lower() == 'no':
        x_test[8] = 1
    elif Fever.lower() == 'mild':
        x_test[6] = 1
    elif Fever.lower() == 'moderate':
        x_test[7] = 1
    if dry_cough.lower() == 'no':
        x_test[11] = 1
    elif dry_cough.lower() == 'mild':
        x_test[9] = 1
    elif dry_cough.lower() == 'moderate':
        x_test[10] = 1
    return x_test


@login_required(login_url='/Account/login')
def predict(request):
    return render(request, 'predict.html')


@login_required(login_url='/Account/login')
def predict_chances(request):
    if request.POST.get('action') == 'post':
        # Receive data from client
        cough = str(request.POST.get('cough'))
        fever = str(request.POST.get('fever'))
        sore_throat = str(request.POST.get('sore_throat'))
        breathing = str(request.POST.get('breathing'))
        modulePath = os.path.dirname(__file__)  # get current directory
        filePath = os.path.join(modulePath, 'LGBM.txt')
        with open(filePath, 'rb') as f:
            LGBM = pickle.load(f)
        result = LGBM.predict([encoding(breathing, sore_throat, fever, cough)])
        classification = result[0]
        if classification == 0:
            classification = "NEGATIVE"
        else:
            classification = "POSITIVE"

        print(classification)
        PredictionResults.objects.create(user=request.user.username, cough=cough, fever=fever,
                                         sore_throat=sore_throat, breathing=breathing,
                                         classification=classification)

        return JsonResponse({'result': classification, 'cough': cough,
                             'fever': fever, 'sore_throat': sore_throat, 'breathing': breathing},
                            safe=False)
