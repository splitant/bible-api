#!/usr/bin/python

from bibleapi import bible_api
import unittest

""" Create a test class inherits from unittest Class """
class TestBibleAPIMethods(unittest.TestCase):

    def setUp(self):
        self._bibleAPI = bible_api.BibleAPI()

        self._initBibleVersions()
        self._initBibleBooks()

    def _initBibleVersions(self):
        self._bibleVersionsTest = {"LSG": "Louis-Segond", "semeur": "Semeur", "segond_21": "Segond 21", "martin": "Martin", "darby": "Darby", "ostervald": "Ostervald", "kingjames": "King-James", "COL": "La Colombe", "PDV": "Parole de Vie", "PVI": "Parole Vivante", "BFC": "La Bible en français courant", "NBS": "Nouvelle Bible Segond", "NFC": "Nouvelle Français courant", "BCC1923": "Bible catholique Crampon 1923"}
    
    def _initBibleBooks(self):
        self._bibleBooksTest = {'genese': 'Genèse', 'exode': 'Exode', 'levitique': 'Lévitique', 'nombres': 'Nombres', 'deuteronome': 'Deutéronome', 'josue': 'Josué', 'juges': 'Juges', 'ruth': 'Ruth', '1-samuel': '1 Samuel', '2-samuel': '2 Samuel', '1-rois': '1 Rois', '2-rois': '2 Rois', '1-chroniques': '1 Chroniques', '2-chroniques': '2 Chroniques', 'esdras': 'Esdras', 'nehemie': 'Néhémie', 'esther': 'Esther', 'job': 'Job', 'psaumes': 'Psaumes', 'proverbes': 'Proverbes', 'ecclesiaste': 'Ecclésiaste', 'cantique-des-cantiques': 'Cantique des cantiques', 'esaie': 'Esaïe', 'jeremie': 'Jérémie', 'lamentations': 'Lamentations', 'ezechiel': 'Ezéchiel', 'daniel': 'Daniel', 'osee': 'Osée', 'joel': 'Joël', 'amos': 'Amos', 'abdias': 'Abdias', 'jonas': 'Jonas', 'michee': 'Michée', 'nahum': 'Nahum',
                                'habakuk': 'Habakuk', 'sophonie': 'Sophonie', 'agee': 'Aggée', 'zacharie': 'Zacharie', 'malachie': 'Malachie', 'matthieu': 'Matthieu', 'marc': 'Marc', 'luc': 'Luc', 'jean': 'Jean', 'actes': 'Actes', 'romains': 'Romains', '1-corinthiens': '1 Corinthiens', '2-corinthiens': '2 Corinthiens', 'galates': 'Galates', 'ephesiens': 'Ephésiens', 'philippiens': 'Philippiens', 'colossiens': 'Colossiens', '1-thessaloniciens': '1 Thessaloniciens', '2-thessaloniciens': '2 Thessaloniciens', '1-timothee': '1 Timothée', '2-timothee': '2 Timothée', 'tite': 'Tite', 'philemon': 'Philémon', 'hebreux': 'Hébreux', 'jacques': 'Jacques', '1-pierre': '1 Pierre', '2-pierre': '2 Pierre', '1-jean': '1 Jean', '2-jean': '2 Jean', '3-jean': '3 Jean', 'jude': 'Jude', 'apocalypse': 'Apocalypse'}
        
    def test_get_bible_versions(self):
        self._bibleAPI.getBibleVersions()
        self.assertDictEqual(self._bibleAPI.bibleVersions, self._bibleVersionsTest)
    
    def test_get_bible_books(self):
        self._bibleAPI.getBibleBooks()
        self.assertDictEqual(self._bibleAPI.bibleBooks, self._bibleBooksTest)

    def test_get_verses_from_book(self):
        self.assertFalse(self._bibleAPI.verses)
        verses = self._bibleAPI.getVersesFromBook('LSG', 'genese')
        self.assertTrue(self._bibleAPI.verses)

        self._bibleAPI.getVersesFromBook('LSG', 'genese')
        self.assertIs(verses, self._bibleAPI.verses['LSG.genese']['chapters'])

        self._bibleAPI.getVersesFromBook('semeur', 'levitique')
        self.assertIsNot(verses, self._bibleAPI.verses['semeur.levitique']['chapters'])

        self.assertEqual(len(self._bibleAPI.verses['LSG.genese']['chapters']['1']), 31)
        self.assertEqual(len(self._bibleAPI.verses['semeur.levitique']['chapters']['6']), 23)

        verse = self._bibleAPI.getVerse('segond_21', 'luc', '6', '31')
        self.assertEqual(verse, 'Ce que vous voulez que les hommes fassent pour vous, faites-le [vous aussi] de même pour eux.')

        verse = self._bibleAPI.getVerse('kingjames', 'jean', '15', '13')
        self.assertEqual(verse, 'Greater love hath no man than this, that a man lay down his life for his friends.')

        verse = self._bibleAPI.getVerse('NBS', '1-corinthiens', '13', '13')
        self.assertEqual(verse, 'Or maintenant trois choses demeurent : la foi, l’espérance, l’amour ; mais c’est l’amour qui est le plus grand.')
 
    def test_get_verse(self):
        verse = self._bibleAPI.getVerse('NFC', 'genese', '1', '1')
        self.assertEqual(verse, 'Au commencement Dieu créa les cieux et la terre .')

        verse = self._bibleAPI.getVerse('ostervald', 'genese', '1', '51')
        self.assertEqual(verse, 'Ainsi furent achevés les cieux et la terre, et toute leur armée.')

        verse = self._bibleAPI.getVerse('BFC', 'actes', '2', '-1')
        self.assertEqual(verse, 'Ils tirèrent alors au sort et le sort désigna Matthias, qui fut donc associé aux onze apôtres.')

if __name__ == "__main__":
    unittest.main()
    
