### Part A: Conceptual Questions

#### DRY (Don’t Repeat Yourself)

- **Define DRY and provide a short example of repeated code.**
  
  DRY means avoiding code duplication. Repeated code is when the same logic is written multiple times across different parts of the code, making it harder to maintain.

- **How to refactor to adhere to DRY?**
  
  Refactor by creating reusable functions or methods to handle repeated logic, ensuring the code is defined in one place and reused where necessary.

#### KISS (Keep It Simple, Stupid)

- **Describe KISS and why it is crucial for maintainable code.**
  
  KISS encourages writing simple, clear code that is easy to understand and modify, reducing the risk of introducing bugs and making it easier to maintain in the long run.

- **One potential drawback of oversimplifying code?**
  
  Oversimplifying can lead to a lack of flexibility, making it harder to accommodate future requirements or changes without rewriting significant portions of the code.

#### Introduction to SOLID (High-Level)

- **Pick two SOLID principles and explain them in one sentence.**
  
  - **Single Responsibility Principle (SRP):** A class should only have one responsibility, meaning it should only perform one task.
  - **Open-Closed Principle (OCP):** A class should be open for extension but closed for modification, allowing new features to be added without altering existing code.

- **Why do the SOLID principles matter in large codebases?**
  
  The SOLID principles help keep the codebase organized, maintainable, and flexible, which is crucial for managing large codebases and ensuring they are scalable and easy to update.

  ### Part B: Minimal Examples or Scenarios

#### DRY Violation & Fix

- **Scenario:** Two functions print user details with slight variations.
  
  **Fix:** Combine them into a single function that takes a parameter for which details to print, avoiding duplication.

#### KISS Principle Example

- **Scenario:** A discount method uses overly complex conditions.
  
  **Fix:** Simplify the method by using clear, simple rules or a straightforward formula for calculating the discount.

#### SOLID Application

- **Scenario:** A `Shape` interface has `draw()` and `computeArea()`. Both `Circle` and `Rectangle` share `computeArea()` but have different `draw()` implementations.
  
  **Fix (ISP):** Split the interface into `Drawable` (for `draw()`) and `Computable` (for `computeArea()`) so classes only implement the relevant methods.

  ### Part C: Reflection & Short Discussion

#### Trade-Offs

- **Scenario:** A function calculates both tax and discount separately with almost identical logic. While it seems like a DRY violation, keeping them separate makes the code clearer and easier to modify later.

#### Combining Principles

- **How DRY and KISS guide design:** By following DRY, you avoid repeating code, and by following KISS, you keep things simple. For example, using a shared function to handle common logic can reduce repetition while keeping it easy to understand.

#### SOLID in Practice

- **Is it always necessary to follow every SOLID principle?**  
  No, in small projects, you might not strictly follow every SOLID principle. Early-stage codebases often prioritize rapid development over strict design patterns.

- **Why might a small codebase not adhere strictly to SOLID?**  
  In early stages, simplicity and speed are prioritized over maintainability, and applying SOLID principles can add unnecessary complexity before the project grows.
