import datetime
import json
import random
import time

# from django.utils.timezone import now

import requests
t = (datetime.datetime.now() - datetime.timedelta(days=10)).strftime('%Y-%m-%d %H:%M:%S')

# pk => 数据库自行处理
# fk => 先建立 fk 对象，再建立当前对象
# attr =>
# m2m => 稍后处理

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'confs.settings')
django.setup()
from music.models import m_major as m

def get(url):
    # return requests.get(url).json()
    return json.loads(requests.get(url).content)


from django.contrib.admin import register
def gen_aUser_User_Artist(rg1: tuple=(0,1), rg2: tuple=(0,5)):
    res = get('http://localhost:4000/toplist/artist')
    for v in res['list']['artists'][rg1[0]:rg1[1]]:
        name = v['name']
        qq = random.randint(1000000000, 9999999999)

        u1 = m.auth_User.objects.create_user(username=name, email=f'{qq}@qq.com', password='123',
                                        first_name=f'{name[0]}', last_name=f'{name[1:]}',
                                        is_staff=True, is_active=True,is_superuser=True,
                                        date_joined=t,last_login=t)
        u2 = m.User.objects.create(avatar_id=m.Image.generate(v['img1v1Url']),location_id=random.randint(1,3210),origin_user=u1,
                                   birthday=t,cellphone=f'{random.randint(1000000000, 9999999999)}',experience=random.randint(0,100),
                                   gender=0,github='https://github.com/example',nickname=name,qq=qq)
        desc = get(f'http://localhost:4000/artists?id={v["id"]}')['artist']['briefDesc']
        u3 = m.Artist.objects.create(account=u2,background_id=m.Image.generate(v['picUrl']),description=desc,joined_time=t,stagename=name)
        # u3 = m.Artist.objects.get(pk=2)
        print(u1,u2,u3)

        # songs = get(f'http://localhost:4000/artists?id={v["id"]}')['hotSongs']
        songs = get(f'http://localhost:4000/artist/top/song?id={v["id"]}')['songs']
        print(songs[0])
        # albums = get(f'http://localhost:4000/artist/album?id={v["id"]}&limit=30')['hotAlbums']

        al_ids = {}
        for s in songs[rg2[0]:rg2[1]]:
            img = m.Image.generate(s['al']['picUrl'])
            # img = 9
            al = None
            if not al_ids.get(s['al']['id']):
                al = m.Album.objects.create(artist=u3,background_id=img,
                                            count=random.randint(0,100),description='',
                                            liked_count=random.randint(0,100),pub_company='WXU',
                                            pub_date=t,shared_count=random.randint(0,100),
                                            title=s['al']['name'])
                al_ids[s['al']['id']] = al.id
            else:
                al = m.Album.objects.get(pk=al_ids[s['al']['id']])

            ly = get(f'http://localhost:4000/lyric?id={s["id"]}')['lrc']['lyric']
            s_url = None
            try:
                # s_url = get(f'http://localhost:4000/song/url?id={s["id"]}')['data'][0]['url']
                s_url = get(f'https://dataiqs.com/api/netease/music/?type=songid&id={s["id"]}')['song_url']
                # s_url = f'http://music.163.com/song/media/outer/url?id={s["id"]}.mp3'

            except Exception as e:
                print(get(f'http://localhost:4000/song/url?id={s["id"]}'))
                if input('删库否(Y/N)') == 'Y':
                    m.Song.objects.all().delete()
                    m.Album.objects.all().delete()
                    m.Artist.objects.all().delete()
                    m.User.objects.all().delete()
                    m.auth_User.objects.all().delete()
                return
            s_ = m.Song.objects.create(album=al,img_id=img,
                                  count=random.randint(0,100),data=m.Song.generate_data(s_url),
                                  liked_count=random.randint(0,100),lyrics=ly,pub_date=t,
                                  shared_count=random.randint(0,100),title=s['name'])
            print(s_)

            # time.sleep(1)


# def gen_artist_song(id,length):
#     res = get('http://localhost:4000/toplist/artist').content
#     for v in json.loads(res)['list']['artists'][:length]:

# def gen_artist_album(api_id, id, length):
#     res = get('http://localhost:4000/toplist/artist').content
#     for v in json.loads(res)['list']['artists'][:length]:

# m.Song.objects.all().delete()
# m.Album.objects.all().delete()
# m.Artist.objects.all().delete()
# m.User.objects.all().delete()
# m.auth_User.objects.all().delete()

if __name__ == '__main__':
    # m.Location.generate()

    # gen_aUser_User_Artist(10)

    gen_aUser_User_Artist((0,20),(0,5))
    # gen_aUser_User_Artist((2,5),(0,3))


    # m.PlayTag.generate()
    # m.VideoTag.generate()
    # m.ArtistTag.generate()

    pass
