# import json


# class Airline_Manager:
#     def __init__(self):
#         """
#         This init function will load the data of both lists for code functionality.
#         """
#         self.customer_details_filename = "Airline Management Project\\Database\\customer_detail.txt"
#         self.customer_details = []
#         self.ticket_details_filename = "Airline Management Project\\Database\\ticket_details.txt"
#         self.ticket_details = []

#         try:  # Check for the file availability of customer_details
#             with open(self.customer_details_filename, 'r') as f:
#                 self.customer_details = json.load(f)
#         except (FileNotFoundError, json.JSONDecodeError):
#             self.customer_details = []

#         try:  # Check for the file availability of ticket_details
#             with open(self.ticket_details_filename, 'r') as f:
#                 self.ticket_details = json.load(f)
#         except (FileNotFoundError, json.JSONDecodeError):
#             self.ticket_details = []

#     def save_customer_details(self):
#         """
#         This function will save the details of the list customer_details in the file named customer_detail.txt
#         """
#         with open(self.customer_details_filename, 'w') as f:
#             json.dump(self.customer_details, f, indent=4)

#     def save_ticket_details(self):
#         """
#         This function will save the details of the list ticket_details in the file named ticket_details.txt
#         """
#         with open(self.ticket_details_filename, 'w') as f:
#             json.dump(self.ticket_details, f, indent=4)

#     def add_customer_details(self):
#         while True:
#             try:
#                 print("Please Enter Your Personal Information!")
#                 name = input("Please Enter Your Name: ")
#                 gender = input("Please Enter Your Gender (M/F/O): ")
#                 phone = int(input("Please Enter Your Phone Number: "))
#                 email = input("Please Enter Your Email Address: ")
#                 nationality = input("Please Enter Your Nationality: ")
#                 dob = input("Please Enter Your Date Of Birth (DD/MM/YYYY): ")
#                 print("Now Please Enter Your Passport Information!")
#                 passport_number = input("Please Enter Your Passport Number: ")
#                 coi = input("Please Enter The Country Of Issue Of The Passport: ")
#                 exp_date = input("Please Enter The Expiry Date Of Your Passport (MM/YY): ")
#                 self.customer_details.append({"Personal_Info": {"Name": name,
#                                                                "Gender": gender,
#                                                                "Phone": phone,
#                                                                "Email": email,
#                                                                "Nationality": nationality,
#                                                                "DOB": dob},
#                                               "Passport_Info": {"Passport Number": passport_number,
#                                                                 "Country Of Origin": coi,
#                                                                 "Expiry Date": exp_date}})
#                 self.save_customer_details()

#                 print(f"The Details For the Person {name} Saved In The Airport Records!")
#                 another_person = input("Do you want to enter another detail (yes/no): ").lower()
#                 if another_person not in ["yes", "y"]:
#                     print("Registered User Data In The Records!")
#                     print("Loading Menu!")
#                     break
#             except ValueError as e:
#                 print(f"Error: {e}. Please Input Correct Format For Each Field.")

#     def add_ticket_details(self):
#         while True:
#             try:
#                 print("Please Enter Your Flight Information!")
#                 name = input("Please Enter Your Name: ")
#                 departure = input("Please Enter Your City Of Departure/Airport: ")
#                 destination = input("Please Enter Your Destination City/Airport: ")
#                 departure_date = input("Please Enter The Date Of Departure (DD/MM/YYYY): ")
#                 roundtrip = input("Is It a Round Trip? (Yes/No): ").lower()
#                 return_date = ""
#                 if roundtrip in ["yes", "y"]:
#                     return_date = input("Please Enter Return Date (DD/MM/YYYY): ")
#                 class_of_service = input("Please Enter The Class Of Service (Economy, Business, First Class): ")
#                 number_of_passengers_adults = input("Please Enter The Number Of Adult Passengers: ")
#                 number_of_passengers_children = input("Please Enter The Number Of Children Passengers: ")
#                 number_of_passengers_infant = input("Please Enter The Number Of Infant Passengers: ")
#                 print("Please Enter Your Payment Information!")
#                 payment_method = input("Please Enter The Method Of Payment (Credit/Debit Card, Paytm, Bank Transfer): ")
#                 card_number = expiry = cvv = ""
#                 if payment_method.lower() in ["credit card", "debit card", "credit", "debit"]:
#                     card_number = input("Please Enter Your Card Number: ")
#                     expiry = input("Please Enter Your Card Expiry Date (MM/YY): ")
#                     cvv = input("Please Enter Your CVV: ")
#                 billing_address = input("Please Enter Your Billing Address: ")
#                 special = input("Please Enter Special Requests (If Any or Type None): ")
#                 seat_preference = input("Please Enter Your Seat Preference (Aisle, Window, Middle): ")
#                 print("Please Enter Your Emergency Contact Information!")
#                 ecn = input("Please Enter Emergency Contact Name: ")
#                 ecr = input("Please Enter Emergency Contact Relationship: ")
#                 ecpn = input("Please Enter Emergency Contact Phone Number: ")
#                 ecea = input("Please Enter Emergency Contact Email Address: ")

