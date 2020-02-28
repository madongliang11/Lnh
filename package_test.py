
class Request(object):

    def __init__(self, obj):
        self.obj = obj

    @property
    def user(self):
        return self.obj.authticate()


class Auth(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def authticate(self):
        return True


class APIview(object):

    def dispath(self):
        self.f2()

    def f2(self):
        a = Auth('ma', '18')
        req = Request(a)
        print(req.obj)
        print(req.obj.name)
        print(req.obj.age)
        print(req.user)

obj = APIview()
obj.dispath()
