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
from dialer_audio.views import audio_list, audio_add, audio_del, audio_change

urlpatterns = [
                       # Audio urls
                       url(r'^module/audio/$', audio_list),
                       url(r'^module/audio/add/$', audio_add),
                       url(r'^module/audio/del/(.+)/$', audio_del),
                       url(r'^module/audio/(.+)/$', audio_change),
]
