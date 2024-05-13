import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QComboBox

class ToDoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToDo List")
        self.setFixedSize(400, 300)

        self.tasks = []

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        self.task_input_layout = QHBoxLayout()
        self.task_input_label = QLabel("Task:")
        self.task_input = QLineEdit()
        self.task_input_layout.addWidget(self.task_input_label)
        self.task_input_layout.addWidget(self.task_input)
        self.layout.addLayout(self.task_input_layout)

        self.due_date_input_layout = QHBoxLayout()
        self.due_date_input_label = QLabel("Due Date:")
        self.due_date_input = QLineEdit()
        self.due_date_input_layout.addWidget(self.due_date_input_label)
        self.due_date_input_layout.addWidget(self.due_date_input)
        self.layout.addLayout(self.due_date_input_layout)

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.sort_combo_box = QComboBox()
        self.sort_combo_box.addItem("Sort by Name")
        self.sort_combo_box.addItem("Sort by Due Date")
        self.sort_combo_box.currentIndexChanged.connect(self.sort_tasks)
        self.layout.addWidget(self.sort_combo_box)

        self.task_list = QListWidget()
        self.task_list.itemClicked.connect(self.mark_task_done)
        self.layout.addWidget(self.task_list)

        self.search_input = QLineEdit()
        self.search_input.textChanged.connect(self.search_tasks)
        self.layout.addWidget(self.search_input)

        self.delete_button = QPushButton("Delete Task")
        self.delete_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_button)

        self.delete_all_button = QPushButton("Delete All Tasks")
        self.delete_all_button.clicked.connect(self.delete_all_tasks)
        self.layout.addWidget(self.delete_all_button)

    def add_task(self):
        task = self.task_input.text()
        due_date = self.due_date_input.text()
        self.tasks.append({"task": task, "due_date": due_date, "done": False})
        self.task_list.addItem(task)
        self.task_input.clear()
        self.due_date_input.clear()

    def mark_task_done(self, item):
        task = item.text()
        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        item.setCheckState(QtCore.Qt.Checked)
        for task_item in self.tasks:
            if task_item["task"] == task:
                task_item["done"] = True

    def sort_tasks(self, index):
        if index == 0:  # Sort by Name
            self.tasks.sort(key=lambda x: x["task"])
        elif index == 1:  # Sort by Due Date
            self.tasks.sort(key=lambda x: x["due_date"])
        self.task_list.clear()
        for task_item in self.tasks:
            self.task_list.addItem(task_item["task"])

    def search_tasks(self, text):
        self.task_list.clear()
        for task_item in self.tasks:
            if text.lower() in task_item["task"].lower():
                self.task_list.addItem(task_item["task"])

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            selected_task = selected_items[0].text()
            self.task_list.takeItem(self.task_list.row(selected_items[0]))
            for task_item in self.tasks:
                if task_item["task"] == selected_task:
                    self.tasks.remove(task_item)

    def delete_all_tasks(self):
        self.task_list.clear()
        self.tasks = []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_list_app = ToDoListApp()
    todo_list_app.show()
    sys.exit(app.exec_())