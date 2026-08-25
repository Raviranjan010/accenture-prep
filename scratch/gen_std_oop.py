import os

# 1. oop-concepts.md
oop_content = """# Core CS Fundamentals: Object-Oriented Programming (OOP)

## 1. What is it?
**Object-Oriented Programming (OOP)** is a software programming model that organizes code around real-world "objects" rather than just isolated functions and commands.

### Beginner Vocabulary Glossary
Before looking at any code, let's define the fundamental terms:
- **Programming / Code**: Writing instructions for a computer to perform tasks.
- **Variable**: A named storage container in computer memory used to hold data (e.g., storing a user's age `age = 21`).
- **Function / Method**: A reusable block of code that performs a specific action when called (e.g., `calculateTotal()`).
- **Class**: A **blueprint** or master template used to create objects. It defines what attributes (variables) and actions (methods) an object will have.
- **Object**: A specific, real instance created from a class blueprint containing actual data values.

---

## 2. Why does it matter?
1. **Accenture Assessment & Technical Interviews**: OOP is one of the most heavily tested CS topics in technical MCQs and live coding rounds.
2. **Code Reusability & Maintainability**: Instead of rewriting code for every new feature, you can extend existing class blueprints.
3. **Enterprise Scalability**: Large production software systems (e.g., e-commerce platforms, banking apps) rely on OOP to keep millions of lines of code organized and modular.

---

## 3. When to use it?
- **Use OOP when**: Building medium-to-large software applications with complex domain entities that interact with each other (e.g., Users, Products, Orders, Payments).
- **Do not use OOP when**: Writing small, single-purpose scripts (e.g., automating a file rename or simple data transformation script) where functional/procedural scripts are faster.

---

## 4. How it works
1. **Class Definition**: You write a class defining variables (state) and methods (behavior).
2. **Instantiation (Object Creation)**: When the program runs, it creates an object using the `new` keyword.
3. **Memory Allocation**: The computer allocates RAM memory (on the **Heap**) for the new object, while a pointer reference is stored on the **Stack**.
4. **Method Invocation**: You trigger object methods (e.g., `myCar.drive()`) to manipulate the object's internal data.

---

## 5. Key rules or syntax

### Class and Object Syntax (Java / C++)
```java
// Class Blueprint
class Car {
    // 1. Attributes (State / Variables)
    String color;
    int speed;

    // 2. Constructor (Special method to initialize new objects)
    public Car(String c, int s) {
        this.color = c;
        this.speed = s;
    }

    // 3. Method (Behavior / Action)
    public void drive() {
        System.out.println("Driving at " + speed + " km/h.");
    }
}

// Object Instantiation in Main Method
public class Main {
    public static void main(String[] args) {
        Car myCar = new Car("Red", 100); // Creating an Object
        myCar.drive(); // Output: Driving at 100 km/h.
    }
}
```
*Why constructors work*: Constructors automatically allocate and assign initial values to object memory the moment an object is instantiated.

---

## 6. Simple example

### Level 1 (Easy): Basic Class and Object
- **Concept**: Creating a `Student` object from a `Student` class blueprint.
```java
class Student {
    String name;
    int marks;

    void displayInfo() {
        System.out.println(name + " scored " + marks + " marks.");
    }
}

public class SimpleDemo {
    public static void main(String[] args) {
        Student s1 = new Student();
        s1.name = "Ravi";
        s1.marks = 95;
        s1.displayInfo(); // Output: Ravi scored 95 marks.
    }
}
```

---

## 7. Detailed example

### The 4 Pillars of OOP & SOLID Principles

#### Pillar 1: Encapsulation
- **Definition**: Bundling data (variables) and methods inside a single unit (class) while restricting direct access to internal state using access specifiers (`private`, `protected`, `public`).
- **Simple Beginner Example**: Hiding a person's age variable so it cannot be set to a negative number.
- **Realistic Enterprise Example**:
```java
public class BankAccount {
    // Private variable: cannot be modified directly from outside
    private double balance;

    public BankAccount(double initialBalance) {
        if (initialBalance >= 0) {
            this.balance = initialBalance;
        }
    }

    // Controlled getter method
    public double getBalance() {
        return this.balance;
    }

    // Controlled setter method with validation
    public void deposit(double amount) {
        if (amount > 0) {
            this.balance += amount;
            System.out.println("Successfully deposited ₹" + amount);
        } else {
            System.out.println("Invalid deposit amount!");
        }
    }
}
```

#### Pillar 2: Abstraction
- **Definition**: Hiding complex internal implementation details and showing only essential interfaces to the user.
- **Simple Beginner Example**: Driving a car using a steering wheel without needing to understand fuel injection mechanics.
- **Realistic Enterprise Example**:
```java
// Abstract interface: specifies WHAT to do, not HOW to do it
interface PaymentProcessor {
    void processPayment(double amount);
}

class StripePayment implements PaymentProcessor {
    public void processPayment(double amount) {
        // Complex Stripe API token handshake & encryption details hidden here
        System.out.println("Processing ₹" + amount + " via Stripe API.");
    }
}

class PayPalPayment implements PaymentProcessor {
    public void processPayment(double amount) {
        // Complex PayPal OAuth & REST payload hidden here
        System.out.println("Processing ₹" + amount + " via PayPal OAuth.");
    }
}
```

#### Pillar 3: Inheritance
- **Definition**: Mechanism where a child class (subclass) automatically derives variables and methods from a parent class (superclass), promoting code reuse.
- **Simple Beginner Example**: `Dog` class inheriting `eat()` from `Animal` class.
- **Realistic Enterprise Example**:
```java
class User {
    protected String userId;
    protected String email;

    public void login() {
        System.out.println(email + " logged in successfully.");
    }
}

// AdminUser inherits all properties of User and adds admin-specific features
class AdminUser extends User {
    private int adminAccessLevel;

    public void deleteDatabaseBackup() {
        System.out.println("Admin " + userId + " executed database wipe.");
    }
}
```

#### Pillar 4: Polymorphism
- **Definition**: The ability of a single method or object to take on multiple forms depending on the context.
- **Compile-Time Polymorphism (Method Overloading)**: Same method name with different parameters in the same class.
- **Run-Time Polymorphism (Method Overriding)**: Subclass provides a specific implementation of a method already declared in its parent class.
- **Realistic Enterprise Example (Method Overriding)**:
```java
class NotificationSender {
    public void sendNotification(String message) {
        System.out.println("Sending default notification: " + message);
    }
}

class EmailNotification extends NotificationSender {
    @Override
    public void sendNotification(String message) {
        System.out.println("Sending Email via SMTP: " + message);
    }
}

class SMSNotification extends NotificationSender {
    @Override
    public void sendNotification(String message) {
        System.out.println("Sending SMS via Twilio Gateway: " + message);
    }
}
```

---

### SOLID Principles Overview
1. **Single Responsibility Principle (SRP)**: A class should have one, and only one, reason to change.
2. **Open/Closed Principle (OCP)**: Classes should be open for extension, but closed for modification.
3. **Liskov Substitution Principle (LSP)**: Derived classes must be completely substitutable for their base classes without breaking app logic.
4. **Interface Segregation Principle (ISP)**: Clients should not be forced to depend upon interface methods they do not use.
5. **Dependency Inversion Principle (DIP)**: Depend on abstractions (interfaces), not on concrete implementations.

---

## 8. Practical use case
**E-Commerce Platform Architecture**:
In a real-world platform like Amazon:
- `Product` class encapsulates price, stock quantity, and discounts.
- `User` class is extended via Inheritance into `Customer` and `Seller`.
- `PaymentProcessor` interface uses Abstraction & Polymorphism to process payments through Credit Card, UPI, or NetBanking interchangeably without breaking the checkout service code.

---

## 9. Common mistakes

### Concept 1: Encapsulation Mistakes
- *Mistake*: Making class variables `public` for convenience.
- *Why it happens*: Avoids writing getters/setters, but allows external code to mutate invalid states (e.g., `account.balance = -50000`).

### Concept 2: Polymorphism & Overriding Mistakes
- *Mistake*: Confusing Method Overloading (Compile-Time, same class, different parameters) with Method Overriding (Run-Time, parent-child, exact same parameters).
- *Why it happens*: Both use similar method names. Always check parameter signatures and class hierarchy.

### Concept 3: Inheritance Mistakes
- *Mistake*: Creating deep, rigid inheritance chains (e.g., `A` extends `B` extends `C` extends `D` extends `E`).
- *Why it happens*: Overusing inheritance instead of composition ("Has-A" relationship). Changes in base class `A` accidentally break child classes `E`.

---

## 10. Tips & tricks

### Shortcut 1: The "Is-A" vs "Has-A" Test
- **Concept**: To decide between Inheritance and Composition:
  - If "Dog **Is-A** Animal" makes sense $\implies$ Use **Inheritance** (`class Dog extends Animal`).
  - If "Car **Has-A** Engine" makes sense $\implies$ Use **Composition** (`class Car { Engine e; }`).

### Shortcut 2: The `@Override` Annotation Shield
- **Rule**: Always write `@Override` above overridden methods. If you make a typo in the method name, the compiler will raise an error immediately instead of silently treating it as a new method.

### Shortcut 3: Interface Decoupling Rule
- **Rule**: Declare variable types as Interfaces, not concrete classes:
  - *Slow/Rigid*: `ArrayList<String> list = new ArrayList<>();`
  - *Best Practice*: `List<String> list = new ArrayList<>();` (Allows changing implementation to `LinkedList` later in 1 second).

---

## 11. Practice exercises

1. **(Easy - Recall)** What is the difference between a Class and an Object?
2. **(Easy - Recall)** Which access modifier restricts variable visibility strictly within the same class?
3. **(Easy - Concept)** Is method overloading resolved at compile-time or run-time?
4. **(Medium - Why)** Why should instance variables in a class be declared `private` rather than `public`?
5. **(Medium - Scenario)** A developer writes `class Bird { void fly() {} }` and `class Ostrich extends Bird {}`. Why does this violate Liskov Substitution Principle (LSP)?
6. **(Medium - Applied)** Identify whether Method Overloading or Overriding is present:
   ```java
   class MathUtils {
       int add(int a, int b) { return a + b; }
       double add(double a, double b) { return a + b; }
   }
   ```
7. **(Medium - Scenario)** What will be the output of the following code snippet?
   ```java
   class Parent {
       void show() { System.out.println("Parent"); }
   }
   class Child extends Parent {
       void show() { System.out.println("Child"); }
   }
   public class Test {
       public static void main(String[] args) {
           Parent obj = new Child();
           obj.show();
       }
   }
   ```
8. **(Hard - Applied)** Design a Java class structure for a `Shape` interface with `getArea()` method, implemented by `Rectangle` and `Circle` classes.
9. **(Hard - Scenario)** In Java, why is multiple inheritance through classes disallowed, but multiple inheritance through interfaces allowed?
10. **(Hard - Architecture)** Explain how the Single Responsibility Principle (SRP) prevents code regression when modifying business logic in an enterprise backend.

---

## 12. Q&A with explanations

1. **Answer**: A **Class** is a blueprint/template that defines structure and behaviors. An **Object** is a specific instance created from that blueprint residing in memory with actual values.
2. **Answer**: `private`.
3. **Answer**: Compile-time (Static Polymorphism).
4. **Answer**: Declaring variables `private` enforces **Encapsulation**. It prevents external code from mutating fields directly into invalid states, ensuring data validation occurs through setter methods.
5. **Answer**: Ostriches cannot fly. Subclass `Ostrich` inheriting `fly()` from `Bird` causes unexpected runtime behavior or forced dummy overrides when an `Ostrich` is passed where a `Bird` is expected, breaking LSP.
6. **Answer**: **Method Overloading** (same method name `add` with different parameter types in the same class).
7. **Answer**: Output: **"Child"**. Because `obj` refers to a `Child` instance in memory, runtime polymorphism invokes the overridden `Child` method.
8. **Answer**:
   ```java
   interface Shape { double getArea(); }
   class Circle implements Shape {
       double r;
       Circle(double r) { this.r = r; }
       public double getArea() { return Math.PI * r * r; }
   }
   ```
9. **Answer**: To prevent the **Diamond Problem** (ambiguity when two parent classes define the same method with different implementations). Interfaces specify method contracts without instance state ambiguity.
10. **Answer**: SRP ensures each class has only one reason to change (e.g., `UserRepository` handles DB operations, `EmailService` handles emails). Changing database logic won't accidentally break email delivery code.

---

## 13. Quick revision

> [!TIP]
> ### 🚀 OOP Cheat-Sheet
> - **4 Pillars**:
>   - **Encapsulation**: Private data + Public getters/setters.
>   - **Abstraction**: Hide internal complexity behind interfaces.
>   - **Inheritance**: `extends` keyword, code reuse ("Is-A").
>   - **Polymorphism**: Overloading (Compile-time) vs Overriding (Run-time).
> - **Overloading**: Same class, same method name, **different parameters**.
> - **Overriding**: Parent-child, same method name, **exact same parameters**.
> - **Memory**: Stack stores reference pointers; Heap stores actual Object data.

---

## 14. Connection to next topic
Now that you understand how objects structure data in memory during application runtime, the next step is learning how to persist this data permanently in relational tables. Continue to **[dbms-normalization-joins.md](dbms-normalization-joins.md)** to learn about Database Management Systems, Normalization, and SQL Joins!
"""

with open('02-technical-coding/cs-fundamentals/oop-concepts.md', 'w', encoding='utf-8') as f:
    f.write(oop_content)

print("oop-concepts.md updated.")
