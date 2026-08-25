# Core CS Fundamentals: Object-Oriented Programming (OOP)

## 1. The 4 Pillars of OOP

### 1. Encapsulation
- **Definition**: Bundling data (variables) and methods operating on that data inside a single unit (class) while restricting direct access to internal state using access specifiers (`private`, `protected`).
- **Real-World Analogy**: A capsule medicine containing multiple ingredients hidden from the user.
- **Code Example (Java)**:
```java
public class BankAccount {
    private double balance; // Encapsulated data

    public void deposit(double amount) {
        if (amount > 0) {
            this.balance += amount;
        }
    }
    public double getBalance() {
        return this.balance;
    }
}
```

### 2. Abstraction
- **Definition**: Hiding background complex implementation details and displaying only essential functional interfaces to the user.
- **Real-World Analogy**: Driving a car by pressing the accelerator without needing to understand internal engine combustion logic.
- **Code Example (Java)**:
```java
abstract class Vehicle {
    abstract void startEngine(); // Essential interface
}

class Car extends Vehicle {
    void startEngine() {
        System.out.println("Engine started via electronic ignition.");
    }
}
```

### 3. Inheritance
- **Definition**: Mechanism where a child class (subclass) derives properties and behaviors from a parent class (superclass), promoting code reuse.
- **Types**: Single, Multilevel, Hierarchical, Multiple (supported via Interfaces in Java/C++).
- **Code Example (Java)**:
```java
class Animal {
    void eat() { System.out.println("Eating..."); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking..."); }
}
```

### 4. Polymorphism
- **Definition**: Ability of an object or method to take on multiple forms.
- **Compile-Time Polymorphism (Method Overloading)**: Same method name with different parameter signatures resolved at compile time.
- **Run-Time Polymorphism (Method Overriding)**: Child class provides a specific implementation of a method already declared in its parent class, resolved at runtime using virtual tables (vtable).
- **Code Example (Method Overriding)**:
```java
class Shape {
    void draw() { System.out.println("Drawing Shape"); }
}
class Circle extends Shape {
    @Override
    void draw() { System.out.println("Drawing Circle"); }
}
```

---

## 2. SOLID Principles Overview

1. **Single Responsibility Principle (SRP)**: A class should have one, and only one, reason to change.
2. **Open/Closed Principle (OCP)**: Software entities should be open for extension, but closed for modification.
3. **Liskov Substitution Principle (LSP)**: Subtypes must be substitutable for their base types without breaking application behavior.
4. **Interface Segregation Principle (ISP)**: Clients should not be forced to depend on interfaces they do not use.
5. **Dependency Inversion Principle (DIP)**: High-level modules should not depend on low-level modules; both should depend on abstractions.

---

## 3. Top Interview Questions & MCQs

1. **What is the difference between Abstract Class and Interface in Java?**
   - *Answer*: Abstract classes can have state (instance variables) and implemented non-abstract methods. Interfaces (prior to Java 8) contain only method signatures (now support default/static methods) and cannot maintain instance state. A class can implement multiple interfaces but extend only one abstract class.
2. **What is Virtual Function in C++?**
   - *Answer*: A function declared in a base class using `virtual` keyword, overridden by derived classes to enable dynamic (runtime) dispatch via `vptr` and `vtable`.
