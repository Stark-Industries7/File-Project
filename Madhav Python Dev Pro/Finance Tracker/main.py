import sys
import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QComboBox, QGridLayout, QHBoxLayout, QLabel, QFormLayout, QInputDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette

# Constants
FORMAT = "%d-%m-%Y"
COLUMNS = ["Date", "Amount", "Category", "Description"]
CATEGORIES = {"I": "Income", "E": "Expense", "INV": "Investment"}

class Finance:
    FILENAME = "Finance.csv"
    
    @classmethod
    def initialize(cls):
        try:
            pd.read_csv(cls.FILENAME)
        except FileNotFoundError:
            with open(cls.FILENAME, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=COLUMNS)
                writer.writeheader()

    @classmethod
    def add_transaction(cls, date, amount, category, description):
        with open(cls.FILENAME, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=COLUMNS)
            writer.writerow({"Date": date, "Amount": amount, "Category": category, "Description": description})
    
    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.FILENAME)
        df["Date"] = pd.to_datetime(df["Date"], format=FORMAT)
        s_date = datetime.strptime(start_date, FORMAT)
        e_date = datetime.strptime(end_date, FORMAT)

        mask = (df["Date"] >= s_date) & (df["Date"] <= e_date)
        filtered_df = df.loc[mask]
        
        return filtered_df

    @classmethod
    def plot_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.FILENAME)
        df["Date"] = pd.to_datetime(df["Date"], format=FORMAT)

        # Filter transactions based on the date range
        s_date = datetime.strptime(start_date, FORMAT)
        e_date = datetime.strptime(end_date, FORMAT)
        mask = (df["Date"] >= s_date) & (df["Date"] <= e_date)
        filtered_df = df.loc[mask]

        total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
        total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
        total_investment = filtered_df[filtered_df["Category"] == "Investment"]["Amount"].sum()

        categories = ["Income", "Expense", "Investment"]
        amounts = [total_income, total_expense, total_investment]
        colors = ["#4CAF50", "#FF5722", "#3F51B5"]

        fig, axes = plt.subplots(1, 2, figsize=(16, 7))

        axes[0].bar(categories, amounts, color=colors, alpha=0.7)
        axes[0].set_title("Your Financial Health")
        axes[0].set_xlabel("Transaction Type ₹")
        axes[0].set_ylabel("Amounts ₹")
        axes[0].grid(axis='y', linestyle='--', alpha=0.7)

        axes[1].pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140, colors=colors)
        axes[1].set_title("Your Proportion of Transactions")

        plt.tight_layout()
        plt.show()


class FinanceTrackerApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Initialize Finance CSV
        Finance.initialize()

        # Set window title and size
        self.setWindowTitle("Personal Finance Tracker")
        self.setFixedSize(600, 500)

        # Set the background color and font
        self.setStyleSheet("""
            background-color: #f1f1f1;
            font-family: 'Arial', sans-serif;
            color: #333333;
        """)

        # Create the layout
        self.layout = QVBoxLayout()

        # Title Label
        title_label = QLabel("Personal Finance Tracker")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #4CAF50; margin-bottom: 20px;")
        self.layout.addWidget(title_label)

        # Transaction Form
        self.form_layout = QFormLayout()

        self.date_input = QLineEdit(self)
        self.date_input.setPlaceholderText("DD-MM-YYYY")
        self.date_input.setStyleSheet("background-color: #e0e0e0; color: #333333; padding: 10px; border-radius: 5px;")
        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText("Amount")
        self.amount_input.setStyleSheet("background-color: #e0e0e0; color: #333333; padding: 10px; border-radius: 5px;")
        self.category_input = QComboBox(self)
        self.category_input.addItems(["Income", "Expense", "Investment"])
        self.category_input.setStyleSheet("background-color: #e0e0e0; color: #333333; padding: 10px; border-radius: 5px;")
        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText("Description")
        self.description_input.setStyleSheet("background-color: #e0e0e0; color: #333333; padding: 10px; border-radius: 5px;")

        # Add inputs to form layout
        self.form_layout.addRow("Date:", self.date_input)
        self.form_layout.addRow("Amount:", self.amount_input)
        self.form_layout.addRow("Category:", self.category_input)
        self.form_layout.addRow("Description:", self.description_input)

        self.layout.addLayout(self.form_layout)

        # Buttons for Add, View, and Plot Transactions
        self.buttons_layout = QHBoxLayout()
        
        self.add_button = QPushButton("Add Transaction", self)
        self.add_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-size: 16px;
            margin: 10px;
        """)
        self.add_button.clicked.connect(self.add_transaction)

        self.view_button = QPushButton("View Transactions", self)
        self.view_button.setStyleSheet("""
            background-color: #2196F3;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-size: 16px;
            margin: 10px;
        """)
        self.view_button.clicked.connect(self.view_transactions)

        self.plot_button = QPushButton("Plot Transactions", self)
        self.plot_button.setStyleSheet("""
            background-color: #FF9800;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-size: 16px;
            margin: 10px;
        """)
        self.plot_button.clicked.connect(self.plot_transactions)

        self.buttons_layout.addWidget(self.add_button)
        self.buttons_layout.addWidget(self.view_button)
        self.buttons_layout.addWidget(self.plot_button)

        self.layout.addLayout(self.buttons_layout)

        # Table to display transactions
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(COLUMNS)
        self.table.setStyleSheet("""
            QTableWidget {
                border: none;
                font-size: 14px;
                background-color: #ffffff;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
            }
        """)
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

    def add_transaction(self):
        date = self.date_input.text()
        amount = self.amount_input.text()
        category = self.category_input.currentText()
        description = self.description_input.text()

        # Validate inputs
        if not date or not amount or not category or not description:
            return

        # Add transaction to file
        Finance.add_transaction(date, amount, category, description)

        # Clear inputs after submission
        self.date_input.clear()
        self.amount_input.clear()
        self.category_input.setCurrentIndex(0)
        self.description_input.clear()

    def view_transactions(self):
        # Get date range from user input
        start_date, ok_start = QInputDialog.getText(self, "Start Date", "Enter start date (DD-MM-YYYY):")
        if not ok_start:
            return
        end_date, ok_end = QInputDialog.getText(self, "End Date", "Enter end date (DD-MM-YYYY):")
        if not ok_end:
            return

        # Get transactions in the given range
        transactions = Finance.get_transactions(start_date, end_date)
        if transactions.empty:
            return
        
        # Display transactions in table
        self.table.setRowCount(len(transactions))
        for i, row in transactions.iterrows():
            self.table.setItem(i, 0, QTableWidgetItem(row["Date"].strftime(FORMAT)))
            self.table.setItem(i, 1, QTableWidgetItem(str(row["Amount"])))
            self.table.setItem(i, 2, QTableWidgetItem(row["Category"]))
            self.table.setItem(i, 3, QTableWidgetItem(row["Description"]))

    def plot_transactions(self):
        # Get date range from user input
        start_date, ok_start = QInputDialog.getText(self, "Start Date", "Enter start date (DD-MM-YYYY):")
        if not ok_start:
            return
        end_date, ok_end = QInputDialog.getText(self, "End Date", "Enter end date (DD-MM-YYYY):")
        if not ok_end:
            return

        # Plot the transactions for the date range
        Finance.plot_transactions(start_date, end_date)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FinanceTrackerApp()
    window.show()
    sys.exit(app.exec_())