import urllib.request
import html
from xml.etree import ElementTree

from typing import List

from home.scheduler.trigger.cron import Trigger


class Osmer(Trigger):
    def __init__(
        self, name: str, events: List["home.Event"], url: str, *args, **kwargs
    ):
        """
        >>> url = "https://dev.meteo.fvg.it/xml/previsioni/PW20211013.xml"
        >>> crawler = Osmer("forecast", [], url)
        >>> root = crawler.open(url)
        >>> forecast = root.findtext("previsioni/scadenze/scadenza[@id='1']/zone/zona[@id='{}']/PROBABILITAPRECIPITAZIONI".format(4))
        >>> int(forecast.replace("&gt;", "").replace("&lt;", ""))
        10
        """
        super(Osmer, self).__init__(name, events, *args, **kwargs)
        self._base_url = url

    def unescape(self, xml_text: str):
        """
        Remove &gt; and &lt; escapes, since they will broken the xml once escaped
        Unescape html elements inside xml.
        """
        xml_text = xml_text.replace("&gt;", "")
        xml_text = xml_text.replace("&lt;", "")
        xml_text = html.unescape(xml_text)
        return xml_text

    def open(self, url):
        request = urllib.request.Request(url, headers={"Accept": "application/xml"})
        response = urllib.request.urlopen(request)
        tree = ElementTree.parse(response)
        return tree.getroot()

    EXAMPLE = """
<data id="meteo.fvg_previsioni_xml">
<lingua>italiano</lingua>
<autore>meteo.fvg</autore>
<autore_url>http://www.meteo.fvg.it</autore_url>
<autore_email>support@meteo.fvg.it</autore_email>
<ultimo_aggiornamento>13-10-2021 09:25:37 UTC</ultimo_aggiornamento>
<previsioni>
<emissione>13-10-2021 09:17:00 UTC</emissione>
<SITUAZIONEGENERALE_TESTO>
Sulla regione affluiscono in quota correnti fredde da nord. Gioved&igrave; un debole fronte atlantico passer&agrave; sull'area alpina; venerd&igrave; alta pressione.
</SITUAZIONEGENERALE_TESTO>
<scadenze>
<scadenza id="1" data_validita="14-10-2021" giorno="DOMANI">
<zone>
<zona id="1" nome="REGIONE" descrizione="Regione">
<ATTENDIBILITA um="%">70</ATTENDIBILITA>
<TESTO>
Cielo in genere poco nuvoloso, forse anche sereno sulla costa, mentre sulle Alpi potr&agrave; essere variabile con vento da nord moderato in quota. Temperature basse per la stagione di notte e al mattino; gelate sull'area montana. Zero termico a 1500 m al mattino, 2000 m nel pomeriggio.
</TESTO>
<EVOLUZIONE00_SIMBOLO>0</EVOLUZIONE00_SIMBOLO>
<EVOLUZIONE00_DESCRIZIONE>sereno</EVOLUZIONE00_DESCRIZIONE>
<EVOLUZIONE12_SIMBOLO>0</EVOLUZIONE12_SIMBOLO>
<EVOLUZIONE12_DESCRIZIONE>sereno</EVOLUZIONE12_DESCRIZIONE>
<EVOLUZIONE24_SIMBOLO>1</EVOLUZIONE24_SIMBOLO>
<EVOLUZIONE24_DESCRIZIONE>variabile</EVOLUZIONE24_DESCRIZIONE>
</zona>
<zona id="2" nome="A1" descrizione="Alpi_Carniche">
<ATTENDIBILITA um="%">70</ATTENDIBILITA>
<TESTO>
Cielo poco nuvoloso o variabile con temperature basse per la stagione di notte e al mattino; gelate notturne. In quota vento da nord moderato e freddo anche di giorno per la stagione. Zero termico a 1500 m al mattino, 2000 m nel pomeriggio.
</TESTO>
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<QUOTANEVICATA um="m">-</QUOTANEVICATA>
<VENTO2000_DIREZIONE um="ottanti">N</VENTO2000_DIREZIONE>
<VENTO3000_DIREZIONE um="ottanti">N</VENTO3000_DIREZIONE>
<VENTO2000_INTENSITA um="m/s">8</VENTO2000_INTENSITA>
<VENTO3000_INTENSITA um="m/s">13</VENTO3000_INTENSITA>
<TMED1000 um="°C">5</TMED1000>
<TMED2000 um="°C">-2</TMED2000>
<ZEROTERMICO um="m">1700</ZEROTERMICO>
<CIELO_SIMBOLO>2</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>variabile</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>16</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE>N moderato</VENTO_DESCRIZIONE>
</zona>
<zona id="3" nome="A2" descrizione="Alpi_Giulie">
<ATTENDIBILITA um="%">70</ATTENDIBILITA>
<TESTO>
Cielo poco nuvoloso o variabile con temperature basse per la stagione di notte e al mattino; gelate notturne. In quota vento da nord moderato e freddo anche di giorno per la stagione. Zero termico a 1500 m al mattino, 2000 m nel pomeriggio.
</TESTO>
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<QUOTANEVICATA um="m">-</QUOTANEVICATA>
<VENTO2000_DIREZIONE um="ottanti">N</VENTO2000_DIREZIONE>
<VENTO3000_DIREZIONE um="ottanti">N</VENTO3000_DIREZIONE>
<VENTO2000_INTENSITA um="m/s">10</VENTO2000_INTENSITA>
<VENTO3000_INTENSITA um="m/s">16</VENTO3000_INTENSITA>
<TMED1000 um="°C">4</TMED1000>
<TMED2000 um="°C">-3</TMED2000>
<ZEROTERMICO um="m">1500</ZEROTERMICO>
<CIELO_SIMBOLO>2</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>variabile</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>16</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE>N moderato</VENTO_DESCRIZIONE>
</zona>
<zona id="4" nome="A3" descrizione="Prealpi_Carniche">
<ATTENDIBILITA um="%">70</ATTENDIBILITA>
<TESTO>
Cielo poco nuvoloso o variabile con temperature basse per la stagione di notte e al mattino; gelate notturne. In quota vento da nord moderato e freddo anche di giorno per la stagione. Zero termico a 1500 m al mattino, 2000 m nel pomeriggio.
</TESTO>
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<QUOTANEVICATA um="m">-</QUOTANEVICATA>
<VENTO2000_DIREZIONE um="ottanti">N</VENTO2000_DIREZIONE>
<VENTO3000_DIREZIONE um="ottanti">N</VENTO3000_DIREZIONE>
<VENTO2000_INTENSITA um="m/s">6</VENTO2000_INTENSITA>
<VENTO3000_INTENSITA um="m/s">13</VENTO3000_INTENSITA>
<TMED1000 um="°C">6</TMED1000>
<TMED2000 um="°C">-1</TMED2000>
<ZEROTERMICO um="m">2200</ZEROTERMICO>
<CIELO_SIMBOLO>1</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>poco nuvoloso</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="5" nome="A4" descrizione="Prealpi_Giulie">
<ATTENDIBILITA um="%">70</ATTENDIBILITA>
<TESTO>
Cielo poco nuvoloso o variabile con temperature basse per la stagione di notte e al mattino; gelate notturne. In quota vento da nord moderato e freddo anche di giorno per la stagione. Zero termico a 1500 m al mattino, 2000 m nel pomeriggio.
</TESTO>
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<QUOTANEVICATA um="m">-</QUOTANEVICATA>
<VENTO2000_DIREZIONE um="ottanti">N</VENTO2000_DIREZIONE>
<VENTO3000_DIREZIONE um="ottanti">N</VENTO3000_DIREZIONE>
<VENTO2000_INTENSITA um="m/s">6</VENTO2000_INTENSITA>
<VENTO3000_INTENSITA um="m/s">16</VENTO3000_INTENSITA>
<TMED1000 um="°C">5</TMED1000>
<TMED2000 um="°C">-2</TMED2000>
<ZEROTERMICO um="m">1800</ZEROTERMICO>
<CIELO_SIMBOLO>1</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>poco nuvoloso</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="6" nome="A5" descrizione="Pordenone">
<ATTENDIBILITA um="%">60</ATTENDIBILITA>
<TESTO/>
<CIELO_SIMBOLO>1</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>poco nuvoloso</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="7" nome="A6" descrizione="Udine">
<ATTENDIBILITA um="%">60</ATTENDIBILITA>
<TESTO/>
<CIELO_SIMBOLO>1</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>poco nuvoloso</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="8" nome="A7" descrizione="Gorizia">
<ATTENDIBILITA um="%">60</ATTENDIBILITA>
<TESTO/>
<CIELO_SIMBOLO>1</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>poco nuvoloso</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="9" nome="A8" descrizione="Lignano">
<ATTENDIBILITA um="%">60</ATTENDIBILITA>
<TESTO/>
<CIELO_SIMBOLO>0</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>sereno</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="10" nome="A9" descrizione="Trieste">
<ATTENDIBILITA um="%">60</ATTENDIBILITA>
<TESTO/>
<CIELO_SIMBOLO>0</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>sereno</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="11" nome="F1" descrizione="Monti">
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<QUOTANEVICATA um="m">-</QUOTANEVICATA>
<TMED1000 um="°C">5</TMED1000>
<TMED2000 um="°C">-2</TMED2000>
<ZEROTERMICO um="m">1700</ZEROTERMICO>
</zona>
<zona id="12" nome="F2" descrizione="Alta_Pianura">
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
</zona>
<zona id="13" nome="F3" descrizione="Bassa_Pianura">
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<TMIN um="°C">1/4</TMIN>
<TMAX um="°C">15/17</TMAX>
</zona>
<zona id="14" nome="F4" descrizione="Costa">
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<TMIN um="°C">6/9</TMIN>
<TMAX um="°C">15/17</TMAX>
</zona>
<zona id="15" nome="Z1" descrizione="Monti">
<ATTENDIBILITA um="%">70</ATTENDIBILITA>
<TESTO>
Cielo poco nuvoloso o variabile con temperature basse per la stagione di notte e al mattino; gelate notturne. In quota vento da nord moderato e freddo anche di giorno per la stagione. Zero termico a 1500 m al mattino, 2000 m nel pomeriggio.
</TESTO>
<EVOLUZIONE00_SIMBOLO>0</EVOLUZIONE00_SIMBOLO>
<EVOLUZIONE00_DESCRIZIONE>sereno</EVOLUZIONE00_DESCRIZIONE>
<EVOLUZIONE12_SIMBOLO>1</EVOLUZIONE12_SIMBOLO>
<EVOLUZIONE12_DESCRIZIONE>variabile</EVOLUZIONE12_DESCRIZIONE>
<EVOLUZIONE24_SIMBOLO>1</EVOLUZIONE24_SIMBOLO>
<EVOLUZIONE24_DESCRIZIONE>variabile</EVOLUZIONE24_DESCRIZIONE>
</zona>
<zona id="16" nome="Z2" descrizione="Alta_Pianura">
<ATTENDIBILITA um="%">70</ATTENDIBILITA>
<TESTO>
Cielo poco nuvoloso con temperature basse per la stagione di notte e al mattino; al livello del suolo valori prossimi allo zero gradi.
</TESTO>
<EVOLUZIONE00_SIMBOLO>0</EVOLUZIONE00_SIMBOLO>
<EVOLUZIONE00_DESCRIZIONE>sereno</EVOLUZIONE00_DESCRIZIONE>
<EVOLUZIONE12_SIMBOLO>1</EVOLUZIONE12_SIMBOLO>
<EVOLUZIONE12_DESCRIZIONE>variabile</EVOLUZIONE12_DESCRIZIONE>
<EVOLUZIONE24_SIMBOLO>1</EVOLUZIONE24_SIMBOLO>
<EVOLUZIONE24_DESCRIZIONE>variabile</EVOLUZIONE24_DESCRIZIONE>
</zona>
<zona id="17" nome="Z3" descrizione="Bassa_Pianura">
<ATTENDIBILITA um="%">70</ATTENDIBILITA>
<TESTO>
Cielo poco nuvoloso con temperature basse per la stagione di notte e al mattino; al livello del suolo valori prossimi allo zero gradi.
</TESTO>
<EVOLUZIONE00_SIMBOLO>0</EVOLUZIONE00_SIMBOLO>
<EVOLUZIONE00_DESCRIZIONE>sereno</EVOLUZIONE00_DESCRIZIONE>
<EVOLUZIONE12_SIMBOLO>0</EVOLUZIONE12_SIMBOLO>
<EVOLUZIONE12_DESCRIZIONE>sereno</EVOLUZIONE12_DESCRIZIONE>
<EVOLUZIONE24_SIMBOLO>1</EVOLUZIONE24_SIMBOLO>
<EVOLUZIONE24_DESCRIZIONE>variabile</EVOLUZIONE24_DESCRIZIONE>
</zona>
<zona id="18" nome="Z4" descrizione="Costa">
<ATTENDIBILITA um="%">70</ATTENDIBILITA>
<TESTO>
Cielo sereno o poco nuvoloso con Borino al mattino, poi brezza.
</TESTO>
<EVOLUZIONE00_SIMBOLO>0</EVOLUZIONE00_SIMBOLO>
<EVOLUZIONE00_DESCRIZIONE>sereno</EVOLUZIONE00_DESCRIZIONE>
<EVOLUZIONE12_SIMBOLO>0</EVOLUZIONE12_SIMBOLO>
<EVOLUZIONE12_DESCRIZIONE>sereno</EVOLUZIONE12_DESCRIZIONE>
<EVOLUZIONE24_SIMBOLO>1</EVOLUZIONE24_SIMBOLO>
<EVOLUZIONE24_DESCRIZIONE>variabile</EVOLUZIONE24_DESCRIZIONE>
</zona>
</zone>
<elenco_localita>
<localita id="1" nome="Gemona">
<TEMPORALIPARTICOLARI>100</TEMPORALIPARTICOLARI>
</localita>
<localita id="2" nome="Carso">
<TEMPORALIPARTICOLARI>100</TEMPORALIPARTICOLARI>
<NEVEPARTICOLARE>100</NEVEPARTICOLARE>
</localita>
<localita id="3" nome="Claut">
<TEMPORALIPARTICOLARI>100</TEMPORALIPARTICOLARI>
<NEVEPARTICOLARE>100</NEVEPARTICOLARE>
<TMIN um="°C">-1</TMIN>
<TMAX um="°C">13</TMAX>
</localita>
<localita id="4" nome="Cividale">
<TEMPORALIPARTICOLARI>100</TEMPORALIPARTICOLARI>
</localita>
<localita id="5" nome="Sappada">
<NEVEPARTICOLARE>100</NEVEPARTICOLARE>
</localita>
<localita id="6" nome="Piancavallo">
<NEVEPARTICOLARE>100</NEVEPARTICOLARE>
<TMIN um="°C">-2</TMIN>
<TMAX um="°C">6</TMAX>
</localita>
<localita id="7" nome="Tarvisio">
<TMIN um="°C">-3</TMIN>
<TMAX um="°C">11</TMAX>
</localita>
<localita id="8" nome="Lussari">
<TMIN um="°C">-4</TMIN>
<TMAX um="°C">2</TMAX>
</localita>
<localita id="9" nome="Zoncolan">
<TMIN um="°C">-3</TMIN>
<TMAX um="°C">5</TMAX>
</localita>
<localita id="10" nome="Sella_Nevea">
<TMIN um="°C">-2</TMIN>
<TMAX um="°C">6</TMAX>
</localita>
<localita id="11" nome="Canin-Gilberti">
<TMIN um="°C">-5</TMIN>
<TMAX um="°C">2</TMAX>
</localita>
<localita id="12" nome="Forni_Avoltri">
<TMIN um="°C">-3</TMIN>
<TMAX um="°C">12</TMAX>
</localita>
</elenco_localita>
<VENTO3000_DIREZIONE um="ottanti">N</VENTO3000_DIREZIONE>
<VENTO3000_INTENSITA um="m/s">17</VENTO3000_INTENSITA>
<VENTOALLARGO_DIREZIONE_MATTINA um="ottanti">ENE</VENTOALLARGO_DIREZIONE_MATTINA>
<VENTOALLARGO_INTENSITA_MATTINA um="kt">10</VENTOALLARGO_INTENSITA_MATTINA>
<VENTOALLARGO_DIREZIONE_POMERIGGIO um="ottanti">W</VENTOALLARGO_DIREZIONE_POMERIGGIO>
<VENTOALLARGO_INTENSITA_POMERIGGIO um="kt">5</VENTOALLARGO_INTENSITA_POMERIGGIO>
<BREZZA>35</BREZZA>
</scadenza>
<scadenza id="2" data_validita="15-10-2021" giorno="DOPODOMANI">
<zone>
<zona id="1" nome="REGIONE" descrizione="Regione">
<ATTENDIBILITA um="%">90</ATTENDIBILITA>
<TESTO>
Cielo sereno; temperature minime ancora relativamente basse per la stagione, mentre ad alta quota vi sar&agrave; un deciso aumento con zero termico a 3000 m. Venti di brezza o Borino sulla costa.
</TESTO>
<EVOLUZIONE00_SIMBOLO>0</EVOLUZIONE00_SIMBOLO>
<EVOLUZIONE00_DESCRIZIONE>sereno</EVOLUZIONE00_DESCRIZIONE>
<EVOLUZIONE12_SIMBOLO>0</EVOLUZIONE12_SIMBOLO>
<EVOLUZIONE12_DESCRIZIONE>sereno</EVOLUZIONE12_DESCRIZIONE>
<EVOLUZIONE24_SIMBOLO>0</EVOLUZIONE24_SIMBOLO>
<EVOLUZIONE24_DESCRIZIONE>sereno</EVOLUZIONE24_DESCRIZIONE>
</zona>
<zona id="2" nome="A1" descrizione="Alpi_Carniche">
<ATTENDIBILITA um="%">90</ATTENDIBILITA>
<TESTO>
Cielo sereno; temperature minime ancora relativamente basse per la stagione nelle valli, mentre ad alta quota vi sar&agrave; un deciso aumento con zero termico a 3000 m.
</TESTO>
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<QUOTANEVICATA um="m">-</QUOTANEVICATA>
<VENTO2000_DIREZIONE um="ottanti">NE</VENTO2000_DIREZIONE>
<VENTO3000_DIREZIONE um="ottanti">N</VENTO3000_DIREZIONE>
<VENTO2000_INTENSITA um="m/s">3</VENTO2000_INTENSITA>
<VENTO3000_INTENSITA um="m/s">6</VENTO3000_INTENSITA>
<TMED1000 um="°C">7</TMED1000>
<TMED2000 um="°C">2</TMED2000>
<ZEROTERMICO um="m">3000</ZEROTERMICO>
<CIELO_SIMBOLO>0</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>sereno</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="3" nome="A2" descrizione="Alpi_Giulie">
<ATTENDIBILITA um="%">90</ATTENDIBILITA>
<TESTO>
Cielo sereno; temperature minime ancora relativamente basse per la stagione nelle valli, mentre ad alta quota vi sar&agrave; un deciso aumento con zero termico a 3000 m.
</TESTO>
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<QUOTANEVICATA um="m">-</QUOTANEVICATA>
<VENTO2000_DIREZIONE um="ottanti">NE</VENTO2000_DIREZIONE>
<VENTO3000_DIREZIONE um="ottanti">N</VENTO3000_DIREZIONE>
<VENTO2000_INTENSITA um="m/s">6</VENTO2000_INTENSITA>
<VENTO3000_INTENSITA um="m/s">6</VENTO3000_INTENSITA>
<TMED1000 um="°C">7</TMED1000>
<TMED2000 um="°C">2</TMED2000>
<ZEROTERMICO um="m">3000</ZEROTERMICO>
<CIELO_SIMBOLO>0</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>sereno</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="4" nome="A3" descrizione="Prealpi_Carniche">
<ATTENDIBILITA um="%">90</ATTENDIBILITA>
<TESTO>
Cielo sereno; temperature minime ancora relativamente basse per la stagione nelle valli, mentre ad alta quota vi sar&agrave; un deciso aumento con zero termico a 3000 m.
</TESTO>
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<QUOTANEVICATA um="m">-</QUOTANEVICATA>
<VENTO2000_DIREZIONE um="ottanti">NE</VENTO2000_DIREZIONE>
<VENTO3000_DIREZIONE um="ottanti">N</VENTO3000_DIREZIONE>
<VENTO2000_INTENSITA um="m/s">3</VENTO2000_INTENSITA>
<VENTO3000_INTENSITA um="m/s">6</VENTO3000_INTENSITA>
<TMED1000 um="°C">9</TMED1000>
<TMED2000 um="°C">3</TMED2000>
<ZEROTERMICO um="m">3200</ZEROTERMICO>
<CIELO_SIMBOLO>0</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>sereno</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="5" nome="A4" descrizione="Prealpi_Giulie">
<ATTENDIBILITA um="%">90</ATTENDIBILITA>
<TESTO>
Cielo sereno; temperature minime ancora relativamente basse per la stagione nelle valli, mentre ad alta quota vi sar&agrave; un deciso aumento con zero termico a 3000 m.
</TESTO>
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<QUOTANEVICATA um="m">-</QUOTANEVICATA>
<VENTO2000_DIREZIONE um="ottanti">NE</VENTO2000_DIREZIONE>
<VENTO3000_DIREZIONE um="ottanti">N</VENTO3000_DIREZIONE>
<VENTO2000_INTENSITA um="m/s">6</VENTO2000_INTENSITA>
<VENTO3000_INTENSITA um="m/s">6</VENTO3000_INTENSITA>
<TMED1000 um="°C">7</TMED1000>
<TMED2000 um="°C">2</TMED2000>
<ZEROTERMICO um="m">3000</ZEROTERMICO>
<CIELO_SIMBOLO>0</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>sereno</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="6" nome="A5" descrizione="Pordenone">
<ATTENDIBILITA um="%">60</ATTENDIBILITA>
<TESTO/>
<CIELO_SIMBOLO>0</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>sereno</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="7" nome="A6" descrizione="Udine">
<ATTENDIBILITA um="%">60</ATTENDIBILITA>
<TESTO/>
<CIELO_SIMBOLO>0</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>sereno</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="8" nome="A7" descrizione="Gorizia">
<ATTENDIBILITA um="%">60</ATTENDIBILITA>
<TESTO/>
<CIELO_SIMBOLO>0</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>sereno</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="9" nome="A8" descrizione="Lignano">
<ATTENDIBILITA um="%">60</ATTENDIBILITA>
<TESTO/>
<CIELO_SIMBOLO>0</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>sereno</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="10" nome="A9" descrizione="Trieste">
<ATTENDIBILITA um="%">60</ATTENDIBILITA>
<TESTO/>
<CIELO_SIMBOLO>0</CIELO_SIMBOLO>
<CIELO_DESCRIZIONE>sereno</CIELO_DESCRIZIONE>
<PIOGGIA_SIMBOLO>100</PIOGGIA_SIMBOLO>
<PIOGGIA_DESCRIZIONE/>
<NEVE_SIMBOLO>100</NEVE_SIMBOLO>
<NEVE_DESCRIZIONE/>
<TEMPORALE_SIMBOLO>100</TEMPORALE_SIMBOLO>
<TEMPORALE_DESCRIZIONE/>
<NEBBIA_SIMBOLO>100</NEBBIA_SIMBOLO>
<NEBBIA_DESCRIZIONE/>
<VENTO_SIMBOLO>100</VENTO_SIMBOLO>
<VENTO_DESCRIZIONE/>
</zona>
<zona id="11" nome="F1" descrizione="Monti">
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<QUOTANEVICATA um="m">-</QUOTANEVICATA>
<TMED1000 um="°C">7</TMED1000>
<TMED2000 um="°C">2</TMED2000>
<ZEROTERMICO um="m">3000</ZEROTERMICO>
</zona>
<zona id="12" nome="F2" descrizione="Alta_Pianura">
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
</zona>
<zona id="13" nome="F3" descrizione="Bassa_Pianura">
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<TMIN um="°C">2/5</TMIN>
<TMAX um="°C">16/19</TMAX>
</zona>
<zona id="14" nome="F4" descrizione="Costa">
<PROBABILITAPRECIPITAZIONI um="%">&lt;10</PROBABILITAPRECIPITAZIONI>
<PROBABILITATEMPORALI um="%">&lt;10</PROBABILITATEMPORALI>
<TMIN um="°C">7/10</TMIN>
<TMAX um="°C">16/19</TMAX>
</zona>
<zona id="15" nome="Z1" descrizione="Monti">
<ATTENDIBILITA um="%">90</ATTENDIBILITA>
<TESTO>
Cielo sereno; temperature minime ancora relativamente basse per la stagione nelle valli, mentre ad alta quota vi sar&agrave; un deciso aumento con zero termico a 3000 m.
</TESTO>
<EVOLUZIONE00_SIMBOLO>0</EVOLUZIONE00_SIMBOLO>
<EVOLUZIONE00_DESCRIZIONE>sereno</EVOLUZIONE00_DESCRIZIONE>
<EVOLUZIONE12_SIMBOLO>0</EVOLUZIONE12_SIMBOLO>
<EVOLUZIONE12_DESCRIZIONE>sereno</EVOLUZIONE12_DESCRIZIONE>
<EVOLUZIONE24_SIMBOLO>0</EVOLUZIONE24_SIMBOLO>
<EVOLUZIONE24_DESCRIZIONE>sereno</EVOLUZIONE24_DESCRIZIONE>
</zona>
<zona id="16" nome="Z2" descrizione="Alta_Pianura">
<ATTENDIBILITA um="%">90</ATTENDIBILITA>
<TESTO>
Cielo sereno; temperature minime ancora relativamente basse per la stagione.
</TESTO>
<EVOLUZIONE00_SIMBOLO>0</EVOLUZIONE00_SIMBOLO>
<EVOLUZIONE00_DESCRIZIONE>sereno</EVOLUZIONE00_DESCRIZIONE>
<EVOLUZIONE12_SIMBOLO>0</EVOLUZIONE12_SIMBOLO>
<EVOLUZIONE12_DESCRIZIONE>sereno</EVOLUZIONE12_DESCRIZIONE>
<EVOLUZIONE24_SIMBOLO>0</EVOLUZIONE24_SIMBOLO>
<EVOLUZIONE24_DESCRIZIONE>sereno</EVOLUZIONE24_DESCRIZIONE>
</zona>
<zona id="17" nome="Z3" descrizione="Bassa_Pianura">
<ATTENDIBILITA um="%">90</ATTENDIBILITA>
<TESTO>
Cielo sereno; temperature minime ancora relativamente basse per la stagione.
</TESTO>
<EVOLUZIONE00_SIMBOLO>0</EVOLUZIONE00_SIMBOLO>
<EVOLUZIONE00_DESCRIZIONE>sereno</EVOLUZIONE00_DESCRIZIONE>
<EVOLUZIONE12_SIMBOLO>0</EVOLUZIONE12_SIMBOLO>
<EVOLUZIONE12_DESCRIZIONE>sereno</EVOLUZIONE12_DESCRIZIONE>
<EVOLUZIONE24_SIMBOLO>0</EVOLUZIONE24_SIMBOLO>
<EVOLUZIONE24_DESCRIZIONE>sereno</EVOLUZIONE24_DESCRIZIONE>
</zona>
<zona id="18" nome="Z4" descrizione="Costa">
<ATTENDIBILITA um="%">90</ATTENDIBILITA>
<TESTO>
Cielo sereno; temperature minime ancora relativamente basse per la stagione. Venti di brezza o Borino sulla costa.
</TESTO>
<EVOLUZIONE00_SIMBOLO>0</EVOLUZIONE00_SIMBOLO>
<EVOLUZIONE00_DESCRIZIONE>sereno</EVOLUZIONE00_DESCRIZIONE>
<EVOLUZIONE12_SIMBOLO>0</EVOLUZIONE12_SIMBOLO>
<EVOLUZIONE12_DESCRIZIONE>sereno</EVOLUZIONE12_DESCRIZIONE>
<EVOLUZIONE24_SIMBOLO>0</EVOLUZIONE24_SIMBOLO>
<EVOLUZIONE24_DESCRIZIONE>sereno</EVOLUZIONE24_DESCRIZIONE>
</zona>
</zone>
<elenco_localita>
<localita id="1" nome="Gemona">
<TEMPORALIPARTICOLARI>100</TEMPORALIPARTICOLARI>
</localita>
<localita id="2" nome="Carso">
<TEMPORALIPARTICOLARI>100</TEMPORALIPARTICOLARI>
<NEVEPARTICOLARE>100</NEVEPARTICOLARE>
</localita>
<localita id="3" nome="Claut">
<TEMPORALIPARTICOLARI>100</TEMPORALIPARTICOLARI>
<NEVEPARTICOLARE>100</NEVEPARTICOLARE>
<TMIN um="°C">0</TMIN>
<TMAX um="°C">15</TMAX>
</localita>
<localita id="4" nome="Cividale">
<TEMPORALIPARTICOLARI>100</TEMPORALIPARTICOLARI>
</localita>
<localita id="5" nome="Sappada">
<NEVEPARTICOLARE>100</NEVEPARTICOLARE>
</localita>
<localita id="6" nome="Piancavallo">
<NEVEPARTICOLARE>100</NEVEPARTICOLARE>
<TMIN um="°C">0</TMIN>
<TMAX um="°C">9</TMAX>
</localita>
<localita id="7" nome="Tarvisio">
<TMIN um="°C">0</TMIN>
<TMAX um="°C">13</TMAX>
</localita>
<localita id="8" nome="Lussari">
<TMIN um="°C">0</TMIN>
<TMAX um="°C">5</TMAX>
</localita>
<localita id="9" nome="Zoncolan">
<TMIN um="°C">1</TMIN>
<TMAX um="°C">6</TMAX>
</localita>
<localita id="10" nome="Sella_Nevea">
<TMIN um="°C">0</TMIN>
<TMAX um="°C">9</TMAX>
</localita>
<localita id="11" nome="Canin-Gilberti">
<TMIN um="°C">-1</TMIN>
<TMAX um="°C">5</TMAX>
</localita>
<localita id="12" nome="Forni_Avoltri">
<TMIN um="°C">-2</TMIN>
<TMAX um="°C">15</TMAX>
</localita>
</elenco_localita>
<VENTO3000_DIREZIONE um="ottanti">N</VENTO3000_DIREZIONE>
<VENTO3000_INTENSITA um="m/s">10</VENTO3000_INTENSITA>
<VENTOALLARGO_DIREZIONE_MATTINA um="ottanti">ENE</VENTOALLARGO_DIREZIONE_MATTINA>
<VENTOALLARGO_INTENSITA_MATTINA um="kt">10</VENTOALLARGO_INTENSITA_MATTINA>
<VENTOALLARGO_DIREZIONE_POMERIGGIO um="ottanti">Var.</VENTOALLARGO_DIREZIONE_POMERIGGIO>
<VENTOALLARGO_INTENSITA_POMERIGGIO um="kt">5</VENTOALLARGO_INTENSITA_POMERIGGIO>
<BREZZA>35</BREZZA>
</scadenza>
</scadenze>
<TENDENZA_TESTO>
Sabato cielo da poco nuvoloso a variabile; domenica cielo sereno o poco nuvoloso. Sulla costa soffier&agrave; in genere Bora moderata. Temperature in aumento.
</TENDENZA_TESTO>
</previsioni>
<osservazioni data="12-10-2021">
<stazioni>
<stazione id="1" nome="TRIESTE">
<TMIN um="°C">12.2</TMIN>
<TMAX um="°C">17.7</TMAX>
<RR um="mm">0.0</RR>
</stazione>
<stazione id="2" nome="GRADO">
<TMIN um="°C">n.d.</TMIN>
<TMAX um="°C">n.d.</TMAX>
<RR um="mm">n.d.</RR>
</stazione>
<stazione id="3" nome="LIGNANO">
<TMIN um="°C">10.9</TMIN>
<TMAX um="°C">18.1</TMAX>
<RR um="mm">n.d.</RR>
</stazione>
<stazione id="4" nome="PORDENONE">
<TMIN um="°C">6.3</TMIN>
<TMAX um="°C">16.3</TMAX>
<RR um="mm">0.0</RR>
</stazione>
<stazione id="5" nome="UDINE">
<TMIN um="°C">4.9</TMIN>
<TMAX um="°C">16.9</TMAX>
<RR um="mm">0.0</RR>
</stazione>
<stazione id="6" nome="GORIZIA">
<TMIN um="°C">6.6</TMIN>
<TMAX um="°C">16.3</TMAX>
<RR um="mm">0.0</RR>
</stazione>
<stazione id="7" nome="CIVIDALE">
<TMIN um="°C">8.0</TMIN>
<TMAX um="°C">16.8</TMAX>
<RR um="mm">0.0</RR>
</stazione>
<stazione id="8" nome="GEMONA">
<TMIN um="°C">5.9</TMIN>
<TMAX um="°C">16.6</TMAX>
<RR um="mm">0.0</RR>
</stazione>
<stazione id="9" nome="TOLMEZZO">
<TMIN um="°C">6.0</TMIN>
<TMAX um="°C">15.2</TMAX>
<RR um="mm">0.0</RR>
</stazione>
<stazione id="10" nome="TARVISIO">
<TMIN um="°C">-0.8</TMIN>
<TMAX um="°C">10.7</TMAX>
<RR um="mm">0.0</RR>
</stazione>
<stazione id="11" nome="FORNI DI SOPRA">
<TMIN um="°C">2.4</TMIN>
<TMAX um="°C">12.3</TMAX>
<RR um="mm">0.0</RR>
</stazione>
<stazione id="12" nome="ZONCOLAN">
<TMIN um="°C">0.2</TMIN>
<TMAX um="°C">6.3</TMAX>
<RR um="mm">n.d.</RR>
</stazione>
<stazione id="13" nome="PIANCAVALLO">
<TMIN um="°C">0.5</TMIN>
<TMAX um="°C">8.5</TMAX>
<RR um="mm">0.8</RR>
</stazione>
</stazioni>
</osservazioni>
</data>
<!--

AREE: 
A1 Alpi Carniche
A2 Alpi Giulie
A3 Prealpi Carniche
A4 Prealpi Giulie
A5 Pordenone
A6 Udine
A7 Gorizia
A8 Lignano
A9 Trieste

ZONE/FASCE:
Z1 F1 Monti
Z2 F2 Alta Pianura
Z3 F3 Bassa Pianura
Z4 F4 Costa

CIELO:
  0 sereno
  1 poco nuvoloso
  2 variabile
  3 nuvoloso
  4 coperto
  5 sole/nebbia

PIOGGIA:
100 none
  6 debole
  7 moderata
  8 abbondante
  9 intensa
 36 molto intensa

NEVE:
100 none
 10 moderata
 11 abbondante
 12 intensa

TEMPORALE:
100 none
 13 temporale

NEBBIA:
100 none
 14 nebbia
 15 foschia

VENTO:
100 none
 16 N   moderato
 17 NE  moderato
 18 ENE moderato
 19 E   moderato
 20 SE  moderato
 21 S   moderato
 22 SW  moderato
 23 W   moderato
 24 NW  moderato
 25 N   forte
 26 NE  forte
 27 ENE forte
 28 E   forte
 29 SE  forte
 30 S   forte
 31 SW  forte
 32 W   forte
 33 NW  forte
 34 ENE molto forte
 35 brezza

EVOLUZIONI (simboli):
  0 sereno
  1 variabile
  2 coperto
  3 variabile con piogge moderate
  4 variabile con piogge abbondanti
  5 variabile con piogge abbondanti e temporali
  6 variabile con temporali
  7 variabile con piogge moderate e nevicate
  8 variabile con nevicate
  9 coperto con piogge moderate
 10 coperto con piogge abbondanti
 11 coperto con piogge intense
 12 coperto con piogge abbondanti e temporali
 13 coperto con temporali
 14 coperto con piogge abbondanti e nevicate
 15 coperto con nevicate
-->    
    """


from home.scheduler.trigger.crawler.osmer_fvg import will_rain
