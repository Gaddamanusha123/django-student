I developed a Student Management System using Django, where I built a simple and efficient way to manage student information. Through the Django Admin panel, users can easily add, update, and view student details like name, age, course, and roll number.

The main focus of my project controlling how different users interact with the system. So, I implemented role-based access control in the admin panel.

For the admin user, I provided full access. They can view all student records, add new students, update existing details, and also delete records if needed. Basically, they have complete control over the system.

For normal users, I restricted access to make the system safer and more controlled. They can only see limited fields like name and course, and they are allowed to edit only specific fields. They cannot delete any data, which helps prevent accidental data loss.

I implemented the Django Admin using features like ModelAdmin, where I controlled which fields are visible and what actions are allowed based on the user role.

Overall, this project helped me understand how to build a secure and user-friendly admin system, and how to manage permissions effectively in a real-world application.