#                 self.ticket_details.append({"Flight Information": {"Name": name,
#                                                                    "Departure-City": departure,
#                                                                    "Destination-City": destination,
#                                                                    "Departure-Date": departure_date,
#                                                                    "Return-Date": return_date,
#                                                                    "Class-Of-Service": class_of_service,
#                                                                    "Number-Of-Passengers": {
#                                                                        "Adults": number_of_passengers_adults,
#                                                                        "Children": number_of_passengers_children,
#                                                                        "Infants": number_of_passengers_infant}},
#                                             "Payment-Info": {"Payment-Method": payment_method,
#                                                              "Card-Info": {
#                                                                  "Card-Number": card_number,
#                                                                  "Expiry-Date": expiry,
#                                                                  "CVV": cvv},
#                                                              "Billing-Address": billing_address},
#                                             "Additional-Information": {"Special-Requests": special,
#                                                                        "Seat-Preference": seat_preference},
#                                             "Emergency Information": {"Emergency-Contact-Name": ecn,
#                                                                       "Emergency-Contact-Relationship": ecr,
#                                                                       "Emergency-Contact-Phone-Number": ecpn,
#                                                                       "Emergency-Contact-Email-Address": ecea}})
#                 self.save_ticket_details()
#                 print(f"The Ticket Details For The Person {name} Saved In The Airport Records!")
#                 print("Loading Menu!")

#                 another_person = input("Do You Want To Add Another Person's Details (Yes/No): ").lower()
#                 if another_person not in ["yes", "y"]:
#                     print("Registered Data In The Airport Records!")
#                     print("Loading Menu!")
#                     break

#             except ValueError as e:
#                 print(f"Error: {e}. Please Input Correct Format For Each Field.")

#     def remove_customer_info(self):
#         while True:
#             try:
#                 num = int(input("Enter The Number Of Customer Details You Want To Remove: "))
#                 if num > len(self.customer_details):
#                     raise ValueError(f"Invalid Number Of Query: There Are Only {len(self.customer_details)} Customer Details Present In The Airport Record!")
#                 for _ in range(num):
#                     name = input("Please Enter The Name Of The Customer To Remove Details: ")
#                     for info in self.customer_details:
#                         if info["Personal_Info"]["Name"].lower() == name.lower():
#                             self.customer_details.remove(info)
#                             self.save_customer_details()
#                             print(f"The Customer Details Of The Person {name} Are Deleted From The Airport Records!")
#                             print("Loading Menu!")
#                             break
#             except ValueError as e:
#                 print(e)

#     def remove_ticket_details(self):
#         while True:
#             try:
#                 name = input("Please Enter The Name Of The Customer To Remove Booking Details: ")
#                 found = False
#                 for info in self.ticket_details:
#                     if info["Flight Information"]["Name"].lower() == name.lower():
#                         self.ticket_details.remove(info)
#                         self.save_ticket_details()
#                         print(f"The Booking Details Of The Person {name} Are Deleted From The Airport Records!")
#                         print("Loading Menu!")
#                         found = True
#                         break
#                 if not found:
#                     print(f"No Ticket Details Found For The Name: {name}")
#                     print("Loading Menu!")

#                 another_ticket_details = input("Do You Want To Remove Another Ticket Detail (Yes/No): ").lower()
#                 if another_ticket_details not in ["yes", "y"]:
#                     print("Loading Menu!")
#                     break

#             except ValueError as e:
#                 print(e)

#     def show_personal_info_of_customers(self):
#         if self.customer_details:
#             print("| NAME | GENDER | EMAIL | PHONE-NUMBER | DATE-OF-BIRTH | NATIONALITY | PASSPORT-NUMBER |")
#             for info in self.customer_details:
#                 print(f'| {info["Personal_Info"]["Name"]} | {info["Personal_Info"]["Gender"]} | {info["Personal_Info"]["Email"]} | {info["Personal_Info"]["Phone"]} | {info["Personal_Info"]["DOB"]} | {info["Personal_Info"]["Nationality"]} | {info["Passport_Info"]["Passport Number"]} |')
#             print("Loading Menu!")
#         else:
#             print("No Personal Details Are Present In The Airports Records!")
#             print("Loading Menu!")

