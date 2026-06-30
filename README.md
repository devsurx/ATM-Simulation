# STEEL MOUNTAIN - Impenetrable ATM Simulation

STEEL MOUNTAIN is a terminal-based ATM simulation built in Python using Object-Oriented Programming (OOP) principles. The project emulates the workflow of a real ATM, allowing users to create an account, generate an ATM card, authenticate securely, and perform banking operations through a clean command-line interface.

## Features

- Create a new bank account
- Automatic account number generation
- ATM card generation with:
  - 16-digit card number
  - 10-year expiry date
- PIN authentication
- Deposit money
- Withdraw money
- Balance inquiry
- Transaction receipts
- Secure terminal interface

## OOP Concepts Used

- Encapsulation
- Inheritance
- Abstraction
- Polymorphism

## Technologies

- Python 3
- abc (Abstract Base Classes)
- random
- datetime
- time
- subprocess

## Project Structure

- `Account` – Stores account information and banking operations.
- `Card` – Handles ATM card details and PIN.
- `ATM` – Manages authentication and user interaction.
- `Transaction` – Abstract base class for all transactions.
- `DepositTransaction`
- `WithdrawalTransaction`
- `BalanceInquiryTransaction`

## Future Improvements

- Transaction history
- Multiple accounts
- Database integration
- Daily withdrawal limits
- PIN encryption
- Account lock after multiple failed attempts
