from database import Database

class DataManager:
    def __init__(self):
        self.db = Database()

    def get_all_data(self):
        return self.db.get_all_data()
