#include <iostream>
#include <string>

class BankAccount {
private:
    double balance;
    std::string accountNumber;
    static int accountCount;
protected:
    bool validateWithdrawal(double amount) const {
        return (amount <= balance);
    }

public:
    BankAccount(const std::string& accountNumber, double initialBalance)
        : accountNumber(accountNumber), balance(initialBalance)
    {
        accountCount++;
    }

    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        } else {
            std::cout << "Nelze vlozit zapornou nebo nulovou castku!" << std::endl;
        }
    }

    void withdraw(double amount) {
        if (amount <= 0) {
            std::cout << "Castka pro vyber musi byt kladna!" << std::endl;
            return;
        }
        if (validateWithdrawal(amount)) {
            balance -= amount;
        } else {
            std::cout << "Nedostatek prostredku na uctu!" << std::endl;
        }
    }

    double getBalance() const {
        return balance;
    }

    static int getAccountCount() {
        return accountCount;
    }
};

int BankAccount::accountCount = 0;

int main() {
    BankAccount acc1("123456789", 1000.0);
    BankAccount acc2("987654321", 500.0);

    std::cout << "Celkovy pocet uctu: " << BankAccount::getAccountCount() << std::endl;

    acc1.deposit(200);
    acc1.deposit(-200);
    std::cout << "Zustatek acc1: " << acc1.getBalance() << std::endl;

    acc1.withdraw(1500);
    acc1.withdraw(300);
    std::cout << "Zustatek acc1 po vyberu: " << acc1.getBalance() << std::endl;

    acc2.withdraw(100);
    std::cout << "Zustatek acc2: " << acc2.getBalance() << std::endl;

    return 0;
}