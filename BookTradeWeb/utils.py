import json
import typing
import traceback
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from typing import Dict, Any, Callable, List

def make_errors(msg: str) -> Dict[str, Any]:
    return {'error': msg, 'code': 1}

def make_success(msg: str) -> Dict[str, Any]:
    return {'success': msg, 'code': 0}

class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        request.data = {}
        if request.method == 'GET':
            request.data = request.GET.dict()
        elif request.content_type == 'application/json':
            request.data = request.body.replace(b"'", b'"')
            request.data = json.loads(request.data)
        elif request.content_type == 'multipart/form-data':
            request.data = request.POST.dict()
            if not request.FILES == None:
                request.data['file'] = request.FILES['file']
        elif request.content_type == 'application/x-www-form-urlencoded':
            request.data = request.POST.dict()
        return self.do_dispatch(request, *args, **kwargs)

    def do_dispatch(self, *args, **kwargs):
        handler = getattr(self, self.request.method.lower(), None)
        if not callable(handler):
            return JsonResponse(make_errors(f"http method {self.request.method.lower()} not allowed "))
        else:
            try:
                data = handler(*args, **kwargs)
                if data == None:
                    return JsonResponse(make_success('success'))
                elif self.request.method == 'GET' or not isinstance(data, dict):
                    return data
                else:
                    return JsonResponse({'data': data, 'code': 0})
            except Exception as e:
                traceback.print_exc()
                return JsonResponse(make_errors(str(e)))

class Category():
    category_dict = {
        'education' : '教育',
        'art' : '文艺',
        'technology' : '科技',
        'social' : '人文社科',
        'activate' : '励志',
        'life' : '生活',
        'manage' : '经管',
        'in' : '期刊/进口书',
        'video' : '音像',
        'child' : '童书'
    }

    @classmethod
    def GetCategory(cls, key):
        return cls.category_dict.get(key)