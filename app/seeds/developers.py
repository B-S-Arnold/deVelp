from app.models import db, Developer, Skill

# Adds a demo user, you can add other users here if you want
def seed_developers():
    demo = Developer(
        name='demos biz',
        icon='blah blah blah...',
        bio='I am literally the BEST!!!',
        userId=1,
        city='Nowhere',
        state='Alaska'
        )

    skill1 = Skill.query.get(1)
    demo.skills.append(
      skill1
    )

    bryan = Developer(
        name='bryan',
        icon='my awesome icon',
        bio='I love pug',
        userId=4,
        city='Charleston',
        state='West Virginia'
        )

    skill2 = Skill.query.get(2)
    bryan.skills.append(
      skill1
    )
    bryan.skills.append(
      skill2
    )

    # print(Developer.query.get(1))

    # .extend

    casey = Developer(
        name='casey',
        icon='my awesome icon',
        bio='Redux is my favorite',
        userId=5,
        city='Denver',
        state='Colorado'
        )

    skill3 = Skill.query.get(3)
    casey.skills.append(
      skill3
    )

    charles = Developer(
        name='charles',
        icon='my awesome icon',
        bio='Bootstrap is where its at!',
        userId=6,
        city='Somewhere',
        state='Over_The_Rainbow'
        )

    skill4 = Skill.query.get(4)
    charles.skills.append(
      skill4
    )

    jake = Developer(
        name='jake',
        icon='my awesome icon',
        bio='I like recursion...',
        userId=7,
        city='Boonies',
        state='Utah'
        )

    skill5 = Skill.query.get(5)
    jake.skills.append(
      skill5
    )

    db.session.add(demo)
    db.session.add(bryan)
    db.session.add(casey)
    db.session.add(charles)
    db.session.add(jake)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_developers():
    db.session.execute('TRUNCATE developers RESTART IDENTITY CASCADE;')
    db.session.commit()
