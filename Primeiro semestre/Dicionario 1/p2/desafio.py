from collections import namedtuple
from dataclasses import dataclass

# Definição da Tupla Nomeada para Funcionários
Employee = namedtuple('Employee', ['id', 'name', 'department', 'salary'])

# Dicionário para armazenar os funcionários
employees_db = {}

# Classe de dados para representar um novo funcionário
@dataclass
class NewEmployee:
    name: str
    department: str
    salary: float

# Função para adicionar um novo funcionário ao banco de dados
def add_employee(emp_id: int, emp_data: NewEmployee):
    employees_db[emp_id] = Employee(emp_id, emp_data.name, emp_data.department, emp_data.salary) # Implemente esta função

# Função para exibir todos os funcionários
def display_employees():
    return employees_db.items()  # Implemente esta função

# Função para buscar um funcionário por ID
def find_employee(emp_id: int):
    return employees_db.get(emp_id, None) # Implemente esta função

# Função para calcular a folha de pagamento total da empresa
def calculate_payroll():
    pagamento = sum([entry.salary for entry in employees_db.values()])
    print(f"Folha de pagamento total: {pagamento}")# Implemente esta função

# Função principal
def main():
    while True:
        print("\n1. Adicionar Funcionário")
        print("2. Exibir Funcionários")
        print("3. Buscar Funcionário por ID")
        print("4. Calcular Folha de Pagamento")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            # Adicionar Funcionário
            emp_id = int(input("ID do funcionário: "))
            name = input("Nome do funcionário: ")
            department = input("Departamento do funcionário: ")
            salary = float(input("Salário do funcionário: "))

            new_employ_data = NewEmployee(name=name, department=department, salary=salary)
            add_employee(emp_id, new_employ_data) #concluir implementação...

        elif choice == '2':
            # Exibir Funcionários
            print(display_employees())
        elif choice == '3':
            # Buscar Funcionário por ID
            emp_id = int(input("ID do funcionário a ser buscado: "))
            print(find_employee(emp_id))
            
        elif choice == '4':
            # Calcular Folha de Pagamento
            calculate_payroll()
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__": main()