from datetime import date

from views import Index, About, Code


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'some_key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/code/': Code(),
    '/about/': About(),
}
