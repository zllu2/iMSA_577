from nbgrader.plugins import ExportPlugin
from nbgrader.api import MissingEntry
import json

class JsonExportPlugin(ExportPlugin):
    """JSON exporter plugin."""

    def export(self, gradebook):

        if self.to == "":
            dest = "grades.json"
        else:
            dest = self.to

        #self.log.info("Exporting grades to %s", dest)

        assignment = gradebook.find_assignment("module")

        max_score = assignment.max_score

        # Try to find the submission in the database. If it doesn't
        # exist, the `MissingEntry` exception will be raised, which
        # means the student didn't submit anything, so we assign them a
        # score of zero.
        try:
            submission = gradebook.find_submission("module", "student")
        except MissingEntry:
            score = 0.0
        else:
            score = max(0.0, submission.score) / max_score

        feedback = "Congrats! All test cases passed!"
        if score < 0.999:
            feedback = "Your solution failed one or more test cases!"
        dict_to_coursera = {'fractionalScore':score, "feedback":feedback}

        with open(dest, 'w') as fout:
            json.dump(dict_to_coursera, fout)