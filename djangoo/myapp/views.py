from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def images(request):
    if request.method == 'GET':
        return JsonResponse({"message": "Getting Images!"})
    if request.method == 'POST':
        return JsonResponse({"message": "Posting Images!"}, status=201)