#     def show_ticket_details_specific_persons(self):
#         name = input("Please Enter The Name Of The Customer To Show Ticket Details: ")
#         found = False
#         for info in self.ticket_details:
#             if info["Flight Information"]["Name"].lower() == name.lower():
#                 # Use .get to safely access dictionary keys and provide default values
#                 num_adults = info["Flight Information"]["Number-Of-Passengers"].get("Adults", "N/A")
#                 num_children = info["Flight Information"]["Number-Of-Passengers"].get("Children", "N/A")
#                 num_infants = info["Flight Information"]["Number-Of-Passengers"].get("Infants", "N/A")
#                 payment_method = info["Payment-Info"].get("Payment-Method", "N/A")
#                 billing_address = info["Payment-Info"].get("Billing-Address", "N/A")
#                 special_requests = info["Additional-Information"].get("Special-Requests", "N/A")
#                 seat_preference = info["Additional-Information"].get("Seat-Preference", "N/A")
#                 return_date = info["Flight Information"].get("Return-Date", "N/A")

#                 print("| NAME | DEPARTURE-CITY | DESTINATION-CITY | DEPARTURE-DATE | RETURN-DATE | CLASS-OF-SERVICE | ADULTS | CHILDREN | INFANTS | PAYMENT-METHOD | BILLING-ADDRESS | SPECIAL-REQUESTS | SEAT-PREFERENCE |")
#                 print(f'| {info["Flight Information"]["Name"]} | {info["Flight Information"]["Departure-City"]} | {info["Flight Information"]["Destination-City"]} | {info["Flight Information"]["Departure-Date"]} | {return_date} | {info["Flight Information"]["Class-Of-Service"]} | {num_adults} | {num_children} | {num_infants} | {payment_method} | {billing_address} | {special_requests} | {seat_preference} |')
#                 print("Loading Menu!")
#                 found = True
#                 break
#         if not found:
#             print(f"No Details Found For The Name: {name}")
#             print("Loading Menu!")

#     def about(self):
#         print(
#         """
#         Welcome to the Airline Management System!

#         This system allows you to manage customer and ticketing information efficiently. Here are the main features and how to use them:

#         1. Add Customer Information:
#             - Choose option (1) from the main menu.
#             - Enter the customer's name, gender, phone number, email address, nationality, date of birth, passport number, country of issue, and expiry date.
#             - The system will save these details for future reference.

#         2. Add Ticketing Information:
#             - Choose option (2) from the main menu.
#             - Ensure the customer details are already added.
#             - Enter the customer's name (must match the existing customer details).
#             - Provide flight details such as departure city, destination city, departure date, return date (if applicable), class of service, number of passengers (adults, children, infants), payment method, billing address, special requests, seat preference, and emergency contact information.
#             - The system will save the ticketing details linked to the customer.

#         3. Remove Specific Customer Information:
#             - Choose option (3) from the main menu.
#             - Enter the name of the customer to remove their personal details from the records.

#         4. Remove Specific Ticket Information:
#             - Choose option (4) from the main menu.
#             - Enter the name of the customer to remove their booking details from the records.

#         5. Display All Customer Information:
#             - Choose option (5) from the main menu.
#             - The system will display all the saved customer details.

#         6. Display Ticket Details Of A Specific Person:
#             - Choose option (6) from the main menu.
#             - Enter the name of the customer to view their ticket details.

#         7. About The Program:
#             - Choose option (7) from the main menu to view this help guide.

#         8. Quit:
#             - Choose option (8) from the main menu to exit the program.

#         Please follow the prompts on the screen to input the required information. If you need any assistance, refer back to this guide by selecting option (7) from the main menu.

#         Enjoy using the Airline Management System!
#                 """)
#         print("Loading Menu!")



# # Class Object Initialization
# air_manager = Airline_Manager()

# # Main Program
# def main():
#     while True:
#         print("__________________________________Airline Manager__________________________________")
#         print("Please Choose From The Options Below: ")
#         print("(1) Add Customer Information")
#         print("(2) Add Ticketing Information")
#         print("(3) Remove Specific Customer Information")
#         print("(4) Remove Specific Ticket Information")
#         print("(5) Display All Customer Information")
#         print("(6) Display Ticket Details Of A Specific Person")
#         print("(7) About The Program")
#         print("(8) Quit")
#         try:
#             choice = int(input("Please Enter The Number Of Choice You Want To Perform (In Number): "))
#             if choice == 1:
#                 air_manager.add_customer_details()
#             elif choice == 2:
#                 air_manager.add_ticket_details()
#             elif choice == 3:
#                 air_manager.remove_customer_info()
#             elif choice == 4:
#                 air_manager.remove_ticket_details()
#             elif choice == 5:
#                 air_manager.show_personal_info_of_customers()
#             elif choice == 6:
#                 air_manager.show_ticket_details_specific_persons()
#             elif choice == 7:
#                 air_manager.about()
#             elif choice == 8:
#                 print("Quitting Program...")
#                 break
#             else:
#                 print("Please Type The Given Numbers For Operation Of Code!")
#         except ValueError:
#             print("Invalid Value Format. Please Input Numeric Values!")


