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
    s6 = course.Student(5, 'F')
    s7 = course.Student(5, 'G')
    s8 = course.Student(5, 'H')
    s9 = course.Student(5, 'L')
    return [s1, s2, s3, s4, s5]


@pytest.fixture
def questions() -> List[survey.Question]:
    q1 = survey.NumericQuestion(1, 'numeric 1', 5, 25)
    q2 = survey.MultipleChoiceQuestion(2, ' Multiple Question 2', ['a', 'b'])
    q3 = survey.CheckboxQuestion(3, ' Checkbox Question 3', ['X', 'Y'])
    q4 = survey.YesNoQuestion(4, 'YesNoQuestion 4')
    q5 = survey.NumericQuestion(1, 'numeric 5', 15, 250)
    q6 = survey.MultipleChoiceQuestion(2, ' Multiple Question 6', ['a', 'b'])
    q7 = survey.CheckboxQuestion(3, ' Checkbox Question 7', ['X', 'Y'])
    q8 = survey.YesNoQuestion(4, 'YesNoQuestion 8')
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


@pytest.fixture
def criterions():
    c1 = criterion.HomogeneousCriterion()
    c2 = criterion.HeterogeneousCriterion()
    c3 = criterion.LonelyMemberCriterion()

    d1 = {"Homogeneous": c1, "Heterogeneous": c2, "LonelyMember": c3}
    return d1


@pytest.fixture
def courses():
    course1 = course.Course('CSC 101')
    course2 = course.Course('CSC 102')
    course3 = course.Course('CSC 103')
    course4 = course.Course('CSC 104')
    return [course1, course2, course3, course4]


@pytest.fixture
def groups(students):
    group1 = grouper.Group(students[0:3])
    group2 = grouper.Group(students[3:6])
    group3 = grouper.Group(students[6:10])
    return [group1, group2, group3]


@pytest.fixture
def weights():
    return [3, 5, 7]


@pytest.fixture
def surveys(questions, criterions, weights):
    survey1 = survey.Survey(questions)
    crt = list(criterions)
    for i, question in enumerate(questions):
        survey1.set_criterion(crt[i], question)
        survey1.set_weight(weights[i], question)
    return survey1


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


class TestAnswer:
    def test_is_valid(self, questions, answers, students):
        """
        :param questions:
        :param answers:
        :param students:
        :return:
        """
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


class TestMultipleChoiceQuestion:
    def test_get_similarity(self, questions, answers, students):
        """
        q2 = MultipleChoiceQuestion(2, ' Multiple Question 2', ['a', 'b'])
        :param questions:
        :param answers:
        :param students:
        :return:
        """
        q1 = questions[1]

        a1 = survey.Answer('aa')
        a2 = survey.Answer('bb')
        a3 = survey.Answer('aa')
        a4 = survey.Answer('a')
        a5 = survey.Answer('')
        assert q1.get_similarity(a1, a3) == 1
        assert q1.get_similarity(a1, a2) == 0
        assert q1.get_similarity(a1, a4) == 0
        assert q1.get_similarity(a1, a5) == 0


class TestNumericQuestion:
    def test_get_similarity(self, questions, answers, students):
        q1 = survey.NumericQuestion(1, 'aa', 100, 200)
        a1 = survey.Answer(111)
        a2 = survey.Answer(98)
        a3 = survey.Answer(123)
        a4 = survey.Answer(111)
        a5 = survey.Answer(201)

        assert q1.get_similarity(a1, a4) == 1.0
        assert q1.get_similarity(a1, a2) is False
        assert q1.get_similarity(a1, a3) == 0.88
        assert q1.get_similarity(a1, a5) is False


class TestCheckboxQuestion:
    def test_get_similarity(self, questions, answers, students):
        q1 = survey.CheckboxQuestion(1, 'C', ['a', 'b', 'c', 'd', 'e', 'f'])
        a1 = survey.Answer(['a', 'b', 'c', 'd'])
        a2 = survey.Answer(['e', 'b', 'c', 'f'])
        a3 = survey.Answer(['a', 'b', 'c', 'd'])
        a4 = survey.Answer(['g'])

        assert q1.get_similarity(a1, a2) == 0.33
        assert q1.get_similarity(a1, a3) == 1.0
        assert q1.get_similarity(a1, a4) == 0.0


class TestYesNoQuestion:
    def test_get_similarity(self, questions, answers, students):
        """
        It inherits from checkbox question so it is not necessary
        :param questions:
        :param answers:
        :param students:
        :return:
        """
        pass


class TestHomogeneousCriterion:
    def test_score_answer(self, criterions, questions, answers):
        q1 = survey.MultipleChoiceQuestion(1, 'MC2', ['a', 'b', 'c', 'd'])
        a1 = survey.Answer('a')
        a2 = survey.Answer('b')
        a3 = survey.Answer('a')
        a4 = survey.Answer('c')
        a5 = survey.Answer('b')

        lst_ans = [a1, a2, a3]
        lst_ans2 = []
        c1 = criterions["Homogeneous"]
        assert c1.score_answers(q1, lst_ans) == 0.33


class TestHeterogeneousCriterion:
    def test_score_answer(self, criterions, questions, answers):
        q1 = survey.MultipleChoiceQuestion(1, 'MC2', ['a', 'b'])
        a1 = survey.Answer('a')
        a2 = survey.Answer('b')
        a3 = survey.Answer('a')

        lst_ans = [a1, a2, a3]
        c1 = criterions["Heterogeneous"]
        assert c1.score_answers(q1, lst_ans) == (1 - 0.33)


class TestLonelyMemberCriterion:
    def test_score_answer(self, criterions, questions, answers):
        c1 = criterions["LonelyMember"]
        q1 = questions[1]
        a1 = survey.Answer('a')
        a2 = survey.Answer('b')
        a3 = survey.Answer('a')
        assert c1.score_answers(q1, [a1, a2, a3]) == 0.0
        assert c1.score_answers(q1, [a1, a3]) == 1.0


def test_slice_list():
    lst = [1, 3, 4, 5, 7, 9, 10]
    lst2 = list(range(9))
    assert grouper.slice_list(lst, 2) == [[1, 3], [4, 5], [7, 9], [10]]
    assert grouper.slice_list(lst, 1) == [[1], [3], [4], [5], [7], [9], [10]]
    assert grouper.slice_list(lst, 3) == [[1, 3, 4], [5, 7, 9], [10]]
    assert grouper.slice_list(lst, 6) == [[1, 3, 4, 5, 7, 9], [10]]


class TestAlphaGrouper:
    def test_make_grouping(self, courses, students, questions, answers, surveys,
                           criterions, weights):
        course1 = courses[0]
        course1.enroll_students(students)
        survey1 = surveys[0]
        question1 = questions[0]
        answer1 = answers[0]
        survey1.set_weight(weights)
        survey1.set_criterion(criterions)

        assert grouper.AlphaGrouper(course1) == students


class TestRandomGrouper:
    def test_make_grouping(self):
        pass

