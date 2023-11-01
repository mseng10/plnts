class Auto_Command(Command):
    def __int__(self, time, inc):
        super().__init__("create")
        self.time = time
        self.next_time = time + inc

    def ready(self, curr_time):
        return self.time >= curr_time
