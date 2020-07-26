import course
import survey
import criterion
import grouper
import pytest
from typing import List, Set, FrozenSet


@pytest.fixture
def students():
    s1 = course.Student(1, 'A')
    s2 = course.Student(2, 'B')
    s3 = course.Student(3, 'C')
    s4 = course.Student(4, 'D')
    s5 = course.Student(5, 'E')
    return [s1, s2, s3, s4, s5]


@pytest.fixture
def questions() -> List[survey.Question]:
    q1 = survey.NumericQuestion(1, 'numeric 1', 5, 25)
    q2 = survey.MultipleChoiceQuestion(2, ' Multiple Question 2', ['a', 'b'])
    q3 = survey.CheckboxQuestion(3, ' Checkbox Question 3', ['X', 'Y'])
    q4 = survey.YesNoQuestion(4, 'YesNoQuestion 4')
    return [q1, q2, q3, q4]


@pytest.fixture
def answers() -> List[List[survey.Answer]]:
    a1 = survey.Answer(7)
    a2 = survey.Answer('a')
    a3 = survey.Answer('X')
    a4 = survey.Answer(True)
    a5 = survey.Answer(8)
    a6 = survey.Answer('b')
    a7 = survey.Answer('Y')
    a8 = survey.Answer(False)
    return [[a1, a2, a3, a4], [a5, a6, a7, a8], [a1, a6, a7, a4],
            [a5, a6, a7, a4]]


class TestStudent:
    def test___str___(self, students) -> None:
        assert students[0].name == str(students[0])

    def test_set_answer(self, students, questions, answers):
        stu1 = students[0]
        stu1.set_answer(questions[0], answers[0][0])
        assert stu1.get_answer(questions[0]) == answers[0][0]

    def test_get_answer(self, questions, students, answers):
        stu1 = students[0]
        stu1.set_answer(questions[0], answers[0][0])
        assert stu1.get_answer(questions[0]) == answers[0][0]

    def test_has_answer(self, students, questions, answers):
        stu1 = students[0]
        stu1.set_answer(questions[0], answers[0][0])
        assert stu1.has_answer(questions[0])


class TestCourse:

    def test_enroll_students(self, students) -> None:
        stu_list = students
        course1 = course.Course('csc1')
        course1.enroll_students(students)
        s1 = students[0]
        s2 = students[1]
        s3 = students[2]
        s4 = students[3]
        s5 = students[4]
        assert course1.students == [s1, s2, s3, s4, s5]
        assert course1.students == stu_list

    def test_all_answered(self, students) -> None:
        """
        Will be completed after validate answer is done
        :param students:
        :return None:
        """
        student1 = students[0]
        student2 = students[1]
        student3 = students[2]

    def test_get_students(self, students) -> None:
        stu_list = students
        course1 = course.Course('csc1')
        course1.enroll_students(students)

        assert course1.get_students() == tuple(stu_list)


class TestHomogeneousCriterion:
    def test_score_answer(self, questions, answers):
        pass


class TestHeterogeneousCriterion:
    def test_score_answer(self, questions, answers):
        pass


class TestAnswer:
    def test_is_valid(self, questions, answers, students):
        q1 = questions[0]
        q2 = questions[1]
        q3 = questions[2]
        q4 = questions[3]

        a1 = answers[0][0]
        a2 = answers[1][1]
        a3 = answers[0][2]
        a4 = survey.Answer(9)

        stu1 = students[0]
        stu1.set_answer(q1, a1)

        stu2 = students[1]
        stu2.set_answer(q2, a2)

        stu3 = students[2]
        stu3.set_answer(q3, a3)

        stu4 = students[3]
        stu4.set_answer(q4, a4)

        assert a1.is_valid(q1)
        assert a2.is_valid(q2)
        assert a3.is_valid(q3)
        assert a4.is_valid(q4) is False
