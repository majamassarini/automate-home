import datetime

from typing import List
from home import event

from home.scheduler.trigger.crawler.osmer_fvg import Osmer


class Trigger(Osmer):

    EVENT = event.rain.forecast.Event.On

    def __init__(
        self,
        name: str,
        events: List["home.Event"],
        url,
        zone: int = 4,
        probability: int = 60,
    ):
        """
        Check if rain is in the forecast.
        A trigger scheduled every day at 2pm since the forecast is emitted in the afternoon.

        :param name: the trigger name
        :param events: the events carried on by this trigger
        :param zone: 1 Regione, 2 Alpi Carniche, 3 Alpi Giulie
        4 Prealpi Carniche, 5 Prealpi Giulie, 6 Pordenone
        7 Udine, 8 Gorizia, 9 Lignano, 10 Trieste, 11 Monti,
        12 Alta Pianura, 13 Bassa Pianura, 14 Costa
        :param probability: the forecast probability
        """
        all_events = events.copy()
        all_events.append(self.EVENT)
        super(Trigger, self).__init__(name, all_events, url, hour=14)
        self._probability = probability
        self._zone = zone

    def _today(self):
        return datetime.datetime.now(self._timezone)

    def is_triggered(self):
        """
        >>> import home
        >>> import unittest.mock
        >>> from xml.etree import ElementTree
        >>> crawler = home.scheduler.trigger.crawler.osmer_fvg.will_rain.on.Trigger("forecast",
        ...                                                            [],
        ...                                                            "https://dev.meteo.fvg.it/xml/previsioni/")
        >>> xml = crawler.unescape(crawler.EXAMPLE)
        >>> crawler.open = lambda url: ElementTree.fromstring(xml)
        >>> crawler.is_triggered()
        False
        """
        today = self._today()
        root = self.open(
            f"{self._base_url}PW{today.year}{today.month:02}{today.day:02}.xml"
        )
        will_rain_probability = 0
        if root:
            will_rain = root.findtext(
                "previsioni/scadenze/scadenza[@id='1']/zone/zona[@id='{}']/PROBABILITAPRECIPITAZIONI".format(
                    self._zone
                )
            )
            if will_rain:
                try:
                    will_rain_probability = int(will_rain)
                except ValueError:
                    will_rain_probability = int(
                        will_rain.replace("&gt;", "").replace("&lt;", "")
                    )

        if will_rain_probability > self._probability:
            return True
        else:
            return False
