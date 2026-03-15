# ── Product data ──────────────────────────────
product_id   = 1001            # whole number → int
product_name  = "iPhone 15"    # text → str
price      =79999.99       # decimal → float
discount     = 10.5           # percentage → float
stock_qty     = 50             # count → int
is_available   =True           # yes/no → bool
is_featured   : bool  = False          # yes/no → bool
description   : str   = "Latest iPhone from Apple"
offer_code    : str | None = None      # optional → None if no offer

# ── Calculate final price ─────────────────────
discount_amt  = price * discount / 100
final_price   = price - discount_amt
gst           = final_price * 0.18
total_price   = final_price + gst

print("=" * 40)
print("       PRODUCT DETAILS")
print("=" * 40)
print(f"  Product   : {product_name}")
print(f"  Price     : ₹{price:,.2f}")
print(f"  Discount  : ₹{discount_amt:,.2f} ({discount}% off)")
print(f"  After disc: ₹{final_price:,.2f}")
print(f"  GST (18%) : ₹{gst:,.2f}")
print(f"  Total     : ₹{total_price:,.2f}")
print(f"  In Stock  : {is_available}")
print(f"  Offer Code: {offer_code}")
print("=" * 40)


# user_registration.py
# Exactly how Zomato, Swiggy, Instagram store users

def register_user(
    name      : str,
    email     : str,
    age       : int,
    password  : str,
    phone     : str,
    is_premium: bool = False
) -> dict:
    """
    Registers a new user.
    Returns user profile dict — exactly like a database row.
    """

    # ── Validate email ────────────────────────
    if "@" not in email or "." not in email:
        return {"success": False, "message": "Invalid email!"}

    # ── Validate age ──────────────────────────
    if age < 18:
        return {"success": False, "message": "Must be 18 or older!"}

    # ── Validate password ─────────────────────
    if len(password) < 8:
        return {"success": False, "message": "Password too short!"}

    # ── Create user profile ───────────────────
    user = {
        # int fields
        "user_id"        : 1001,
        "age"            : age,
        "login_count"    : 0,

        # str fields
        "name"           : name.strip(),          # remove spaces
        "email"          : email.lower(),         # always lowercase
        "phone"          : phone,

        # bool fields
        "is_active"      : True,
        "is_verified"    : False,                 # email not verified yet
        "is_premium"     : is_premium,
        "is_admin"       : False,

        # None fields — not available yet
        "last_login"     : None,                  # never logged in
        "profile_pic"    : None,                  # not uploaded yet
        "middle_name"    : None,                  # optional field
        "deleted_at"     : None,                  # not deleted
    }

    return {"success": True, "message": "Registered!", "user": user}


# ── Test it ───────────────────────────────────
if __name__ == "__main__":

    # Valid registration
    result = register_user(
        name       = "Subham Kumar Das",
        email      = "Subham@Gmail.Com",     # mixed case — gets lowercased
        age        = 21,
        password   = "Subham@123",
        phone      = "9876543210",
        is_premium = False
    )

    if result["success"]:
        user = result["user"]
        print("\n✅ Registration Successful!")
        print("-" * 35)
        print(f"  ID         : {user['user_id']}")
        print(f"  Name       : {user['name']}")
        print(f"  Email      : {user['email']}")  # lowercase applied!
        print(f"  Age        : {user['age']}")
        print(f"  Active     : {user['is_active']}")
        print(f"  Verified   : {user['is_verified']}")
        print(f"  Premium    : {user['is_premium']}")
        print(f"  Last Login : {user['last_login']}")  # None
        print(f"  Profile Pic: {user['profile_pic']}") # None
    else:
        print(f"❌ Failed: {result['message']}")

    print()

    # Invalid — underage
    result2 = register_user("Kid", "kid@gmail.com", 15, "pass1234", "1234567890")
    print(f"Underage test : {result2['message']}")

    # Invalid — bad email
    result3 = register_user("Test", "notanemail", 21, "pass1234", "1234567890")
    print(f"Bad email test: {result3['message']}")