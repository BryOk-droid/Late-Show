from server.app import create_app, db
from server.models import Guest, Episode, Appearance
from datetime import date

app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    # Clear old data
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()

    # Guests
    guest1 = Guest(name="Trevor Noah", occupation="Comedian")
    guest2 = Guest(name="Zendaya", occupation="Actress")

    # Episodes
    ep1 = Episode(date=date(2024, 6, 10), number=101)
    ep2 = Episode(date=date(2024, 6, 11), number=102)

    # Appearances
    app1 = Appearance(guest=guest1, episode=ep1, rating=5)
    app2 = Appearance(guest=guest2, episode=ep2, rating=4)

    # Add and commit
    db.session.add_all([guest1, guest2, ep1, ep2, app1, app2])
    db.session.commit()

    print("✅ Done seeding!")
