__author__ = 'wuwy'
from blog.models import Visitor
from datetime import datetime


class VisitorMiddleWare:

    def process_request(self, request):
        visitor = Visitor()
        visitor.ip = str(request.META['REMOTE_ADDR'])
        visitor.time = datetime.now()
        visitor.save()
        print(111)

    def __init__(self):
        pass


