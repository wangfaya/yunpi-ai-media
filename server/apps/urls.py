# coding: utf-8
from server.apps.audio_module.urls import user_urls



sub_urls = [
    ('/api', user_urls)

]


def register_urls(app):
    """
    生成路由
    """

    for pre_url, routes in sub_urls:
        for suf_url, handler in routes:
            app.add_url_rule(r"{}{}".format(pre_url, suf_url), view_func=handler)
