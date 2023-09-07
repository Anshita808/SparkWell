from django.urls import path, re_path
from . import views
from .views import SignupView, LoginView, user_detail,TrainerSignupView,TrainerLoginView,tariner_detail,CreateWorkoutPlanView,GetTrainerWorkoutPlans , CreateUserWorkoutLogView,GetUserWorkoutLogs,GetAllWorkoutPlans,CreateGoal,GetUserGoals,CreateNutritionPlanView,GetTrainerNutritionPlans,GetAllNutritionPlans,CreateUserNutritionLog,GetUserNutritionLogs

urlpatterns=[
    path("", views.my_view , name="my_view"),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signuptrainer/' , TrainerSignupView.as_view() , name='signuptrainer'),
    path('logintrainer/' , TrainerLoginView.as_view() , name='logintrainer'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/<str:user_id>/', user_detail, name='user_detail'),
    path('trainer/<str:user_id>/',tariner_detail , name="trainer_detain" ),
    path('create-workout-plan/', CreateWorkoutPlanView.as_view(), name='create-workout-plan'),
    path('trainers/<str:trainer_id>/workout-plans/', GetTrainerWorkoutPlans.as_view(), name='get-trainer-workout-plans'),
    path('create_user_workout_log/', CreateUserWorkoutLogView.as_view(), name='create_user_workout_log'),
    path('user/<str:user_id>/workout-logs/', GetUserWorkoutLogs.as_view(), name='get-user-workout-logs'),
    path('all-workout-plans/', GetAllWorkoutPlans.as_view(), name='all-workout-plans'),
    path('create_goal/' , CreateGoal.as_view(), name="create_goal"),
    path('user/<str:user_id>/goals/', GetUserGoals.as_view(), name='goals'),
    path('create-nutrition-plan/', CreateNutritionPlanView.as_view(), name='create-nutrition-plan'),
    path('trainers/<str:trainer_id>/nutrition-plans/', GetTrainerNutritionPlans.as_view(), name='get-trainer-nutrition-plans'),
    path('all-nutrition-plans/', GetAllNutritionPlans.as_view(), name='all-workout-plans'),
    path('create_user_nutrition_log/', CreateUserNutritionLog.as_view(), name='create_user_workout_log'),
    path('user/<str:user_id>/nutrition-logs/', GetUserNutritionLogs.as_view(), name='get-user-nutrition-logs'),
]