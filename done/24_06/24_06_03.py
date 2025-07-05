
from __future__ import annotations
import sqlite3, smtplib, ssl, datetime
from typing import Optional, List
from email.message import EmailMessage

DB_PATH = "users.sqlite3"

class User:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        middle_name: str,
        birthday: datetime.date,
        email: str,
        user_id: Optional[int] = None,
    ):
        self.id = user_id
        self.first_name, self.last_name = first_name, last_name
        self.middle_name, self.birthday, self.email = middle_name, birthday, email

    def get_full_name(self) -> str:
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_short_name(self) -> str:
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."

    def get_age(self) -> int:
        today = datetime.date.today()
        years = today.year - self.birthday.year
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            years -= 1
        return years

    def __str__(self) -> str:
        return f"{self.get_full_name()} ({self.birthday.isoformat()})"

#Database
def _get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               first_name TEXT, last_name TEXT, middle_name TEXT,
               birthday TEXT, email TEXT UNIQUE)"""
    )
    return conn

def add_user_to_db(user: User) -> User:
    conn = _get_conn()

    # Проверка на существование email
    cur = conn.execute("SELECT id FROM users WHERE email = ?", (user.email,))
    row = cur.fetchone()
    if row:
        raise ValueError(f"Користувач з email {user.email} вже існує в базі.")

    with conn:
        cur = conn.execute(
            """INSERT INTO users(first_name, last_name, middle_name, birthday, email)
               VALUES(?, ?, ?, ?, ?)""",
            (
                user.first_name,
                user.last_name,
                user.middle_name,
                user.birthday.isoformat(),
                user.email,
            ),
        )
        user.id = cur.lastrowid
    return user

def search_users(
    *, first_name: str = "", last_name: str = "", email: str = ""
) -> List[User]:
    conn = _get_conn()
    query = (
        "SELECT id,first_name,last_name,middle_name,birthday,email "
        "FROM users WHERE 1=1"
    )
    params: list[str] = []
    if first_name:
        query += " AND first_name LIKE ?"
        params.append(f"%{first_name}%")
    if last_name:
        query += " AND last_name LIKE ?"
        params.append(f"%{last_name}%")
    if email:
        query += " AND email LIKE ?"
        params.append(f"%{email}%")

    cur = conn.execute(query, params)
    rows = cur.fetchall()
    return [
        User(
            r[1], r[2], r[3],
            datetime.date.fromisoformat(r[4]),
            r[5], user_id=r[0]
        )
        for r in rows
    ]

#SMTP
def send_welcome_email(user: User) -> None:
    smtp_user = "litus.dev@gmail.com"
    smtp_pass = "shgs wdja thov levc"

    msg = EmailMessage()
    msg["Subject"] = "Дякуємо за реєстрацію!"
    msg["From"] = smtp_user
    msg["To"] = user.email
    msg.set_content(
        f"Вітаємо, {user.get_full_name()}!\n"
        "Дякуємо, що приєдналися до нашого сервісу."
    )

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(smtp_user, smtp_pass)
        smtp.send_message(msg)

#registration
def register_user(user: User) -> User:
    user = add_user_to_db(user)
    send_welcome_email(user)
    return user


if __name__ == "__main__":
    u = User(
        "Ігор", "Петров", "Сергійович",
        datetime.date(2000, 5, 12),
        "litus.work@gmail.com",
    )
    registered = register_user(u)
    print("Зареєстровано:", registered)
