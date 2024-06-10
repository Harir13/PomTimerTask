import time

class PomodoroTimer:
    def __init__(self, work_minutes=25, break_minutes=5):
        self.work_minutes = work_minutes
        self.break_minutes = break_minutes

    def run(self):
        print("Pomodoro timer started. Work for {} minutes.".format(self.work_minutes))
        self._countdown(self.work_minutes * 60)
        print("Time's up! Take a {} minute break.".format(self.break_minutes))
        self._countdown(self.break_minutes * 60)
        print("Break time's over. Back to work!")

    def _countdown(self, seconds):
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')
            time.sleep(1)
            seconds -= 1
        print(' ' * len(timer), end='\r')

if __name__ == "__main__":
    pomodoro = PomodoroTimer()
    pomodoro.run()
