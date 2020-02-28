import json
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.authentication import BaseAuthentication


# FBV
# 加这个装饰器表示该函数免除csrf认证
@csrf_exempt
def users(request):
    user_list = ['madl', 'josn']
    return HttpResponse(json.dumps(user_list))


# CBV
'''
源码解析：
从路由开始——》调用as_view()方法——》view()方法——》最终调用dispatch()函数——》通过getattr(self, request.method.lower())
映射到对应的request.method方法上['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
'''

# 如果多个类公用的功能，可以写个基类
class MyBaseView(object):
    def dispatch(self, request, *args, **kwargs):
        print('before')
        ret = super(MyBaseView, self).dispatch(request, *args, **kwargs)
        print('after')
        return ret


class Studentsview(MyBaseView, View):
    # 重写父类View的dispatch方法
    # def dispatch(self, request, *args, **kwargs):
    #     # return HttpResponse('dispath')
    #     func = getattr(self, request.method.lower())
    #     return func(request, *args, **kwargs)

    # def dispatch(self, request, *args, **kwargs):
    #     print('before')
    #     ret = super(Studentsview, self).dispatch(request, *args, **kwargs)
    #     print('after')
    #     return ret

    def get(self, request, *args, **kwargs):
        return HttpResponse('GET')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')

    def put(self, request, *args, **kwargs):
        return HttpResponse('PUT')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('DELETE')


class TeacherView(MyBaseView, View):
    # 重写父类View的dispatch方法
    # def dispatch(self, request, *args, **kwargs):
    #     # return HttpResponse('dispath')
    #     func = getattr(self, request.method.lower())
    #     return func(request, *args, **kwargs)

    # def dispatch(self, request, *args, **kwargs):
    #     print('before')
    #     ret = super(TeacherView, self).dispatch(request, *args, **kwargs)
    #     print('after')
    #     return ret

    def get(self, request, *args, **kwargs):
        return HttpResponse('GET方法')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')

    def put(self, request, *args, **kwargs):
        return HttpResponse('PUT')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('DELETE')


###################################################
@method_decorator(csrf_exempt, name='dispatch')
class Workerview(View):

    # 免于csrf认证
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(Workerview, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse('GET')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')

    def put(self, request, *args, **kwargs):
        return HttpResponse('PUT')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('DELETE')

###################################################
def get_order(request):
    return HttpResponse('get_order')

def add_order(request):
    return HttpResponse('add_order')

def update_order(request):
    return HttpResponse('update_order')

def delete_order(request):
    return HttpResponse('delete_order')


###################################################
@csrf_exempt
def order(request):
    if request.method == 'GET':
        return HttpResponse('获取订单')
    elif request.method == 'POST':
        return HttpResponse('创建订单')
    elif request.method == 'PUT':
        return HttpResponse('更新订单')
    elif request.method == 'DELETE':
        return HttpResponse('删除订单')
    else:
        return HttpResponse('错误的请求方式')

####################################################


@method_decorator(csrf_exempt, name='dispatch')
class OrderView(View):
    def get(self, request, *args, **kwargs):
        ret = {
            'code': 1000,
            'msg': 'xxxx'
        }
        return HttpResponse(json.dumps(ret), status=201)

    def post(self, request, *args, **kwargs):
        return HttpResponse('创建订单')

    def put(self, request, *args, **kwargs):
        return HttpResponse('更新订单')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('删除订单')


'''
rest framework
APIView继承的django中自带的View
'''
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions

class MyAuthentication(object):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        # 获取用户名密码，去数据校验
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return ('alex', None)

    def authenticate_header(self, val):
        pass


# @method_decorator(csrf_exempt, name='dispatch')
class DogView(APIView):
    authentication_classes = [MyAuthentication, ]

    def get(self, request, *args, **kwargs):
        # self.dispatch()
        print(request)
        # 如果认证成功，会获取到用户信息
        print(request.user)
        ret = {
            'code': 1000,
            'msg': 'xxxx'
        }
        return HttpResponse(json.dumps(ret), status=201)

    def post(self, request, *args, **kwargs):
        return HttpResponse('创建Dog')

    def put(self, request, *args, **kwargs):
        return HttpResponse('更新Dog')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('删除Dog')