from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import dateparser, time

DEFAULT_INTERVAL = 30  # One minute
DEFAULT_BREAK_ROOM = 'break room'
DEFAULT_LOCAL    = 'en_US'


class CoffeeBreak(BotPlugin):
    """
    Used to schedule and notify team members of coffee breaks
    """

    def activate(self):
        """
        Triggers on plugin activation

        You should delete it if you're not using it to override any default behaviour
        """
        super(CoffeeBreak, self).activate()
        # interval = {True: self.config['INTERVAL'], False: DEFAULT_INTERVAL}[self.config]
        # self.start_poller(interval, self.coffeebreak)

    def deactivate(self):
        """
        Triggers on plugin deactivation
        You should delete it if you're not using it to override any default behaviour
        """
        super(CoffeeBreak, self).deactivate()

    def get_configuration_template(self):
        """
        Defines the configuration structure this plugin supports
        You should delete it if your plugin doesn't use any configuration like this
        """
        return {'BREAK_ROOM': DEFAULT_BREAK_ROOM,
                'TEAM_MEMBERS': None,
                'INTERVAL': DEFAULT_INTERVAL
                }

    def check_configuration(self, configuration):
        """
        Triggers when the configuration is checked, shortly before activation

        Raise a errbot.ValidationException in case of an error

        You should delete it if you're not using it to override any default behaviour
        """
        super(CoffeeBreak, self).check_configuration(configuration)


    @webhook
    def example_webhook(self, incoming_request):
        """A webhook which simply returns 'Example'"""
        return "Example"

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd
    def coffeebreak(self, message, args):
        return "Time for a coffeebreak!"
        self.start_coffeebreak()
        self.start_timer()

    def start_coffeebreak(self):
        message = "It's time for a coffeebreak! {break_room}".format(break_room=self.config["BREAK_ROOM"])
        #message = "It's time for a coffeebreak! {break_room}".format(break_room='break room')
        yield message
        #self.start_timer()

    def start_timer(self):
        stop_time = dateparser.parse("in {interval} minutes".format(interval=self.config["INTERVAL"]))
        print("Stop time is {stop}".format(time=stop_time))
        yield "Stop time is {stop}".format(time=stop_time)

