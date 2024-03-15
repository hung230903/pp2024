import numpy as np
from math import *

class Student:
    def __init__(self, name, DoB, student_id):
        self.name = name
        self.DoB = DoB
        self.student_id = student_id
        self.marks = {} 

    def add_mark(self, subject, mark):
        self.marks[subject] = floor(float(mark) * 10) / 10

    def display_info(self):
        print(f"ID: {self.student_id} - Name: {self.name} - DoB: {self.DoB}")
        if self.marks:
            print("Marks: ")
            for subject, mark in self.marks.items():
                print(f"{subject}: {mark}")

    def gpa(self):
        if not self.marks:
            return 0
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)

    def weighted_gpa(self,credits) :
        if not self.marks:
            return 0
        total_weighted_marks = sum(np.array(list(self.marks.values()) * np.array(credits)))
        total_credit = sum(credits)
        return total_weighted_marks / total_credit 
