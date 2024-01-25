"""
WSGI config for multiple_expressions_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from static_ranges import Ranges # *
from dj_static import Cling, MediaCling # *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multiple_expressions_backend.settings')
application = Ranges(Cling(MediaCling(get_wsgi_application()))) # *

# import os
# from django.core.wsgi import get_wsgi_application
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multiple_expressions_backend.settings')
# application = get_wsgi_application()

# * New setting to allow for partial requests (video looping and weeking)
# Followed this post: https://snehaveerakumar.medium.com/upload-videos-with-proper-seekbar-in-django-21039b1fd87