from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from exam.models import Course, Question
from student.models import Student
from teacher.models import Teacher
import random

class Command(BaseCommand):
    help = 'Seed exam data with courses and questions'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to seed exam data...'))
        
        # Create courses
        courses_data = [
            {
                'name': 'Python Programming',
                'question_count': 10,
                'total_marks': 50,
                'questions': [
                    {
                        'question': 'What is Python?',
                        'option1': 'A programming language',
                        'option2': 'A snake',
                        'option3': 'A database',
                        'option4': 'An operating system',
                        'answer': 'Option1',
                        'marks': 5
                    },
                    {
                        'question': 'Which of the following is used to create a list in Python?',
                        'option1': '[]',
                        'option2': '()',
                        'option3': '{}',
                        'option4': '<>',
                        'answer': 'Option1',
                        'marks': 5
                    },
                    {
                        'question': 'What is the output of print(2 + "2")?',
                        'option1': '4',
                        'option2': '22',
                        'option3': 'TypeError',
                        'option4': 'None',
                        'answer': 'Option3',
                        'marks': 5
                    },
                    {
                        'question': 'Which method is used to add an element to a list?',
                        'option1': 'add()',
                        'option2': 'append()',
                        'option3': 'insert()',
                        'option4': 'push()',
                        'answer': 'Option2',
                        'marks': 5
                    },
                    {
                        'question': 'What is the correct way to create a function in Python?',
                        'option1': 'function myFunction():',
                        'option2': 'def myFunction():',
                        'option3': 'create myFunction():',
                        'option4': 'func myFunction():',
                        'answer': 'Option2',
                        'marks': 5
                    },
                    {
                        'question': 'Which of the following is a mutable data type in Python?',
                        'option1': 'tuple',
                        'option2': 'string',
                        'option3': 'list',
                        'option4': 'int',
                        'answer': 'Option3',
                        'marks': 5
                    },
                    {
                        'question': 'What does the len() function do?',
                        'option1': 'Returns the length of a string',
                        'option2': 'Returns the length of a list',
                        'option3': 'Returns the length of any sequence',
                        'option4': 'All of the above',
                        'answer': 'Option4',
                        'marks': 5
                    },
                    {
                        'question': 'Which operator is used for exponentiation in Python?',
                        'option1': '^',
                        'option2': '**',
                        'option3': '^^',
                        'option4': 'pow',
                        'answer': 'Option2',
                        'marks': 5
                    },
                    {
                        'question': 'What is the correct way to comment in Python?',
                        'option1': '// This is a comment',
                        'option2': '/* This is a comment */',
                        'option3': '# This is a comment',
                        'option4': '<!-- This is a comment -->',
                        'answer': 'Option3',
                        'marks': 5
                    },
                    {
                        'question': 'Which method is used to remove whitespace from the beginning and end of a string?',
                        'option1': 'trim()',
                        'option2': 'strip()',
                        'option3': 'clean()',
                        'option4': 'remove()',
                        'answer': 'Option2',
                        'marks': 5
                    }
                ]
            },
            {
                'name': 'Web Development',
                'question_count': 8,
                'total_marks': 40,
                'questions': [
                    {
                        'question': 'What does HTML stand for?',
                        'option1': 'Hyper Text Markup Language',
                        'option2': 'High Tech Modern Language',
                        'option3': 'Home Tool Markup Language',
                        'option4': 'Hyperlink and Text Markup Language',
                        'answer': 'Option1',
                        'marks': 5
                    },
                    {
                        'question': 'Which HTML tag is used to define an internal style sheet?',
                        'option1': '<script>',
                        'option2': '<style>',
                        'option3': '<css>',
                        'option4': '<link>',
                        'answer': 'Option2',
                        'marks': 5
                    },
                    {
                        'question': 'What does CSS stand for?',
                        'option1': 'Computer Style Sheets',
                        'option2': 'Cascading Style Sheets',
                        'option3': 'Creative Style Sheets',
                        'option4': 'Colorful Style Sheets',
                        'answer': 'Option2',
                        'marks': 5
                    },
                    {
                        'question': 'Which property is used to change the background color?',
                        'option1': 'bgcolor',
                        'option2': 'background-color',
                        'option3': 'color',
                        'option4': 'bg-color',
                        'answer': 'Option2',
                        'marks': 5
                    },
                    {
                        'question': 'What does JavaScript do?',
                        'option1': 'Styles web pages',
                        'option2': 'Makes web pages interactive',
                        'option3': 'Creates databases',
                        'option4': 'Manages servers',
                        'answer': 'Option2',
                        'marks': 5
                    },
                    {
                        'question': 'Which method is used to add an element to the end of an array in JavaScript?',
                        'option1': 'push()',
                        'option2': 'pop()',
                        'option3': 'shift()',
                        'option4': 'unshift()',
                        'answer': 'Option1',
                        'marks': 5
                    },
                    {
                        'question': 'What is the purpose of the <head> tag in HTML?',
                        'option1': 'To display content on the page',
                        'option2': 'To contain metadata about the document',
                        'option3': 'To create a header section',
                        'option4': 'To link to external files',
                        'answer': 'Option2',
                        'marks': 5
                    },
                    {
                        'question': 'Which CSS property controls the text size?',
                        'option1': 'text-size',
                        'option2': 'font-size',
                        'option3': 'text-style',
                        'option4': 'font-style',
                        'answer': 'Option2',
                        'marks': 5
                    }
                ]
            },
            {
                'name': 'Database Management',
                'question_count': 6,
                'total_marks': 30,
                'questions': [
                    {
                        'question': 'What does SQL stand for?',
                        'option1': 'Structured Query Language',
                        'option2': 'Standard Query Language',
                        'option3': 'Simple Query Language',
                        'option4': 'System Query Language',
                        'answer': 'Option1',
                        'marks': 5
                    },
                    {
                        'question': 'Which SQL command is used to extract data from a database?',
                        'option1': 'GET',
                        'option2': 'EXTRACT',
                        'option3': 'SELECT',
                        'option4': 'OBTAIN',
                        'answer': 'Option3',
                        'marks': 5
                    },
                    {
                        'question': 'Which SQL command is used to update data in a database?',
                        'option1': 'MODIFY',
                        'option2': 'UPDATE',
                        'option3': 'CHANGE',
                        'option4': 'ALTER',
                        'answer': 'Option2',
                        'marks': 5
                    },
                    {
                        'question': 'What is a primary key?',
                        'option1': 'A key that opens the database',
                        'option2': 'A unique identifier for each record',
                        'option3': 'The first column in a table',
                        'option4': 'A key used for encryption',
                        'answer': 'Option2',
                        'marks': 5
                    },
                    {
                        'question': 'Which SQL command is used to delete data from a database?',
                        'option1': 'REMOVE',
                        'option2': 'DELETE',
                        'option3': 'DROP',
                        'option4': 'ERASE',
                        'answer': 'Option2',
                        'marks': 5
                    },
                    {
                        'question': 'What is normalization in database design?',
                        'option1': 'Making the database smaller',
                        'option2': 'Organizing data to reduce redundancy',
                        'option3': 'Speeding up database queries',
                        'option4': 'Backing up the database',
                        'answer': 'Option2',
                        'marks': 5
                    }
                ]
            }
        ]

        # Create courses and questions
        for course_data in courses_data:
            # Create course
            course, created = Course.objects.get_or_create(
                course_name=course_data['name'],
                defaults={
                    'question_number': course_data['question_count'],
                    'total_marks': course_data['total_marks']
                }
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created course: {course.course_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Course already exists: {course.course_name}'))
            
            # Create questions for this course
            for question_data in course_data['questions']:
                question, created = Question.objects.get_or_create(
                    course=course,
                    question=question_data['question'],
                    defaults={
                        'marks': question_data['marks'],
                        'option1': question_data['option1'],
                        'option2': question_data['option2'],
                        'option3': question_data['option3'],
                        'option4': question_data['option4'],
                        'answer': question_data['answer']
                    }
                )
                
                if created:
                    self.stdout.write(f'  - Created question: {question.question[:50]}...')
                else:
                    self.stdout.write(f'  - Question already exists: {question.question[:50]}...')

        # Create some sample users if they don't exist
        self.create_sample_users()
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded exam data!'))
        self.stdout.write(self.style.SUCCESS(f'Created {Course.objects.count()} courses'))
        self.stdout.write(self.style.SUCCESS(f'Created {Question.objects.count()} questions'))

    def create_sample_users(self):
        """Create sample students and teachers if they don't exist"""
        
        # Create sample students
        students_data = [
            {'username': 'john_student', 'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com'},
            {'username': 'jane_student', 'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane@example.com'},
            {'username': 'mike_student', 'first_name': 'Mike', 'last_name': 'Johnson', 'email': 'mike@example.com'},
        ]
        
        for student_data in students_data:
            user, created = User.objects.get_or_create(
                username=student_data['username'],
                defaults={
                    'first_name': student_data['first_name'],
                    'last_name': student_data['last_name'],
                    'email': student_data['email'],
                    'is_staff': False,
                    'is_superuser': False
                }
            )
            
            if created:
                user.set_password('student123')
                user.save()
                
                student, created = Student.objects.get_or_create(
                    user=user,
                    defaults={
                        'mobile': f'+1{random.randint(1000000000, 9999999999)}',
                        'address': f'{random.randint(100, 999)} Main St, City, State'
                    }
                )
                
                if created:
                    self.stdout.write(f'Created student: {user.first_name} {user.last_name}')
        
        # Create sample teachers
        teachers_data = [
            {'username': 'prof_wilson', 'first_name': 'Dr. Sarah', 'last_name': 'Wilson', 'email': 'sarah@university.edu'},
            {'username': 'prof_brown', 'first_name': 'Prof. Robert', 'last_name': 'Brown', 'email': 'robert@university.edu'},
        ]
        
        for teacher_data in teachers_data:
            user, created = User.objects.get_or_create(
                username=teacher_data['username'],
                defaults={
                    'first_name': teacher_data['first_name'],
                    'last_name': teacher_data['last_name'],
                    'email': teacher_data['email'],
                    'is_staff': True,
                    'is_superuser': False
                }
            )
            
            if created:
                user.set_password('teacher123')
                user.save()
                
                teacher, created = Teacher.objects.get_or_create(
                    user=user,
                    defaults={
                        'mobile': f'+1{random.randint(1000000000, 9999999999)}',
                        'address': f'{random.randint(100, 999)} University Ave, City, State',
                        'salary': random.randint(50000, 80000)
                    }
                )
                
                if created:
                    self.stdout.write(f'Created teacher: {user.first_name} {user.last_name}') 