# -*-  coding: utf-8 -*-

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

"""HITAP Hizmet Tazminat Sil

Hitap'da personelin Hizmet Tazminat bilgilerinin silinmesi sağlayan class.

"""

from ulakbus.services.personel.hitap.hitap_sil import HITAPSil


class HizmetTazminatSil(HITAPSil):
    """
    HITAP Silme servisinden kalıtılmış Hizmet Mahkeme Bilgisi Silme servisi

    """

    @staticmethod
    def get_name():
        # Zato service ismi
        return "hizmet_tazminat_sil"

    DEPLOY = True
    CONNECTION = "channel"
    DATA_FORMAT = "json"
    CHANNEL_NAME = "hizmet.tazminat.sil.channel"
    URL_PATH = '/personel/hitap/hizmet-tazminat-sil'
    TRANSPORT = "plain_http"
    IS_ACTIVE = True
    IS_INTERNAL = False

    def handle(self):
        """Servis çağrıldığında tetiklenen metod.

        Attributes:
            service_name (str): İlgili Hitap sorgu servisinin adı
            service_dict (dict): ''HizmetTazminat'' modelinden gelen kayıtların alanları,
                    HizmetTazminatDelete servisinin alanlarıyla eşlenmektedir.
        """

        self.service_dict['fields']['tckn'] = self.request.payload.get('tckn', '')
        self.service_dict['fields']['kayitNo'] = self.request.payload.get('kayit_no', '')
        self.service_dict['required_fields'] = ['tckn', 'kayitNo']

        super(HizmetTazminatSil, self).handle()
