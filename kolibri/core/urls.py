# -*- coding: utf-8 -*-
"""TODO: Write something about this module (everything in the docstring
enters the docs)

.. moduleauthor:: Learning Equality <info@learningequality.org>

"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [
    url('^', views.IndexView.as_view(), name='index'),
    # url('.* ', views.TODOView.as_view())
]
