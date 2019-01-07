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
from dialer_contact.views import *

urlpatterns = [
                       # Phonebook urls
                       url(r'^phonebook/$', phonebook_list),
                       url(r'^phonebook/add/$', phonebook_add),
                       url(r'^phonebook/contact_count/$', get_contact_count),
                       url(r'^phonebook/del/(.+)/$', phonebook_del),
                       url(r'^phonebook/(.+)/$', phonebook_change),

                       # Contacts urls
                       url(r'^contact/$', contact_list),
                       url(r'^contact/add/$', contact_add),
                       url(r'^contact_import/$', contact_import),
                       url(r'^contact/del/(.+)/$', contact_del),
                       url(r'^contact/(.+)/$', contact_change),
]
