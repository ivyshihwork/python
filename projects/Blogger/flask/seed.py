"""
Populate blogger database with fake data using the SQLAlchemy ORM.
"""

import random
import string
import hashlib
import secrets
from faker import Faker
from blogger.src.models import Person, Blog, Post, Comment, blog_follow, db
from blogger.src import create_app

PERSON_COUNT = 80
BLOG_COUNT = 30
POST_COUNT = 250
COMMENT_COUNT = 1200

# assert LIKE_COUNT <= (USER_COUNT * TWEET_COUNT)


def random_passhash():
    """Get hashed and salted password of length N | 8 <= N <= 15"""
    raw = ''.join(
        random.choices(
            string.ascii_letters + string.digits + '!@#$%&',  # valid pw characters
            k=random.randint(8, 15)  # length of pw
        )
    )

    salt = secrets.token_hex(16)

    return hashlib.sha512((raw + salt).encode('utf-8')).hexdigest()


def truncate_tables():
    """Delete all rows from database tables"""
    db.session.execute(blog_follow.delete())
    Comment.query.delete()
    Post.query.delete()
    Blog.query.delete()
    Person.query.delete()
    db.session.commit()


def main():
    """Main driver function"""
    app = create_app()
    app.app_context().push()
    truncate_tables()
    fake = Faker()
    #################
    # Create person
    #################
    last_person = None  # save last user
    for _ in range(PERSON_COUNT):
        fake = Faker()
        first_name = fake.first_name(),
        last_name = fake.last_name()
        last_person = Person(
            first_name=first_name,
            last_name=last_name,
            username=first_name[0][0].lower(
            ) + last_name.lower() + str(random.randint(1, 150)),
            password=random_passhash()

        )
        db.session.add(last_person)

    # insert Person
    db.session.commit()
    #################
    # Create Blog
    #################
    last_blog = None  # save last tweet
    for _ in range(BLOG_COUNT):
        fake = Faker()
        last_blog = Blog(
            title=fake.sentence(),
            summary=fake.paragraph(nb_sentences=3),
            last_action=random.choice(['Created', 'Updated']),
            last_updated=fake.past_datetime(start_date='-3y'),
            person_id=random.randint(
                last_person.id - PERSON_COUNT + 1, last_person.id)
        )
        db.session.add(last_blog)

    # # insert blog
    db.session.commit()
    ####################################################################
    # person relationship with blog - subquery in Blog called Follows
    ####################################################################
    person_blog_pairs = set()
    while len(person_blog_pairs) < BLOG_COUNT:

        candidate = (
            random.randint(last_person.id - PERSON_COUNT + 1, last_person.id),
            random.randint(last_blog.id - BLOG_COUNT + 1, last_blog.id)
        )

        if candidate in person_blog_pairs:
            continue  # pairs must be unique

        person_blog_pairs.add(candidate)

    new_blog_follow = [{"person_id": pair[0], "blog_id": pair[1]}
                       for pair in list(person_blog_pairs)]
    insert_blog_follow_query = blog_follow.insert().values(new_blog_follow)
    db.session.execute(insert_blog_follow_query)

    # insert blog_follow
    db.session.commit()

    #################
    # Create Post
    #################
    last_post = None
    for _ in range(POST_COUNT):
        last_post = Post(
            title=fake.sentence(),
            content=fake.text(),
            last_action=random.choice(['Created', 'Updated']),
            last_updated=fake.past_datetime(start_date='-30d'),
            blog_id=random.randint(
                last_blog.id - BLOG_COUNT + 1, last_blog.id)
        )
        db.session.add(last_post)

    # insert blog
    db.session.commit()

    #################
    # Create Comment
    #################
    last_comment = None
    for _ in range(COMMENT_COUNT):
        last_comment = Comment(
            content=fake.text(),
            last_action=random.choice(['Created', 'Updated']),
            last_updated=fake.past_datetime(start_date='-30d'),
            post_id=random.randint(
                last_post.id - POST_COUNT + 1, last_post.id),
            person_id=random.randint(
                last_person.id - PERSON_COUNT + 1, last_person.id)
        )
        db.session.add(last_comment)

    # insert blog
    db.session.commit()


# run script
main()
