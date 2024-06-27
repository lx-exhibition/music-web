from django.apps import AppConfig
from django.core.signals import request_started, request_finished
from utils.handlers import pre_req, post_req


class ExampleAppConfig(AppConfig):
    name = 'music'

    def ready(self):
        request_started.connect(pre_req)
        request_finished.connect(post_req)
