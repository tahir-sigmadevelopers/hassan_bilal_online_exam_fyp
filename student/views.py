from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from exam import models as QMODEL
from teacher import models as TMODEL
import json


#for showing signup/login button for student
def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'student/studentclick.html')

def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request,'student/studentsignup.html',context=mydict)

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_dashboard_view(request):
    dict={
    
    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    }
    return render(request,'student/student_dashboard.html',context=dict)

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_exam_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/student_exam.html',{'courses':courses})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def take_exam_view(request,pk):
    course = QMODEL.Course.objects.get(id=pk)
    total_questions = QMODEL.Question.objects.all().filter(course=course).count()
    questions = QMODEL.Question.objects.all().filter(course=course)
    total_marks = 0
    
    for q in questions:
        total_marks = total_marks + q.marks
    
    return render(request,'student/take_exam.html',{
        'course': course,
        'total_questions': total_questions,
        'total_marks': total_marks,
        'questions': questions
    })

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def start_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    questions=QMODEL.Question.objects.all().filter(course=course)
    
    # Calculate total marks
    total_marks = 0
    for question in questions:
        total_marks += question.marks
    
    if request.method=='POST':
        pass
    response= render(request,'student/start_exam.html',{
        'course':course,
        'questions':questions,
        'total_marks': total_marks
    })
    response.set_cookie('course_id',course.id)
    return response


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def calculate_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course = QMODEL.Course.objects.get(id=course_id)
        
        total_marks = 0
        questions = QMODEL.Question.objects.all().filter(course=course)
        
        for i, question in enumerate(questions):
            # Try both old and new cookie naming formats
            selected_ans = request.COOKIES.get(f'q{i+1}') or request.COOKIES.get(str(i+1))
            actual_answer = question.answer
            
            if selected_ans == actual_answer:
                total_marks = total_marks + question.marks
        
        student = models.Student.objects.get(user_id=request.user.id)
        
        # Check if result already exists for this student and course
        existing_result = QMODEL.Result.objects.filter(student=student, exam=course).first()
        
        if existing_result:
            # Update existing result
            existing_result.marks = total_marks
            existing_result.save()
        else:
            # Create new result
            result = QMODEL.Result()
            result.marks = total_marks
            result.exam = course
            result.student = student
            result.save()

        return HttpResponseRedirect('view-result')
    else:
        # Redirect to exam selection if no course_id found
        return HttpResponseRedirect('student-exam')



@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def view_result_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/view_result.html',{'courses':courses})
    

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def check_marks_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    student = models.Student.objects.get(user_id=request.user.id)
    results= QMODEL.Result.objects.all().filter(exam=course).filter(student=student)
    
    # Calculate total possible marks for this course
    total_possible_marks = 0
    questions = QMODEL.Question.objects.all().filter(course=course)
    for question in questions:
        total_possible_marks += question.marks
    
    # Calculate statistics for each result
    results_with_stats = []
    for result in results:
        percentage = 0
        if total_possible_marks > 0:
            percentage = (result.marks / total_possible_marks) * 100
        
        results_with_stats.append({
            'result': result,
            'total_possible_marks': total_possible_marks,
            'percentage': round(percentage, 1)
        })
    
    # Calculate overall statistics
    total_attempts = len(results)
    total_obtained_marks = sum(result.marks for result in results)
    average_score = 0
    if total_attempts > 0:
        average_score = total_obtained_marks / total_attempts
    latest_score = results.first().marks if results.exists() else 0
    
    # Calculate overall percentage
    overall_percentage = 0
    if total_possible_marks > 0 and total_attempts > 0:
        overall_percentage = (total_obtained_marks / (total_possible_marks * total_attempts)) * 100
    
    context = {
        'results': results,
        'results_with_stats': results_with_stats,
        'total_possible_marks': total_possible_marks,
        'total_attempts': total_attempts,
        'total_obtained_marks': total_obtained_marks,
        'average_score': round(average_score, 1),
        'latest_score': latest_score,
        'overall_percentage': round(overall_percentage, 1),
        'course': course
    }
    
    return render(request,'student/check_marks.html', context)

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_marks_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/student_marks.html',{'courses':courses})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def report_cheating_view(request):
    """Handle cheating violation reports from JavaScript"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            violation_type = data.get('violation_type')
            course_id = request.COOKIES.get('course_id')
            
            if course_id and violation_type:
                course = QMODEL.Course.objects.get(id=course_id)
                student = models.Student.objects.get(user_id=request.user.id)
                
                # Create cheating attempt record
                CheatingAttempt.objects.create(
                    student=student,
                    exam=course,
                    violation_type=violation_type,
                    description=data.get('description', '')
                )
                
                return JsonResponse({'status': 'success', 'message': 'Violation recorded'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
  