# create update read delete index
CRUDI stands for Create Update Read Delete Index. This referes to the databases. We utilize HTTP requests to either create, udate, read, delete, or get the index of an item in our database. See table below for how it relates to our guided exploration 3.


| ACTION | MEANING | HTTP | URI in admin|
|  -- | -- | -- | -- |
| CREATE | Create new instance | POST | .../student/add/ |
| Read | Retrieve resource instance | GET | ../student/# ?|
| Update | Modify existing resource | PUT | ../student/#/change|
| Delete | Destroy | DELETE|../student/#/delete |
| index | Enumerate collection | GET | ../student/#/  ? |

## other
The following code should allow us to see our objects on the website, so a read/GET. It does create a button on the admin side that says view on site; however, as of now it does not work. 

```python
def get_absolute_url(self):
        return reverse("student-detail", args=[str(self.id)])
```

Later we will be able to use this with views and templates to get a URI that brings us to a page where users can perform their own CRUDI/HTTP requests. 

Resources:

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

https://www.youtube.com/watch?v=mOu9fpfzyUg&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=5