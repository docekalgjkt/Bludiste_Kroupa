import xml.etree.ElementTree as ET
from init import Bludiste


def nacti_bludiste_z_xml(soubor):
    """
    Načte bludiště z XML souboru.
    :param soubor: Cesta k XML souboru.
    :return: Instance třídy Bludiste.
    """
    strom = ET.parse(soubor)
    koren = strom.getroot()

    sirka = int(koren.find("sirka").text)
    vyska = int(koren.find("vyska").text)

    zacatek_x = int(koren.find("zacatek/x").text)
    zacatek_y = int(koren.find("zacatek/y").text)
    konec_x = int(koren.find("konec/x").text)
    konec_y = int(koren.find("konec/y").text)

    mapa = []
    for radek in koren.find("mapa"):
        radek_hodnoty = [int(bunka.text) if bunka.text.isdigit() else bunka.text for bunka in radek]
        mapa.append(radek_hodnoty)

    return Bludiste(sirka, vyska, (zacatek_x, zacatek_y), (konec_x, konec_y), mapa)