import pyodbc
import datetime

class UserManager:
    def __init__(self):
        self.connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            'Server=DESKTOP-OM4IIFB;'
            'Database=TZ_banking_system2;'
            'trusted_Connection=yes;'
        )
        self.cursor = self.connection.cursor()
        print("Connected Successfully")

    def get_all_users(self):
        query = "SELECT * FROM Users"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_active_users(self):
        query = """
        SELECT * FROM users
        WHERE last_active_at >= DATEADD(MONTH, -1, GETDATE())
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_user_balances(self):
        query = "SELECT id, total_balance FROM users"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_card_limits(self):
        query = "SELECT id, user_id, limit_amount FROM cards"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        print("Connection Closed")

class TransactionManager:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def transfer_money(self, from_card, to_card, amount):
        query = """
        INSERT INTO transactions (from_card_id, to_card_id, amount, status, created_at, transaction_type)
        VALUES (?, ?, ?, 'pending', GETDATE(), 'transfer')
        """
        self.cursor.execute(query, (from_card, to_card, amount))
        self.connection.commit()
        print(f"Transfer of {amount} from Card {from_card} to Card {to_card} initiated.")

    def get_daily_transactions(self):
        query = """
        SELECT * FROM transactions
        WHERE created_at >= CAST(GETDATE() AS DATE)
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_weekly_transactions(self):
        query = """
        SELECT * FROM transactions
        WHERE created_at >= DATEADD(DAY, -7, GETDATE())
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_large_transactions(self, threshold=500000):
        query = """
        SELECT * FROM transactions
        WHERE amount > ?
        """
        self.cursor.execute(query, (threshold,))
        return self.cursor.fetchall()

    def withdraw_money(self, card_id, amount):
        query = """
        INSERT INTO transactions (from_card_id, amount, status, created_at, transaction_type)
        VALUES (?, ?, 'pending', GETDATE(), 'withdrawal')
        """
        self.cursor.execute(query, (card_id, amount))
        self.connection.commit()
        print(f"Withdrawal of {amount} from Card {card_id} initiated.")
    
    def deposit_money(self, card_id, amount):
        query = """
        INSERT INTO transactions (to_card_id, amount, status, created_at, transaction_type)
        VALUES (?, ?, 'pending', GETDATE(), 'deposit')
        """
        self.cursor.execute(query, (card_id, amount))
        self.connection.commit()
        print(f"Deposit of {amount} to Card {card_id} initiated.")

class ExtraFunctions:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
    
    def generate_report(self, period):
        query = """
        SELECT report_type, created_at, total_transactions, flagged_transactions, total_amount
        FROM reports WHERE report_type = ?
        """
        self.cursor.execute(query, (period,))
        return self.cursor.fetchall()
    
    def monitor_blocked_cards(self):
        query = "SELECT user_id, reason FROM blocked_users"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_user_transaction_history(self, user_id):
        query = """
        SELECT * FROM transactions
        WHERE from_card_id IN (SELECT id FROM cards WHERE user_id = ?) 
        OR to_card_id IN (SELECT id FROM cards WHERE user_id = ?)
        """
        self.cursor.execute(query, (user_id, user_id))
        return self.cursor.fetchall()
    
    def analyze_balances(self):
        query = """
        WITH MostFrequentUser AS (
            SELECT TOP 1 id
            FROM transactions 
            GROUP BY id 
            ORDER BY COUNT(id) DESC
        )
        SELECT 
            AVG(total_balance) AS average_balance,
            (SELECT id FROM MostFrequentUser) AS most_frequent_user
        FROM users;
         """
        self.cursor.execute(query)
        return self.cursor.fetchone()

class UserManagement:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()


    def identify_vip_users(self, threshold=1000000):
        query = """
        UPDATE users
        SET is_vip = 1
        WHERE id IN (
            SELECT from_card_id FROM transactions 
            WHERE amount >= ?
            GROUP BY from_card_id
        )
        """
        self.cursor.execute(query, (threshold,))
        self.connection.commit()
        print("VIP users updated successfully.")

    def vip_users(self):
        query = "SELECT id, name, email, total_balance FROM users WHERE is_vip = 1"
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def add_user(self, name, email, phone_number, bonus_amount=100000):
        query = """
        INSERT INTO users (name, email, phone_number, total_balance, created_at, last_active_at)
        VALUES (?, ?, ?, ?, GETDATE(), GETDATE())
        """
        self.cursor.execute(query, (name, email, phone_number, bonus_amount))
        self.connection.commit()
        print(f"New user {name} registered with welcome bonus of {bonus_amount}.")


    def block_user(self, user_id, reason):
        query = "INSERT INTO blocked_users (user_id, reason) VALUES (?, ?)"
        self.cursor.execute(query, (user_id, reason))
        self.connection.commit()
        print(f"User {user_id} blocked for {reason}.")


    def monitor_blocked_users(self):
        query = "SELECT * FROM blocked_users"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_user_cards(self, user_id):
        query = """
        SELECT id, card_number, balance, is_blocked, card_type, limit_amount 
        FROM cards WHERE user_id = ?
        """
        self.cursor.execute(query, (user_id,))
        cards = self.cursor.fetchall()
    
        if not cards:
            print(f"No cards found for user ID {user_id}.")
            return []
    
        return cards


    def apply_cashback(self, user_id, transaction_id, percentage=5):
        query = "SELECT amount FROM transactions WHERE id = ?"
        self.cursor.execute(query, (transaction_id,))
        amount = self.cursor.fetchone()[0]

        cashback = (amount * percentage) / 100
        update_balance_query = "UPDATE users SET total_balance = total_balance + ? WHERE id = ?"
        self.cursor.execute(update_balance_query, (cashback, user_id))
        self.connection.commit()
        print(f"Cashback of {cashback} applied to user {user_id}.")


    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        print("Connection Closed")

class TransactionManagement:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def verify_large_transaction(self, transaction_id):
        query = "SELECT amount FROM transactions WHERE id = ?"
        self.cursor.execute(query, (transaction_id,))
        transaction = self.cursor.fetchone()

        if transaction is not None:  
            amount = transaction[0]  
            if amount > 500000:
                print(f"Transaction {transaction_id} requires 2FA verification.")
                return True
            else:
                print(f"Transaction {transaction_id} does not require 2FA verification.")
        else:
            print(f"Transaction {transaction_id} not found.")

        return False

    def detect_suspicious_transactions(self, user_id):
        query = """
        SELECT COUNT(*) FROM transactions
        WHERE from_card_id IN (SELECT id FROM cards WHERE user_id = ?)
        AND created_at >= DATEADD(MINUTE, -5, GETDATE())
        """
        self.cursor.execute(query, (user_id,))
        count = self.cursor.fetchone()[0]

        if count >= 3:
            print(f"User {user_id} has made {count} transactions in the last 5 minutes. Flagging for review.")
            return True
        else:
            print(f"No suspicious transactions found for User {user_id}.")
    
        return False

    def prevent_incorrect_transfers(self, card_number):
        query = "SELECT id FROM cards WHERE card_number = ?"
        self.cursor.execute(query, (card_number,))
        recipient = self.cursor.fetchone()

        if recipient:
            print(f"Transaction recipient confirmed: User ID {recipient[0]}")
            return recipient[0]
        else:
            print("Invalid card number. Transaction denied.")
            return None

    def issue_loan(self, user_id, amount, repayment_period):
        query = """
        INSERT INTO loans (user_id, amount, repayment_period, status, created_at)
        VALUES (?, ?, ?, 'active', GETDATE())
        """
        self.cursor.execute(query, (user_id, amount, repayment_period))
        self.connection.commit()
        print(f"Loan of {amount} issued to User {user_id} with {repayment_period}-month repayment period.")

    def repay_loan(self, loan_id, amount):
        query = "UPDATE loans SET amount = amount - ? WHERE id = ?"
        self.cursor.execute(query, (amount, loan_id))
        self.connection.commit()
        print(f"Loan {loan_id} repaid with {amount}.")

    def schedule_payment(self, user_id, card_id, amount, payment_date, service_type):
        query = """
        INSERT INTO scheduled_payments (user_id, card_id, amount, payment_date, status, created_at)
        VALUES (?, ?, ?, ?, 'pending', GETDATE())
        """
        self.cursor.execute(query, (user_id, card_id, amount, payment_date))
        self.connection.commit()
        print(f"Payment scheduled for {service_type} from Card {card_id} on {payment_date}.")

class ReportingAndMonitoring:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def total_user_balance(self):
        query = "SELECT SUM(total_balance) AS total_funds FROM users"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        print(f"Total Circulating Funds: {result[0]} sum")
        return result[0]

    def top_transaction_user(self, period):
        valid_periods = ["DAY", "WEEK", "MONTH"]  
        if period.upper() not in valid_periods:
            raise ValueError("Invalid period. Choose from 'DAY', 'WEEK', or 'MONTH'.")

        query = f"""
        SELECT TOP 1 c.user_id, COUNT(*) AS transaction_count
        FROM transactions t
        JOIN cards c ON t.from_card_id = c.id  -- Linking transactions to users
        WHERE t.created_at >= DATEADD({period.upper()}, -1, GETDATE())
        GROUP BY c.user_id
        ORDER BY COUNT(*) DESC
        """
        self.cursor.execute(query)
        result = self.cursor.fetchone()
    
        if result:
            print(f"User {result[0]} made the most transactions ({result[1]}) in the last {period.lower()}.")
            return result
        else:
            print(f"No transactions found for the last {period.lower()}.")
            return None

    def most_spent_services(self):
        query = """
        SELECT transaction_type, SUM(amount) AS total_spent
        FROM transactions
        WHERE transaction_type IN ('transfer', 'withdrawal', 'deposit')  -- Ensure relevant types
        GROUP BY transaction_type
        ORDER BY total_spent DESC
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        if results:
            print("Most Spent Services:")
            for row in results:
                print(f"{row[0]}: {row[1]}")
        else:
            print("No transaction data available.")
        return results

    def analyze_cash_flow(self):
        query = """
        SELECT
            SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE 0 END) AS total_deposits,
            SUM(CASE WHEN transaction_type = 'withdrawal' THEN amount ELSE 0 END) AS total_withdrawals
        FROM transactions
        """
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        print(f"Total Deposits: {result[0]}, Total Withdrawals: {result[1]}")
        return result

    def average_card_usage_duration(self):
        query = """
        SELECT AVG(DATEDIFF(DAY, created_at, GETDATE())) AS avg_usage_days FROM cards
        """
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        print(f"Average Card Usage Duration: {result[0]} days")
        return result[0]

