# Part A: Conceptual Questions

## Composition vs. Aggregation

### Define both composition and aggregation.
- **Composition**: A strong "has-a" relationship where the contained object’s lifecycle is managed by the container.
- **Aggregation**: A looser "has-a" relationship where the contained object exists independently of the container.

### Example for each concept:
- **Composition**: A `House` has `Rooms`, and if the house is destroyed, the rooms are also destroyed.
- **Aggregation**: A `Library` has `Books`, but books can exist independently of the library.

### Which relationship implies a stronger form of ownership?
**Composition** implies a stronger ownership, as the contained object's lifecycle is tied to the container.

## When to Use

### Scenario where composition is more appropriate than inheritance:
In a **banking system**, a `BankAccount` contains `Transactions`. When the account is deleted, the transactions should also be deleted.

### Scenario where aggregation is sufficient:
In a **university system**, a `Department` aggregates `Professors`. Professors can exist independently and move between departments.

## Differences from Inheritance

### How composition/aggregation differ from inheritance:
- **Inheritance**: Models an "is-a" relationship (e.g., a `Dog` is an `Animal`).
- **Composition/Aggregation**: Models a "has-a" relationship (e.g., a `Car` has an `Engine`).

### Why favor composition over inheritance?
Composition provides flexibility and avoids tight coupling, offering more control over object relationships.

## Real-World Analogy

### System using both composition and aggregation:
A **Car** has an **Engine** (composition), but it has a **Driver** (aggregation), since the driver can be changed without affecting the car.

### Why do these distinctions matter in code?
Composition leads to stronger ownership and dependency, while aggregation allows more flexibility with looser coupling, leading to cleaner and more maintainable code.

```cpp
#ifndef PERSON_H
#define PERSON_H

#include "Address.h"
#include <string>

class Person {
private:
    std::string name;
    Address* address;  // Aggregation: Person has a reference (pointer) to Address

public:
    // Constructor
    Person(std::string name, Address* address) : name(name), address(address) {}

    // Getter for name
    std::string getName() const {
        return name;
    }

    // Getter for address
    Address* getAddress() const {
        return address;
    }

    // Setter for address
    void setAddress(Address* address) {
        this->address = address;
    }
};

#endif // PERSON_H
Address.h
cpp
Copy
#ifndef ADDRESS_H
#define ADDRESS_H

#include <string>

class Address {
private:
    std::string street;
    std::string city;

public:
    // Constructor
    Address(std::string street, std::string city) : street(street), city(city) {}

    // Getter for street
    std::string getStreet() const {
        return street;
    }

    // Getter for city
    std::string getCity() const {
        return city;
    }

    // Setter for street
    void setStreet(std::string street) {
        this->street = street;
    }

    // Setter for city
    void setCity(std::string city) {
        this->city = city;
    }
};

#endif // ADDRESS_H
main.cpp
cpp
Copy
#include <iostream>
#include "Person.h"
#include "Address.h"

int main() {
    // Create an Address object
    Address address("123 Main St", "Springfield");
    
    // Create a Person object with a reference to the Address
    Person person("John Doe", &address);
    
    // Output Person's details
    std::cout << "Name: " << person.getName() << std::endl;
    std::cout << "Address: " << person.getAddress()->getStreet() << ", " 
              << person.getAddress()->getCity() << std::endl;

    // Modify Address via the Person
    Address newAddress("456 Elm St", "Shelbyville");
    person.setAddress(&newAddress);

    // Output the updated Address
    std::cout << "Updated Address: " << person.getAddress()->getStreet() << ", " 
              << person.getAddress()->getCity() << std::endl;

    return 0;
}
```
### Ownership & Lifecycle

- **What happens to the "child" object if the "parent" is destroyed in composition?**

  In composition, the "child" is destroyed when the "parent" is destroyed because the parent owns the child.

- **How might the child object continue to exist independently in aggregation?**

  In aggregation, the "child" can exist independently of the "parent" since the child’s lifecycle is not tied to the parent.

### Advantages & Pitfalls

- **Advantage of using composition for object lifecycles?**

  Composition ensures proper memory management by making the parent responsible for the child’s lifecycle, preventing orphaned objects.

- **Pitfall of using composition where aggregation is needed?**

  Composition tightly couples objects, reducing flexibility and reusability, as the child’s lifecycle is tied to the parent.

### Contrast with Inheritance

- **Difference between "has-a" and "is-a" relationships?**

  "Has-a" (composition/aggregation) means ownership or association (e.g., a `Car` has an `Engine`), while "is-a" (inheritance) means type hierarchy (e.g., a `Dog` is a `Mammal`).

- **Why avoid inheritance when composition or aggregation works?**

  Inheritance can tightly couple classes, making code harder to modify and extend, while composition and aggregation provide more flexibility.
