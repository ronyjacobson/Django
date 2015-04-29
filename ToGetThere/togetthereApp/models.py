from django.db import models
import datetime

# Change your models (in models.py).
# Run python manage.py makemigrations <App Name> to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.



class User(models.Model):
    facebook_id = models.CharField(unique=True, max_length=30, blank = True)
    first_name = models.CharField(max_length=35, db_index=True)
    last_name = models.CharField(max_length=35, db_index=True, blank = True)
    email = models.EmailField(unique=True, db_index=True, blank = True)
    birthday = models.DateField(blank = True)
    created = models.DateTimeField(auto_now_add=True)

    # bday =  datetime.datetime(year, month, day)
    # user = User(facebook_id = '', first_name= '', last_name= '', email = '', birthday=bday)

    def age(self):
        return (datetime.datetime.now().date() - self.birthday).days / 365

    def __unicode__(self):
        return self.first_name +" "+ self.last_name

    def as_json(self):
        return dict(
            id = self.pk,
            facebook_id = self.facebook_id,
            first_name = self.first_name,
            last_name = self.last_name,
            full_name = self.first_name +" "+ self.last_name,
            email = self.email,
            age = self.age(),
            birthday = self.birthday.isoformat(),
            created = self.created.isoformat())



class City(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __unicode__(self):
        return self.name

    def as_json(self):
        return dict(
            id = self.pk,
            city = self.name)



class Street(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField(max_length=50, db_index=True)

    def __unicode__(self):
        return self.name

    def as_json(self):
        cityName = City.objects.get(self.city)
        return dict(
            id = self.pk,
            street = self.name,
            city = cityName)




class SP(models.Model):
    # CATEGORIES:
    MEDICAL = 'medical'
    RESTAURANTS = 'restaurants'
    SHOPPING = 'shopping'
    PUBLIC_SERVICES = 'public_services'
    TRANSPORTATION = 'transportation'
    HELP = 'help'

    CATEGORY_CHOICES = (
        (MEDICAL, 'Medical'),
        (RESTAURANTS, 'Restaurants'),
        (SHOPPING, 'Shopping'),
        (PUBLIC_SERVICES, 'Public Services'),
        (TRANSPORTATION, 'Transportation'),
        (HELP, 'Help'),
    )


    # Fields:
    name = models.CharField(max_length=100, db_index=True)
    desc = models.CharField(max_length=225, blank = True)
    street_num = models.IntegerField(db_index=True)
    street = models.ForeignKey(Street)
    city = models.ForeignKey(City)
    longitude = models.DecimalField(max_digits=7, decimal_places=7, db_index=True, blank=True, null=True)
    latitude = models.DecimalField(max_digits=7, decimal_places=7, db_index=True, blank=True, null=True)
    phone = models.CharField(max_length=13, db_index=True, blank = True)
    is_verified = models.BooleanField(default=False)
    discount = models.IntegerField(default=0, db_index=True, blank = True)
    category = models.CharField(max_length=45, choices=CATEGORY_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    website = models.URLField(blank = True)
    rank =  models.BigIntegerField(default=0, blank=True)
    voters = models.IntegerField(default=0, blank=True)



    # Accessibility Fields

    # Functions
    class Meta:
        unique_together = (("name", "street", "street_num"),)



    def address(self):
        city = unicode(City.objects.get(self.city).name)
        street = Street.objects.get(self.street).name

    def __unicode__(self):
        return self.name + ', ' + self.address

    #Json Parsers
    def as_json(self, withReviews):
        cityName = self.city.name
        streetName = self.street.name

        response= dict(
            id = self.pk,
            name = self.name,
            desc = self.desc,
            city = cityName,
            street = streetName,
            streetNum = self.street_num,
            longitude = self.longitude,
            latitude = self.latitude,
            phone = self.phone,
            is_verified =self.is_verified,
            discount = self.discount,
            category =self.category,
            website = self.website)

        if (withReviews):
            reviews = self.review_set.all()
            reviewsList = list()
            for review in reviews:
                reviewsList.append(review.as_json())
            print reviewsList
            response['reviews'] = reviewsList

        return response





class Review(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField(blank = True)
    likes = models.IntegerField(default=0, blank= True, db_index=True)
    sp = models.ForeignKey(SP)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def as_json(self):
        return dict(
            id = self.pk,
            title = self.title,
            content = self.content,
            likes = self.likes,
            created = self.created.isoformat(),
            user = self.user.as_json())
