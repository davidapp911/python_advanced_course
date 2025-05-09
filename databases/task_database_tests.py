from sqlalchemy.orm import sessionmaker
import task_database_setup as db


def main():
    session = sessionmaker(bind=db.engine)
    session = session()

    # Generates 3 random films
    for i in range(3):
        new_film = db.Film(title=f"Film {i}", director=f"Director {i}", release_year=(2024 - i))
        session.add(new_film)
    session.commit()

    films = session.query(db.Film).all() # queries all  films out of the table

    for film in films:
        print(film)

    print("<<<<<< Updating Film 0 >>>>>>>>")
    film = session.query(db.Film).filter(db.Film.title == "Film 0").first()

    if film:
        film.title = f"The Chronicles of Narnia" # updates the film title
        session.commit()
    else:
        print("Film 0 not found")

    film = session.query(db.Film).filter(db.Film.title == "The Chronicles of Narnia").first()
    print(film)

    print("<<<<<< Deleting all films... >>>>>>>>")

    session.query(db.Film).delete() # removes all films
    session.commit()

    print(session.query(db.Film).all()) # show the empty table



if __name__ == "__main__":
    main()