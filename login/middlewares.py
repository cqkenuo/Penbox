from django.shortcuts import redirect
from django.conf import settings

class LoginAccquireMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url = request.get_full_path()
        is_login = request.session.get('is_login', None)
        if is_login or url.startswith(getattr(settings, "WHITE_URL", ())):
            pass
        else:
            # 返回login页面重新登陆，next表示从哪个页面返回
            return redirect('/login/?next=%s' % url)

        response = self.get_response(request)

        return response

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     pass
    #
    # def process_exception(self,request,exception):
    #     pass