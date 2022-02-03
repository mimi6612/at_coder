from time import perf_counter


class Timer:
    """class Timer"""

    def __init__(self, time, name):
        self.time = time
        self.name = name


class PerformanceCounter:
    """処理時間の計測のためのクラス"""

    def __init__(self, name="process[0]"):
        self.timers = [Timer(perf_counter(), name)]
        self.length = 1

    def append_timer(self, name=""):
        """タイマーを追加"""
        default_name = f"process[{self.length}]"
        if name == "":
            name = default_name

        self.length += 1
        self.timers.append(Timer(perf_counter(), name))

    def print_time(self):
        """処理時間をプリント"""
        for i in range(self.length - 1):
            elapsed_time = self.timers[i + 1].time - self.timers[i].time
            print(f"{self.timers[i].name} ~ {self.timers[i+1].name}: {elapsed_time}")
