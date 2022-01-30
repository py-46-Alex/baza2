import sqlalchemy

bdaa = 'postgresql://meloman1:meloman1@localhost:5432/muzofond'
engine = sqlalchemy.create_engine(bdaa)
connection = engine.connect()
#connection.execute("""INSERT INTO artist(id, name, band, genre) VALUES(1, 'WSheyla', 'Woman in jaaz', 'jaaz');""")


# connection.execute("""INSERT INTO artist(id, name, band, genre) VALUES(2, 'LP', 'Laura Perzelotti', 'Rock');""")
# connection.execute("""INSERT INTO artist(id, name, band, genre) VALUES(3, 'Metallica', 'Sperman', 'Hell metall');""")
# connection.execute("""INSERT INTO artist(id, name, band, genre) VALUES(4, 'ACDC', 'Spiderman', 'Hard Rock');""")
# connection.execute("""INSERT INTO artist(id, name, band, genre) VALUES(5, 'Limp bizkit', 'Jon Doe', 'Rock');""")
# connection.execute("""INSERT INTO artist(id, name, band, genre) VALUES(6, 'Николай Басков', 'Басков Николай', 'Попсятина');""")
# connection.execute("""INSERT INTO artist(id, name, band, genre) VALUES(7, 'My best friend', 'Man that Plays', 'Rock');""")
# connection.execute("""INSERT INTO artist(id, name, band, genre) VALUES(8, 'Elvies Presley', 'The King', 'Classic');""")

# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(1, 2, 'The King', 2004);""")
# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(2, 2, 'The Queen', 2005);""")
# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(7, 1, 'My kife is Jaaz', 1999);""")
# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(3, 2, 'My knife is Jaaz', 1999);""")
# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(4, 2, 'My knifes in Jaazes', 1998);""")
# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(5, 2, 'My knifes', 1997);""")
# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(6, 2, 'My knifes in Jaazes', 1998);""")
# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(8, 3, 'All you need is FOK', 2008);""")
# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(9, 4, 'My friends like my', 2009);""")
# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(10, 5, 'My songs', 2019);""")
# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(11, 6, 'Мусорная попса', 2017);""")
# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(12, 7, 'Strange things', 2013);""")
# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(13, 8, 'Kings album', 2007);""")
# connection.execute("""INSERT INTO albums(album_id, artist_id, album_name, year) VALUES(14, 8, 'Allalbums', 2008);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(1, 'First day', 182, 1);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(3, 'Second day', 183, 1);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(4, 'Second day', 184, 2);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(5, 'Secondry day', 172, 3);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(6, '1Secondry day', 282, 4);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(7, 'Human', 212, 5);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(8, 'Lie', 213, 6);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(9, 'Love', 214, 7);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(10, 'Hater', 215, 8);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(11, 'Always', 290, 9);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(12, 'ForgetMe', 292, 10);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(13, 'Mellon', 150, 11);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(14, 'Noodele', 112, 2);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(15, 'My Hobbie', 299, 2);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(17, 'My life', 299, 2);""")
# connection.execute("""INSERT INTO track_info(track_id, track_name, time_of_track, album_in_id) VALUES(18, 'longest', 309, 2);""")

# название и год выхода альбомов, вышедших в 2018 году;
# juio = connection.execute("""SELECT id, band FROM artist;""").fetchmany(10)
# first1 = connection.execute("""SELECT album_name, year FROM albums WHERE year=2008;""").fetchmany(100)
# print(first1)

#название и продолжительность самого длительного трека;
name_of_track = connection.execute("""SELECT track_name, time_of_track FROM track_info ORDER BY time_of_track DESC;""").fetchmany(1)[0][0]
seconds_of_track = connection.execute("""SELECT time_of_track FROM track_info ORDER BY time_of_track DESC;""").fetchmany(1)[0][0]
print(f'Cамый длинный трэк в базе назван {name_of_track},  продолжительность трэка {seconds_of_track} секунд ')

#название треков, продолжительность которых не менее 3,5 минуты;
litle_track = connection.execute("""SELECT track_name FROM track_info WHERE time_of_track > 209;""").fetchmany(1000)
print(f'Имена трэков более 3.5 минут: {litle_track}')

#названия сборников, вышедших в период с 2018 по 2020 год включительно;
name_of_alboms = connection.execute("""SELECT album_name FROM albums WHERE year BETWEEN 2018 AND 2020;""").fetchmany(1000)
print(f'Имена сборников вышедших в период с 2018 по 2020 год: {name_of_alboms}')

#исполнители, чье имя состоит из 1 слова;
#thing_1 = connection.execute("""SELECT name FROM artist WHERE len(name) = 1;""").fetchmany(1000)
#print(f'Исполнители, чье имя состоит из 1 слова: {thing_1}')
# Не понял почему не работает запрос

# название треков, которые содержат слово "мой"/"my"
my_like = connection.execute("""SELECT track_name FROM track_info WHERE track_name iLIKE '%%my%%';""").fetchmany(1000)
my_like2 = connection.execute("""SELECT track_name FROM track_info WHERE track_name iLIKE '%%мой%%';""").fetchmany(1000)
print(f'Песни где есть слово "мой"/"my" : {my_like} {my_like2}')