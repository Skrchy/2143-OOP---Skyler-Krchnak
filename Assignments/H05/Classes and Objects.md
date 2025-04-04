# Part A: Conceptual Questions

## Definition of a Class and an Object

### What is a class in object-oriented programming?
A **class** is a blueprint for creating objects, defining their attributes and behaviors.

### What is an object, and how does it relate to a class?
An **object** is an instance of a class, created using its blueprint, with specific data for the defined attributes.

## Constructors and Destructors

### Define a constructor. What is its role in a class?
A **constructor** initializes an object when it is created, setting up initial values for its attributes.

### Define a destructor. Why is it important in managing an object’s lifecycle?
A **destructor** cleans up resources (e.g., memory) when an object is destroyed, preventing memory leaks.

## Object Lifecycle

### Briefly describe the lifecycle of an object from instantiation to destruction.
An object is created with a **constructor**, performs tasks, and is then destroyed with a **destructor** to free resources.

### Why is it important for a class to manage its resources (e.g., memory) during its lifecycle?
Proper resource management prevents **memory leaks** and ensures efficient use of system resources.

# Part B: Minimal Coding Example

### Class Design

```cpp
#include <iostream>
#include <string>
using namespace std;

class Creature {
private:
    string name;
public:
    // Constructor
    Creature(string n) : name(n) {}

    // Destructor
    ~Creature() {
        cout << name << " is being destroyed!" << endl;
    }

    // Method to display the creature's state
    void display() {
        cout << "Creature: " << name << endl;
    }
};

int main() {
    Creature goblin("Goblin");
    goblin.display();
    return 0;
}
```

## Explanation
The Creature class uses a constructor to initialize the name attribute when an object is created. The destructor is called when the object is destroyed, printing a message indicating the destruction. The object lifecycle is managed by the constructor initializing the object and the destructor cleaning up when the object goes out of scope.

# Part C: Reflection & Short-Answer

### Importance of Constructors:
Constructors initialize an object’s attributes, ensuring it starts its lifecycle in a valid and consistent state. They provide the necessary setup for an object to function properly.

### Role of Destructors:
Destructors are crucial in languages without automatic garbage collection because they release resources like memory and file handles when an object is destroyed, preventing resource leaks.

### Lifecycle Management:
If a class does not properly manage its resources, it can lead to issues like **memory leaks** (where memory is not freed) or **resource exhaustion** (where system resources like file handles are not released), potentially causing program instability.
