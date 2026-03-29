import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"
 
#initialize csv file 

def initialize_file():
    if not os.path.exists(FILE_NAME):
       with open(FILE_NAME, mode="w", newline="")as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Date"])
            

#add expense

def add_expense():
    try:
         amount = float(input("Enter amount: "))
    except ValueError:
         print("Invalid amount! please enter a number")
         return

    category = input("Enter category: ").capitalize()
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, mode="a", newline="")as file:
         writer = csv.writer(file)
         writer.writerow([amount, category, date])

    print("Expense added successfully!")

    #view expenses

def view_expenses():
     with open(FILE_NAME, mode="r") as file:
          reader = csv.DictReader(file)
          print("\n--------All Expenses-------")
          for row in reader:
               print(f"Amount: {row['Amount']}")
               print(f"Category: {row['Category']}")
               print(f"Date: {row['Date']}")
               print("--------------------")

#total spending
def total_spending():
     total = 0
     with open(FILE_NAME, mode="r") as file:
          reader = csv.DictReader(file)
          for row in reader:
               total += float(row["Amount"])
     
     print(f"\n total spending: {total}")


#Category summary

def category_summary():
     categories = {}

     with open(FILE_NAME, mode="r") as file:
          reader = csv.DictReader(file)
          for row in reader:
               category = row["Category"]
               amount = float(row["Amount"])
               categories[category] = categories.get(category, 0) + amount
     
     print("\n--- category summary---")
     for category, total in categories.items():
          print(f"{category}: {total}")


#monthly summary

def monthly_summary():
     month = input("Enter month (YYYY-MM): ")

     total = 0
     with open(FILE_NAME, mode="r") as file:
          reader = csv.DictReader(file)
          for row in reader:
               if row["Date"].startswith(month):
                    total += float(row["Amount"])

     print(f"Total spending for {month}: {total}")


#menu system

def menu():
     initialize_file()

     while True:
          print("\n==== SmartExpenses =====")
          print("1. Add Expense")
          print("2. View Expense")
          print("3. Total Spending")
          print("4. Category Summary")
          print("5. Monthly Summary")
          print("6. Exit")

          choice = input("Choose option: ")

          if choice == "1":
               add_expense()
          elif choice == "2":
               view_expenses()
          elif choice == "3":
               total_spending()
          elif choice == "4":
               category_summary()
          elif choice == "5":
               monthly_summary()
          elif choice == "6":
               print("Goodbye!")
               break
          else:
               print("Invalid Choice")
               
menu()







