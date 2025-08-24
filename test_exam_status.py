#!/usr/bin/env python
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinexam.settings')
django.setup()

from exam.models import Course, Result
from student.models import Student
from django.contrib.auth.models import User

def test_exam_status():
    print("=" * 60)
    print("TESTING EXAM STATUS LOGIC")
    print("=" * 60)
    
    # Get all courses
    courses = Course.objects.all()
    print(f"\n📚 Available Courses ({courses.count()}):")
    for course in courses:
        print(f"• {course.course_name}")
    
    # Get all students
    students = Student.objects.all()
    print(f"\n👨‍🎓 Students ({students.count()}):")
    for student in students:
        print(f"• {student.user.first_name} {student.user.last_name} ({student.user.username})")
    
    # Test the logic for each student
    for student in students:
        print(f"\n" + "=" * 40)
        print(f"EXAM STATUS FOR: {student.user.first_name} {student.user.last_name}")
        print("=" * 40)
        
        courses_with_status = []
        for course in courses:
            has_taken_exam = Result.objects.filter(student=student, exam=course).exists()
            courses_with_status.append({
                'course': course,
                'has_taken_exam': has_taken_exam
            })
            print(f"• {course.course_name}: {'✅ Taken' if has_taken_exam else '❌ Not Taken'}")
    
    # Show all results
    print(f"\n" + "=" * 60)
    print("ALL EXAM RESULTS")
    print("=" * 60)
    
    results = Result.objects.all()
    if results.exists():
        for result in results:
            print(f"• {result.student.user.first_name} {result.student.user.last_name} - {result.exam.course_name}: {result.marks} marks")
    else:
        print("No exam results found yet.")

if __name__ == "__main__":
    test_exam_status() 