class Card:
    def __init__(self, owner, seria, balance, password):
        self.owner = owner
        self.seria = seria
        self.balance = balance
        self.password = password
        self.phone = ''

    def get_info(self):
        return f"""
    Egasi: {self.owner}
    Seria Raqami: {self.seria}
    Balance: {self.balance} so'm
    Parol: {self.password}
    Telefon Raqami: {self.phone if self.phone else 'Ulanmagan'}
    """

    def to_dict(self):
        return {
            "owner": self.owner,
            "seria": self.seria,
            "balance": self.balance,
            "password": self.password,
            "phone": self.phone
        }

class Atm:
    def __init__(self, bank_name):
        self.bank = bank_name
        self.cards = []

    def add_card(self, new_card):
        if not any(card.seria == new_card.seria for card in self.cards):
            self.cards.append(new_card)
            print(f"Karta {new_card.seria} muvaffaqiyatli qo'shildi.")
        else:
            print("Bunday karta allaqachon mavjud!")

    def find_card(self, seria, password):
        for card in self.cards:
            if card.seria == seria and card.password == password:
                return card
        return None

    def balance(self):
        seria = input("Karta raqamini kiriting: ")
        password = input("Parolni kiriting: ")
        card = self.find_card(seria, password)
        if card:
            print(f"Hisobingizda: {card.balance} so'm")
        else:
            print("Karta raqami yoki parol noto'g'ri!")

    def deposit(self):
        seria = input("Karta raqamini kiriting: ")
        password = input("Parolni kiriting: ")
        card = self.find_card(seria, password)
        if not card:
            print("Karta raqami yoki parol noto'g'ri!")
            return
        try:
            amount = int(input("Qoshmoqchi bolgan summangizni kiriting: "))
            if amount > 0:
                card.balance += amount
                print(f"{amount} so'm muvaffaqiyatli qo'shildi. Yangi balans: {card.balance} so'm")
            else:
                print("Summa musbat bo'lishi kerak!")
        except ValueError:
            print("Iltimos, faqat raqam kiriting!")

    def withdraw(self):
        seria = input("Karta raqamini kiriting: ")
        password = input("Parolni kiriting: ")
        card = self.find_card(seria, password)
        if not card:
            print("Karta raqami yoki parol noto'g'ri!")
            return
        try:
            amount = int(input("Yechmoqchi bo'lgan summangizni kiriting: "))
            if amount <= 0:
                print("Summa musbat bo'lishi kerak!")
            elif amount > card.balance:
                print("Hisobda yetarli mablag' yo'q!")
            else:
                card.balance -= amount
                print(f"{amount} so'm muvaffaqiyatli yechildi. Qoldiq: {card.balance} so'm")
        except ValueError:
            print("Iltimos, faqat raqam kiriting!")

    def link_phone(self):
        seria = input("Karta raqamini kiriting: ")
        password = input("Parolni kiriting: ")
        card = self.find_card(seria, password)
        if not card:
            print("Karta raqami yoki parol noto'g'ri!")
            return
        phone = input("Yangi telefon raqamini kiriting (+998...): ")
        card.phone = phone
        print("Telefon raqami muvaffaqiyatli ulandi!")

    def view_all_cards(self):
        if not self.cards:
            print("Hozircha hech qanday karta qo'shilmagan.")
        for card in self.cards:
            print(card.get_info())

    def show_menu(self):
        while True:
            print("\n" + "="*40)
            print(f"  {self.bank} BANK ATM")
            print("="*40)
            print("1. Balansni ko'rish")
            print("2. Pul qo'shish")
            print("3. Pul yechish")
            print("4. Telefon raqamini ulash")
            print("5. Barcha kartalarni ko'rish (admin)")
            print("6. Chiqish")
            print("-"*40)

            choice = input("Tanlovingizni kiriting (1-6): ")

            if choice == '1':
                self.balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.link_phone()
            elif choice == '5':
                self.view_all_cards()
            elif choice == '6':
                print("Xayr! ATMdan muvaffaqiyatli chiqdingiz.")
                break
            else:
                print("Noto'g'ri tanlov! Iltimos 1-6 gacha raqam kiriting.")


atm = Atm("MyBank")

card1 = Card("Ali Valiev", "8600123412345678", 500000, "1234")
card2 = Card("Vali Akbarov", "1234567890123456", 150000, "0000")

atm.add_card(card1)
atm.add_card(card2)

atm.show_menu()