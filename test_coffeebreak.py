import coffeebreak
import logging
from errbot.backends.test import FullStackTest
# pytest_plugins = ['errbot.backends.test']


class TestCoffeeBreak(FullStackTest):
    extra_plugin_dir = '.'

    def setUp(self):
        plugin_config =  { 'BREAK_ROOM': 'break room',
                           'TEAM_MEMBERS': 'jwilkers',
                           'INTERVAL': '1 day'
                         }

        super().setUp(extra_plugin_dir='.',
                    loglevel=logging.ERROR,
                    extra_config=plugin_config)

    def test_command(self):
        self.push_message('!coffeebreak')
        expected = 'Time for a coffeebreak!'
        result = self.pop_message()
        assert expected in result

    def test_start_coffeebreak(self):
        plugin = self._bot.plugin_manager.get_plugin_obj_by_name('CoffeeBreak')
        expected = "It's time for a coffeebreak! break room"
        result = plugin.start_coffeebreak()
        assert expected in result
