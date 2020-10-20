from django.test import TestCase
from django.urls import reverse
from todo.models import Todo

# Create your tests here.
def create_todo(description, done=False):
    return Todo.objects.create(description=description, done=done)

def get_todo(id):
    return Todo.objects.get(pk=id)


class TodoTests(TestCase):

    def test_todo_appear_after_creation(self):
        todo = create_todo("Go to class", False)
        response = self.client.get(reverse("todo:index"))
        self.assertContains(response, "Go to class")

    def test_todo_disappear_after_done(self):
        todo = create_todo("Find a computer",False)
        # print(todo.done)
        # print(todo.id)
        response = self.client.get(reverse("todo:done", args=(todo.id,)))
        todo = get_todo(todo.id)
        response_done = self.client.post(reverse("todo:index"))
        self.assertNotContains(response_done, "Find a computer")
        self.assertTrue(todo.done)

    def test_done_redirects_to_index(self):
        todo = create_todo("Take a walk",False)
        response = self.client.get(reverse("todo:done", args=(todo.id,)))
        self.assertEqual(response.url, "/todo/")

    def test_404_response_with_incorrect_id(self):
        id = 1
        # todo = create_todo("Jogging", False)
        while True:
            try:
                todo = get_todo(id)
            except Todo.DoesNotExist:
                break
            id += 1
        # print("id =", id)
        response = self.client.get(reverse("todo:done", args=(id,)))
        self.assertEqual(response.status_code, 404)
        # print(response.status_code)
