# Configuration file for nbgrader.
c = get_config()

#------------------------------------------------------------------------------
# ClearSolutions(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## The delimiter marking the beginning of a solution
#c.ClearSolutions.begin_solution_delimeter = 'BEGIN SOLUTION'

## The code snippet that will replace code solutions
c.ClearSolutions.code_stub = {'python': '# YOUR CODE HERE\n'}

## The delimiter marking the end of a solution
#c.ClearSolutions.end_solution_delimeter = 'END SOLUTION'

## A key that is unique per instructor and course. This can be specified, either
#  by setting the config option, or using the --course option on the command
#  line.
c.CourseDirectory.course_id = 'accy577_linden_test'
