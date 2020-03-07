pytest_plugins = ['errbot.backends.test']

extra_plugin_dir = '.'

def test_command(testbot):
    testbot.push_message('!coffeebreak')
    assert 'Time for a coffeebreak!' in testbot.pop_message()
