from django.http import JsonResponse
from django.views import View
from .models import Account
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
class AccountView(View):

    def get(self, request, *args, **kwargs):
        try:
            accounts = list(Account.objects.values())
            return JsonResponse(accounts, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            account = Account.objects.create(**data)
            return JsonResponse({'account': account.id, 'uuid': account.uuid, 'name': account.name}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def put(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            account = Account.objects.get(id=data['id'])
            for key, value in data.items():
                setattr(account, key, value)
            account.save()
            return JsonResponse({'message': 'Account updated successfully', 'account': account.id}, status=200)
        except Account.DoesNotExist:
            return JsonResponse({'error': 'Account not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def delete(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            account = Account.objects.get(id=data['id'])
            account.delete()
            return JsonResponse({'message': 'Account deleted successfully', 'account': account.id}, status=200)
        except Account.DoesNotExist:
            return JsonResponse({'error': 'Account not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
