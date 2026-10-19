# ==========================================
# 1. INHERITANCE & POLIMORFISME
# ==========================================

class Employee:
    """Base Class (Kelas Induk)"""
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    # Polimorfisme: Method ini akan di-override oleh kelas turunan
    def get_role_description(self):
        return f"{self.name} is a general employee."

    def work(self):
        return f"{self.name} is doing general tasks."


class Developer(Employee):
    """Sub-class 1"""
    def get_role_description(self):
        return f"{self.name} is a Software Developer."

    def work(self):
        return f"{self.name} is writing code and fixing bugs."


class Manager(Employee):
    """Sub-class 2"""
    def get_role_description(self):
        return f"{self.name} is a Project Manager."

    def work(self):
        return f"{self.name} is managing the team and planning sprints."


class Designer(Employee):
    """Sub-class 3"""
    def get_role_description(self):
        return f"{self.name} is a UI/UX Designer."

    def work(self):
        return f"{self.name} is designing wireframes and prototypes."


# ==========================================
# 2. MULTI-CLASS (Interaksi antar kelas)
# ==========================================

class HRSystem:
    """Kelas kedua yang berinteraksi dengan kelas Employee"""
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    # Menggunakan if/elif untuk mengecek tipe kelas
    def process_payroll(self):
        print("\n--- Processing Payroll ---")
        for emp in self.employees:
            if isinstance(emp, Developer):
                bonus = emp.base_salary * 0.10
            elif isinstance(emp, Manager):
                bonus = emp.base_salary * 0.25
            elif isinstance(emp, Designer):
                bonus = emp.base_salary * 0.15
            else:
                bonus = 0

            total = emp.base_salary + bonus
            print(f"Paying {emp.name}: Base ${emp.base_salary} + Bonus ${bonus} = Total ${total}")

    # Kelas ini mengurus logika bisnis, cetak laporan, DAN simulasi database
    def generate_report(self):
        print("\n--- Generating Employee Report ---")
        for emp in self.employees:
            # Di sini kita menggunakan POLIMORFISME dengan benar
            print(f"- {emp.get_role_description()} | Task: {emp.work()}")

        print("Report generated and printed to console.")

    def save_to_database(self):
        print("\n--- Saving to Database ---")
        # Simulasi menyimpan ke database
        print(f"Saved {len(self.employees)} employees to SQL Database.")
        print("Database connection closed.")


# ==========================================
# 3. EKSEKUSI PROGRAM
# ==========================================
if __name__ == "__main__":
    # Inisialisasi HR System (Multi-class)
    hr_system = HRSystem()

    # Membuat objek dari berbagai kelas turunan (Inheritance)
    dev = Developer("Budi", 8000)
    mgr = Manager("Siti", 12000)
    des = Designer("Joko", 7000)

    # Menambahkan ke sistem
    hr_system.add_employee(dev)
    hr_system.add_employee(mgr)
    hr_system.add_employee(des)

    # Memanggil method
    hr_system.process_payroll()
    hr_system.generate_report()
    hr_system.save_to_database()
