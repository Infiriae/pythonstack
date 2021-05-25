from django.contrib import messages


def like(request,id):

    user = User.objects.get(id=request.session["user_logged_in"])

    quote = Quote.objects.get(id=id)

    quote.fans.add(user)

    movie_id = quote.movie.id

    return redirect(f'/quotes/{movie_id})


def activity(request):

    context = {
        user

    }

    return render(request,"activity.html",context)


class MovieManager(models.Manager):
    def validate(self,postData):
        errors = {}
        if len(postData['title'])<2:
            errors['title'] = "Title cannot be less than 2 characters"
        if len(postData['director'])<2:
            errors['director'] = "Director cannot be less than 2 characters"
        return errors


class Movie(models.Model):
    objects = MovieManager()

def add_movie(request):
    errors = Movie.objects.validate(request.POST)

    if errors:
        for error in errors.values()
            messages.error(request,error)
        return redirect("/")

class UserManager(models.Manager):
    def validate(self,formData):
        errors = {}

        if len(formData["first_name"]) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(formData["last_name"]) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        if len(formData["email"]) < 2:
            errors['email'] = "Email should be at least 2 characters"
        if len(formData["password"]) < 2:
            errors['password'] = "Password should be at least 2 characters"
        if formData["confirm_password"] != formData['password']:
            errors['confirm_password'] = "Password doesn't match"

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    objects =
