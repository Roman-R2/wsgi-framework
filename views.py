from r2_framework.templator import render


class Index:
    def __call__(self, request, *args, **kwargs):
        return '200 OK', render('index.html',
                                date=request.get('date', None))


class About:
    def __call__(self, request, *args, **kwargs):
        return '200 OK', render('about.html')


class Code:
    def __call__(self, request, *args, **kwargs):
        return '200 OK', render('code.html')
