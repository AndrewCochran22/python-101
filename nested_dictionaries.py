ramit = {
    "name": "Ramit",
    "email": "ramit@gmail.com",
    "interests": ["movies", "tennis"],
    "friends": [
        {
            "name": "Jasmine",
            "email": "jasmine@yahoo.com",
            "interests": ["photography", "tennis"]
        },
        {
            "name": "Jan",
            "email": "jan@hotmail.com",
            "interests": ["movies", "tv"]
        }
    ]
}

email = ramit["email"]
print("Ramit's email address is, " +  email + ".")

interests = ramit["interests"][0]
print("Ramit's first interest is, " + interests + ".")

email1 = ramit["friends"][0]["email"]
print("Jasmine's email is, " + email1 + ".")

jan_int = ramit["friends"][1]["interests"][1]
print("Jan's second interest is: " + jan_int)