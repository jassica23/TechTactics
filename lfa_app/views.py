from django.shortcuts import render, redirect
from .models import LFA
def step1_problem(request):
    if request.method == "POST":
        problem = request.POST.get("problem")
        lfa = LFA.objects.create(problem=problem)
        return redirect("step2", lfa_id=lfa.id)
    return render(request, "step1_problem.html")


def step2_outcome(request, lfa_id):
    lfa = LFA.objects.get(id=lfa_id)
    if request.method == "POST":
        lfa.student_outcome = request.POST.get("student_outcome")
        lfa.save()
        return redirect("step3", lfa_id=lfa.id)
    return render(request, "step2_outcome.html", {"lfa": lfa})


def step3_activities(request, lfa_id):
    lfa = LFA.objects.get(id=lfa_id)
    if request.method == "POST":
        lfa.activities = request.POST.get("activities")
        lfa.save()
        return redirect("step4", lfa_id=lfa.id)
    return render(request, "step3_activities.html", {"lfa": lfa})


def step4_stakeholders(request, lfa_id):
    lfa = LFA.objects.get(id=lfa_id)
    if request.method == "POST":
        lfa.stakeholders = request.POST.get("stakeholders")
        lfa.save()
        return redirect("step5", lfa_id=lfa.id)
    return render(request, "step4_stakeholders.html", {"lfa": lfa})


def step5_indicators(request, lfa_id):
    lfa = LFA.objects.get(id=lfa_id)
    if request.method == "POST":
        lfa.indicators = request.POST.get("indicators")
        lfa.save()
        return redirect("summary", lfa_id=lfa.id)
    return render(request, "step5_indicators.html", {"lfa": lfa})


def summary(request, lfa_id):
    lfa = LFA.objects.get(id=lfa_id)
    return render(request, "summary.html", {"lfa": lfa})
