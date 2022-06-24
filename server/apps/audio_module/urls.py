from .curd import AudioSynthetic

audio_urls = [
    ('/audio/synthetic', AudioSynthetic.as_view('login_code')),

]