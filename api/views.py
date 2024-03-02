""" Views """

import requests
import environ

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

env = environ.Env()
environ.Env.read_env('.env')


class Bank_List(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        try:
            bank_url = env("BANK_API_HOST")
            response = requests.get(f'{bank_url}/v1/pagos/p2p/bancos')
            try:
                return JsonResponse(response.json(), status=200, safe=False, json_dumps_params={'ensure_ascii': False})
            except requests.JSONDecodeError:
                return JsonResponse({'error': 'JSONDecodeError',
                                     'message': 'Error al transformar la respuesta del banco',
                                     'url': f'{bank_url}/v1/pagos/p2p/bancos',
                                     'data': response.text})
        except Exception as e:
            return JsonResponse({'message': f'Error al obtener la lista de bancos: {e}'}, status=500)
