expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

def add_expense_interactively(expenses):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    new_expense = {'tanggal': date, 'deskripsi': description, 'jumlah': amount}
    expenses.append(new_expense)
    print("Pengeluaran berhasil ditambahkan.")
    return expenses

def get_expenses_by_date(expenses, date):
    expenses_date =[expense for expense in expenses if expense['tanggal'] == date]
    return expenses_date

def calculate_total_expenses(expenses):
    total = sum(expense['jumlah'] for expense in expenses)
    return total

def generate_expenses_report(expenses):
    report = []
    for expense in expenses:
        report.append(f"{expense['tanggal']} - {expense['deskripsi']} - Rp {expense['jumlah']}")
    return report

def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")

get_user_input = lambda command : int(input(command))

def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            date = input("Masukkan tanggal (YYYY-MM-DD): ")
            expenses_on_date = get_expenses_by_date(expenses, date)
            print(f"\nPengeluaran pada tanggal {date}:")
            for expense in expenses_on_date:
                print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")
        elif choice == 4:
            expenses_report = generate_expenses_report(expenses)
            print("\nLaporan Pengeluaran Harian:")
            for entry in expenses_report:
                print(entry)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")

if __name__ == "__main__":
    main()
