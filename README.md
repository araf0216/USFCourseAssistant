# USF Course Assistant
				                
Automated Course Monitoring: Full-stack application that automates the monitoring of course seat availability via real-time notifications for status updates, and enabling automatic registration for select courses.

## Back-End Functionality

### User Login and Session Management
Scraping cookies from USF Microsoft Sign In allows us to bypass MFA method requirements and periodically sign in (with their prior consent!) but without requiring manual, real-time approval. This project requires having a user's Microsoft sign-in session periodically refreshed/extended to avoid session expiration and loss.

### Auto-Registration
This functionality involves automating the user login and then navigating to select class and register as soon as course is available.

### Availability Status Checking
Course availability data is scraped separately from USF Staff Schedule Search site.

## Front-End
Integration of Front-End in development with Django.
