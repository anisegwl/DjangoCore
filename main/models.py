from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Question(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False) 

    def __str__(self):
        return self.choice_text
    
class Publisher(models.Model):
	name = models.CharField(max_length=100)
	founded = models.IntegerField()
	location = models.CharField(max_length=100)
    
class Author(models.Model):
	name = models.CharField(max_length=100)
	birth_date = models.DateField()
	nationality = models.CharField(max_length=50)
    
class Book(models.Model):
	FICTION = 'F'
	NON_FICTION = 'NF'
	GENRE_CHOICES = [
    	(FICTION, 'Fiction'),
    	(NON_FICTION, 'Non-Fiction'),
	]
    
	title = models.CharField(max_length=200)
	genre = models.CharField(max_length=5, choices=GENRE_CHOICES)
	publish_date = models.DateField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
	authors = models.ManyToManyField(Author, related_name='books')

class Questions(models.Model):
   question_text = models.CharField(max_length=200)
   choice_1 = models.CharField(max_length=200)
   choice_2 = models.CharField(max_length=200)
   choice_3 = models.CharField(max_length=200)
   choice_4 = models.CharField(max_length=200)
   correct_answer = models.CharField(max_length=200, choices=[
       ('choice_1', 'Choice 1'),
       ('choice_2', 'Choice 2'),
       ('choice_3', 'Choice 3'),
       ('choice_4', 'Choice 4'),
   ])
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


   def __str__(self):
       return self.question_text[:50]
