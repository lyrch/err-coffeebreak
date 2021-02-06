import coffeebreak

pytest_plugins = ['errbot.backends.test']

extra_plugin_dir = '.'

def setup_class(self):
    config_message = """
        {'BREAK_ROOM': 'break room',
         'TEAM_MEMBERS': 'jwilkers',
         'INTERVAL': '1 day'}
        """
    testbot.push_message("{config_command}".format(config_command=config_message))
    #testbot._bot.plugin_manager.set_plugin_configuration(testbot, 

def test_command(testbot):
    testbot.push_message('!coffeebreak')
    expected = 'Time for a coffeebreak!'
    result = testbot.pop_message()
    assert expected in result

def test_start_coffeebreak(testbot):
    config_message = """ !plugin config CoffeeBreak \
        {'BREAK_ROOM': 'break room', \
         'TEAM_MEMBERS': 'jwilkers', \
         'INTERVAL': '1 day'}
        """
    testbot.push_message("{config_command}".format(config_command=config_message))
    plugin = testbot._bot.plugin_manager.get_plugin_obj_by_name('CoffeeBreak')
    expected = "It's time for a coffeebreak! break room"
    result = plugin.start_coffeebreak()
    assert expected in result
