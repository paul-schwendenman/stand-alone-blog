from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, TemplateDoesNotExist
import json

def render_to_json(func):
    def wrapper(request, *args, **kw):
        response_data = func(request, *args, **kw)

        return HttpResponse(json.dumps(response_data),
            content_type="application/json")
    return wrapper

def render_to_template(template):
    def real_decorator(func):
        def wrapper(request, *args, **kw):
            response_data = func(request, *args, **kw)
           
            if isinstance(response_data, dict):
                response_data['user__'] = request.user
                response_data['params'] = request.REQUEST
           
                return render_to_response(template, response_data,
                            context_instance=RequestContext(request))
            elif isinstance(response_data, HttpResponse):
                return response_data
        return wrapper
    return real_decorator

def render_to_template_json(template):
    def real_decorator(func):
        def wrapper(request, *args, **kw):
            response_data = func(request, *args, **kw)
           
            if isinstance(response_data, dict):
                try:
                    return render_to_response(template, response_data,
                                context_instance=RequestContext(request))
                except TemplateDoesNotExist:
                    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")
            elif isinstance(response_data, HttpResponse):
                return response_data
        return wrapper
    return real_decorator

