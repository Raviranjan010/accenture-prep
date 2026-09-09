# CS Fundamentals: Object-Oriented Programming (OOP)

## What this is
Object-Oriented Programming (OOP) is a software design paradigm structured around "objects" containing data (attributes/fields) and code (methods/functions). It enforces modularity, code reusability, maintainability, and encapsulation across industrial software development.

---

## Formula / Rule / Pattern

| Core OOP Pillar | Technical Definition | Code Realization / Keyword |
| :--- | :--- | :--- |
| **Encapsulation** | Bundling data and methods into a single unit; restricting direct access | `private` variables + `public` getters/setters |
| **Abstraction** | Hiding complex internal implementation details, exposing only essential interfaces | `interface`, `abstract class` |
| **Inheritance** | Mechanism where a child class acquires properties of a parent class | `extends` (Java), `: public` (C++) |
| **Polymorphism** | Ability of a single method name or operator to exhibit multiple behaviors | Overloading (Compile-time), Overriding (Runtime) |

---

## Shortcut: Compile-Time vs Runtime Polymorphism Matrix

> [!TIP]
> ### The Polymorphism Disambiguation Matrix
> Distinguish Overloading from Overriding using this 3-point checklist:
> 
> 1. **Overloading (Compile-Time)**: Same method name, **different parameter signature**, occurs **within the same class**. Resolved by compiler during compilation.
> 2. **Overriding (Runtime)**: Same method name, **identical parameter signature**, occurs across **Parent and Child classes**. Resolved dynamically at runtime using virtual method tables (`vtable`).
> 
> *Why it works*: 90% of OOP assessment questions test whether changing parameters or class hierarchy changes overloading to overriding.

---

## Worked Examples

### Example 1: Encapsulation (Easy)
- **Question**: Why are class member variables declared `private` in Java?
- **Step-by-step Solution**:
  1. `private` prevents external classes from directly mutating variable states arbitrarily.
  2. Access is controlled via controlled `public` getter and setter methods containing validation logic.
  3. **Concept**: Encapsulation & Data Hiding.

### Example 2: Method Overriding & Dynamic Binding (Medium)
- **Code snippet**:
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
- **Step-by-step Solution**:
  1. `obj` reference type is `Parent`, but instance type created at runtime is `Child`.
  2. Since `show()` is overridden, Java performs dynamic method dispatch at runtime.
  3. The overridden method in `Child` executes.
  4. **Output**: `Child`.

### Example 3: Abstract Class vs Interface Tradeoff (Hard)
- **Question**: When should an architect choose an `Abstract Class` over an `Interface` in Java 8+?
- **Step-by-step Solution**:
  1. Use `Abstract Class` when classes share common non-static state (`protected`/`private` fields) or constructor initialization logic.
  2. Use `Interface` when defining a pure contract across completely unrelated classes (e.g. `Comparable`, `Serializable`), supporting multiple inheritance of interfaces.

---

## Practice Questions (PYQ Bank)

Q1. Which OOP feature binds code and data together while keeping both safe from outside interference?  
a) Inheritance  
b) Encapsulation  
c) Polymorphism  
d) Abstraction  

Q2. What is the output of overloading a method with identical parameter types and names but a different return type in Java?  
a) Overriding occurs  
b) Compile-time error  
c) Runtime error  
d) Code executes cleanly  

Q3. Can an abstract class in Java be instantiated using the `new` operator directly?  
a) Yes  
b) No (Abstract classes cannot be instantiated directly)  

Q4. Which keyword is used by a child class to call a overridden parent method in Java?  
a) `this`  
b) `super`  
c) `parent`  
d) `base`  

Q5. Which type of polymorphism is achieved through method overloading?  
a) Compile-time polymorphism  
b) Runtime polymorphism  
c) Dynamic polymorphism  
d) Deferred polymorphism  

Q6. In C++, which keyword enables dynamic method binding for runtime polymorphism?  
a) `static`  
b) `virtual`  
c) `inline`  
d) `friend`  

Q7. Multiple inheritance of classes (one child class inheriting directly from two parent classes) is NOT directly supported in which language?  
a) C++  
b) Python  
c) Java (classes)  
d) Lisp  

Q8. What type of member variable is shared across all instances of a class?  
a) `private` variable  
b) `static` variable  
c) `local` variable  
d) `transient` variable  

Q9. What is a constructor?  
a) A special method called automatically when an object instance is instantiated  
b) A method that destroys objects  
c) A static loop  
d) An interface  

Q10. Can a `final` class be inherited in Java?  
a) Yes  
b) No (`final` keyword prevents inheritance)  

Q11. What is operator overloading?  
a) Giving extended meaning to existing language operators (+, -, *) for user-defined object types  
b) Deleting operators  
c) Writing math equations  
d) Converting integers to floats  

Q12. What access modifier restricts member visibility strictly to the defining class and its subclasses?  
a) `public`  
b) `private`  
c) `protected`  
d) `default`  

Q13. In Java, all classes implicitly inherit from which root superclass?  
a) `java.lang.System`  
b) `java.lang.Object`  
c) `java.lang.Class`  
d) `java.util.Base`  

Q14. What is a pure virtual function in C++?  
a) A virtual function set to `= 0` making the class abstract  
b) A normal function  
c) A static function  
d) A private constructor  

Q15. Why does Method Overriding require exact parameter signature matching?  
a) To match the exact function signature in the virtual method table (`vtable`) for runtime resolution  
b) To save RAM  
c) To prevent syntax errors  
d) Compiler requirement only  

---

## Answers

1. **b) Encapsulation** — Encapsulation binds state and behavior into a single class container.
2. **b) Compile-time error** — Method overloading in Java requires different parameter types/counts; changing return type alone is invalid.
3. **b) No** — Abstract classes cannot be instantiated directly with `new`.
4. **b) `super`** — `super.methodName()` calls parent class implementation.
5. **a) Compile-time polymorphism** — Method overloading is resolved during compilation.
6. **b) `virtual`** — `virtual` keyword populates the vtable in C++.
7. **c) Java (classes)** — Java prevents multiple class inheritance to avoid the Diamond Problem.
8. **b) `static` variable** — Static variables belong to the class rather than instance objects.
9. **a) A special method called automatically...** — Constructor definition.
10. **b) No** — `final` class cannot be extended.
11. **a) Giving extended meaning to existing language operators...** — Operator overloading definition.
12. **c) `protected`** — Accessible within defining class, package, and subclasses.
13. **b) `java.lang.Object`** — Root of Java class hierarchy.
14. **a) A virtual function set to `= 0`...** — Definition of pure virtual function in C++.
15. **a) To match the exact function signature in the virtual method table...** — Runtime lookup mechanism.

---

## Where this appears in the real Accenture test
Appears in Stage 2: Core CS Fundamentals Technical MCQ section.

---

## Recommended videos
- [Accenture Technical Assessment Walkthrough (2026-relevant)](https://www.youtube.com/watch?v=DwZZNJxBAn0) — CS fundamentals questions.
- [Accenture Mock Technical Assessment](https://www.youtube.com/watch?v=JM2Uc9KJ-Ys) — Code execution and OOP Q&A.
