#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The primary maintainer of this project is
# Arezqui Belaid <info@star2billing.com>
#

from django.conf.urls import url
from mod_sms.views import sms_dashboard, sms_campaign_list, sms_campaign_add,\
        sms_campaign_del, sms_campaign_duplicate, sms_campaign_text_message,\
        update_sms_campaign_status_cust, sms_campaign_change, update_sms_campaign_status_admin,\
        sms_report, export_sms_report

urlpatterns = [

                       # SMS Campaign urls
                       url(r'^sms_dashboard/$', sms_dashboard),
                       url(r'^sms_campaign/$', sms_campaign_list),
                       url(r'^sms_campaign/add/$', sms_campaign_add),
                       url(r'^sms_campaign/del/(.+)/$', sms_campaign_del),
                       url(r'^sms_campaign/duplicate/(.+)/$', sms_campaign_duplicate),
                       url(r'^sms_campaign/text_message/(.+)/$', sms_campaign_text_message),

                       # SMS Campaign Actions (start|stop|pause|abort) for customer UI
                       url(r'^sms_campaign/update_sms_campaign_status_cust/(\d*)/(\d*)/$',
                       update_sms_campaign_status_cust),
                       url(r'^sms_campaign/(.+)/$', sms_campaign_change),

                       # SMS Campaign Actions (start|stop|pause|abort) for Admin UI
                       url(r'^update_sms_campaign_status_admin/(\d*)/(\d*)/$',
                       update_sms_campaign_status_admin),

                       # SMS Report urls
                       url(r'^sms_report/$', sms_report),
                       url(r'^export_sms_report/$', export_sms_report),
]
