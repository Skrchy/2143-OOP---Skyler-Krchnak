# Part A: Conceptual Questions

## Definition

### What is abstraction in OOP?
Abstraction is the concept of hiding complex implementation details and showing only the essential features of an object, allowing users to interact with it at a higher level.

### Provide a short real-world analogy illustrating how abstraction hides unnecessary details.
A **TV remote** is a good analogy—users can control the TV without needing to understand how the internal circuitry works. They only need to know which buttons to press to perform actions.

## Abstraction vs. Encapsulation

### Briefly compare abstraction and encapsulation.
- **Abstraction** focuses on hiding unnecessary details and exposing only relevant information to the user.
- **Encapsulation** is about bundling data and methods that operate on that data within a single unit or class and restricting direct access to the data.

### Why might someone confuse the two concepts?
Both abstraction and encapsulation aim to reduce complexity, but abstraction hides implementation details, while encapsulation hides data and restricts access to it. The concepts are often used together, which can lead to confusion.

## Designing with Abstraction

### Imagine you are modeling a smart thermostat in a home automation system. 
- **Attributes**: `currentTemperature`, `targetTemperature`, `mode`
- **Methods**: `setTemperature()`, `adjustMode()`

### Explain why you would omit certain internal details (e.g., circuit design, firmware routines).
Internal details like circuit design or firmware routines are not necessary for the user to interact with the thermostat. Focusing on user-facing features (like temperature control and mode adjustment) keeps the design simple and relevant.

## Benefits of Abstraction

### Name two benefits of abstraction in large-scale software projects.
1. **Improved maintainability**: Changes to implementation don’t affect the user interface.
2. **Easier debugging and testing**: By focusing on essential features, abstraction helps isolate problems.

### In a short sentence, how can abstraction reduce code complexity?
Abstraction reduces complexity by hiding implementation details and exposing only the necessary components for user interaction.

# Part B: Minimal Class Example (Pseudo-code)

### Scenario: Model a Banking System

```cpp
#include <iostream>
#include <string>
using namespace std;

// Abstract base class for BankAccount
class BankAccount {
public:
    virtual void deposit(double amount) = 0; // Deposit method
    virtual void withdraw(double amount) = 0; // Withdraw method
    virtual double getBalance() = 0; // Get balance method
    virtual ~BankAccount() {} // Virtual destructor
};

// Derived class for SavingsAccount
class SavingsAccount : public BankAccount {
private:
    double balance;
public:
    SavingsAccount() : balance(0) {}

    void deposit(double amount) override {
        balance += amount;
        // Internal operations like logging and encryption are hidden
    }

    void withdraw(double amount) override {
        if (balance >= amount) {
            balance -= amount;
        } else {
            cout << "Insufficient balance!" << endl;
        }
    }

    double getBalance() override {
        return balance;
    }
};

int main() {
    BankAccount* account = new SavingsAccount();
    account->deposit(1000);
    account->withdraw(200);
    cout << "Balance: $" << account->getBalance() << endl;

    delete account;
    return 0;
}
```

#### Explanation
In this example, the BankAccount class serves as an abstract base class, defining the core interface methods like deposit(), withdraw(), and getBalance(). The SavingsAccount class implements these methods while hiding internal details such as logging, encryption, or ledger balancing. The user interacts with the BankAccount interface and doesn’t need to know about the underlying complexities.
