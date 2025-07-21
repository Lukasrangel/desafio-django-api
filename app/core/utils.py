from django.http import JsonResponse


class JsonResponseHelper:

    @staticmethod
    def success(message,data=None, status=200):
        return JsonResponse({
            "success": True,
            'message': message,
            "data": data,
        }, status=status)

    @staticmethod
    def error(error=None,status=400):
        return JsonResponse({
            "success": False,
            "data": None,
            "error": error
        }, status=status)