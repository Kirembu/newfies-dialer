#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2015 Star2Billing S.L.
#
# The primary maintainer of this project is
# Arezqui Belaid <info@star2billing.com>
#
from django.conf.urls import handler404, handler500, \
    include, url
from django.conf import settings
from django.views.i18n import javascript_catalog
from django.views.static import serve
from apirest.urls import urlpatterns as urlpatterns_apirest
from agent.api_urls import urlpatterns as urlpatterns_agent_apirest
from appointment.urls import urlpatterns as urlpatterns_appointment
from frontend.urls import urlpatterns as urlpatterns_frontend
from frontend import views as frontend_views
from dialer_contact.urls import urlpatterns as urlpatterns_dialer_contact
from dialer_campaign.urls import urlpatterns as urlpatterns_dialer_campaign
from dialer_cdr.urls import urlpatterns as urlpatterns_dialer_cdr
from dnc.urls import urlpatterns as urlpatterns_dnc
from user_profile.urls import urlpatterns as urlpatterns_user_profile
from survey.urls import urlpatterns as urlpatterns_survey
from dialer_audio.urls import urlpatterns as urlpatterns_dialer_audio
from frontend_notification.urls import urlpatterns as urlpatterns_frontend_notification
# from agent.urls import urlpatterns as urlpatterns_agent
# from callcenter.urls import urlpatterns as urlpatterns_callcenter
from mod_sms.urls import urlpatterns as urlpatterns_mod_sms
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib import admin
import os


admin.autodiscover()
dajaxice_autodiscover()

js_info_dict = {
    'domain': 'djangojs',
    'packages': ('dialer_campaign',
                 'user_profile',
                 'survey',
                 'audiofield'),
}

urlpatterns = [
                       url(r'^logout/$', frontend_views.logout_view),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^i18n/', include('django.conf.urls.i18n')),
                       url(r'^jsi18n/$', javascript_catalog, js_info_dict),
                       url(r'^admin_tools/', include('admin_tools.urls')),
                       url(r'^static/(?P<path>.*)$', serve,
                        {'document_root': settings.STATIC_ROOT}),
                       # (r'^sentry/', include('sentry.web.urls')),
                       # (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
                       url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
                       url(r'^accounts/', include('registration.backends.default.urls')),
                       ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]

urlpatterns += urlpatterns_apirest
urlpatterns += urlpatterns_agent_apirest
urlpatterns += urlpatterns_frontend
urlpatterns += urlpatterns_dialer_contact
urlpatterns += urlpatterns_dialer_campaign
urlpatterns += urlpatterns_dialer_cdr
urlpatterns += urlpatterns_dnc
urlpatterns += urlpatterns_user_profile
urlpatterns += urlpatterns_survey
urlpatterns += urlpatterns_dialer_audio
urlpatterns += urlpatterns_frontend_notification
# urlpatterns += urlpatterns_agent
# urlpatterns += urlpatterns_callcenter
urlpatterns += urlpatterns_appointment
urlpatterns += urlpatterns_mod_sms

urlpatterns += [
    url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip(os.sep),
        serve, {'document_root': settings.MEDIA_ROOT}),
]


handler404 = 'urls.custom_404_view'
handler500 = 'urls.custom_500_view'


def custom_404_view(request, template_name='404.html'):
    """404 error handler which includes ``request`` in the context.

    Templates: `404.html`
    Context: None
    """
    from django.template import Context, loader
    from django.http import HttpResponseServerError

    t = loader.get_template('404.html')  # Need to create a 404.html template.
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))


def custom_500_view(request, template_name='500.html'):
    """500 error handler which includes ``request`` in the context.

    Templates: `500.html`
    Context: None
    """
    from django.template import Context, loader
    from django.http import HttpResponseServerError

    t = loader.get_template('500.html')  # Need to create a 500.html template.
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))
