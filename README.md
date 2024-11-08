# USF Course Assistant
				                
Automated Course Monitoring: Full-stack application that automates the monitoring of course seat availability via real-time notifications for status updates, and enabling automatic registration for select courses.

## Back-End Functionality

### Availability Status Checking
Course availability data is fetched and monitored from USF's Staff Schedule Search site. This data will be fetched and refreshed/updated frequently.

### Auto-Registration
This functionality involves automating the total process of the user signing in to USF Microsoft account, navigating to USF's OASIS course registration menu, search the particular course(s), and finally register upon course availability. This is implemented such that the user can simply "set it and forget it" while the program takes care of the total process without the user's manual intervention.

### User Login and Session Management
Each user's account will be logged into (with prior consent) periodically without requiring the user's manual, real-time approval to ensure that auto-registration can be performed at any time as soon as a selected course is available to the user. This periodic Microsoft sign-in will be used to refresh/extend the user session and avoid session expiration and loss in which case the manual, real-time approval will be required once again.

## Front-End
Integration of Front-End in development with Django.
