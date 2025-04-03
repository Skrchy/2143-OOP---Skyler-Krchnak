### Encapsulation:
Encapsulation is an OOP principle where data and methods are bundled together within a class. It restricts direct access to internal data, providing controlled access through getters and setters. This helps prevent unintended changes and keeps data safe.

---

### Visibility Modifiers:
- **Public**: 
  - **Benefit**: Accessible from anywhere.
  - **Drawback**: Increases risk of unintended modifications.

- **Private**:
  - **Benefit**: Protects data from external access.
  - **Drawback**: Limits flexibility for external interactions.

- **Protected**:
  - **Benefit**: Accessible by the class and its subclasses.
  - **Drawback**: Can lead to misuse in subclasses.

---

### When to Use Protected:
Use protected when you want subclasses to access or modify internal data but prevent external classes from doing so. For example, a subclass may need to use or extend a base class's functionality.

---

### Impact on Maintenance:
Encapsulation reduces debugging complexity by isolating functionality and making it easier to change internal implementation without affecting other parts of the code.

**Example**: If a list inside a class were public, external code could modify it inappropriately, causing bugs. Encapsulation ensures controlled access to avoid this.

---

### Real-World Analogy:
Think of a car: the **public interface** includes the steering wheel and pedals, which you use to drive. The **private implementation** includes the engine and other parts you don't see or interact with. Keeping the private parts hidden ensures safety and proper function.

# Part B: Small-Class Design (Minimal Coding)

## Class Skeleton

### BankAccount Class (C++)

class BankAccount {
private:
    double balance;       // Private data member: Account balance
    int accountNumber;    // Private data member: Account number

public:
    // Constructor to initialize the account
    BankAccount(int accNum, double initialBalance) : accountNumber(accNum), balance(initialBalance) {}

    // Public method to deposit money
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;  // Increase balance only if the amount is positive
        }
    }

    // Public method to withdraw money
    bool withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;  // Decrease balance if the amount is positive and less than or equal to current balance
            return true;
        }
        return false;
    }

    // Public method to check balance
    double getBalance() const {
        return balance;  // Return the current balance
    }
};



#### Part C: Reflection & Short-Answer

## Pros and Cons

### Benefits of Hiding Internal Data Behind Methods
1. **Data Integrity**: Ensures data is only modified in controlled ways, preventing invalid changes.
2. **Flexibility**: Allows changes to internal implementation without affecting external code.

### Potential Limitation or Overhead
- **Performance Overhead**: Extra function calls and validations can introduce a small performance cost.

---

## Encapsulation vs. Other Concepts

### Encapsulation vs. Abstraction
- **Encapsulation** hides data and ensures it's only accessed or modified via methods.
- **Abstraction** hides complexity and exposes only essential functionality.
  
Encapsulation focuses on how data is managed, while abstraction simplifies interaction by hiding implementation details.

### Information Hiding in Encapsulation & Abstraction
Both encapsulation and abstraction hide internal details:
- **Encapsulation** protects data access.
- **Abstraction** simplifies interaction with complex systems.

---

## Testing Encapsulated Classes

### Testing Strategy
1. **Public Getter Methods**: Use getters to verify the internal state.
2. **Unit Tests for Public Methods**: Test methods like `deposit()` and `withdraw()` to ensure correct behavior.
3. **Friend Classes/Mocking**: Use friend classes or mocks to access private members for testing when needed.
