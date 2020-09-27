from django.test import TestCase
from django.urls import reverse
from todo.models import Todo

# Create your tests here.
def create_todo(description, done):
    return Todo.objects.create(description=description, done=done)


class TodoTests(TestCase):

    def test_1(self):
        todo = create_todo("Go to class", False)
        todo.save()
        response = self.client.get(reverse("todo:index"))
        self.assertContains(response, "Go to class")

    def test_2(self):
        todo = create_todo("Find a computer",False)
        todo.save()
        print(todo.done)
        print(todo.id)
        # how to invoke a url???
        response = self.client.get(reverse("todo:done", pk = todo.id))

        print(todo.done)
        # self.assertContains(response, "Find a computer")
        # t = Todo.objects.get(id=todo_id)
        # response_done = self.client.post('/todo', {'id': })
        # self.assertNotContains(response_done,"Find a computer")
        # self.assertContains(response_done,"marked as done")

    # def test_3(self):
    #     se

