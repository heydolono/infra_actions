from rest_framework.response import Response


def index(request):
    return Response('У меня получилось!')


def second_page(request):
    return Response('А это вторая страница')
