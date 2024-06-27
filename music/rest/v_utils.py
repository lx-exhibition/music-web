import datetime
import json
import random
import re
import time

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http.response import FileResponse

from utils.general import send_msg
from ..models import m_major as m
from . import s_rest as s

UTILS = ['email', 'register', 'login', 'logout', 'img', 'imgs', 'img-user',
         'my-artists', 'my-videos', 'my-CreatedSongLists', 'my-CollectedSongLists', 'my-Messages',
         'g-Artist', 'g-Song', 'g-Album', 'g-Comment','g-Video', 'g-PlayList', 'g-Message',
         'g-Search',
         'e-Recommends', 'e-Albums', 'e-PlayLists', 'e-Artists', 'e-Ranks',
         'o-Advanced', 'o-Download',

         'join', 'o-Friends',
         ]

def validate_email(req: Request):
    s = None
    try:
        s = req._request.session['email-token']
    except KeyError:
        raise ValidationError("未发送邮箱")

    t, token, receiver = s.split('$')
    sended_token = req.data.get('token')

    delta = time.time()-float(t)
    if delta > 60:
        raise ValidationError({'err': "邮箱验证超时(60s)"})
    if sended_token != token:
        raise ValidationError({'err': "验证码错误"})

    send_msg('邮箱验证成功', '邮箱验证成功', receiver)
    # return Response('邮箱验证成功')
    return True



