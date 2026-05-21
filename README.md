# Interactive University Registration System

A command-line Python application that simulates a student portal. This project demonstrates core Object-Oriented Programming (OOP) concepts including Abstraction, Inheritance, Encapsulation, and Polymorphism.

## Features
- **Browse Catalog:** View available theoretical lectures and practical labs.
- **Register for Courses:** Add courses to your schedule by Course ID.
- **Dynamic Billing:** Automatically calculates tuition based on course type (applies lab fees for practicals and tech taxes for lectures).
- **Error Handling:** Gracefully handles invalid inputs and duplicate registrations.

## Technical Implementation
1. **The Blueprint (Abstraction):** Uses the `abc` module to define an abstract `Course` base class.
2. **Specialization (Inheritance):** `TheoreticalLecture` and `PracticalLab` inherit from `Course` but implement their own `calculate_tuition()` logic.
3. **Data Protection (Encapsulation):** Uses `@property` decorators to protect attributes like `credit_hours` and `capacity` from illogical inputs (e.g., negative numbers).
4. **Smart Behavior (Polymorphism):** The `StudentSchedule` iterates through generic `Course` objects, dynamically calling the correct overridden methods.

## How to Run
1. Ensure you have Python 3.x installed.
2. Clone this repository to your local machine.
3. Open your terminal and navigate to the project directory.
4. Run the script: `python main.py`
5. Follow the interactive menu on the screen!
