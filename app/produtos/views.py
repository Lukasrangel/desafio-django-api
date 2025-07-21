from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Produto
import json
from .serializers import ProdutoSerializer
from core.utils import JsonResponseHelper


@method_decorator(csrf_exempt, name='dispatch')
class ProdutoAPI(View):
    def get(self, request):
        produtos = Produto.objects.all()
        data = [
            {
                "id": produto.id,
                "nome": produto.nome,
                "preco": float(produto.preco)
            }
            for produto in produtos
        ]
        return JsonResponse(data, safe=False)

    def post(self, request):

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponseHelper.errors('Requisição inválida')
        
        serializer = ProdutoSerializer(data)
        if not serializer.is_valid():
            return JsonResponseHelper.errors(serializer.errors)

        produto = Produto.objects.create(**serializer.validated_data)

        response_data = {
            "id": produto.id,
            "nome": produto.nome,
            "preco": float(produto.preco)
        }
        return JsonResponseHelper.success("Produto cadastrado com sucesso", response_data, status=201)
