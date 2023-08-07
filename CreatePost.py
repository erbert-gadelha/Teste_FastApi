import sqlite3

class CreatePost:
    def __init__(self, cursor):
        cursor.execute('SELECT * FROM post');
        self.count = len(cursor.fetchall());
    
    def criaPost(self, post, cursor):
        index = self.count;
        self.count = self.count + 1;

        cursor.execute('INSERT INTO post (id, user, title, body) VALUES ({0}, "{1}", "{2}", "{3}")'.format(index, post['user'], post['title'], post['body']));
        for tag in post['tags']:
            cursor.execute('INSERT INTO post_tag (post, tag) VALUES ({0}, "{1}")'.format(index, tag));
        
