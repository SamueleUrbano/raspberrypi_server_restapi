import datetime

class Badge:

    database_id        : int
    badge_id           : str
    formal_badge_id    : str
    first_name         : str
    last_name          : str
    birth_date         : datetime
    phone_number       : str
    email_address      : str
    created_date       : datetime
    last_modified_date : datetime
    is_active          : bool
    activation_date    : datetime
    is_expired         : bool
    expiration_date    : datetime
    created_by_id      : int
    last_modified_by_id: int

    def __init__( self, database_id, badge_id, formal_badge_id, first_name, last_name, birth_date, phone_number, email_address, created_date, last_modified_date, is_active, activation_date, is_expired, expiration_date, created_by_id, last_modified_by_id ):
        self.database_id         = database_id
        self.badge_id            = badge_id
        self.formal_badge_id     = formal_badge_id
        self.first_name          = first_name
        self.last_name           = last_name
        self.birth_date          = birth_date
        self.phone_number        = phone_number
        self.email_address       = email_address
        self.created_date        = created_date
        self.last_modified_date  = last_modified_date
        self.is_active           = is_active
        self.activation_date     = activation_date
        self.is_expired          = is_expired
        self.expiration_date     = expiration_date
        self.created_by_id       = created_by_id
        self.last_modified_by_id = last_modified_by_id

    def __repr__(self):
        return f"""Badge: 
                        database_id = { self.database_id },
                        badge_id = { self.badge_id },
                        formal_badge_id = { self.formal_badge_id },
                        first_name = { self.first_name },
                        last_name = { self.last_name },
                        birth_date = { self.birth_date },
                        phone_number = { self.phone_number },
                        email_address = { self.email_address },
                        created_date = { self.created_date },
                        last_modified_date = { self.last_modified_date }
                        is_active = { self.is_active },
                        activation_date = { self.activation_date },
                        is_expired = { self.is_expired },
                        expiration_date = { self.expiration_date },
                        created_by_id = { self.created_by_id }, 
                        last_modified_by_id = { self.last_modified_by_id }
                """