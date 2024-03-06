import os
from datetime import datetime

class DiaryApp:
    def __init__(self, diary_folder='diaries'):
        self.diary_folder = diary_folder
        self.create_diary_folder()

    def create_diary_folder(self):
        if not os.path.exists(self.diary_folder):
            os.makedirs(self.diary_folder)

    def get_diary_filename(self, date):
        return os.path.join(self.diary_folder, f"{date}.txt")

    def write_diary_entry(self, date, entry):
        filename = self.get_diary_filename(date)
        with open(filename, 'w') as file:
            file.write(entry)

    def read_diary_entry(self, date):
        filename = self.get_diary_filename(date)
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return file.read()
        else:
            return "No entry for this date."

    def start_diary(self):
        while True:
            print("1. Write diary entry")
            print("2. Read diary entry")
            print("3. Exit")
            choice = input("Choose an option (1/2/3): ")

            if choice == '1':
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                entry = input("Write your diary entry: ")
                self.write_diary_entry(date, entry)
                print("Diary entry saved successfully.")
            elif choice == '2':
                date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
                entry = self.read_diary_entry(date)
                print(f"Diary entry for {date}:\n{entry}")
            elif choice == '3':
                print("Exiting diary app. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    diary_app = DiaryApp()
    diary_app.start_diary()
