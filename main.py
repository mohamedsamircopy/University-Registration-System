from abc import ABC, abstractmethod

# ==========================================
# REQUIREMENT 1: The Blueprint (Abstraction)
# ==========================================
class Course(ABC):
    def __init__(self, course_id, name, base_cost, credit_hours):
        self.course_id = course_id
        self.name = name
        self.base_cost = base_cost
        # This triggers the setter for data protection
        self.credit_hours = credit_hours 

    # ==========================================
    # REQUIREMENT 3: Data Protection (Encapsulation)
    # ==========================================
    @property
    def credit_hours(self):
        return self.__credit_hours

    @credit_hours.setter
    def credit_hours(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Credit hours must be a positive integer.")
        if value > 6:
            raise ValueError("A single course cannot exceed 6 credit hours.")
        self.__credit_hours = value

    @abstractmethod
    def calculate_tuition(self):
        """Must be implemented by subclasses"""
        pass

    @abstractmethod
    def display_course_info(self):
        """Must be implemented by subclasses"""
        pass


# ==========================================
# REQUIREMENT 2: Specialization (Inheritance)
# ==========================================
class PracticalLab(Course):
    def __init__(self, course_id, name, base_cost, credit_hours, equipment_fee):
        super().__init__(course_id, name, base_cost, credit_hours)
        self.equipment_fee = equipment_fee

    def calculate_tuition(self):
        return (self.base_cost * self.credit_hours) + self.equipment_fee

    def display_course_info(self):
        return f"[Lab] {self.course_id}: {self.name} | {self.credit_hours} Credits | Equip Fee: ${self.equipment_fee}"


class TheoreticalLecture(Course):
    def __init__(self, course_id, name, base_cost, credit_hours, capacity):
        super().__init__(course_id, name, base_cost, credit_hours)
        # Using encapsulation for capacity as well
        self.capacity = capacity 

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if not isinstance(value, int) or value < 10:
            raise ValueError("Lecture capacity must be at least 10 students.")
        self.__capacity = value

    def calculate_tuition(self):
        base = self.base_cost * self.credit_hours
        tech_tax = base * 0.05  # 5% technology fee
        return base + tech_tax

    def display_course_info(self):
        return f"[Lecture] {self.course_id}: {self.name} | {self.credit_hours} Credits | Capacity: {self.capacity}"


# ==========================================
# REQUIREMENT 4: Smart Behavior (Polymorphism)
# ==========================================
class StudentSchedule:
    def __init__(self):
        self.registered_courses = []

    def add_course(self, course):
        self.registered_courses.append(course)
        print(f"\n[SUCCESS] Successfully registered for {course.name}!")

    def view_schedule(self):
        print("\n--- Current Schedule ---")
        if not self.registered_courses:
            print("No courses registered yet.")
        for course in self.registered_courses:
            print(course.display_course_info())
        print("------------------------")

    def print_tuition_bill(self):
        print("\n================ FINAL TUITION BILL ================")
        total_cost = 0
        for course in self.registered_courses:
            # Polymorphism in action: Calls the specific formula for Lab or Lecture
            course_cost = course.calculate_tuition()
            total_cost += course_cost
            print(f"{course.name.ljust(25)} : ${course_cost:.2f}")
        print("====================================================")
        print(f"TOTAL DUE:                ${total_cost:.2f}")
        print("====================================================\n")


# ==========================================
# REQUIREMENT 5: Terminal Interaction
# ==========================================
def main():
    # Pre-populate the university catalog
    catalog = [
        TheoreticalLecture("CS101", "Intro to AI", 200, 3, 150),
        TheoreticalLecture("MATH201", "Linear Algebra", 180, 4, 100),
        PracticalLab("CS101L", "AI Programming Lab", 200, 1, 150),
        PracticalLab("PHY101", "Physics Sandbox", 190, 2, 200)
    ]
    
    schedule = StudentSchedule()

    while True:
        print("\n--- UNIVERSITY REGISTRATION PORTAL ---")
        print("[1] View Available Courses")
        print("[2] Register for a Course")
        print("[3] View My Schedule")
        print("[4] Print Tuition Bill")
        print("[5] Exit")

        choice = input("\nEnter your choice (1-5): ")

        try:
            if choice == '1':
                print("\n--- Available Courses ---")
                for course in catalog:
                    print(course.display_course_info())
                
            elif choice == '2':
                course_id = input("Enter the Course ID to register: ").upper()
                found = False
                for course in catalog:
                    if course.course_id == course_id:
                        # Prevent duplicate registration
                        if any(c.course_id == course_id for c in schedule.registered_courses):
                            print("\n[WARNING] You are already registered for this course.")
                        else:
                            schedule.add_course(course)
                        found = True
                        break
                if not found:
                    print("\n[ERROR] Course not found. Please check the Course ID.")

            elif choice == '3':
                schedule.view_schedule()

            elif choice == '4':
                if not schedule.registered_courses:
                    print("\n[WARNING] Your schedule is empty. Register for courses first.")
                else:
                    schedule.print_tuition_bill()

            elif choice == '5':
                print("\nLogging out... Thank you for using the portal!")
                break

            else:
                print("\n[ERROR] Invalid input. Please type a number between 1 and 5.")

        except Exception as e:
            print(f"\n[ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()