# from cli.process import Process
# from datetime import datetime, timedelta
#
#
# class Recurrent(Process):
#     """Command that allows itself to be runnable. TODO:Maybe split into Runnable class with Plant?"""
#
#     def __init__(self, key: str, description: str, last_run, inc: int) -> None:  # duh
#         self.last_run = last_run
#         self.inc: int = inc
#         Process.__init__(self, key=key, description=description)
#
#     def ready(self, curr_time) -> bool:
#         """Is this command ready to process?"""
#         return (
#             datetime.strptime(self.last_run, "%m-%d-%Y") + timedelta(days=self.inc)
#             >= curr_time
#         )
#
#     def process(self) -> None:
#         super().process()
#         self.last_run: str = datetime.now().strftime("%m-%d-%Y")
