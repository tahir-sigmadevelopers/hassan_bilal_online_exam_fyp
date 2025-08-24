#!/usr/bin/env python
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinexam.settings')
django.setup()

from exam.models import Course, Question
from student.models import Student
from teacher.models import Teacher
from django.contrib.auth.models import User

def verify_seed_data():
    print("=" * 60)
    print("VERIFYING SEEDED EXAM DATA")
    print("=" * 60)
    
    # Check Courses
    print("\n📚 COURSES:")
    print("-" * 30)
    courses = Course.objects.all()
    for course in courses:
        print(f"• {course.course_name}")
        print(f"  - Questions: {course.question_number}")
        print(f"  - Total Marks: {course.total_marks}")
        print()
    
    # Check Questions
    print("\n❓ QUESTIONS BY COURSE:")
    print("-" * 30)
    for course in courses:
        questions = Question.objects.filter(course=course)
        print(f"\n{course.course_name} ({questions.count()} questions):")
        for i, question in enumerate(questions, 1):
            print(f"  {i}. {question.question[:60]}...")
            print(f"     Marks: {question.marks}")
            print(f"     Answer: {question.answer}")
    
    # Check Users
    print("\n👥 USERS:")
    print("-" * 30)
    
    students = Student.objects.all()
    print(f"\nStudents ({students.count()}):")
    for student in students:
        print(f"• {student.user.first_name} {student.user.last_name} ({student.user.username})")
    
    teachers = Teacher.objects.all()
    print(f"\nTeachers ({teachers.count()}):")
    for teacher in teachers:
        print(f"• {teacher.user.first_name} {teacher.user.last_name} ({teacher.user.username})")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print("=" * 60)
    print(f"📚 Total Courses: {Course.objects.count()}")
    print(f"❓ Total Questions: {Question.objects.count()}")
    print(f"👨‍🎓 Total Students: {Student.objects.count()}")
    print(f"👨‍🏫 Total Teachers: {Teacher.objects.count()}")
    print("=" * 60)

if __name__ == "__main__":
    verify_seed_data() 