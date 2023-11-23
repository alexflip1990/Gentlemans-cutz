# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Appointment


# class AddAppointmentViewTest(TestCase):
#     def setUp(self):
#         # Create a test user
#         self.user = User.objects.create_user(
#             username='testuser', password='testpassword')

#     def test_add_appointment_success(self):
#         self.client.login(username='testuser', password='testpassword')

#         # Define form data as a dictionary
#         form_data = {
#             'service': 'Classic Cut',
#             'time': '9 AM',
#             # Include other required fields from your form
#         }

#         response = self.client.post('add_appointment/', data=form_data)
#         # 302 is the status code for a redirect
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, '/view_appointment/')

#         # Verify that the appointment is created
#         appointment = Appointment.objects.filter(user=self.user)
#         self.assertEqual(appointment.count(), 1)
#         # Add more assertions as needed

#     def test_add_appointment_failure(self):
#         self.client.login(username='testuser', password='testpassword')

#         # Define invalid form data as a dictionary to simulate a failure scenario
#         form_data = {
#             'service': '',  # Invalid data
#             'time': '9 AM',
#             # Include other required fields from your form
#         }

#         response = self.client.post('add_appointment/', data=form_data)
#         # 200 is the status code for a successful response
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(
#             response, 'An appointment has already been made for this time and date')
#         # Add more assertions as needed




