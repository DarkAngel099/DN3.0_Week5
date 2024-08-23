import os
import logging
from datetime import datetime

def process_transaction(transaction_data):
    try:
        if not os.path.exists('transaction_data.txt'):
            raise FileNotFoundError("Transaction data file not found.")

        if not isinstance(transaction_data, dict):
            raise ValueError("Invalid transaction data format.")

        with open('transaction_data.txt', 'a') as file:
            file.write(f"{transaction_data}\n")

        print("Transaction processed successfully.")

    except ValueError as ve:
        print(f"Error: {ve}")
        log_error(ve)

    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
        log_error(fnfe)
        create_transaction_file()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        log_error(e)

def create_transaction_file():
    with open('transaction_data.txt', 'w') as file:
        file.write("Transaction Log\n")
    print("Transaction data file created successfully.")

def validate_transaction_data(transaction_data):
    if not isinstance(transaction_data, dict):
        return False

    required_keys = ['transaction_id', 'amount', 'currency']
    for key in required_keys:
        if key not in transaction_data:
            return False

    if not isinstance(transaction_data['amount'], (int, float)) or transaction_data['amount'] <= 0:
        return False

    return True

def prompt_for_valid_transaction():
    print("Invalid transaction data. Please enter the details again.")
    transaction_id = input("Transaction ID: ")
    amount = input("Amount: ")
    currency = input("Currency: ")

    try:
        amount = float(amount)
    except ValueError:
        print("Amount must be a number.")
        return None

    return {
        'transaction_id': transaction_id,
        'amount': amount,
        'currency': currency
    }

def log_error(error):
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()} - {str(error)}\n")

def main():
    while True:
        transaction_data = {
            'transaction_id': 'TX12345',
            'amount': 100.0,
            'currency': 'USD'
        }

        if not validate_transaction_data(transaction_data):
            transaction_data = prompt_for_valid_transaction()
            if not transaction_data:
                continue


        process_transaction(transaction_data)


        continue_processing = input("Do you want to process another transaction? (yes/no): ")
        if continue_processing.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
