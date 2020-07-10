#!/usr/bin/python

import json

class BibleAPI:
    SOURCE_DIRECTORY = 'bible'

    def __init__(self):
        self._bibleVersions = dict()
        self._bibleBooks = dict()

        self._currentVersion = ''
        self._currentBook = ''
        self._currentChapter = ''
        self._currentVerse = ''
        self._verses = dict()

    @property
    def verses(self):
        return self._verses

    @verses.setter
    def verses(self, verses):
        self._verses = verses

    @property
    def currentVersion(self):
        return self._currentVersion

    @currentVersion.setter
    def currentVersion(self, currentVersion):
        self._currentVersion = currentVersion

    @property
    def currentBook(self):
        return self._currentBook

    @currentBook.setter
    def currentBook(self, currentBook):
        self._currentBook = currentBook

    @property
    def currentChapter(self):
        return self._currentChapter

    @currentChapter.setter
    def currentChapter(self, currentChapter):
        self._currentChapter = currentChapter
    
    @property
    def currentVerse(self):
        return self._currentVerse

    @currentVerse.setter
    def currentVerse(self, currentVerse):
        self._currentVerse = currentVerse

    @property
    def bibleVersions(self):
        return self._bibleVersions

    @bibleVersions.setter
    def bibleVersions(self, bibleVersions):
        self._bibleVersions = bibleVersions

    @property
    def bibleBooks(self):
        return self._bibleBooks

    @bibleBooks.setter
    def bibleBooks(self, bibleBooks):
        self._bibleBooks = bibleBooks

    def getBibleVersions(self):
        file_path = self.SOURCE_DIRECTORY + '/bible_versions.json'

        with open(file_path, 'r', encoding='utf8') as json_file:
            data = json_file.read()
            self._bibleVersions = json.loads(data)
        
        return self._bibleVersions

    def getBibleBooks(self):
        file_path = self.SOURCE_DIRECTORY + '/bible_books.json'

        with open(file_path, 'r', encoding='utf8') as json_file:
            data = json_file.read()
            self._bibleBooks = json.loads(data)
        
        return self._bibleBooks

    def getVersesFromBook(self, version, book):
        self._currentVersion = version
        self._currentBook = book

        key_version_book = self._currentVersion + '.' + self._currentBook
        if not key_version_book in self._verses:
            path_file = self.SOURCE_DIRECTORY + '/' + self._currentVersion + '/' + self._currentBook + '.json'
            with open(path_file, 'r', encoding='utf8') as json_file:
                data = json_file.read()
                self._verses[key_version_book] = json.loads(data)

        return self._verses[key_version_book]['chapters']

    def getVerse(self, version, book, chapter, num_verse):
        verses = self.getVersesFromBook(version, book)

        verse = ''

        if chapter in verses:
            self._currentChapter = chapter

            if not num_verse in verses[chapter]:
                if (int(num_verse) <= 0):
                    new_chapter = int(chapter) - 1
                elif (int(num_verse) > len(verses[chapter])):
                    new_chapter = int(chapter) + 1
                
                if str(new_chapter) in verses:
                    if new_chapter < int(self._currentChapter):
                        new_verse_number = len(verses[str(new_chapter)])
                    else:
                        new_verse_number = 1
                        
                    self._currentChapter = str(new_chapter)
                    self._currentVerse = str(new_verse_number)
                    verse = verses[self._currentChapter][str(new_verse_number)]
            else:
                verse = verses[self._currentChapter][num_verse]
                self._currentVerse = num_verse
        
        return verse

    def getVersesFromSearch(self, pattern, version = '', book = '', chapter = ''):
        """ TODO : in the future """
        pass

