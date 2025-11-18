from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QListWidget
from PyQt5.QtCore import QTimer

class PomodoroApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pomodoro Timer")
        self.setGeometry(100, 100, 300, 400)

        self.tasks = []
        self.work_time = 25 * 60  # 25 menit
        self.break_time = 5 * 60  # 5 menit
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.layout = QVBoxLayout()

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Add a task")
        self.layout.addWidget(self.task_input)

        self.add_task_btn = QPushButton("Add Task", self)
        self.add_task_btn.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_task_btn)

        self.task_list = QListWidget(self)
        self.layout.addWidget(self.task_list)

        self.timer_label = QLabel("25:00", self)
        self.timer_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.layout.addWidget(self.timer_label)

        self.start_btn = QPushButton("Start Timer", self)
        self.start_btn.clicked.connect(self.start_timer)
        self.layout.addWidget(self.start_btn)

        self.setLayout(self.layout)

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.task_input.clear()

    def start_timer(self):
        if not self.tasks:
            return
        self.current_task = self.tasks.pop(0)
        self.task_list.takeItem(0)
        self.run_timer(self.work_time, "Work")

    def run_timer(self, duration, mode):
        self.timer.start(1000)
        self.mode = mode
        self.remaining_time = duration

    def update_timer(self):
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.timer_label.setText(f"{minutes:02}:{seconds:02}")
            self.remaining_time -= 1
        else:
            self.timer.stop()
            if self.mode == "Work":
                self.run_timer(self.break_time, "Break")
            else:
                if self.tasks:
                    self.current_task = self.tasks.pop(0)
                    self.task_list.takeItem(0)
                    self.run_timer(self.work_time, "Work")
                else:
                    self.timer_label.setText("25:00")

if __name__ == "__main__":
    app = QApplication([])
    window = PomodoroApp()
    window.show()
    app.exec_()
