from datetime import datetime, timedelta

def get_upcomming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        try:
            birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:
            continue

        birthday_this_year = birthday_date.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_date:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:  # Saturday
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Sunday
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return result

users = [
    {"name": "John Doe", "birthday": "1985.07.18"},
    {"name": "Jane Smith", "birthday": "1990.07.16"},
    {"name": "Weekend Test", "birthday": "1992.07.28"},
    {"name": "Old Date", "birthday": "1980.01.01"},
    {"name": "Invalid Format", "birthday": "01-01-1980"},
    {"name": "Alice Johnson", "birthday": "1975.12.05"},
    {"name": "Bob Brown", "birthday": "2001.03.15"},
    {"name": "Charlie Black", "birthday": "1968.06.22"},
    {"name": "Diana Blue", "birthday": "2005.11.30"},
    {"name": "Edward Green", "birthday": "1999.08.09"},
    {"name": "Fake Format 1", "birthday": "1998/04/20"},
    {"name": "Gregory Hall", "birthday": "1982.10.11"},
    {"name": "Hannah Lee", "birthday": "1995.01.25"},
    {"name": "Ivan Grey", "birthday": "1979.09.03"},
    {"name": "Julia White", "birthday": "1987.04.17"},
    {"name": "Kevin Stone", "birthday": "1993.06.29"},
    {"name": "Laura Moon", "birthday": "1965.02.14"},
    {"name": "Michael Sun", "birthday": "2000.12.01"},
    {"name": "Nancy Star", "birthday": "1989.05.08"},
    {"name": "Oscar Knight", "birthday": "1991.07.07"},
    {"name": "Patricia Wave", "birthday": "1972.03.10"},
    {"name": "Quentin River", "birthday": "2004.09.21"},
    {"name": "Rachel Cloud", "birthday": "1984.08.18"},
    {"name": "Steven Fire", "birthday": "1978.01.12"},
    {"name": "Test Format 2", "birthday": "15.05.1990"},
    {"name": "Uma Frost", "birthday": "1996.10.05"},
    {"name": "Victor Ash", "birthday": "1969.11.30"},
    {"name": "Wendy Lake", "birthday": "2002.02.22"},
    {"name": "Xander Peak", "birthday": "1994.12.15"},
    {"name": "Yara Breeze", "birthday": "1983.06.06"}
]

upcoming_birthdays = get_upcomming_birthdays(users)
print("Список привітань на цьому тиждні:", upcoming_birthdays) 