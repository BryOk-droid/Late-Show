from server.app import create_app, db
from server.models import Guest, Episode, Appearance
from datetime import date

app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()

   
    guest1 = Guest(name="Trevor Noah", occupation="Comedian")
    guest2 = Guest(name="Zendaya", occupation="Actress")
    guest3 = Guest(name="Elon Musk", occupation="Entrepreneur")
    guest4 = Guest(name="Michelle Obama", occupation="Author")

    
    ep1 = Episode(date=date(2024, 6, 10), number=101)
    ep2 = Episode(date=date(2024, 6, 11), number=102)
    ep3 = Episode(date=date(2024, 6, 12), number=103)
    ep4 = Episode(date=date(2024, 6, 13), number=104)

    
    app1 = Appearance(guest=guest1, episode=ep1, rating=5)
    app2 = Appearance(guest=guest2, episode=ep2, rating=4)
    app3 = Appearance(guest=guest3, episode=ep3, rating=3)
    app4 = Appearance(guest=guest4, episode=ep4, rating=5)
    app5 = Appearance(guest=guest2, episode=ep3, rating=4)
    app6 = Appearance(guest=guest1, episode=ep4, rating=5)

    
    db.session.add_all([guest1, guest2, guest3, guest4, ep1, ep2, ep3, ep4, app1, app2, app3, app4, app5, app6])
    db.session.commit()

    print("✅ Done seeding!")
