from app import create_app
from models import db, user_datastore
from flask_security.utils import hash_password

app, _ = create_app()

with app.app_context():
    # 1️⃣ Create roles if not exist
    admin_role = user_datastore.find_or_create_role(name='admin', description='Administrator')
    user_role = user_datastore.find_or_create_role(name='user', description='User')
    db.session.commit()

    # 2️⃣ Check if admin user exists
    admin_user = user_datastore.find_user(email="admin@abc.com")
    
    if not admin_user:
        # Create admin user with role object
        admin_user = user_datastore.create_user(
            email="admin@abc.com",
            username="admin",
            password=hash_password("admin123"),
            roles=[admin_role]  # ✅ assign Role object, not string
        )
        db.session.commit()
        print("Admin user created and role assigned")
    else:
        # Admin exists but might not have a role
        if not admin_user.roles:
            user_datastore.add_role_to_user(admin_user, admin_role)
            db.session.commit()
            print("Admin role assigned to existing user")
        else:
            print("Admin user already has roles")
