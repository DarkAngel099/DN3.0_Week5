import os
import logging
from datetime import datetime

# Function to process transactions
def process_transaction(transaction_data):
    try:
        # Ensure the transaction data file exists
        if not os.path.exists('transaction_data.txt'):
            raise FileNotFoundError("Transaction data file not found.")

        # Simulate transaction processing logic
        if not isinstance(transaction_data, dict):
            raise ValueError("Invalid transaction data format.")

        # Simulate writing the transaction to the file
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

# Function to create the transaction data file if not found
def create_transaction_file():
    with open('transaction_data.txt', 'w') as file:
        file.write("Transaction Log\n")
    print("Transaction data file created successfully.")

# Function to validate transaction data
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

# Function to prompt the user to correct invalid data
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

# Function to log errors to a file
def log_error(error):
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()} - {str(error)}\n")

# Main function to process transactions and handle errors
def main():
    while True:
        # Simulate getting transaction data (this would typically come from a user or an external source)
        transaction_data = {
            'transaction_id': 'TX12345',
            'amount': 100.0,
            'currency': 'USD'
        }

        # Validate the transaction data
        if not validate_transaction_data(transaction_data):
            transaction_data = prompt_for_valid_transaction()
            if not transaction_data:
                continue

        # Process the transaction
        process_transaction(transaction_data)

        # Ask the user if they want to process another transaction
        continue_processing = input("Do you want to process another transaction? (yes/no): ")
        if continue_processing.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
