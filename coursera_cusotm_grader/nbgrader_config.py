c = get_config()

#set just 1 assignment and 1 student, assume /grader is the working dir,
#need to copy assignment notebook to /grader/submitted/student/module/ 
#so that gradebook.find_submission("module", "student") can find it
c.CourseDirectory.db_assignments = [dict(name="module")]
c.CourseDirectory.db_students = [dict(id="student")]
