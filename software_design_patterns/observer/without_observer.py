from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan

# register a new user
register_new_user("Muhammad Amir", "Am@ir", "amir@test.com")

# send a password reset message
password_forgotten("amir@test.com")

# upgrade the plan
upgrade_plan("amir@test.com")