class SecurityAudit:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def block_card(self, card_id, reason="Lost or Stolen"):
        query = """
        UPDATE cards 
        SET status = 'blocked', blocked_reason = ? 
        WHERE id = ?
        """
        self.cursor.execute(query, (reason, card_id))
        self.connection.commit()
        print(f"Card {card_id} has been blocked due to {reason}.")

    def detect_unusual_activity(self, user_id):
        query = """
        WITH UserAvg AS (
            SELECT id, AVG(amount) AS avg_amount
            FROM transactions
            WHERE id = ?
            GROUP BY id
        )
        SELECT t.id, t.amount, ua.avg_amount
        FROM transactions t
        JOIN UserAvg ua ON t.id = ua.id
        WHERE t.id = ? AND t.amount > ua.avg_amount * 5
        """
        self.cursor.execute(query, (user_id, user_id))
        results = self.cursor.fetchall()

        if results:
            print(f"Unusual activity detected for User {user_id}!")
            for row in results:
                print(f"Transaction {row[0]}: {row[1]} UZS (Avg: {row[2]} UZS)")
            return True
        else:
            print(f"No unusual activity detected for User {user_id}.")
            return False

class AdditionalServices:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def automatic_savings(self, user_id, transaction_id):
        query = """
        SELECT t.amount, c.user_id
        FROM transactions t
        JOIN cards c ON t.to_card_id = c.id
        WHERE t.id = ?;
        """  
        self.cursor.execute(query, (transaction_id,))
        transaction = self.cursor.fetchone()
        
        if transaction:
            print(f"Transaction found: Amount {transaction[0]}, User {transaction[1]}")
            if transaction[1] != user_id:
                print(f" User ID mismatch! Expected {user_id}, but transaction belongs to {transaction[1]}")
                return

            savings_amount = transaction[0] * 0.05  # 5% savings
            savings_query = """
            UPDATE users SET savings_balance = savings_balance + ? WHERE id = ?
            """
            self.cursor.execute(savings_query, (savings_amount, user_id))
            self.connection.commit()
            print(f"Saved {savings_amount} UZS from transaction {transaction_id} for User {user_id}.")
        else:
            print("Transaction not found.")

    def transfer_to_heirs(self, deceased_user_id, heir_user_id):
        query = """
        SELECT total_balance FROM users WHERE id = ?
        """
        self.cursor.execute(query, (deceased_user_id,))
        balance = self.cursor.fetchone()
        
        if balance and balance[0] > 0:
            transfer_query = """
            UPDATE users SET total_balance = total_balance - ? WHERE id = ?
            """
            self.cursor.execute(transfer_query, (balance[0], deceased_user_id))
            
            receive_query = """
            UPDATE users SET total_balance = total_balance + ? WHERE id = ?
            """
            self.cursor.execute(receive_query, (balance[0], heir_user_id))
            
            self.connection.commit()
            print(f"Transferred {balance[0]} UZS from User {deceased_user_id} to heir {heir_user_id}.")
        else:
            print("No balance available to transfer.")

    def foreign_currency_transaction(self, user_id, amount, currency):
        exchange_rates = {"USD": 12000, "EUR": 13000, "RUB": 150}
        if currency not in exchange_rates:
            print("Unsupported currency.")
            return
        
        converted_amount = amount * exchange_rates[currency]
        query = """
        UPDATE users SET total_balance = total_balance - ? WHERE id = ?
        """
        self.cursor.execute(query, (converted_amount, user_id))
        self.connection.commit()
        print(f"User {user_id} made a transaction of {amount} {currency} ({converted_amount} UZS).")

    def schedule_payment(self, user_id, recipient_id, amount, scheduled_date, description):
        query = """
        INSERT INTO scheduled_payments (user_id, recipient_id, amount, scheduled_date, description)
        VALUES (?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (user_id, recipient_id, amount, scheduled_date, description))
        self.connection.commit()
        print(f"Scheduled payment of {amount} UZS to recipient {recipient_id} on {scheduled_date} for {description}.")

    def analyze_card_usage(self, user_id):
        query = """
        SELECT TOP 5 location, COUNT(*) AS usage_count
        FROM transactions
        WHERE id = ?
        GROUP BY location
        ORDER BY usage_count DESC;
        """
        self.cursor.execute(query, (user_id,))
        transactions = self.cursor.fetchall()

        if transactions:
            for transaction in transactions:
                print(f"Location: {transaction[0]}, Usage Count: {transaction[1]}")
        else:
            print("No transactions found.")



if __name__ == "__main__":
    manager = UserManager()
    transaction_manager = TransactionManager(manager.connection)
    extra_functions = ExtraFunctions(manager.connection)
    user_management = UserManagement(manager.connection)
    transaction_management = TransactionManagement(manager.connection)
    report_manager = ReportingAndMonitoring(manager.connection)
    security_audit = SecurityAudit(manager.connection)
    additional_services = AdditionalServices(manager.connection)

    def print_menu():
        print("\nBanking System Menu:")
        print("0. Quit")
        print("1. View all users")
        print("2. View active users in last month")
        print("3. Check user balances")
        print("4. View card limits")
        print("5. View daily transactions")
        print("6. View large transactions (Above 500000)")
        print("7. Generate daily report")
        print("8. Generate weekly report")
        print("9. Generate monthly report")
        print("10. Monitor blocked cards")
        print("11. View user transaction history")
        print("12. Analyze user balances")
        print("13. Identify VIP users")
        print("14. View VIP users")
        print("15. Register a new user")
        print("16. Block a user")
        print("17. Monitor blocked users")
        print("18. View user cards")
        print("19. Apply cashback")
        print("20. Verify large transaction")
        print("21. Detect suspicious transactions")
        print("22. Prevent incorrect transfers")
        print("23. Issue a loan")
        print("24. Repay a loan")
        print("25. Schedule a payment")
        print("26. Get total user balance")
        print("27. Get top transaction user")
        print("28. View most spent services")
        print("29. Analyze cash flow")
        print("30. Get average card usage duration")
        print("31. Block a lost/stolen card")
        print("32. Detect unusual activities")
        print("33. Automatic savings")
        print("34. Transfer funds to heirs")
        print("35. Foreign currency transaction")
        print("36. Analyze card usage")
        print("37. Transfer money")
        print("38. Withdraw money")
        print("39. Deposit money")

    print_menu() 

    while True:
        command = input("\nPlease enter your command: ")

        if command == "0":
            print("Exiting system... Goodbye!")
            manager.close_connection()
            break
        elif command == "1":
            print(manager.get_all_users())
        elif command == "2":
            print(manager.get_active_users())
        elif command == "3":
            print(manager.get_user_balances())
        elif command == "4":
            print(manager.get_card_limits())
        elif command == "5":
            print(transaction_manager.get_daily_transactions())
        elif command == "6":
            print(transaction_manager.get_large_transactions())
        elif command == "7":
            print(extra_functions.generate_report("daily"))
        elif command == "8":
            print(extra_functions.generate_report("weekly"))
        elif command == "9":
            print(extra_functions.generate_report("monthly"))
        elif command == "10":
            print(extra_functions.monitor_blocked_cards())
        elif command == "11":
            user_id = int(input("Enter user ID: "))
            print(extra_functions.get_user_transaction_history(user_id))
        elif command == "12":
            print(extra_functions.analyze_balances())
        elif command == "13":
            user_management.identify_vip_users()
        elif command == "14":
            print(user_management.vip_users())
        elif command == "15":
            name = input("Enter full name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            user_management.add_user(name, email, phone)
        elif command == "16":
            user_id = int(input("Enter user ID to block: "))
            reason = input("Enter reason: ")
            user_management.block_user(user_id, reason)
        elif command == "17":
            print(user_management.monitor_blocked_users())
        elif command == "18":
            user_id = int(input("Enter user ID: "))
            print(user_management.get_user_cards(user_id))
        elif command == "19":
            user_id = int(input("Enter user ID: "))
            transaction_id = int(input("Enter transaction ID: "))
            user_management.apply_cashback(user_id, transaction_id)
        elif command == "20":
            transaction_id = int(input("Enter transaction ID: "))
            transaction_manager.verify_large_transaction(transaction_id)
        elif command == "21":
            user_id = int(input("Enter user ID: "))
            transaction_manager.detect_suspicious_transactions(user_id)
        elif command == "22":
            card_number = input("Enter card number: ")
            transaction_manager.prevent_incorrect_transfers(card_number)
        elif command == "23":
            user_id = int(input("Enter user ID: "))
            amount = int(input("Enter loan amount: "))
            duration = int(input("Enter loan duration (months): "))
            transaction_manager.issue_loan(user_id, amount, duration)
        elif command == "24":
            user_id = int(input("Enter user ID: "))
            amount = int(input("Enter repayment amount: "))
            transaction_manager.repay_loan(user_id, amount)
        elif command == "25":
            user_id = int(input("Enter user ID: "))
            recipient_id = int(input("Enter recipient ID: "))
            amount = int(input("Enter amount: "))
            date_str = input("Enter scheduled date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            description = input("Enter description: ")
            transaction_manager.schedule_payment(user_id, recipient_id, amount, date, description)
        elif command == "26":
            print(report_manager.total_user_balance())
        elif command == "27":
            period = input("Enter period (DAY/WEEK/MONTH): ")
            print(report_manager.top_transaction_user(period))
        elif command == "28":
            print(report_manager.most_spent_services())
        elif command == "29":
            print(report_manager.analyze_cash_flow())
        elif command == "30":
            print(report_manager.average_card_usage_duration())
        elif command == "31":
            card_id = int(input("Enter card ID: "))
            reason = input("Enter reason: ")
            security_audit.block_card(card_id, reason)
        elif command == "32":
            user_id = int(input("Enter user ID: "))
            security_audit.detect_unusual_activity(user_id)
        elif command == "33":
            user_id = int(input("Enter user ID: "))
            transaction_id = int(input("Enter transaction ID: "))
            additional_services.automatic_savings(user_id, transaction_id)
        elif command == "34":
            from_user = int(input("Enter sender user ID: "))
            to_user = int(input("Enter recipient user ID: "))
            additional_services.transfer_to_heirs(from_user, to_user)
        elif command == "35":
            user_id = int(input("Enter user ID: "))
            amount = float(input("Enter amount: "))
            currency = input("Enter currency (USD/EUR/etc.): ")
            additional_services.foreign_currency_transaction(user_id, amount, currency)
        elif command == "36":
            user_id = int(input("Enter user ID: "))
            additional_services.analyze_card_usage(user_id)
        elif command == "37":
            from_user = int(input("Enter sender user ID: "))
            to_user = int(input("Enter recipient user ID: "))
            amount = int(input("Enter amount: "))
            transaction_manager.transfer_money(from_user, to_user, amount)
        elif command == "38":
            user_id = int(input("Enter user ID: "))
            amount = int(input("Enter amount: "))
            transaction_manager.withdraw_money(user_id, amount)
        elif command == "39":
            user_id = int(input("Enter user ID: "))
            amount = int(input("Enter amount: "))
            transaction_manager.deposit_money(user_id, amount)
        else:
            print("Invalid command! Please enter a valid number.")
