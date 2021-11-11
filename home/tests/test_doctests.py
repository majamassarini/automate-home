# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import doctest
import home


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(home.configs))
    tests.addTests(doctest.DocTestSuite(home.options))

    tests.addTests(doctest.DocTestSuite(home.appliance.socket.energy_guard))
    tests.addTests(doctest.DocTestSuite(home.appliance.socket.presence))
    tests.addTests(doctest.DocTestSuite(home.appliance.socket.presence.christmas))
    tests.addTests(doctest.DocTestSuite(home.appliance.light))
    tests.addTests(doctest.DocTestSuite(home.appliance.light.event.brightness))
    tests.addTests(doctest.DocTestSuite(home.appliance.light.event.saturation))
    tests.addTests(doctest.DocTestSuite(home.appliance.light.event.temperature))
    tests.addTests(
        doctest.DocTestSuite(home.appliance.light.event.circadian_rhythm.hue)
    )
    tests.addTests(
        doctest.DocTestSuite(home.appliance.light.event.circadian_rhythm.brightness)
    )
    tests.addTests(
        doctest.DocTestSuite(home.appliance.light.event.circadian_rhythm.saturation)
    )
    tests.addTests(
        doctest.DocTestSuite(home.appliance.light.event.circadian_rhythm.temperature)
    )
    tests.addTests(
        doctest.DocTestSuite(home.appliance.light.event.lux_balancing.brightness)
    )
    tests.addTests(
        doctest.DocTestSuite(home.appliance.light.event.show.starting_brightness)
    )
    tests.addTests(
        doctest.DocTestSuite(home.appliance.light.event.show.ending_brightness)
    )
    tests.addTests(doctest.DocTestSuite(home.appliance.light.presence))
    tests.addTests(doctest.DocTestSuite(home.appliance.light.presence.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.light.zone))
    tests.addTests(doctest.DocTestSuite(home.appliance.light.zone.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.light.indoor.dimmerable))
    tests.addTests(doctest.DocTestSuite(home.appliance.light.indoor.dimmerable.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.light.indoor.hue))
    tests.addTests(doctest.DocTestSuite(home.appliance.light.indoor.hue.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.curtain.indoor.blackout))
    tests.addTests(doctest.DocTestSuite(home.appliance.curtain.indoor.blackout.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.curtain.outdoor))
    tests.addTests(doctest.DocTestSuite(home.appliance.curtain.outdoor.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.curtain.outdoor.bedroom))
    tests.addTests(doctest.DocTestSuite(home.appliance.curtain.outdoor.bedroom.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.sound.player))
    tests.addTests(doctest.DocTestSuite(home.appliance.sound.player.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.thermostat.presence))
    tests.addTests(
        doctest.DocTestSuite(home.appliance.thermostat.presence.event.setpoint)
    )
    tests.addTests(
        doctest.DocTestSuite(home.appliance.thermostat.presence.event.keep.setpoint)
    )
    tests.addTests(doctest.DocTestSuite(home.appliance.thermostat.presence.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.alarm))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.alarm.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.anemometer))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.anemometer.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.crepuscular))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.crepuscular.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.luxmeter))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.luxmeter.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.motion))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.motion.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.powermeter))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.powermeter.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.rainmeter))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.rainmeter.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.scene))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.scene.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.thermometer))
    tests.addTests(doctest.DocTestSuite(home.appliance.sensor.thermometer.state))
    tests.addTests(doctest.DocTestSuite(home.appliance.sprinkler))
    tests.addTests(doctest.DocTestSuite(home.appliance.sprinkler.state))
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.circadian_rhythm))
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.sun.sunhit))
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.sun.sunleft))
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.sun.sunset))
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.sun.sunrise))
    tests.addTests(
        doctest.DocTestSuite(home.scheduler.trigger.sun.twilight.civil.sunrise)
    )
    tests.addTests(
        doctest.DocTestSuite(home.scheduler.trigger.sun.twilight.civil.sunset)
    )
    tests.addTests(
        doctest.DocTestSuite(home.scheduler.trigger.sun.twilight.astronomical.sunrise)
    )
    tests.addTests(
        doctest.DocTestSuite(home.scheduler.trigger.sun.twilight.astronomical.sunset)
    )
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.state.delay))
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.state.entering.delay))
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.protocol))
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.protocol.delay))
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.protocol.enum))
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.protocol.mean))
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.protocol.multi))
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.protocol.timer))
    tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.crawler.osmer_fvg))
    tests.addTests(
        doctest.DocTestSuite(home.scheduler.trigger.crawler.osmer_fvg.will_rain.on)
    )
    tests.addTests(
        doctest.DocTestSuite(home.scheduler.trigger.crawler.osmer_fvg.will_rain.off)
    )

    tests.addTests(doctest.DocTestSuite(home.builder.scheduler.trigger.cron))
    tests.addTests(
        doctest.DocTestSuite(home.builder.scheduler.trigger.circadian_rhythm)
    )
    tests.addTests(
        doctest.DocTestSuite(home.builder.scheduler.trigger.circadian_rhythm)
    )
    tests.addTests(
        doctest.DocTestSuite(home.builder.scheduler.trigger.state.entering.delay)
    )
    tests.addTests(
        doctest.DocTestSuite(
            home.builder.scheduler.trigger.state.entering.delay.duration
        )
    )
    tests.addTests(
        doctest.DocTestSuite(home.builder.scheduler.trigger.state.exiting.delay)
    )
    tests.addTests(doctest.DocTestSuite(home.builder.scheduler.trigger.protocol.delay))
    tests.addTests(doctest.DocTestSuite(home.builder.scheduler.trigger.protocol.enum))
    tests.addTests(doctest.DocTestSuite(home.builder.scheduler.trigger.protocol.multi))
    tests.addTests(doctest.DocTestSuite(home.builder.scheduler.trigger.sun.sunhit))
    tests.addTests(
        doctest.DocTestSuite(
            home.builder.scheduler.trigger.crawler.osmer_fvg.will_rain.off
        )
    )

    # tests.addTests(doctest.DocTestSuite(home.redis.gateway.client.pubsub))
    # tests.addTests(doctest.DocTestSuite(home.redis.gateway.client.storage))

    # tests.addTests(doctest.DocTestSuite(home.scheduler.trigger.date.resettable))

    return tests
