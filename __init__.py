import plugins

def _initialise(bot):
    plugins.register_handler(_on_message, type="allmessages", priority=2)
    
def _on_message(bot, event, command):
    print("miep")
