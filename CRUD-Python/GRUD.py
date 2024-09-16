import mysql.connector
from mysql.connector import Error
from datetime import date

#Function to connect to MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='client_management',
            user='root', 
            password ='admin'       
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
        return connection
    except Error as e:
        print(f"Error al conectarse a MySQL: {e}")
        return None

    #create a new client
def create_client(connection, name, email, phone, address):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO clients (name, email, phone, address, registration_date) VALUES (%s, %s, %s, %s, %s)"
        data = (name, email, phone, address, date.today())
        cursor.execute(query, data)
        connection.commit()
        print(f"Cliente {name} creado exitosamente.")
    except Error as e:
        print(f"Error al crear el cliente: {e}")

    #read all customers
def read_clients(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM clients"
        cursor.execute(query)
        results = cursor.fetchall()
        print("List of clients:")
        for row in results:
            print(row)
    except Error as e:
        print(f"Error reading clients: {e}")

    #update a client
def update_client(connection, client_id, name, email, phone, address):
    try:
        cursor = connection.cursor()
        query = "UPDATE clients SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
        data = (name, email, phone, address, client_id)
        cursor.execute(query, data)
        connection.commit()
        print(f"Client {client_id} successfully updated.")
    except Error as e:
        print(f"Error updating client: {e}")

    # delete a customer
def delete_client(connection, client_id):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM clients WHERE id=%s"
        cursor.execute(query, (client_id,))
        connection.commit()
        print(f"Client {client_id} successfully removed.")
    except Error as e:
        print(f"Error deleting client: {e}")
# menu
def main():
    connection = create_connection()
    if connection:
        while True:
            print("\nCustomer Management System")
            print("1. Create client")
            print("2. Read clients")
            print("3. Update client")
            print("4. Delete client")
            print("5. Exit")
            
            choice = input("Select an option: ")
            
            if choice == '1':
                name = input("Customer name: ")
                email = input("Customer email: ")
                phone = input("Customer phone: ")
                address = input("Customer address: ")
                create_client(connection, name, email, phone, address)
                
            elif choice == '2':
                read_clients(connection)
                
            elif choice == '3':
                client_id = int(input("Client ID to update: "))
                name = input("New customer name: ")
                email = input("New customer email: ")
                phone = input("Customer's new phone: ")
                address = input("New customer address: ")
                update_client(connection, client_id, name, email, phone, address)
                
            elif choice == '4':
                client_id = int(input("Customer ID to delete: "))
                delete_client(connection, client_id)
                
            elif choice == '5':
                if connection.is_connected():
                    connection.close()
                print("Closed")
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    main()