# if __name__ == "__main__":
#     main()




import sqlite3
from tabulate import tabulate

def create_tables():
    with sqlite3.connect('Airline Management Project\\Database\\airline_management.db') as db_connection:
        cursor = db_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS customer_details (
                            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            age INTEGER NOT NULL,
                            gender TEXT NOT NULL,
                            address TEXT NOT NULL,
                            phone TEXT NOT NULL
                        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS ticket_details (
                            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            customer_id INTEGER NOT NULL,
                            flight_number TEXT NOT NULL,
                            departure TEXT NOT NULL,
                            destination TEXT NOT NULL,
                            FOREIGN KEY (customer_id) REFERENCES customer_details (customer_id)
                        )''')
        db_connection.commit()

def add_customer(name, age, gender, address, phone):
    with sqlite3.connect('Airline Management Project\\Database\\airline_management.db') as db_connection:
        cursor = db_connection.cursor()
        cursor.execute('''INSERT INTO customer_details (name, age, gender, address, phone)
                          VALUES (?, ?, ?, ?, ?)''', (name, age, gender, address, phone))
        db_connection.commit()

def view_customers():
    with sqlite3.connect('Airline Management Project\\Database\\airline_management.db') as db_connection:
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM customer_details')
        customers = cursor.fetchall()
        headers = ["Customer ID", "Name", "Age", "Gender", "Address", "Phone"]
        return tabulate(customers, headers, tablefmt="grid")

def add_ticket(customer_id, flight_number, departure, destination):
    with sqlite3.connect('Airline Management Project\\Database\\airline_management.db') as db_connection:
        cursor = db_connection.cursor()
        cursor.execute('''INSERT INTO ticket_details (customer_id, flight_number, departure, destination)
                          VALUES (?, ?, ?, ?)''', (customer_id, flight_number, departure, destination))
        db_connection.commit()

def view_tickets():
    with sqlite3.connect('Airline Management Project\\Database\\airline_management.db') as db_connection:
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM ticket_details')
        tickets = cursor.fetchall()
        headers = ["Ticket ID", "Customer ID", "Flight Number", "Departure", "Destination"]
        return tabulate(tickets, headers, tablefmt="grid")

def delete_customer(customer_id):
    with sqlite3.connect('Airline Management Project\\Database\\airline_management.db') as db_connection:
        cursor = db_connection.cursor()
        cursor.execute('DELETE FROM customer_details WHERE customer_id = ?', (customer_id,))
        cursor.execute('DELETE FROM ticket_details WHERE customer_id = ?', (customer_id,))
        db_connection.commit()

def delete_ticket(ticket_id):
    with sqlite3.connect('Airline Management Project\\Database\\airline_management.db') as db_connection:
        cursor = db_connection.cursor()
        cursor.execute('DELETE FROM ticket_details WHERE ticket_id = ?', (ticket_id,))
        db_connection.commit()

if __name__ == "__main__":
    create_tables()

    while True:
        print("\nAirline Management System")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Add Ticket")
        print("4. View Tickets")
        print("5. Delete Customer")
        print("6. Delete Ticket")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            add_customer(name, age, gender, address, phone)
            print("Customer added successfully.")

        elif choice == "2":
            customers = view_customers()
            print("\nCustomers:")
            print(customers)

        elif choice == "3":
            customer_id = int(input("Enter customer ID: "))
            flight_number = input("Enter flight number: ")
            departure = input("Enter departure location: ")
            destination = input("Enter destination: ")
            add_ticket(customer_id, flight_number, departure, destination)
            print("Ticket added successfully.")

        elif choice == "4":
            tickets = view_tickets()
            print("\nTickets:")
            print(tickets)

        elif choice == "5":
            customer_id = int(input("Enter customer ID to delete: "))
            delete_customer(customer_id)
            print("Customer deleted successfully.")

        elif choice == "6":
            ticket_id = int(input("Enter ticket ID to delete: "))
            delete_ticket(ticket_id)
            print("Ticket deleted successfully.")

        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
