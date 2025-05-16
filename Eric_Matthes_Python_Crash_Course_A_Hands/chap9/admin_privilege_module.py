from user_module import User

class Privileges:
    def __init__(self,privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print(f"Privilages: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print(f"{self.first_name} {self.last_name} has no privileges")

class Admin(User):
    def __init__(self, first_name, last_name, age, location, occupation, privileges=None):
        super().__init__(first_name, last_name, age, location, occupation)
        self.privileges = Privileges(privileges)