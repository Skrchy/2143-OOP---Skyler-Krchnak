# Part A: Conceptual Questions

## Inheritance Definition

### What is Inheritance?
- **Inheritance** allows a class to inherit attributes and methods from another, promoting code reuse.

### Inheritance vs. Composition/Aggregation
- **Inheritance** creates a parent-child class relationship.
- **Composition** is a "has-a" relationship (e.g., a `Car` has an `Engine`).
- **Aggregation** is a looser "has-a" relationship (e.g., a `University` has `Departments`).

---

## Types of Inheritance

1. **Single Inheritance**: One base class, one derived class.
   - Example: `Dog` inherits from `Animal`.

2. **Multiple Inheritance**: One derived class inherits from multiple base classes.
   - Example: `FlyingCar` inherits from both `Car` and `Airplane`.

---

## Overriding Methods

- **Method overriding** lets a derived class change or extend a base class method.
- Override a method to maintain a consistent interface (polymorphism), rather than adding a new method which could break consistency.

---

## Real-World Analogy

- **Example**: A `SportsCar` inherits features from a `Car` but adds specific traits like high-speed performance.
- This mirrors OOP inheritance, where `SportsCar` extends `Car` with additional or modified functionality.

# Part B: Minimal Coding

## Option 1: Minimal Coding

### Base Class

Create a simple base class called `Vehicle` with:
- A `brand` attribute (or `manufacturer`).
- A method `drive()` that prints something generic like "Vehicle is driving."

### Derived Class

Define a derived class `Car` that inherits from `Vehicle`. Add a new attribute (e.g., `doors`) and override the `drive()` method to show it’s a car specifically driving.

### Short Driver Code

Demonstrate creating a `Vehicle` object and a `Car` object. Call `drive()` on both to illustrate the difference.

#### Part B: Minimal Coding

#include <iostream>
#include <string>
using namespace std;

// Base Class: Vehicle
class Vehicle {
public:
    string brand;  // Attribute: brand

    // Constructor
    Vehicle(string b) : brand(b) {}

    // Method: drive
    virtual void drive() {
        cout << "Vehicle is driving." << endl;
    }
};

// Derived Class: Car
class Car : public Vehicle {
public:
    int doors;  // Attribute: doors

    // Constructor
    Car(string b, int d) : Vehicle(b), doors(d) {}

    // Overridden Method: drive
    void drive() override {
        cout << "The " << brand << " car with " << doors << " doors is driving." << endl;
    }
};

// Main function (Short Driver Code)
int main() {
    // Creating a Vehicle object
    Vehicle vehicle("GenericBrand");
    vehicle.drive();  // Output: Vehicle is driving.

    // Creating a Car object
    Car car("Toyota", 4);
    car.drive();  // Output: The Toyota car with 4 doors is driving.

    return 0;
}

# Part C: Short Reflection & Discussion

## When to Use Inheritance

### Scenario Where Inheritance is Beneficial:
Inheritance is beneficial when there is a clear "is-a" relationship between classes. For example, in a **vehicle system**, a `Car` class can inherit from a `Vehicle` class. A `Car` **is a** type of `Vehicle`, and therefore can inherit common attributes and methods, like a `drive()` method, from the base class. This promotes code reuse and simplifies maintenance by avoiding duplication.

### Scenario Where Inheritance Might Be Overkill:
Inheritance might be overkill when the relationship between classes isn't a natural "is-a" relationship. For example, trying to make `Dog` and `Car` inherit from a common class `Animal` simply because they are both classes would create unnecessary complexity. A better solution in this case might be **composition**, where `Car` has an `Engine` and `Dog` has a `Tail`, rather than forcing them into an inheritance hierarchy that doesn’t make sense.

## Method Overriding vs. Overloading

### Method Overriding (Runtime Polymorphism):
**Method overriding** occurs when a subclass provides its own implementation of a method that is already defined in its superclass. This is a form of **runtime polymorphism**, where the method that gets executed is determined by the object's runtime type, not the type of the reference variable. This allows for more flexible and dynamic behavior.

Example:

class Animal {
public:
    virtual void sound() {
        cout << "Some generic animal sound" << endl;
    }
};

class Dog : public Animal {
public:
    void sound() override {
        cout << "Bark" << endl;
    }
};

## Inheritance vs. Interfaces/Abstract Classes

### How does the concept of inheritance differ from implementing an interface (or an abstract base class)?

**Inheritance** allows a class to inherit both methods and attributes from another class, forming an "is-a" relationship. In this case, the derived class is a more specialized version of the base class. It can override or extend the behavior of the inherited methods.

On the other hand, **interfaces** and **abstract classes** provide a contract that a class must follow. An **interface** only defines method signatures, with no implementation, and the implementing class must provide its own implementation. An **abstract class** can have both fully implemented methods and abstract methods (without implementation), and derived classes are required to implement the abstract methods.

The primary difference is that inheritance involves a direct relationship between classes, where the derived class inherits both behavior and state from the base class, while interfaces and abstract classes focus on defining expected behavior without dictating state.

## Pitfalls of Multiple Inheritance

### Name one potential problem with multiple inheritance (e.g., diamond problem).

One potential problem with multiple inheritance is the **diamond problem**. This occurs when a class inherits from two classes that have a common base class. If both parent classes override a method from the shared ancestor, it can create ambiguity for the derived class regarding which version of the method it should use. This ambiguity can lead to unexpected behavior or errors in the program.

### Suggest a strategy or approach (like virtual inheritance in C++ or an interface-based design) to mitigate this issue.

To mitigate the **diamond problem**, **virtual inheritance** can be used in C++ to ensure that only one instance of the common ancestor class is shared by both parent classes. This eliminates ambiguity by avoiding multiple copies of the same base class.

Alternatively, **interface-based design** or **composition** can be used to avoid multiple inheritance altogether. These approaches focus on defining behavior through interfaces or composing objects that implement specific functionality, rather than inheriting behavior and state from multiple parent classes.
