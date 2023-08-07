import sqlite3;
from CreatePost import CreatePost;
from SearchPost import SearchPost;

class AssertDB:
    
    def __init__(self, url):
        self._con = sqlite3.connect(url);
        self._cur = self._con.cursor();

        self.c_post = CreatePost(self.cur);
        self.s_post = SearchPost(self.cur);
    
        try:        
            self._cur.execute('SELECT * FROM post');
            self._cur.execute('SELECT * FROM post_tag');
        except sqlite3.OperationalError:

            try:
                self._cur.execute('DROP TABLE post');
            except sqlite3.OperationalError:
                pass;
            try:
                self._cur.execute('DROP TABLE post_tag');
            except sqlite3.OperationalError:
                pass;
            
            self._cur.execute('CREATE TABLE post(id, user, title, body)');
            self._cur.execute('CREATE TABLE post_tag (post, tag)');
            
            print("[aviso] Tabela 'post' e 'post_tag' foram criadas.");
    
    def settle(self):
        self._cur.execute('SELECT * FROM post');
        count = len(self._cur.fetchall());
        print(count);
        if(count > 0):
            return False;

        db = CreatePost(self._cur);
        db.criaPost( {'user': 'vinicius13', 'title': "pokemon eh massa", 'body': 'to gostando mto dos ultimos episodios. E vcs?', 'tags':['pokemon', 'anime']});
        db.criaPost( {'user': 'vinicius13', 'title': 'pokemon >> digimon', 'body': 'digimon eh paia dms kk', 'tags':['pokemon', 'digimon', 'humor']});
        db.criaPost( {'user': 'marquinh0s', 'title': 'one piece ta em hiato eh?', 'body': 'faz um tempo q n tem capitulo novo. Algm sabe?', 'tags':['one piece', 'op', 'gear 5', 'mangá']});
        db.criaPost( {'user': 'verona', 'title': 'party de genshin', 'body': 'alguma alma caridosa ta afim de me ajudar numa campnha nivel 8?', 'tags':['games', 'genshin impact', 'garena']});
        db.criaPost( {'user': 'aldebaram', 'title': 'esse seya eh um canalha', 'body': 'o bixo me atacou de costas,boy. isso n existe n. E olha q eu tava pegando leve com esse bixo visse', 'tags':['cdz']});
        db.criaPost( {'user': 'aiorus', 'title': 'counter pra ikki de fenix', 'body': 'tipo assim.. o cara sempre volta? alguem sabe alguma forma de causar morte morrida no cara?', 'tags':['cdz', 'cavaleiros do zodiaco']});
        db.criaPost( {'user': 'eren', 'title': 'tatakae', 'body': 'tatakae', 'tags':['aot', 'anime']});
        db.criaPost( {'user': 'pikachu', 'title': 'great ball', 'body': 'mais espacosa que a comum, menos confortavel que a ultra. Pelo preco acho que vale a pena', 'tags':['pokemon', 'humor']});
        self._con.commit();

        return True;
    



    def publishPost(self, post):
        return self.c_post.criaPost(post, self.cur)
    
    def searchForTags(self, tags):
        return self.s_post.getTags(tags, self.cur)
    
    def searchForPosts(self, posts):
        return self.s_post.getPosts(posts, self.cur)

    def getAllPosts(self):
        aux = self.s_post.getAll(self.cur)
        return aux

    def getAllTags(self):
        return self.s_post.getTags(self.cur)










    @property
    def con(self):
        return self._con;

    @con.setter
    def con(self, param):
        return None;

    @property
    def cur(self):
        return self._cur;

    @cur.setter
    def cur(self, param):
        return None;