# 更新内容:
# 1. 进度条，音量控制

import os
try:
    os.makedirs('assets/music')
except:
    pass

import copy
import json
import os
import random
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel, QPushButton, \
    QTableWidget, QTableWidgetItem, QSizePolicy, QLineEdit,QProgressBar,QSlider
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtCore import QUrl, Qt, QTimer, QThread
import requests

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Player')
        self.setup_ui()
        self.setup_player()
        # self.setWindowIcon(QIcon('logo.ico'))
    def setup_ui(self):
        # 选中歌曲的标签，导入文件按钮，导入文件列表按钮，播放按钮，暂停按钮，上一首/下一首按钮
        self.song_label = QLabel('No song is playing')
        self.song_label.setFixedWidth(150)
        self.importfiles_button = QPushButton('import file list')
        self.importfiles_button.clicked.connect(self.import_files)
        self.play_button = QPushButton('play')
        self.play_button.clicked.connect(self.on_play)
        self.stop_button = QPushButton('stop')
        self.stop_button.clicked.connect(self.on_stop)
        self.pre_button = QPushButton('pre song')
        self.pre_button.clicked.connect(self.on_pre)
        self.next_button = QPushButton('next song')
        self.next_button.clicked.connect(self.on_next)
        self.playmode_button = QPushButton('sequential play')
        self.playmode_button.clicked.connect(self.on_playmode)
        self.sound_slider = QSlider(Qt.Horizontal)
        self.sound_slider.setRange(0,100)
        self.sound_slider.setValue(20)
        self.sound_slider.setSingleStep(1)
        self.sound_slider.sliderMoved.connect(self.on_sliderchange)
        self.sound_slider.sliderPressed.connect(self.on_sliderchange)
        self.sound_slider.valueChanged.connect(self.on_sliderchange)

        # 设置并添加样式（纵向排列）
        layout = QVBoxLayout()
        layout.addWidget(self.song_label)
        layout.addWidget(self.importfiles_button)
        layout.addWidget(self.play_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.pre_button)
        layout.addWidget(self.next_button)
        layout.addWidget(self.playmode_button)
        layout.addWidget(self.sound_slider)

        # 音乐搜索框（过滤框），音乐表格
        self.filter_text = QLineEdit()
        self.filter_text.textChanged.connect(self.on_filtertextchange)
        self.filter_text.returnPressed.connect(self.on_filtertextenter)
        self.filter_text.setToolTip('过滤音乐(ctrl + f)')
        self.music_table = QTableWidget()
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.music_table.setColumnCount(2)
        # self.music_table.setColumnWidth(0,200)
        # self.music_table.setColumnWidth(1,150)
        self.music_table.setFixedWidth(410)
        self.music_table.setHorizontalHeaderLabels(['音乐名称', '路径'])
        self.music_table.itemClicked.connect(self.on_tableitemClicked)
        self.music_table.itemDoubleClicked.connect(self.on_tableitemDoubleclick)

        song_layout = QVBoxLayout()
        song_layout.addWidget(self.filter_text)
        song_layout.addWidget(self.music_table)
        self.progress_bar = QProgressBar()
        song_layout.addWidget(self.progress_bar)
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(100)


        # orz
        self.search_text = QLineEdit()
        self.search_text.returnPressed.connect(self.on_searchtextEnter)
        self.search_text.setToolTip('搜索音乐(ctrl + s)')
        self.wmusic_table = QTableWidget()
        self.wmusic_table.setColumnCount(6)
        self.wmusic_table.setColumnWidth(1, 50)
        self.wmusic_table.setColumnWidth(2, 80)
        self.wmusic_table.setColumnWidth(3, 80)
        self.wmusic_table.setFixedWidth(410)
        self.wmusic_table.setHorizontalHeaderLabels(['音乐名称','时长','歌曲','id','专辑','下载'])
        self.wmusic_table.itemClicked.connect(self.on_wtableClicked)
        self.wmusic_table.itemDoubleClicked.connect(self.on_wtableDbClicked)
        self.add_button = QPushButton('add selected music')
        self.add_button.clicked.connect(self.on_add)
        layout1 = QVBoxLayout()
        layout1.addWidget(self.search_text)
        layout1.addWidget(self.wmusic_table)
        layout1.addWidget(self.add_button)


        # 主样式——用于整合上述样式和组件
        main_layout = QHBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(song_layout)
        main_layout.addLayout(layout1)

        self.setLayout(main_layout)
    def setup_player(self):
        self.files = []
        self.files_filtered = []
        self.fileindex_playing = 0
        self.fileindex_prepared = 0
        self.player = QMediaPlayer()
        self.player.setVolume(2)
        self.play_mode = 0 # 播放模式 0 - 循环，1 - 随机
        self.player.mediaStatusChanged.connect(self.on_songplayed)
        # self.player.

        # self.defaut_path='E:/LX/app/魔音Morin/Cache/Song'
        self.defaut_path='assets/music'
        if os.path.exists(self.defaut_path):
            self.add_files([f'{self.defaut_path}/{basename}' for basename in os.listdir(self.defaut_path) if basename.endswith('.mp3')])
        self.switch_file(0)

        self.wfiles = []
        self.wfileindex = 0
        # self.defaut_dowload = 'E:\LX\_武装库\临时工作站\docs\python_apps\music player\download'
        self.defaut_dowload = 'assets/music'
        if not os.path.exists(self.defaut_dowload):
            os.mkdir(self.defaut_dowload)

        if os.path.exists(self.defaut_dowload):
            self.add_files([f'{self.defaut_dowload}/{basename}' for basename in os.listdir(self.defaut_dowload) if basename.endswith('.mp3')])


    def add_files(self, files):
        for file in files:
            if file not in self.files:
                self.files.append(file)
        self.music_table.setRowCount(len(self.files))
        self.files_filtered = self.files
        self.view_table()

    # 导入多个音乐文件
    def import_files(self):
        # file_path, _ = QFileDialog.getOpenFileName(self, "Open Music File", self.defaut_path, 'file(*.mp3;*.wav)')
        print(os.path.exists(self.defaut_path))
        if os.path.exists(self.defaut_path):
            file_list, _ = QFileDialog.getOpenFileNames(self, "Open Music File", self.defaut_path, 'file(*.mp3;*.wav)')
            self.add_files(file_list)
        else:
            print("文件导入失败")


    # 更新音乐表格的显示
    def view_table(self):
        files = self.files_filtered
        self.music_table.setRowCount(len(files))
        for i in range(len(files)):
            file = files[i]
            dirname, basename = os.path.split(file)
            item0 = QTableWidgetItem(basename)
            item1 = QTableWidgetItem(dirname)
            # 表格中的单元格设为只读
            item0.setFlags(item0.flags() & ~Qt.ItemIsEditable)
            item1.setFlags(item1.flags() & ~Qt.ItemIsEditable)
            self.music_table.setItem(i, 0, item0)
            self.music_table.setItem(i, 1, item1)
        self.switch_file(0)

    def view_label(self,str):
        self.song_label.setText(str)

    def view_playbutton(self,str):
        self.play_button.setText(str)

    def view_playbutton1(self):
        if self.fileindex_prepared != self.fileindex_playing:
            self.view_playbutton('play')
        else:
            self.view_playbutton('pause')

    def view_wtableitem(self,row,data):
        for col,cell in enumerate(data):
            item = QTableWidgetItem(cell)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.wmusic_table.setItem(row,col,item)

    # 更改即将播放的歌曲
    def switch_file(self,index):
        # self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.files[0])))
        if self.play_mode == 0:
            self.fileindex_prepared=index
        else:
            self.fileindex_prepared=index+random.randint(0,len(self.files))


    def switch_wfile(self,index):
        self.wfileindex=index

    def on_songplayed(self,state):
        # print('ee')
        if state == QMediaPlayer.EndOfMedia:
            if self.play_mode == 0:
                self.switch_file(self.fileindex_prepared+1)
            else:
                self.switch_file(random.randint(0,len(self.files)))
            self.on_play()

    # 播放或暂停音乐
    def on_play(self):
        # print(QMediaPlayer.StoppedState, QMediaPlayer.PlayingState, QMediaPlayer.PausedState)
        # print(self.fileindex_prepared,self.player.state())
        self.fileindex_prepared = (self.fileindex_prepared%len(self.files)+len(self.files))%len(self.files)
        self.fileindex_playing = (self.fileindex_playing%len(self.files)+len(self.files))%len(self.files)

        state = self.player.state()
        if self.fileindex_prepared == self.fileindex_playing:
            if state != QMediaPlayer.PlayingState:
                if state == QMediaPlayer.StoppedState:
                    try:
                        self.player.setMedia(
                            QMediaContent(QUrl.fromLocalFile(self.files_filtered[self.fileindex_prepared])))
                    except Exception as e:
                        return
                self.player.play()
                # self.player.setPlaybackRate(2)
                # self.player.setPosition(300000)
                self.view_playbutton('pause')
                _, file = os.path.split(self.files_filtered[self.fileindex_prepared])
                self.fileindex_playing = self.fileindex_prepared
                self.view_label(file)
            else:
                self.player.pause()
                self.view_playbutton('play')
        else:
            try:
                self.player.setMedia(
                    QMediaContent(QUrl.fromLocalFile(self.files_filtered[self.fileindex_prepared])))
            except Exception as e:
                return
            self.player.play()
            # self.player.setPlaybackRate(3)
            # self.player.setPosition(200000)
            self.view_playbutton('pause')
            _, file = os.path.split(self.files_filtered[self.fileindex_prepared])
            self.fileindex_playing = self.fileindex_prepared
            self.view_label(file)

    # 停止播放
    def on_stop(self):
        self.player.stop()
        self.view_playbutton('play')

    # 播放上一首
    def on_pre(self):
        self.switch_file(self.fileindex_prepared - 1)
        self.on_play()

    # 播放下一首
    def on_next(self):
        self.switch_file(self.fileindex_prepared + 1)
        self.on_play()

    # 歌曲表格的单元格的单击
    def on_tableitemClicked(self,item):
        index = item.row()
        self.switch_file(index)
        self.view_playbutton1()

    # 歌曲表格的单元格的双击
    def on_tableitemDoubleclick(self,item):
        # print(item.row(),item.column())
        self.switch_file(item.row())
        self.on_play()


    # 搜索框文本改变时，执行播放列表的搜索过滤
    def on_filtertextchange(self):
        text = self.filter_text.text()
        self.files_filtered = copy.copy(self.files)     # 此处必须浅拷贝？！

        if len(text) != 0:
            indexs = [i for i in range(len(self.files)) if self.files[i].find(text)!=-1]
            self.switch_file(0)

            for j,i in enumerate(indexs):
                self.files_filtered[j] = self.files[i]
            self.files_filtered = self.files_filtered[:len(indexs)]
        self.view_table()

        self.switch_file(0)

    # 搜索框按下 enter 时，默认播放第一条已经过搜索过滤的歌曲
    def on_filtertextenter(self):
        self.switch_file(0)
        print(23)
        self.on_play()

    #
    def on_searchtextEnter(self):
        keyword = self.search_text.text()
        if not keyword:
            return
        url = f'http://localhost:4000/search?keywords={keyword}'
        # url = f'https://www.travisblog.asia/search?keywords={keyword}'
        ret = requests.get(url)
        js = json.loads(ret.text)
        musics = js['result']['songs']
        self.wmusic_table.setRowCount(len(musics))
        self.wfiles = []
        for row,music in enumerate(musics):
            name = music['name']
            time = music['duration']/1000
            time = '{:02d}:{:02d}'.format(int(time//60),int(time%60))
            time = f'{time}'
            artists = [art['name'] for art in music['artists']]
            artists = ';'.join(artists)
            id = f"{music['id']}"
            album = music['album']['name']
            print(name,time,artists,id,album)
            self.view_wtableitem(row,[name,time,artists,id,album])

            self.wfiles.append({'name':name,'time':time,'artists':artists,'id':id,'album':album})

    def on_wtableClicked(self,item):
        index = item.row()
        self.switch_wfile(index)
        print(self.wfileindex)

    def on_wtableDbClicked(self,item):
        self.switch_wfile(item.row())
        self.add(item.row())
        self.switch_file(-1)
        self.on_play()

    def add(self,index):
        # 下载歌曲
        song = self.wfiles[index]
        name = song['name']
        id = song['id']
        url = f'http://music.163.com/song/media/outer/url?id={id}.mp3'
        content = requests.get(url).content
        file = f"{self.defaut_dowload}/{name}.mp3"
        print(file)
        if not os.path.exists(file):
            with open(file,'wb') as f:
                f.write(content)
        index = len(self.files)
        self.add_files([file])
        self.switch_file(index)

    def on_add(self):
        # for row,col in self.wmusic_table.selectedIndexes():
        # print('rep')
        items = [item for item in self.wmusic_table.selectedItems()]
        # print('rep')
        for item in items:
            self.add(item.row())

    def on_playmode(self):
        print(self.play_mode)
        if self.play_mode == 0:
            self.play_mode = 1
            self.playmode_button.setText('random play')
        else:
            self.play_mode = 0
            self.playmode_button.setText('sequential play')

    def on_timeout(self):
        try:
            value = 100*self.player.position()//self.player.duration()
            self.progress_bar.setValue(value)
        except Exception as e:
            self.progress_bar.setValue(0)

    def on_sliderchange(self):
        # print(self.player.volume())
        self.player.setVolume(self.sound_slider.value()//10)

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Delete:
            pass
        if key == Qt.Key_P:
            self.on_play()
        if key == Qt.Key_Enter:
            print(key)
            self.on_play()
        if event.modifiers() & Qt.ControlModifier and key == Qt.Key_F:
            print("ctrl + f")
            self.filter_text.setFocus()
        if event.modifiers() & Qt.ControlModifier and key == Qt.Key_S:
            print("ctrl + s")
            self.search_text.setFocus()
        super().keyPressEvent(event)

app=QApplication(sys.argv)

player=MusicPlayer()
player.show()

sys.exit(app.exec_())