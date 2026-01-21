from django.urls import path
from .views import (
    step1_problem,
    step2_outcome,
    step3_activities,
    step4_stakeholders,
    step5_indicators,
    summary,
)

urlpatterns = [
    path("", step1_problem, name="step1"),
    path("outcome/<int:lfa_id>/", step2_outcome, name="step2"),
    path("activities/<int:lfa_id>/", step3_activities, name="step3"),
    path("stakeholders/<int:lfa_id>/", step4_stakeholders, name="step4"),
    path("indicators/<int:lfa_id>/", step5_indicators, name="step5"),
    path("summary/<int:lfa_id>/", summary, name="summary"),
]
