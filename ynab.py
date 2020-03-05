from api import APIClient


class TransactionNotFound(Exception):
    pass


class YNAB(APIClient):
    def __init__(self, token=None):
        super().__init__(token)
        self.token = token
        self.url_base = 'https://api.youneedabudget.com/v1'
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {self.token}'}

    # User
    def get_user(self):
        return self.send_get('user')

    # Budgets
    def get_budgets(self):
        return self.send_get('budgets')

    def get_budget(self, budget_id="last-used"):
        return self.send_get(f'budgets/{budget_id}')

    def get_budget_settings(self, budget_id="last-used"):
        return self.send_get(f'budgets/{budget_id}/settings')

    # Accounts
    def get_accounts(self, budget_id="last-used"):
        return self.send_get(f'budgets/{budget_id}/accounts')

    def get_account(self, budget_id, account_id):
        return self.send_get(f'budgets/{budget_id}/accounts/{account_id}')

    # Categories
    def get_categories(self, budget_id="last-used"):
        return self.send_get(f'budgets/{budget_id}/categories')

    def get_category(self, category_id, budget_id="last-used"):
        return self.send_get(f'budgets/{budget_id}/categories/{category_id}')

    def get_category_for_month(self, category_id, budget_id="last-used", month="current"):
        return self.send_get(f'budgets/{budget_id}/months/{month}/categories/{category_id}')

    def update_category_for_month(self, category_id, data, budget_id="last-used", month="current"):
        return self.send_patch(f'budgets/{budget_id}/months/{month}/categories/{category_id}', data)

    # Payees
    def get_payees(self, budget_id="last-used"):
        return self.send_get(f'budgets/{budget_id}/payees')

    def get_payee(self, budget_id, payee_id):
        return self.send_get(f'budgets/{budget_id}/payees/{payee_id}')

    # Payee Locations
    def get_payee_locations(self, budget_id="last-used"):
        return self.send_get(f'budgets/{budget_id}/payee_locations')

    def get_payee_location(self, budget_id, payee_location_id):
        return self.send_get(f'budgets/{budget_id}/payee_locations/{payee_location_id}')

    def get_locations_for_payee(self, budget_id, payee_id):
        return self.send_get(f'budgets/{budget_id}/payees/{payee_id}/payee_locations')

    # Months
    def get_months(self, budget_id="last-used"):
        return self.send_get(f'budgets/{budget_id}/months')

    def get_month(self, budget_id="last-used", month="current"):
        return self.send_get(f'budgets/{budget_id}/months/{month}')

    # Transactions
    def get_transactions(self, budget_id="last-used"):
        return self.send_get(f'budgets/{budget_id}/transactions')

    def get_transaction(self, budget_id, transaction_id):
        return self.send_get(f'budgets/{budget_id}/transactions{transaction_id}')

    def add_transactions(self, budget_id, data):
        return self.send_post(f'budgets/{budget_id}/transactions', data)

    def update_transactions(self, budget_id, data):
        return self.send_patch(f'budgets/{budget_id}/transactions', data)

    def update_transaction(self, budget_id, transaction_id, data):
        return self.send_put(f'budgets/{budget_id}/transactions/{transaction_id}', data)

    def get_transactions_for_account(self, budget_id, account_id):
        return self.send_get(f'budgets/{budget_id}/accounts/{account_id}/transactions')

    def get_transactions_for_category(self, budget_id, category_id):
        return self.send_get(f'budgets/{budget_id}/categories/{category_id}/transactions')

    def get_transactions_for_payee(self, budget_id, payee_id):
        return self.send_get(f'budgets/{budget_id}/payees/{payee_id}/transactions')

    # Scheduled Transactions
    def get_scheduled_transactions(self, budget_id="last-used"):
        return self.send_get(f'budgets/{budget_id}/scheduled_transactions')

    def get_scheduled_transaction(self, budget_id, scheduled_transaction_id):
        return self.send_get(f'budgets/{budget_id}/scheduled_transactions/{scheduled_transaction_id}')


if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read("config.ini")
    ynab = YNAB(config["YNAB"]["token"])
    budget_data = ynab.get_budget()
    print(budget_data)
