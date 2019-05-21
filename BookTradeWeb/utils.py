import json
import typing
import traceback
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from typing import Dict, Any, Callable, List

def make_errors(msg: str) -> Dict[str, Any]:
    return {'error': msg, 'code': 1}

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
            request.data['file'] = request.FILES['file']
        return self.do_dispatch(request, *args, **kwargs)

    def do_dispatch(self, *args, **kwargs):
        handler = getattr(self, self.request.method.lower(), None)
        if not callable(handler):
            return JsonResponse(make_errors(f"http method {self.request.method.lower()} not allowed "))
        else:
            try:
                data = handler(*args, **kwargs)
                if data is None:
                    data = 'success'
                if self.request.method == 'GET':
                    return HttpResponse(data)
                else:
                    return JsonResponse({'data': data, 'code': 0})
            except Exception as e:
                traceback.print_exc()
                return JsonResponse(make_errors(str(e)))