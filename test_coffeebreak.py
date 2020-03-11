import coffeebreak

pytest_plugins = ['errbot.backends.test']

extra_plugin_dir = '.'

def test_command(testbot):
    testbot.push_message('!coffeebreak')
    expected = 'Time for a coffeebreak!'
    result = testbot.pop_message()
    assert expected in result

def test_start_coffeebreak(testbot):
    plugin = testbot._bot.plugin_manager.get_plugin_obj_by_name('CoffeeBreak')
    expected = "It's time for a coffeebreak! break room"
    result = plugin.start_coffeebreak()
    assert expected in result
