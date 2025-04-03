# Part A: Conceptual Questions

## Definition

### What is Polymorphism?
Polymorphism allows objects to take multiple forms, enabling methods to act differently based on the object they are applied to.

### Why is polymorphism considered one of the pillars of OOP?
Polymorphism promotes code reuse and flexibility by enabling objects of different types to be treated as a common base type.

## Compile-Time vs. Runtime

### What is compile-time polymorphism (method overloading)?
Compile-time polymorphism happens when methods with the same name differ in parameters, resolved during compilation.

### What is runtime polymorphism (method overriding)?
Runtime polymorphism occurs when a method in a base class is redefined in a derived class, with the method called determined at runtime.

### Which type requires an inheritance relationship, and why?
Runtime polymorphism requires inheritance because it relies on method overriding in derived classes.

## Method Overloading

### Why might a class have multiple methods with the same name but different parameter lists?
A class may have overloaded methods to handle different argument types or counts, simplifying the interface.

### How does method overloading simplify user interactions?
Method overloading allows a user to call the same method with different argument types, reducing the need for multiple method names.

## Method Overriding

### How does a derived class override a base class’s method to provide specialized behavior?
A derived class provides its own implementation of a base class method to modify or extend its behavior.

### Why might the virtual keyword be needed?
The virtual keyword in languages like C++ ensures that the correct method is called at runtime, enabling dynamic method dispatch.

# Part B: Minimal Demonstration (Pseudo-code or UML)

## Option 1: Minimal Code (No More Than 20 Lines)

### Base Class & Derived Classes

- Create a base class `Shape` with an abstract or virtual method `draw()`.
- Create two derived classes, `Circle` and `Rectangle`, each overriding `draw()`.

### Demonstration

- Create a list/array of `Shape*` or references.
- Store both a `Circle` and a `Rectangle`.
- Call `draw()` on each object, demonstrating runtime polymorphism.

```cpp
class Shape {
public:
    virtual void draw() = 0;  // Pure virtual method
};

class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing a Circle" << endl;
    }
};

class Rectangle : public Shape {
public:
    void draw() override {
        cout << "Drawing a Rectangle" << endl;
    }
};

int main() {
    Shape* shapes[2];  // Array of Shape pointers
    shapes[0] = new Circle();
    shapes[1] = new Rectangle();

    for (int i = 0; i < 2; i++) {
        shapes[i]->draw();  // Correct draw() method is chosen at runtime
    }

    return 0;
}
```

# Part C: Overloading vs. Overriding Distinctions

## Overloaded Methods

### Imagine a class Calculator that has multiple calculate() methods, each accepting different parameter types (e.g., (int, int), (double, double)).
- **How is compile-time resolution used here?**

In method overloading, the decision of which method to call is made at **compile time** based on the number or types of parameters provided. The compiler selects the appropriate `calculate()` method based on the arguments passed, and the method signature is resolved before the program runs.

Example:
- `calculate(int, int)` is called if integers are passed.
- `calculate(double, double)` is called if doubles are passed.

## Overridden Methods

### In your Shape example (or another scenario), the draw() method is overridden in derived classes.
- **When does the decision for which method to call occur (compile time or runtime)?**

The decision for which method to call in method overriding occurs at **runtime**. This is because the method that gets called is determined by the actual type of the object, not the type of the reference or pointer used to call the method. This is known as **runtime polymorphism**.

### Why does this matter for flexible code design?

Runtime polymorphism allows for **greater flexibility** in code design, as it enables objects of different derived types to be treated uniformly using base class references or pointers. This flexibility allows new classes to be added without modifying existing code, promoting **extensibility** and **maintainability**. With method overriding, you can define behavior that is specific to each derived class while maintaining a consistent interface for interacting with the base class.
