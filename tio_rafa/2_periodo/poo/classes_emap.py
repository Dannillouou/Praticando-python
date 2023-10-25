# Estrutura de classes da EMAp

class Student:

    # Static attribute
    total_students = 0

    def __init__(self, name: str, student_id: int, major: str) -> None:
        self.name = name
        self.student_id = student_id
        self.major = major
        Student.total_students += 1

    def study(self, subject) -> str:
        return f"{self.name} is studying {subject}."
    
    def get_student_info(self) -> str:
        return f"{self.name}, ID: {self.student_id}, Major: {self.major}."
    
    def party(self) -> str:
        return f"{self.name} is partying!"
    
    def drink(self, beverage) -> str:
        return f"{self.name} is drinking {beverage}."
    
class GraduateStudent(Student):

    def __init__(self, name: str, student_id: int, major: str, research_topic: str) -> None:
        super().__init__(name, student_id, major)
        self.research_topic = research_topic

    def research(self):
        return f"{self.name} is conducting research on {self.research_topic}!"
    
    def party(self):
        return f"{self.name} is is attending a sophisticated conference party!"
    
    def drink(self, beverage) -> str:
        return f"{self.name} is sipping {beverage} while discussing {self.research_topic}."
    
class UndergraduateStudent(Student):
    
    def __init__(self, name: str, student_id: int, major: str, year: int) -> None:
        super().__init__(name, student_id, major)
        self.year = year

    def attend_lecture(self, course):
        return f"{self.name} is attending to a {course} lecture."
    
    def get_student_info(self) -> str:
        return f"{self.name}, ID: {self.student_id}, Major: {self.major}, Year: {self.year}!"

    def procrastinate(self):
        return f"{self.name} is procrastinating instead of studying!"
    
class MathStudent(UndergraduateStudent):

    def __init__(self, name: str, student_id: int, year: int, specialization: str) -> None:
        super().__init__(name, student_id, major="Mathematics", year=year)
        self.specialization = specialization

    def solve_math_problem(self, problem):
        return f"{self.name} is solving a {self.specialization} math problem: {problem}."

# creating instances
base_student = Student("Uriel Liann", "S12345", "MAp")
grad_student = GraduateStudent("Jeann Rocha", "S12346", "MAp", "Topology")
undergrad_student = UndergraduateStudent("Sillas Rocha", "S12347", "CdD")
math_student = MathStudent("Mariana Rocha", "M12345", 2023, "Linear Algebra")

# demonstrating cuntions
print(base_student.study("Math"))
print(grad_student.study("Math"))
print(undergrad_student.)
