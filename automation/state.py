import threading

class BotState:
    def __init__(self):
        self.running = False
        self.thread = None

bot_state = BotState()
