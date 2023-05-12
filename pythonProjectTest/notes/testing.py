def get_formatted_name(first, last, middle=''):
    """Строит отформатированное полное имя."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


print("Enter 'q' at any time to quit.")  # код для проверки работы функции get_formatted_name
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeathly formatted name: {formatted_name}.")

import unittest  # импорт модуля для тестирования


class NamesTestCase(unittest.TestCase):  # класс-преемник от unittest.TestCase для тестирования функции
    """Тесты для функции get_formatted_name."""

    def test_first_last_name(self):  # метод для проверки поведения функции на 2 аргументах
        """Имена вида 'Daniel Daniels' работают правильно?"""
        formatted_name = get_formatted_name('daniel', 'daniels')
        self.assertEqual(formatted_name,
                         'Daniel Daniels')  # сравнение полученного formatted_name с ожидаемым результатом (2 аргумент)

    def test_first_middle_last_name(self):  # метод для проверки на 3 аргументах
        """Имена вида 'Daniel Danilovich Daniels' работают правильно?"""
        formatted_name = get_formatted_name('daniel', 'daniels', 'danilovich')
        self.assertEqual(formatted_name, 'Daniel Danilovich Daniels')


if __name__ == '__main__':
    unittest.main()


class AnonymousSurvey():  # класс для анонимного опроса
    """Сбор анонимных ответов на вопросы."""

    def __init__(self, question):
        """Сохраняет вопрос и готовится к сохранению ответов."""
        self.question = question
        self.responses = []

    def show_questions(self):
        """Выводит вопрос."""
        print(self.question)

    def store_response(self, new_response):
        """Сохраняет ответ на вопрос."""
        self.responses.append(new_response)

    def show_results(self):
        """Выводит все полученные ответы."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


question = "What language did you first learn to speak?"  # программа для проверки работы класса
my_survey = AnonymousSurvey(question)

my_survey.show_questions()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

import unittest


class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey."""

    def test_store_single_response(self):
        """Проверка сохранения одного ответа."""
        question = "What language did you first learn to speak?"  # задание вопроса
        my_survey = AnonymousSurvey(question)  # создание экземпляра класса с указанным вопросом
        my_survey.store_response('English')  # сохранение методом одного ответа
        self.assertIn('English', my_survey.responses)  # проверка, что ответ сохранен в списке my_survey.responses

    def test_store_three_responses(self):
        """Проверка сохранения трех ответов."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Italian', 'Spanish']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()

# применение метода setUp() для класса TestAnonymousSurvey:
import unittest


class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey."""

    def setUp(self):
        """Создание опроса и набора ответов для всех последующих тестовых методов."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)  # создает экземпляр класса (анонимного опроса)
        self.responses = ['English', 'Italian', 'Spanish']  # создает список ответов

    def test_store_single_response(self):
        """Проверка сохранения одного ответа."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Проверка сохранения трех ответов."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()