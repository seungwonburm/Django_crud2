import json

from django.http import JsonResponse
from django.views import View
from products.models import Owners, Dogs

class OwnersView(View):
    def get(self, request):
        owners = Owners.objects.all()
        result=[]
        
        for owner in owners:
            dogs=owner.dogs_set.all()
            dog_result=[]
            for dog in dogs:
                dog_info={
                    'name' : dog.name,
                    'age' : dog.age
                }
                dog_result.append(dog_info)

            owner_info={
                'name' : owner.name,
                'age' : owner.age,
                'email' : owner.email,
                'dog_result' : dog_result
            }
            result.append(owner_info)

        return JsonResponse({'result' : result}, status=200)
    
    def post(self, request):
        data = json.loads(request.body)
        Owners.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )
        return JsonResponse({'message' : 'SUCCESS'}, status =201)

class DogsView(View):
    def get(self, request):
        dogs = Dogs.objects.all()
        result=[]
        for dog in dogs:
            dog_info={
                'name' : dog.name,
                'age' : dog.age,
                'owner' : dog.owner.name
            }
            result.append(dog_info)
        return JsonResponse({'result' : result}, status=200)
    
    def post(self, request):
        data = json.loads(request.body)
        Dogs.objects.create(
            name = data['name'],
            age = data['age'],
            owner = Owners.objects.get(name=data['owner'])
        )
        return JsonResponse({'message' : 'SUCCESS!'}, status = 201)