import json
from django.http import JsonResponse

def get(request, *callback_args, **callback_kwargs):
    body = request.body,
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    print(data),
    return JsonResponse(data)
