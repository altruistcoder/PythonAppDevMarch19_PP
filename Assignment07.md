Assignment (Lecture-8)

1. Go through the `myflaskproject` and `student_api` projects. Make sure that you are able to run and understand the working of both the projects.


2. Modify the `student_api` project such that 
	- `/students/?branch=cs` returns only those students which are in `cs` branch. 
	- `/students/?cgpa=8` returns only those student who have 8 cgpa.
	- `/students/?branch=cs&cgpa=8` returns those students who are in `cs` branch and have 8 cgpa.

	Hint: Use `request.args` to get URL parameters dictionary.