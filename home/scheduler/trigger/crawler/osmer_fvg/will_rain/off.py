from home import event
from home.scheduler.trigger.crawler.osmer_fvg.will_rain.on import Trigger as Parent


class Trigger(Parent):

    EVENT = event.rain.forecast.Event.Off

    def is_triggered(self):
        """
        >>> import home
        >>> import unittest.mock
        >>> from xml.etree import ElementTree
        >>> crawler = home.scheduler.trigger.crawler.osmer_fvg.will_rain.off.Trigger("forecast",
        ...                                                            [],
        ...                                                            "https://dev.meteo.fvg.it/xml/previsioni/")
        >>> xml = crawler.unescape(crawler.EXAMPLE)
        >>> crawler.open = lambda url: ElementTree.fromstring(xml)
        >>> crawler.is_triggered()
        True
        """
        return not super(Trigger, self).is_triggered()
