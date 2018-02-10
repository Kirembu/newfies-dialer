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
from django.conf.urls import include, url
from dialer_campaign import views

urlpatterns = [
                       #  Campaign urls
                       url(r'^campaign/$', views.campaign_list),
                       url(r'^campaign/add/$', views.campaign_add),
                       url(r'^campaign/del/(.+)/$', views.campaign_del),
                       url(r'^campaign_duplicate/(.+)/$', views.campaign_duplicate),

                       # Campaign Actions (start|stop|pause|abort)
                       url(r'^campaign/update_campaign_status_cust/(\d*)/(\d*)/$',
                           views.update_campaign_status_cust),
                       url(r'^campaign/(.+)/$', views.campaign_change),
                       # Campaign Actions (start|stop|pause|abort) for Admin UI
                       url(r'^update_campaign_status_admin/(\d*)/(\d*)/$',
                       views.update_campaign_status_admin),

                       #  Subscriber urls
                       url(r'^subscribers/$', views.subscriber_list),
                       url(r'^subscribers/export_subscriber/$', views.subscriber_export),

                       # Send notification to admin regarding dialer setting
                       url(r'^notify/admin/$', views.notify_admin),
]
