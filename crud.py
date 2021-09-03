"""CRUD operations."""

from model import db, User, Location, Plan, Image, Event, Theme, PlanEvent, connect_to_db


def create_user(username, email, password):
    """Create and return a new user."""

    user = User(username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """Get all users from database."""    
    
    return User.query.all()

def get_user_by_id(num):   
    """Get all users from database."""    
    
    return User.query.filter_by(user_id=num).one()

def get_user_by_email(email):
    """Get a user by their email from database."""  

    return User.query.filter(User.email==email).first()


def add_like(event_id):
    """Add a like to an event."""

    update = Event.query.filter_by(event_id=event_id).first()
    update.liked += 1
    db.session.commit()


def create_location(zipcode, cityname, statename):
    """Create and return a new location."""

    location = Location(zipcode=zipcode, cityname=cityname, statename=statename)

    db.session.add(location)
    db.session.commit()

    return location

def get_locations():
    """Get all locations in database."""

    return Location.query.all()    

def get_location_by_id(location_id):
    """Get location and details by it's id from database."""    

    zipcode = Location.query.filter_by(location_id=location_id).one().zipcode
    city = Location.query.filter_by(location_id=location_id).one().cityname
    state = Location.query.filter_by(location_id=location_id).one().statename

    return [city,state,zipcode]


def create_plan(user_id,location_id,overview=None):
    """Create and return a new plan."""

    plan = Plan(user_id=user_id,location_id=location_id,overview=overview)

    db.session.add(plan)
    db.session.commit()

    return plan  

def del_plan_by_id(plan_id):
    """Delete a plan by plan id"""
    
    PlanEvent.query.filter_by(plan_id=plan_id).delete()
    Plan.query.filter_by(plan_id=plan_id).delete()
    db.session.commit()    

def edit_plan_overview(plan_id, overview):
    """Edit a plan's overview."""

    update = Plan.query.filter_by(plan_id=plan_id).one()
    update.overview = overview
    db.session.commit()    

def get_plans(user_id):
    """Return a specific user's plan(s)."""

    return Plan.query.filter_by(user_id=user_id).all()

def get_events_associated_with_plan(plan_id):
    """Return a specific plan's event(s)."""

    return Plan.query.filter_by(plan_id=plan_id).one().events    

def get_plan_by_planid(plan_id):
    """Return plan associated with a plan id."""

    return Plan.query.filter_by(plan_id=plan_id).one()

def get_location_by_planid(plan_id):
    """Return location associated with a plan id."""

    return Plan.query.filter_by(plan_id=plan_id).one().location_id

def create_image(image_location=None, event_id=None):
    """Create and return a new image."""

    image = Image(image_location=image_location, event_id=event_id)

    db.session.add(image)
    db.session.commit()

    return image    

def get_images(num=None):
    """Get all or a number of images from database."""    

    if num == None:
        return Image.query.all()  

    return Image.query.all()[:num]


def create_event(location_id, overview=None, datetime=None, liked=None):
    """Create and return a new event."""

    event = Event(location_id=location_id, overview=overview, datetime=datetime, liked=liked)
    # EX: >>>event5 = create_event(1,'Movie Night','2020,1,1')

    db.session.add(event)
    db.session.commit()

    return event

def get_events(num=None):
    """Get a specific number of events and their overview from database."""    

    if num == None:
        return Event.query.all() 

    return Event.query.all()[:num]

def get_event_by_id(event_id):
    """Show a specific event's details."""

    return Event.query.filter_by(event_id=event_id).one()


def create_theme(tag=None, overview=None):
    """Create and return a new theme."""

    theme = Theme(tag=tag, overview=overview)

    db.session.add(theme)
    db.session.commit()

    return theme     

def get_theme(): #TODO: change this to get only the event's themes; add eventtheme to seed.py
    """get some random themes."""

    return Theme.query.all()

def add_plan_events(plan_id, event_id):
    """Add event(s) to an existing plan."""

    plan_event = PlanEvent(plan_id=plan_id, event_id=event_id)

    db.session.add(plan_event)
    db.session.commit()

    return plan_event



if __name__ == '__main__':
    from server import app
    connect_to_db(app)