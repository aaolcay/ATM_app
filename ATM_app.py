# /*
#  * Copyright (C) 2020  Abdullah Azzam Olcay
#  * Gebze Technical University
#  * Lınkedin: https://tr.linkedin.com/in/abdullah-azzam-olcay-613453183
#  *
#  *
#  * ATM App
#  *
#  *
#  * Please do not remove this header.
#  * */
import os
import time

class Client():
    def __init__(self,ID,Password,Name):
        self.id = ID
        self.password = Password
        self.name = Name
        self.arrear = 0


class Bank():
    def __init__(self):
        self.clients = list() # Müşterileri boş bir list'e atadık

    def be_client(self,ID:str,Password:str,Name:str):
        self.clients.append(Client(ID,Password,Name)) # Müşteri classının içindekileri müşteriler için oluşturulan listeye ekliyoruz




def document_update(client):
    document = open("ATM.txt","a+")
    string = "Client's ID number:{} ----> name:{} ----> arrear:{}".format(client.id, client.name,client.arrear)+"\n"
    document.write(string)
    document.close()

def main():
    bank = Bank() # Classı bank a atadık

    while True:
        os.system("clear")

        print("""
        [1] I'm a client
        [2] Log in """)
        selection = input("Select what you want:\n")
        if selection == "1":
            Ids = [i.id for i in bank.clients] # ***** Önemli
            # bank.clients içerisindeki bilgileri i'ye atayıp
            # i içerisinden id sini çekiyoruz

            # Yukarıda yapılan işlem aslında şudur:
            ### for i in bank.clients:
            ### ids += [i.id]
            # anlamına gelmektedir.

            ID = input("Enter your ID:\n")
            if ID in Ids:
                for client in bank.clients:
                    document_update(client)
                    if ID == client.id:
                        psw = input("Enter your password:\n")
                        print("Welcome {}".format(client.name))

                        if psw == client.password:
                            print("Please wait a second...\n")
                            print("You are directed to the menu.\n")
                            time.sleep(1)
                            while True:
                                print("""
                                [1] Value in your account
                                [2] Deposit money into your account
                                [3] Money transfer
                                [4] Withdraw
                                [Q] Quit""")
                                selection_2 = input("Select what you want in your account:\n")
                                if selection_2 == "1":
                                    print("The value is {}".format(client.arrear))
                                    input("Press enter for going main menu")

                                elif selection_2 == "2":
                                    print("You have {} in your account\n".format(client.arrear))
                                    addition = float(input("How much money do you want to add to your account?\nEnter value:\n"))
                                    confirm = input("Do you confirm this {} value?Y/N:\n".format(addition))
                                    if confirm == "Y" or confirm == "y":
                                        client.arrear += addition
                                        print("Operation is succesful")
                                        input("Press enter for going main menu")
                                    elif confirm == "N" or confirm == "n":
                                        print("The banking is cancelled")
                                        input("Press enter for going main menu")
                                    else:
                                        print("Your selection is not correct.The operation is cancelled\n")
                                        input("Press enter for going main menu")

                                elif selection_2 == "3":
                                    transfer_to_id = input("Enter the ID of account for transfering:\n")
                                    if transfer_to_id in Ids:
                                        for other_client in bank.clients:
                                            if transfer_to_id == other_client.id:
                                                addition = float(input("How much money do you want to transfer?\nEnter value:\n"))
                                                if addition <= client.arrear:
                                                    confirm = input("Do you want to transfer this {} TL to {}\nY/N:\n".format(addition,other_client.name))
                                                    if confirm == "Y" or confirm == "y":
                                                        other_client.arrear += addition
                                                        client.arrear -= addition
                                                        print("The transfer is succesful\n")
                                                        input("Press enter for going main menu")
                                                    elif confirm == "N" or confirm == "n":
                                                        print("The operation is cancelled\n")
                                                        input("Press enter for going main menu")
                                                    else:
                                                        print("Your selection is not correct.The operation is cancelled\n")
                                                        input("Press enter for going main menu")
                                                else:
                                                    print("Your arrear is not enough for this operation.\n")
                                    else:
                                        print("The ID you entered is not found.")
                                        input("Press enter for going main menu")

                                elif selection_2 == "4":
                                    withdraw = float(input("Enter the value of withdrawing:\n"))
                                    if withdraw <= client.arrear:
                                        client.arrear -= withdraw
                                        print("The operation is success")
                                        input("Press enter for going main menu")
                                    else:
                                        print("Your arrear is not enough for this operation.\n")
                                        input("Press enter for going main menu")
                                elif selection_2 == "Q" or selection_2 == "q":
                                    print("Wait for a second, go to main menu..")
                                    time.sleep(1)
                                    break # I want to just quit this if, elif loop. Due to the fact that I write this break on this line
                                          # for this cause. Owing to break, we can go to main menu
                                else:
                                    print("Your selection is absent in the menu, please wait for a second...")
                                    time.sleep(1)
                                    input("Press enter for going main menu")


        elif selection == "2":
            ID = str(input("Enter your ID:\n"))
            Password = str(input("Enter your password:\n"))
            Name = str(input("Enter your name:\n"))
            bank.be_client(ID,Password,Name)




# sadece bu Python dosyasını çalıştırırsak main olarak bu kod çalışır. Eğer farklı bir dosyada çalıştırırsak
# else ile belirtilen kısım döner mesela burada klasörün adını yani bank_app_with_class yazdırılır
# (else de belirtildiği için)

if __name__ == "__main__":
    main()

else:
    print(__name__) # Eğer farklı bir dosya da import edip çağırırsak dosya ismini yazdırır
