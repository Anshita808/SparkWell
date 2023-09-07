from django.shortcuts import get_object_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from rest_framework.decorators import api_view
from .models import User,Trainer,WorkoutPlan,UserWorkoutLog,Goal,NutritionPlan,UserNutritionLog


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
# Create your views here.
def my_view(request):
    return HttpResponse("Hello!")


class SignupView(APIView):
    def post(self, request):
        # Get data from request
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        age = request.data.get('age')
        location = request.data.get('location')
        gender = request.data.get('gender')
        # Check if username, password, and age are provided
        if not username or not password or not age or not email:
            return Response({'error': 'Username, password, age and email are required fields.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create a new user instance
            user = User(username=username , email=email , age=age, location=location , gender = gender , profile_image="https://static.vecteezy.com/system/resources/thumbnails/009/734/564/small/default-avatar-profile-icon-of-social-media-user-vector.jpg")
            # Hash and set the user's password
            user.set_password(password)
            # Save the user instance to the database
            user.save()
            return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': f'Could not create User. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TrainerSignupView(APIView):
    def post(self, request):
        # Get data from request
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        age = request.data.get('age')
        gender = request.data.get('gender')
        contact_number = request.data.get('contact_number')

        # Check if username, password, and age are provided
        if not name or not password or not age or not email:
            return Response({'error': 'Username, password, age and email are required fields.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create a new user instance
            trainer = Trainer(name=name , email=email , age=age, location="" , gender = gender ,specialization="None" , experience=0, contact_number=contact_number , profile_image="https://static.vecteezy.com/system/resources/thumbnails/009/734/564/small/default-avatar-profile-icon-of-social-media-user-vector.jpg", )
            # Hash and set the user's password
            trainer.set_password(password)
            # Save the user instance to the database
            trainer.save()
            return Response({'message': 'Trainer created successfully.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': f'Could not create Trainer. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TrainerLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            trainer = Trainer.objects.get(email=email)
            print(trainer)
        except Trainer.DoesNotExist:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        if trainer.check_password(password):
            # Convert ObjectId to string
            user_id_str = str(trainer.id)

            # Create a payload with user information
            payload = {
                'user_id': user_id_str,
                'username': trainer.name,
                # Add any other user-related information here
            }

            print(payload)
            # Encode the payload to generate a JWT token
            token = jwt_encode_handler(payload)

            return Response({'msg':"Login Successful!",'token': token , 'info':payload}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)
        
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        if user.check_password(password):
            # Convert ObjectId to string
            user_id_str = str(user.id)

            # Create a payload with user information
            payload = {
                'user_id': user_id_str,
                'username': user.username,
                # Add any other user-related information here
            }

            print(payload)
            # Encode the payload to generate a JWT token
            token = jwt_encode_handler(payload)

            return Response({'msg':"Login Successful!",'token': token , 'info':payload}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)
        
# ...................................................................  Authorization..............................................................................

@api_view(['GET', 'PATCH'])
def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = {
            'user_id': str(user.id),
            'username': user.username,
            'email': user.email,
            'age': user.age,
            'location': user.location,
            'gender': user.gender,
            'profile_image': user.profile_image
            # Add any other user-related information here
        }
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        new_username = request.data.get('username')
        new_age = request.data.get('age')
        new_location = request.data.get('location')
        new_gender = request.data.get('gender')
        new_profile = request.data.get('profile_image')
        if new_username:
            user.username = new_username
        if new_age:
            user.age = new_age
        if new_location:
            user.location = new_location
        if new_gender:
            user.gender = new_gender
        if new_profile:
            user.profile_image = new_profile
        
        user.save()
        return Response({'message': 'User details updated successfully.'}, status=status.HTTP_200_OK)
    

@api_view(['GET', 'PATCH'])
def tariner_detail(request, user_id):
    try:
        trainer = Trainer.objects.get(id=user_id)
    except Trainer.DoesNotExist:
        return Response({'error': 'Trainer not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = {
            'user_id': str(trainer.id),
            'name': trainer.name,
            'email': trainer.email,
            'age': trainer.age,
            'location': trainer.location,
            'gender': trainer.gender,
            'profile_image': trainer.profile_image,
            'specialization':trainer.specialization,
            'experience': trainer.experience,
            'contact_number':trainer.contact_number,

            # Add any other user-related information here
        }
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        new_username = request.data.get('name')
        new_age = request.data.get('age')
        new_location = request.data.get('location')
        new_gender = request.data.get('gender')
        new_profile = request.data.get('profile_image')
        new_specialization = request.data.get('specialization')
        new_experience = request.data.get('experience')
        new_contact_number = request.data.get('contact_number')
        
        
        if new_username:
            trainer.name = new_username
        if new_age:
            trainer.age = new_age
        if new_location:
            trainer.location = new_location
        if new_gender:
            trainer.gender = new_gender
        if new_profile:
            trainer.profile_image = new_profile
        if new_specialization:
            trainer.specialization = new_specialization
        if new_experience:
            trainer.experience = new_experience
        if new_contact_number:
            trainer.contact_number = new_contact_number
        
        trainer.save()
        return Response({'message': 'User details updated successfully.'}, status=status.HTTP_200_OK)


class CreateWorkoutPlanView(APIView):
    def post(self, request):
        data = request.data

        # Extract details from request data
        trainer_id = data.get('trainer_id')
        name = data.get('name')
        goal = data.get('goal')
        duration = data.get('duration')
        description = data.get('description')
        exercises = data.get('exercises')
        try:
            # Get the trainer instance
            trainer = Trainer.objects.get(id=trainer_id)
            
            # Create a new workout plan instance with the details
            workout_plan = WorkoutPlan(
                name=name,
                goal=goal,
                duration=duration,
                description=description,
                trainer=trainer,
                exercises = exercises,
                trainer_name=trainer.name  # Store the name of the trainer
            )
            workout_plan.save()

            return Response({'message': 'Workout plan created successfully.'}, status=status.HTTP_201_CREATED)
        except Trainer.DoesNotExist:
            return Response({'error': 'Trainer not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Could not create a workout plan. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetTrainerWorkoutPlans(APIView):
    def get(self, request, trainer_id):
        try:
            # Get the trainer instance
            trainer = Trainer.objects.get(id=trainer_id)
            
            # Get all workout plans created by the trainer
            workout_plans = WorkoutPlan.objects.filter(trainer=trainer)
            
            # Serialize the workout plans and return the response
            serialized_plans = []  # You need to create serializers for WorkoutPlan model
            for plan in workout_plans:
                serialized_plans.append({
                    'user_id': str(plan.id),
                    'name': plan.name,
                    'goal': plan.goal,
                    'duration': plan.duration,
                    'exercises':plan.exercises,
                    'description': plan.description,
                    'trainer_name': plan.trainer_name,
                })
            
            return Response(serialized_plans, status=status.HTTP_200_OK)
        except Trainer.DoesNotExist:
            return Response({'error': 'Trainer not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Could not retrieve workout plans.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetAllWorkoutPlans(APIView):
    def get(self, request):
        try:
            workout_plans = WorkoutPlan.objects.all()
            
            serialized_plans = []
            for plan in workout_plans:
                serialized_plans.append({
                    'user_id': str(plan.id),
                    'name': plan.name,
                    'goal': plan.goal,
                    'duration': plan.duration,
                    'exercises':plan.exercises,
                    'description': plan.description,
                    'trainer_name': plan.trainer_name,
                })
            
            return Response(serialized_plans, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Could not retrieve workout plans.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateUserWorkoutLogView(APIView):
    def post(self, request):
        data = request.data

        # Extract details from request data
        user_id = data.get('user_id')
        date = data.get('date')
        workout_plan = data.get('workout_plan')
        exercises = data.get('exercises')
        duration = data.get('duration')

        try:
            # Get the user instance
            user = User.objects.get(id=user_id)

            # Create a new workout log instance
            workout_log = UserWorkoutLog(
                user=user,
                date=date,
                workout_plan=workout_plan,
                exercises=exercises,
                duration=duration,
                user_name = user.username
            )
            workout_log.save()

            return Response({'message': 'Workout log created successfully.'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Could not create a workout log. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetUserWorkoutLogs(APIView):
    def get(self, request, user_id):
        try:
        # Get the trainer instance
            user = User.objects.get(id=user_id)
            
            # Get all workout plans created by the trainer
            workout_logs = UserWorkoutLog.objects.filter(user = user)
            
            # Serialize the workout plans and return the response
            serialized_plans = []  # You need to create serializers for WorkoutPlan model
            for plan in workout_logs:
                serialized_plans.append({
                    'user_id': str(plan.id),
                    'date': plan.date,
                    'workout_plan': plan.workout_plan,
                    'duration': plan.duration,
                    'exercises': plan.exercises,
                    'user_name': plan.user_name,
                })
            
            return Response(serialized_plans, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Trainer not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Could not retrieve workout plans.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CreateGoal(APIView):
    def post(self, request):
        data = request.data

        # Extract details from request data
        user_id = data.get('user_id')
        goal_type = data.get('goal_type')
        target = data.get('target')
        timeline = data.get('timeline')

        try:
            # Get the user instance
            user = User.objects.get(id=user_id)

            # Create a new workout log instance
            goal = Goal(
                user=user,
                goal_type=goal_type,
                target=target,
                timeline=timeline,
                username = user.username
            )
            goal.save()

            return Response({'message': 'Goal created successfully.'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Could not create a new goal. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class GetUserGoals(APIView):
    def get(self, request, user_id):
        try:
        # Get the trainer instance
            user = User.objects.get(id=user_id)
            
            # Get all workout plans created by the trainer
            goals = Goal.objects.filter(user = user)
            
            # Serialize the workout plans and return the response
            serialized_plans = []  # You need to create serializers for WorkoutPlan model
            for plan in goals:
                serialized_plans.append({
                    'user_id': str(plan.id),
                    'goal_type': plan.goal_type,
                    'target': plan.target,
                    'timeline': plan.timeline,
                    'user_name': plan.username,
                })
            
            return Response(serialized_plans, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Trainer not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Could not retrive the goal. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CreateNutritionPlanView(APIView):
    def post(self, request):
        data = request.data

        # Extract details from request data
        trainer_id = data.get('trainer_id')
        name = data.get('name')
        goal = data.get('goal')
        duration = data.get('duration')
        guidelines = data.get('guidelines')

        try:
            # Get the trainer instance
            trainer = Trainer.objects.get(id=trainer_id)
            
            # Create a new workout plan instance with the details
            nutrition_plan = NutritionPlan(
                name=name,
                goal=goal,
                duration=duration,
                guidelines=guidelines,
                trainer=trainer,
                trainer_name=trainer.name  # Store the name of the trainer
            )
            nutrition_plan.save()

            return Response({'message': 'Nutrition plan created successfully.'}, status=status.HTTP_201_CREATED)
        except Trainer.DoesNotExist:
            return Response({'error': 'Trainer not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Could not create a Nutrition plan. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetTrainerNutritionPlans(APIView):
    def get(self, request, trainer_id):
        try:
            # Get the trainer instance
            trainer = Trainer.objects.get(id=trainer_id)
            
            # Get all workout plans created by the trainer
            nutrition_plans = NutritionPlan.objects.filter(trainer=trainer)
            
            # Serialize the workout plans and return the response
            serialized_plans = []  # You need to create serializers for WorkoutPlan model
            for plan in nutrition_plans:
                serialized_plans.append({
                    'user_id': str(plan.id),
                    'name': plan.name,
                    'goal': plan.goal,
                    'duration': plan.duration,
                    'guidelines': plan.guidelines,
                    'trainer_name': plan.trainer_name,
                })
            
            return Response(serialized_plans, status=status.HTTP_200_OK)
        except Trainer.DoesNotExist:
            return Response({'error': 'Trainer not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Could not retrieve workout plans.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class GetAllNutritionPlans(APIView):
    def get(self, request):
        try:
            nutrition_plans = NutritionPlan.objects.all()
            
            serialized_plans = []
            for plan in nutrition_plans:
                serialized_plans.append({
                    'user_id': str(plan.id),
                    'name': plan.name,
                    'goal': plan.goal,
                    'duration': plan.duration,
                    'guidelines': plan.guidelines,
                    'trainer_name': plan.trainer_name,
                })
            
            return Response(serialized_plans, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Could not retrieve workout plans.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CreateUserNutritionLog(APIView):
    def post(self, request):
        data = request.data

        # Extract details from request data
        user_id = data.get('user_id')
        date = data.get('date')
        nutrition_plan = data.get('nutrition_plan')
        meals = data.get('meals')
        calories = data.get('calories')

        try:
            # Get the user instance
            user = User.objects.get(id=user_id)

            # Create a new workout log instance
            workout_log = UserNutritionLog(
                user=user,
                date=date,
                nutrition_plan=nutrition_plan,
                meals=meals,
                calories=calories,
                user_name = user.username
            )
            workout_log.save()

            return Response({'message': 'Nutrition log created successfully.'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Could not create a nutrition log. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetUserNutritionLogs(APIView):
    def get(self, request, user_id):
        try:
        # Get the trainer instance
            user = User.objects.get(id=user_id)
            
            # Get all workout plans created by the trainer
            nutrition_logs = UserNutritionLog.objects.filter(user = user)
            
            # Serialize the workout plans and return the response
            serialized_plans = []  # You need to create serializers for WorkoutPlan model
            for plan in nutrition_logs:
                serialized_plans.append({
                    'user_id': str(plan.id),
                    'date': plan.date,
                    'nutrition_plan': plan.nutrition_plan,
                    'calories': plan.calories,
                    'meals': plan.meals,
                    'user_name': plan.user_name,
                })
            
            return Response(serialized_plans, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Trainer not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Could not create a nutrition log. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)