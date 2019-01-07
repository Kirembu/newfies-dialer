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

from django.conf.urls import url
from survey.views import *

urlpatterns = [
                       # Survey urls
                       url(r'^module/survey/$', survey_list),
                       url(r'^module/survey/add/$', survey_add),
                       url(r'^module/sealed_survey_view/(.+)/$', sealed_survey_view),
                       url(r'^module/survey/del/(.+)/$', survey_del),
                       url(r'^module/survey/(.+)/$', survey_change),
                       url(r'^module/export_survey/(.+)/$', export_survey),
                       url(r'^module/import_survey/$', import_survey),
                       url(r'^module/sealed_survey/$', sealed_survey_list),
                       url(r'^module/seal_survey/(.+)/$', seal_survey),

                       # Section urls
                       url(r'^section/add/$', section_add),
                       url(r'^section/branch/add/$', section_branch_add),
                       url(r'^section/delete/(?P<id>\w+)/$', section_delete),
                       url(r'^section/(?P<id>\w+)/$', section_change),
                       url(r'^section/script/(?P<id>\w+)/$', section_script_change),
                       url(r'^section/script_play/(?P<id>\w+)/$', section_script_play),
                       url(r'^section/branch/(?P<id>\w+)/$', section_branch_change),

                       # Survey Report urls
                       url(r'^survey_report/$', survey_report),
                       url(r'^export_surveycall_report/$', export_surveycall_report),
                       url(r'^survey_campaign_result/(?P<id>\w+)/$', survey_campaign_result),
]