@api_view(['GET', 'POST'])
def V_utils(req: Request, util, **kwargs):
    if util == 'email':
        token = '{:0<4d}'.format(random.randint(0,9999))
        receiver = req.query_params.get('email')

        req._request.session['email-token'] = f'{time.time()}${token}${receiver}'
        print(receiver)


        if not isinstance(receiver, str) or not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', receiver):
            raise ValidationError("邮箱格式错误, 邮箱格式形如 example@mail.com")

        send_msg('邮箱验证', f'验证码为[{token}], 请在 60 秒内完成邮箱验证', receiver)

        return Response('已发送邮箱验证码')



    if util == 'register' and req._request.method == 'POST':

        if not validate_email(req):
            raise ValidationError("邮箱验证错误")

        # (1) 创建并保存 auth_User 实例
        username = req.data.get('username')
        password = req.data.get('password')
        password_confirm = req.data.get('password_confirm')
        email = req.data.get('email')
        if password != password_confirm:
            raise ValidationError("两次密码不一致")
        try:
            user = m.auth_User.objects.create_user(username=username, password=password, email=email)
        except IntegrityError as e:
            raise ValidationError("用户名已存在")
        except ValueError:
            raise ValidationError("用户注册失败")

        # (2) 创建并保存 User 实例
        avatar = req.data.get('avatar')
        avatar_id = m.Image.objects.create(data=avatar).id
        location_id = req.data.get('location')
        origin_user = user
        birthday = req.data.get('birthday')
        cellphone = req.data.get('cellphone')
        gender = req.data.get('gender')
        github = req.data.get('github')
        nickname = req.data.get('nickname')
        qq = req.data.get('qq')
        try:
            u = m.User.objects.create(avatar_id=avatar_id, location_id=location_id, origin_user=origin_user,
                                  birthday=birthday, cellphone=cellphone, gender=gender, github=github,
                                  nickname=nickname, qq=qq)
            m.Artist.objects.create(account=u, background_id=avatar_id, stagename=nickname)
        except Exception:
            raise ValidationError("创建 User 实例失败")

        return Response("注册成功")

    if util == 'login' and req._request.method == 'POST':
        username = req.data.get('username')
        password = req.data.get('password')
        user = None
        try:
            user = authenticate(username=username, password=password)
        except ValidationError:
            raise ValidationError("用户名或密码为空")

        if user is None:
            raise ValidationError("用户不存在或密码错误")
        login(req, user)
        # print(dir(user))
        # print(user)

        return Response({'msg': "登录成功", 'id': user.user.pk, 'aid': user.user.artist.id})

    if util == 'logout' and req._request.method == 'POST':
        # print(req.COOKIES)
        logout(req)
        return Response("注销成功")

    if util == 'img' and req._request.method == 'GET':
        try:
            id = req.query_params['id']
        except Exception:
            raise ValidationError("GET /rest/img 缺少查询参数 id")
        try:
            img = m.Image.objects.get(id=id)
        except IntegrityError:
            raise ValidationError("无效的参数 id")
        return FileResponse(img.data, content_type='image/png')

    if util == 'imgs' and req._request.method == 'GET':
        imgs = s.S_Image(m.Image.objects.all(), many=True).data
        for i,v in enumerate(imgs):
            imgs[i]['data'] = f'http://localhost:8001/media{imgs[i]['data']}'
        return Response(imgs)


    if util == 'img-user' and req._request.method == 'GET':
        try:
            id = req.query_params['id']
        except Exception:
            raise ValidationError("GET /rest/img 缺少查询参数 id")
        try:
            user = m.User.objects.get(id=id)
        except IntegrityError:
            raise ValidationError("无效的参数 id")
        return FileResponse(user.avatar.data, content_type='image/png')

    if util == 'my-artists' and req._request.method == 'GET':
        try:
            id = req.query_params['id']
        except Exception:
            raise ValidationError(f"GET {req._request.path} 缺少查询参数 id")
        try:
            user = m.User.objects.get(id=id)
        except IntegrityError:
            raise ValidationError("无效的参数 id")
        fans = user.fans
        concerns = user.concerns

        fans_ = s.S_User(fans,many=True).data
        for i,k in enumerate(fans_):
            fans_[i]['avatar'] = f'http://localhost:8001/rest/img/?id={fans_[i]['avatar']}'
            fans_[i]['artist'] = s.S_Artist(fans.all()[i].artist).data

        concerns_ = s.S_User(concerns, many=True).data
        for i,k in enumerate(concerns_):
            concerns_[i]['avatar'] = f'http://localhost:8001/rest/img/?id={concerns_[i]['avatar']}'
            try:
                concerns_[i]['artist'] = s.S_Artist(concerns.all()[i].artist).data
            except:
                concerns_.pop(i)

        return Response({
            'fans': fans_,
            'concerns': concerns_,
        })

    if util == 'my-videos' and req._request.method == 'GET':
        try:
            id = req.query_params['id']
        except Exception:
            raise ValidationError(f"GET {req._request.path} 缺少查询参数 id")
        try:
            user = m.User.objects.get(id=id)
        except IntegrityError:
            raise ValidationError("无效的参数 id")
        videos = s.S_Video(user.videos, many=True).data
        for i, v in enumerate(videos):
            videos[i]['img'] = f'http://localhost:8001/rest/img/?id={videos[i]['img']}'
        return Response(videos)

    if util == 'my-CreatedSongLists' and req._request.method == 'GET':
        try:
            id = req.query_params['id']
        except Exception:
            raise ValidationError(f"GET {req._request.path} 缺少查询参数 id")
        try:
            user = m.User.objects.get(id=id)
        except IntegrityError:
            raise ValidationError("无效的参数 id")
        playlists = s.S_PlayList(user.playlists, many=True).data
        for i, v in enumerate(playlists):
            playlists[i]['img'] = f'http://localhost:8001/rest/img/?id={playlists[i]['img']}'
        return Response(playlists)

    if util == 'my-CollectedSongLists' and req._request.method == 'GET':
        try:
            id = req.query_params['id']
        except Exception:
            raise ValidationError(f"GET {req._request.path} 缺少查询参数 id")
        try:
            user = m.User.objects.get(id=id)
        except IntegrityError:
            raise ValidationError("无效的参数 id")
        playlists = s.S_PlayList(user.collected_playlists, many=True).data
        for i, v in enumerate(playlists):
            playlists[i]['img'] = f'http://localhost:8001/rest/img/?id={playlists[i]['img']}'
        return Response(playlists)

    if util == 'my-Messages' and req._request.method == 'GET':
        try:
            id = req.query_params['id']
        except Exception:
            raise ValidationError(f"GET {req._request.path} 缺少查询参数 id")
        print(id)
        # sends = m.Message.objects.filter(send_user_id=id).values_list('receive_user_id',flat=True).distinct()
        # sends = list(sends)
        # receives = m.Message.objects.filter(receive_user_id=id).values_list('send_user_id',flat=True).distinct()
        # receives = list(receives)
        # print(sends, receives)
        # for v in sends:
        #     try:
        #         receives.index(v)
        #     except:
        #         receives.append(v)
        # print(receives)
        # ret = [s.S_User(m.User.objects.get(id=v)).data for v in receives]
        msgs1 = m.Message.objects.filter(send_user_id=id)
        ids1 = [v.receive_user_id for v in msgs1]
        msgs2 = m.Message.objects.filter(receive_user_id=id)
        ids2 = [v.send_user_id for v in msgs2]
        ids = list(set(ids1 + ids2))
        users = [s.S_User(m.User.objects.get(id=v)).data for v in ids]
        for i,v in enumerate(users):
            users[i]['avatar'] = f'http://localhost:8001/rest/img/?id={v['avatar']}'
        return Response(users)

    if util == 'g-Artist' and req._request.method == 'GET':
        try:
            id = req.query_params['id']
        except Exception:
            raise ValidationError(f"GET {req._request.path} 缺少查询参数 id")
        artist = m.Artist.objects.get(id=id)
        artist_ = s.S_Artist(artist).data
        artist_['albums'] = s.S_Album(artist.albums, many=True).data
        artist_['background'] = f'http://localhost:8001/rest/img/?id={artist_['background']}'
        artist_['songs'] = []
        for v in artist.albums.all():
            artist_['songs'] += s.S_Song(v.songs, many=True).data
        artist_['videos'] = s.S_Video(artist.account.videos, many=True).data


        for i, v in enumerate(artist_['videos']):
            artist_['videos'][i]['img'] = f'http://localhost:8001/rest/img/?id={artist_['videos'][i]['img']}'
        for i, v in enumerate(artist_['albums']):
            artist_['albums'][i]['background'] = f'http://localhost:8001/rest/img/?id={artist_['albums'][i]['background']}'
        for i, v in enumerate(artist_['songs']):
            artist_['songs'][i]['img'] = f'http://localhost:8001/rest/img/?id={artist_['songs'][i]['img']}'
            artist_['songs'][i]['album'] = s.S_Album(m.Album.objects.get(id=artist_['songs'][i]['album'])).data
            artist_['songs'][i]['data'] = f'http://localhost:8001/media{artist_['songs'][i]['data']}'

            artist_['songs'][i]['artist'] = s.S_Artist(m.Song.objects.get(id=v['id']).album.artist).data

        return Response(artist_)

    if util == 'g-Song' and req._request.method == 'GET':
        try:
            id = req.query_params['id']
        except Exception:
            raise ValidationError(f"GET {req._request.path} 缺少查询参数 id")
        song_ = m.Song.objects.get(id=id)
        song = s.S_Song(song_).data
        song['data'] = f'http://localhost:8001/media{song["data"]}'
        song['img'] = f'http://localhost:8001/rest/img/?id={song["img"]}'
        song['artist'] = s.S_Artist(song_.album.artist).data
        song['album'] = s.S_Album(song_.album).data
        song['lyrics'] = song['lyrics'].replace('\n', '<br>')

        return Response(song)

    if util == 'g-Album' and req._request.method == 'GET':
        try:
            id = req.query_params['id']
        except Exception:
            raise ValidationError(f"GET {req._request.path} 缺少查询参数 id")
        album_ = m.Album.objects.get(id=id)
        album = s.S_Album(album_).data
        album['background'] = f"http://localhost:8001/rest/img/?id={album['background']}"
        album['artist'] = s.S_Artist(m.Artist.objects.get(id=album['artist'])).data
        album['songs'] = s.S_Song(album_.songs, many=True).data
        for i, v in enumerate(album['songs']):
            album['songs'][i]['img'] = f'http://localhost:8001/rest/img/?id={album['songs'][i]['img']}'

            album['songs'][i]['data'] = f'http://localhost:8001/media{v['data']}'
            album['songs'][i]['artist'] = s.S_Artist(m.Song.objects.get(id=v['id']).album.artist).data

        return Response(album)

    if util == 'g-Comment' and req._request.method == 'GET':
        try:
            type = req.query_params['type']
        except Exception:
            raise ValidationError(f"GET {req._request.path} 缺少查询参数 type")
        try:
            id = req.query_params['id']
        except Exception:
            raise ValidationError(f"GET {req._request.path} 缺少查询参数 id")

        comments = []
        if type.lower() == 'album':
            comments = s.S_AlbumComment(m.AlbumComment.objects.filter(album_id=id), many=True).data
        if type.lower() == 'song':
            comments = s.S_SongComment(m.SongComment.objects.filter(song_id=id), many=True).data
        if type.lower() == 'playlist':
            comments = s.S_PlayComment(m.PlayComment.objects.filter(playlist_id=id), many=True).data
        if type.lower() == 'video':
            comments = s.S_VideoComment(m.VideoComment.objects.filter(video_id=id), many=True).data
        if type.lower() == 'event':
            comments = s.S_EventComment(m.EventComment.objects.filter(event_id=id), many=True).data

        for i,v in enumerate(comments):
            comments[i]['user'] = s.S_User(m.User.objects.get(id=comments[i]['user'])).data
            comments[i]['img'] = f"http://localhost:8001/rest/img/?id={comments[i]['user']['avatar']}"

        return Response(comments)

    if util == 'g-Video' and req._request.method == 'GET':
        try:
            id = req.query_params['id']
        except Exception:
            raise ValidationError(f"GET {req._request.path} 缺少查询参数 id")
        video = s.S_Video(m.Video.objects.get(id=id)).data
        video['data'] = f"http://localhost:8001/media{video['data']}"
        video['img'] = f"http://localhost:8001/rest/img/?id={video['img']}"

        return Response(video)



    if util == 'g-PlayList' and req._request.method == 'GET':
        try:
            id = req.query_params['id']
        except Exception:
            raise ValidationError(f"GET {req._request.path} 缺少查询参数 id")
        playlist_ = m.PlayList.objects.get(id=id)
        playlist = s.S_PlayList(playlist_).data
        for i,v in enumerate(playlist['join_songs']):
            playlist['join_songs'][i] = s.S_Song(m.Song.objects.get(id=v)).data
        for i,v in enumerate(playlist['collect_users']):
            playlist['collect_users'][i] = s.S_User(m.User.objects.get(id=v)).data
        playlist['img'] = f"http://localhost:8001/rest/img/?id={playlist['img']}"
        playlist['user'] = s.S_User(m.User.objects.get(id=playlist['user'])).data
        for i,v in enumerate(playlist['join_songs']):
            playlist['join_songs'][i]['img'] = f"http://localhost:8001/rest/img/?id={v['img']}"
            playlist['join_songs'][i]['album'] = s.S_Album(m.Album.objects.get(id=v['album'])).data
            playlist['join_songs'][i]['data'] = f'http://localhost:8001/media{v['data']}'

            playlist['join_songs'][i]['artist'] = s.S_Artist(m.Song.objects.get(id=v['id']).album.artist).data

        return Response(playlist)

    if util == 'g-Message' and req._request.method == 'GET':
        try:
            id1 = req.query_params['id1']
            id2 = req.query_params['id2']
        except Exception:
            raise ValidationError(f"GET {req._request.path} 缺少查询参数 id1 或 id2")
        try:
            m.User.objects.get(id=id1)
            m.User.objects.get(id=id2)
        except:
            raise ValidationError(f"user1 或 user2 不存在")
        # messages1_ = m.Message.objects.filter(send_user_id=id1, receive_user_id=id2)
        # messages2_ = m.Message.objects.filter(send_user_id=id2, receive_user_id=id1)
        messages_ = (m.Message.objects.filter(Q(send_user_id=id1,receive_user_id=id2) | Q(send_user_id=id2,receive_user_id=id1))
                     .order_by('send_time'))
        messages = s.S_Message(messages_, many=True).data
        for i,v in enumerate(messages):
            messages[i]['send_user'] = s.S_User(m.User.objects.get(id=v['send_user'])).data
            messages[i]['send_user']['avatar'] = f"http://localhost:8001/rest/img/?id={v['send_user']['avatar']}"

            messages[i]['receive_user'] = s.S_User(m.User.objects.get(id=v['receive_user'])).data
            messages[i]['receive_user']['avatar'] = f"http://localhost:8001/rest/img/?id={v['receive_user']['avatar']}"

        return Response(messages)

    if util == 'e-Recommends' and req._request.method == 'GET':
        albums = s.S_Album(m.Album.objects.all().order_by('-pub_date'), many=True).data
        album_tag = m.AlbumTag.objects.values_list('tag',flat=True).distinct()
        playlists = s.S_PlayList(m.PlayList.objects.all().order_by('-pub_date'), many=True).data
        play_tag = m.PlayTag.objects.values_list('tag',flat=True).distinct()
        artists = s.S_Artist(m.Artist.objects.all().order_by('-joined_time'), many=True).data
        artist_tag = m.ArtistTag.objects.values_list('tag',flat=True).distinct()

        for i,v in enumerate(albums):
            albums[i]['background'] = f"http://localhost:8001/rest/img/?id={v['background']}"
        for i,v in enumerate(playlists):
            playlists[i]['img'] = f"http://localhost:8001/rest/img/?id={v['img']}"
        for i,v in enumerate(artists):
            artists[i]['background'] = f"http://localhost:8001/rest/img/?id={v['background']}"

        return Response({
            'albums': albums[:12],
            'album_tag': album_tag,
            'playlists': playlists[:12],
            'play_tag': play_tag,
            'artists': artists[:12],
            'artist_tag': artist_tag,
        })

    if util == 'e-Albums' and req._request.method == 'GET':
        albums = m.Album.objects.all().order_by('-pub_date')
        tag = None
        subtag = None
        try:
            tag = req.query_params['tag']
            try:
                if tag:
                    albums = albums.filter(tag=tag)
            except:
                albums = []
        except:
            pass
        try:
            subtag = req.query_params['subtag']
            try:
                if subtag:
                    albums = albums.filter(subtag=subtag)
            except:
                albums = []
        except:
            pass
        albums = s.S_Album(albums, many=True).data

        for i,v in enumerate(albums):
            albums[i]['background'] = f"http://localhost:8001/rest/img/?id={v['background']}"

        tags = s.S_AlbumTag(m.AlbumTag.objects.all(), many=True).data

        return Response({
            'albums': albums,
            'tags': tags
        })

    if util == 'e-Artists' and req._request.method == 'GET':
        artists = m.Artist.objects.all().order_by('-joined_time')
        try:
            tag = req.query_params['tag']
            try:
                if tag:
                    artists = artists.filter(tag=tag)
            except:
                artists = []
        except:
            pass
        try:
            subtag = req.query_params['subtag']
            try:
                if subtag:
                    artists = artists.filter(subtag=subtag)
            except:
                artists = []
        except:
            pass
        artists = s.S_Artist(artists, many=True).data

        for i,v in enumerate(artists):
            artists[i]['background'] = f"http://localhost:8001/rest/img/?id={v['background']}"

        tags = s.S_ArtistTag(m.ArtistTag.objects.all(),many=True).data

        return Response({
            'artists': artists,
            'tags': tags
        })

    if util == 'e-PlayLists' and req._request.method == 'GET':
        playlists = m.PlayList.objects.all().order_by('-pub_date')
        try:
            tag = req.query_params['tag']
            try:
                if tag:
                    playlists = playlists.filter(tag=tag)
            except:
                playlists = []
        except:
            pass
        try:
            subtag = req.query_params['subtag']
            try:
                if subtag:
                    playlists = playlists.filter(subtag=subtag)
            except:
                playlists = []
        except:
            pass
        playlists = s.S_PlayList(playlists, many=True).data

        for i,v in enumerate(playlists):
            playlists[i]['img'] = f"http://localhost:8001/rest/img/?id={v['img']}"

        tags = s.S_PlayTag(m.PlayTag.objects.all(),many=True).data

        return Response({
            'playlists': playlists,
            'tags': tags
        })

    if util == 'e-Ranks' and req._request.method == 'GET':
        songs = m.Song.objects.order_by('-shared_count').order_by('-liked_count')[:10]
        songs = s.S_Song(songs,many=True).data
        albums = m.Album.objects.order_by('-shared_count').order_by('-liked_count')[:10]
        albums = s.S_Album(albums,many=True).data
        playlists = m.PlayList.objects.order_by('-shared_count').order_by('-liked_count')[:10]
        playlists = s.S_PlayList(playlists,many=True).data

        for i,v in enumerate(songs):
            songs[i]['img'] = f"http://localhost:8001/rest/img/?id={v['img']}"
        for i,v in enumerate(albums):
            albums[i]['background'] = f"http://localhost:8001/rest/img/?id={v['background']}"
        for i,v in enumerate(playlists):
            playlists[i]['img'] = f"http://localhost:8001/rest/img/?id={v['img']}"

        return Response({
            'songs': songs,
            'albums': albums,
            'playlists': playlists,
        })


    if util == 'g-Search' and req._request.method == 'GET':
        search = req.query_params.get('s')
        if not search:
            search = '!@#$%^&*()_'

        songs = s.S_Song(m.Song.objects.filter(Q(title__contains=search)|Q(album__artist__stagename__contains=search)),many=True).data
        videos = s.S_Video(m.Video.objects.filter(Q(title__contains=search)|Q(user__nickname__contains=search)),many=True).data
        albums = s.S_Album(m.Album.objects.filter(Q(title__contains=search)|Q(artist__stagename__contains=search)),many=True).data
        playlists = s.S_PlayList(m.PlayList.objects.filter(Q(title__contains=search)|Q(user__nickname__contains=search)),many=True).data
        users = s.S_User(m.User.objects.filter(nickname__contains=search),many=True).data
        artists = s.S_Artist(m.Artist.objects.filter(stagename__contains=search),many=True).data

        for i,v in enumerate(songs):
            songs[i]['artist'] = s.S_Artist(m.Song.objects.get(id=v['id']).album.artist).data
        for i,v in enumerate(videos):
            videos[i]['user'] = s.S_User(m.Video.objects.get(id=v['id']).user).data
        for i,v in enumerate(albums):
            albums[i]['artist'] = s.S_Artist(m.Album.objects.get(id=v['id']).artist).data
        for i,v in enumerate(playlists):
            playlists[i]['user'] = s.S_User(m.PlayList.objects.get(id=v['id']).user).data

        return Response({
            'songs': songs,
            'videos': videos,
            'albums': albums,
            'playlists': playlists,
            'users': users,
            'artists': artists,
        })


    if util == 'o-Advanced' and req._request.method == 'GET':
        songs = m.Song.objects.all()
        songs = s.S_Song(songs,many=True).data
        random.shuffle(songs)

        songs = songs[:10]
        for i,v in enumerate(songs):
            songs[i]['img'] = f"http://localhost:8001/rest/img/?id={v['img']}"
            songs[i]['data'] = f"http://localhost:8001/media{v['data']}"

            songs[i]['album'] = s.S_Album(m.Song.objects.get(id=v['id']).album).data
            songs[i]['artist'] = s.S_Artist(m.Song.objects.get(id=v['id']).album.artist).data
        return Response(songs)

    if util == 'join' and req._request.method == 'POST':

        if not validate_email(req):
            raise ValidationError("邮箱验证错误")

        background = req.data.get('background')
        background_id = m.Image.objects.create(data=background).id
        stagename = req.data.get('stagename')
        description = req.data.get('description')
        try:
            artist = m.Artist.objects.create(account=req.user, stagename=stagename,
                                             description=description, background_id=background_id)
        except:
            raise ValidationError("歌手入驻失败")
        return Response(artist)

    if util == 'o-Friends' and req._request.method == 'GET':
        user = req.user.user
        friends_ = s.S_User(user.fans, many=True).data + s.S_User(user.concerns, many=True).data
        friends = []
        events = []
        for v in friends_:
            if v not in friends:
                friends.append(v)
                events += s.S_Event(m.User.objects.get(id=v['id']).events.order_by('-pub_date'), many=True).data
        for v in events:
            v['user'] = s.S_User(m.User.objects.get(id=v['user'])).data
            v['user']['avatar'] = f'http://localhost:8001/rest/img/?id={v['user']['avatar']}'
            print(v['user'])

        return Response(events)


    return Response(f"{req._request.method} /rest/{util}/ 请求方法错误")

