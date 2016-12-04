# -*-  coding: utf-8 -*-

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

"""HITAP Mahkeme Guncelle

Hitap'a personelin Mahkeme bilgilerinin guncellemesini yapar.

"""

from ulakbus.services.personel.hitap.hitap_guncelle import HITAPGuncelle


class HizmetMahkemeGuncelle(HITAPGuncelle):
    """HITAP Guncelleme servisinden kalıtılmış Hizmet Mahkeme Bilgi Guncelleme servisi

    """

    @staticmethod
    def get_name():
        # Zato service ismi
        return "hizmet_mahkeme_guncelle"

    DEPLOY = True
    CONNECTION = "channel"
    DATA_FORMAT = "json"
    CHANNEL_NAME = "hizmet.mahkeme.guncelle.channel"
    URL_PATH = '/personel/hitap/hizmet-mahkeme-guncelle'
    TRANSPORT = "plain_http"
    IS_ACTIVE = True
    IS_INTERNAL = False

    def handle(self):
        """Servis çağrıldığında tetiklenen metod.

        Attributes:
            service_name (str): İlgili Hitap sorgu servisinin adı
            service_dict (dict): Request yoluyla gelen kayıtlar,
                    HizmetMahkemeUpdate servisinin alanlarıyla eşlenmektedir.
                    Filtreden geçecek tarih alanları ve servis tarafında gerekli olan
                    alanlar listede tutulmaktadır.

        """

        self.service_dict = {
            'fields': {
                'kayitNo': self.request.payload.get('kayit_no', ''),
                'tckn': self.request.payload.get('tckn', ''),
                'mahkemeAd': self.request.payload.get('mahkeme_ad', ''),
                'sebep': self.request.payload.get('sebep', ''),
                'kararTarihi': self.request.payload.get('karar_tarihi', ''),
                'kararSayisi': self.request.payload.get('karar_sayisi', ''),
                'kesinlesmeTarihi': self.request.payload.get('kesinlesme_tarihi', ''),
                'asilDogumTarihi': self.request.payload.get('asil_dogum_tarihi', ''),
                'tashihDogumTarihi': self.request.payload.get('tashih_dogum_tarihi', ''),
                'gecerliDogumTarihi': self.request.payload.get('gecerli_dogum_tarihi', ''),
                'asilAd': self.request.payload.get('asil_ad', ''),
                'tashihAd': self.request.payload.get('tashih_ad', ''),
                'asilSoyad': self.request.payload.get('asil_soyad', ''),
                'tashihSoyad': self.request.payload.get('tashih_soyad', ''),
                'aciklama': self.request.payload.get('aciklama', ''),
                'gunSayisi': self.request.payload.get('gun_sayisi', ''),
                'kurumOnayTarihi': self.request.payload.get('kurum_onay_tarihi', '')
            },
            'date_filter': ['kesinlesmeTarihi', 'asilDogumTarihi', 'tashihDogumTarihi',
                            'gecerliDogumTarihi', 'kurumOnayTarihi'],
            'required_fields': ['kayitNo', 'tckn', 'mahkemeAd', 'sebep', 'kararTarihi',
                                'kararSayisi', 'kurumOnayTarihi']

        }
        super(HizmetMahkemeGuncelle, self).handle()
