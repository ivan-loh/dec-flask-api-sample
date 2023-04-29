import random
import pymssql

# Define a list of possible usernames and emails
usernames = ["sophie", "joshua", "lily", "william", "mia", "ethan", "amelia", "jacob", "ava", "logan", "oliver",
             "emily", "noah", "isabella", "james", "charlotte", "samuel", "ella", "daniel", "grace", "henry", "evie",
             "alexander", "madison", "matthew", "abigail", "benjamin", "sophia", "mason", "scarlett", "luke", "mia",
             "leo", "hazel", "owen", "avery", "jackson", "lila", "elijah", "riley", "nathan", "piper", "sebastian",
             "claire", "liam", "taylor", "lucas", "audrey", "aaron", "violet", "zachary", "chloe", "david", "hannah",
             "isaac", "zoey", "jason", "leah", "connor", "brooke", "jeremiah", "nevaeh", "julian", "ruby", "carter",
             "katherine", "levi", "natalie", "wyatt", "ashley", "adrian", "alexa", "cameron", "zoey", "nolan",
             "addison", "colton", "clara", "parker", "elizabeth", "tristan", "may", "hudson", "faith", "landon",
             "sienna", "isaiah", "elsie"]
domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com", "live.com", "mail.com",
           "protonmail.com", "zoho.com", "fastmail.com", "inbox.com", "gmx.com", "yandex.com", "tutanota.com",
           "runbox.com", "startmail.com", "hushmail.com", "riseup.net", "posteo.de", "cock.li", "ctemplar.com", "pm.me",
           "keemail.me", "onionmail.org", "guerrillamail.com", "sharklasers.com", "mailinator.com", "dispostable.com",
           "10minutemail.com", "temp-mail.org", "throwawaymail.com", "getnada.com", "fakeinbox.com", "anonaddy.com",
           "burnermail.io", "mytemp.email", "maildrop.cc", "mailnesia.com", "scryptmail.com", "mailbox.org",
           "torguard.net", "lavabit.com", "runbox.com", "anonymousspeech.com", "sigaint.org", "bitmessage.ch",
           "torbox3uiot6wchz.onion", "protonirockerxow.onion", "vtimea6om7gdjp42.onion"]

# Define the number of random users to insert
num_users = 10

# Connect to the SQL Server database
conn = pymssql.connect(server='localhost',
                       port=1433,
                       database='devdb',
                       user='sa',
                       password='devDBpassword!@#$')

# Insert the specified number of random users into the database
for i in range(num_users):
    # Generate a random username and email
    username = random.choice(usernames) + str(i)
    email = username + "@" + random.choice(domains)
    print(username, email)

    # Insert the new user into the database
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
        conn.commit()

print("Successfully inserted {} random users into the database.".format(num_users))
