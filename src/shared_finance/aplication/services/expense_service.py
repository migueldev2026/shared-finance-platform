class ExpenseService:

    def __init__(self, repository):
        self.repository = repository

    def list_expenses(self):

        return self.repository.get_all()