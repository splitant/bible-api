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
        self._bibleBooksTest = {"0": {"code_book": "genese", "label_book": "Genèse", "id_book_emci": "genese", "id_book_topbible": "1", "id_book_biblecom": "GEN"}, "1": {"code_book": "exode", "label_book": "Exode", "id_book_emci": "exode", "id_book_topbible": "2", "id_book_biblecom": "EXO"}, "2": {"code_book": "levitique", "label_book": "Lévitique", "id_book_emci": "levitique", "id_book_topbible": "3", "id_book_biblecom": "LEV"}, "3": {"code_book": "nombres", "label_book": "Nombres", "id_book_emci": "nombres", "id_book_topbible": "4", "id_book_biblecom": "NUM"}, "4": {"code_book": "deuteronome", "label_book": "Deutéronome", "id_book_emci": "deuteronome", "id_book_topbible": "5", "id_book_biblecom": "DEU"}, "5": {"code_book": "josue", "label_book": "Josué", "id_book_emci": "josue", "id_book_topbible": "6", "id_book_biblecom": "JOS"}, "6": {"code_book": "juges", "label_book": "Juges", "id_book_emci": "juges", "id_book_topbible": "7", "id_book_biblecom": "JDG"}, "7": {"code_book": "ruth", "label_book": "Ruth", "id_book_emci": "ruth", "id_book_topbible": "8", "id_book_biblecom": "RUT"}, "8": {"code_book": "1-samuel", "label_book": "1 Samuel", "id_book_emci": "1-samuel", "id_book_topbible": "9", "id_book_biblecom": "1SA"}, "9": {"code_book": "2-samuel", "label_book": "2 Samuel", "id_book_emci": "2-samuel", "id_book_topbible": "10", "id_book_biblecom": "2SA"}, "10": {"code_book": "1-rois", "label_book": "1 Rois", "id_book_emci": "1-rois", "id_book_topbible": "11", "id_book_biblecom": "1KI"}, "11": {"code_book": "2-rois", "label_book": "2 Rois", "id_book_emci": "2-rois", "id_book_topbible": "12", "id_book_biblecom": "2KI"}, "12": {"code_book": "1-chroniques", "label_book": "1 Chroniques", "id_book_emci": "1-chroniques", "id_book_topbible": "13", "id_book_biblecom": "1CH"}, "13": {"code_book": "2-chroniques", "label_book": "2 Chroniques", "id_book_emci": "2-chroniques", "id_book_topbible": "14", "id_book_biblecom": "2CH"}, "14": {"code_book": "esdras", "label_book": "Esdras", "id_book_emci": "esdras", "id_book_topbible": "15", "id_book_biblecom": "EZR"}, "15": {"code_book": "nehemie", "label_book": "Néhémie", "id_book_emci": "nehemie", "id_book_topbible": "16", "id_book_biblecom": "NEH"}, "16": {"code_book": "esther", "label_book": "Esther", "id_book_emci": "esther", "id_book_topbible": "17", "id_book_biblecom": "EST"}, "17": {"code_book": "job", "label_book": "Job", "id_book_emci": "job", "id_book_topbible": "18", "id_book_biblecom": "JOB"}, "18": {"code_book": "psaumes", "label_book": "Psaumes", "id_book_emci": "psaumes", "id_book_topbible": "19", "id_book_biblecom": "PSA"}, "19": {"code_book": "proverbes", "label_book": "Proverbes", "id_book_emci": "proverbes", "id_book_topbible": "20", "id_book_biblecom": "PRO"}, "20": {"code_book": "ecclesiaste", "label_book": "Ecclésiaste", "id_book_emci": "ecclesiaste", "id_book_topbible": "21", "id_book_biblecom": "ECC"}, "21": {"code_book": "cantique-des-cantiques", "label_book": "Cantique des cantiques", "id_book_emci": "cantique-des-cantiques", "id_book_topbible": "22", "id_book_biblecom": "SNG"}, "22": {"code_book": "esaie", "label_book": "Esaïe", "id_book_emci": "esaie", "id_book_topbible": "23", "id_book_biblecom": "ISA"}, "23": {"code_book": "jeremie", "label_book": "Jérémie", "id_book_emci": "jeremie", "id_book_topbible": "24", "id_book_biblecom": "JER"}, "24": {"code_book": "lamentations", "label_book": "Lamentations", "id_book_emci": "lamentations", "id_book_topbible": "25", "id_book_biblecom": "LAM"}, "25": {"code_book": "ezechiel", "label_book": "Ezéchiel", "id_book_emci": "ezechiel", "id_book_topbible": "26", "id_book_biblecom": "EZK"}, "26": {"code_book": "daniel", "label_book": "Daniel", "id_book_emci": "daniel", "id_book_topbible": "27", "id_book_biblecom": "DAN"}, "27": {"code_book": "osee", "label_book": "Osée", "id_book_emci": "osee", "id_book_topbible": "28", "id_book_biblecom": "HOS"}, "28": {"code_book": "joel", "label_book": "Joël", "id_book_emci": "joel", "id_book_topbible": "29", "id_book_biblecom": "JOL"}, "29": {"code_book": "amos", "label_book": "Amos", "id_book_emci": "amos", "id_book_topbible": "30", "id_book_biblecom": "AMO"}, "30": {"code_book": "abdias", "label_book": "Abdias", "id_book_emci": "abdias", "id_book_topbible": "31", "id_book_biblecom": "OBA"}, "31": {"code_book": "jonas", "label_book": "Jonas", "id_book_emci": "jonas", "id_book_topbible": "32", "id_book_biblecom": "JON"}, "32": {"code_book": "michee", "label_book": "Michée", "id_book_emci": "michee", "id_book_topbible": "33", "id_book_biblecom": "MIC"}, "33": {"code_book": "nahum", "label_book": "Nahum", "id_book_emci": "nahum", "id_book_topbible": "34", "id_book_biblecom": "NAM"}, "34": {"code_book": "habakuk", "label_book": "Habakuk", "id_book_emci": "habakuk", "id_book_topbible": "35", "id_book_biblecom": "HAB"}, "35": {"code_book": "sophonie", "label_book": "Sophonie", "id_book_emci": "sophonie", "id_book_topbible": "36", "id_book_biblecom": "ZEP"}, "36": {"code_book": "agee", "label_book": "Aggée", "id_book_emci": "agee", "id_book_topbible": "37", "id_book_biblecom": "HAG"}, "37": {"code_book": "zacharie", "label_book": "Zacharie", "id_book_emci": "zacharie", "id_book_topbible": "38", "id_book_biblecom": "ZEC"}, "38": {"code_book": "malachie", "label_book": "Malachie", "id_book_emci": "malachie", "id_book_topbible": "39", "id_book_biblecom": "MAL"}, "39": {"code_book": "matthieu", "label_book": "Matthieu", "id_book_emci": "matthieu", "id_book_topbible": "40", "id_book_biblecom": "MAT"}, "40": {"code_book": "marc", "label_book": "Marc", "id_book_emci": "marc", "id_book_topbible": "41", "id_book_biblecom": "MRK"}, "41": {"code_book": "luc", "label_book": "Luc", "id_book_emci": "luc", "id_book_topbible": "42", "id_book_biblecom": "LUK"}, "42": {"code_book": "jean", "label_book": "Jean", "id_book_emci": "jean", "id_book_topbible": "43", "id_book_biblecom": "JHN"}, "43": {"code_book": "actes", "label_book": "Actes", "id_book_emci": "actes", "id_book_topbible": "44", "id_book_biblecom": "ACT"}, "44": {"code_book": "romains", "label_book": "Romains", "id_book_emci": "romains", "id_book_topbible": "45", "id_book_biblecom": "ROM"}, "45": {"code_book": "1-corinthiens", "label_book": "1 Corinthiens", "id_book_emci": "1-corinthiens", "id_book_topbible": "46", "id_book_biblecom": "1CO"}, "46": {"code_book": "2-corinthiens", "label_book": "2 Corinthiens", "id_book_emci": "2-corinthiens", "id_book_topbible": "47", "id_book_biblecom": "2CO"}, "47": {"code_book": "galates", "label_book": "Galates", "id_book_emci": "galates", "id_book_topbible": "48", "id_book_biblecom": "GAL"}, "48": {"code_book": "ephesiens", "label_book": "Ephésiens", "id_book_emci": "ephesiens", "id_book_topbible": "49", "id_book_biblecom": "EPH"}, "49": {"code_book": "philippiens", "label_book": "Philippiens", "id_book_emci": "philippiens", "id_book_topbible": "50", "id_book_biblecom": "PHP"}, "50": {"code_book": "colossiens", "label_book": "Colossiens", "id_book_emci": "colossiens", "id_book_topbible": "51", "id_book_biblecom": "COL"}, "51": {"code_book": "1-thessaloniciens", "label_book": "1 Thessaloniciens", "id_book_emci": "1-thessaloniciens", "id_book_topbible": "52", "id_book_biblecom": "1TH"}, "52": {"code_book": "2-thessaloniciens", "label_book": "2 Thessaloniciens", "id_book_emci": "2-thessaloniciens", "id_book_topbible": "53", "id_book_biblecom": "2TH"}, "53": {"code_book": "1-timothee", "label_book": "1 Timothée", "id_book_emci": "1-timothee", "id_book_topbible": "54", "id_book_biblecom": "1TI"}, "54": {"code_book": "2-timothee", "label_book": "2 Timothée", "id_book_emci": "2-timothee", "id_book_topbible": "55", "id_book_biblecom": "2TI"}, "55": {"code_book": "tite", "label_book": "Tite", "id_book_emci": "tite", "id_book_topbible": "56", "id_book_biblecom": "TIT"}, "56": {"code_book": "philemon", "label_book": "Philémon", "id_book_emci": "philemon", "id_book_topbible": "57", "id_book_biblecom": "PHM"}, "57": {"code_book": "hebreux", "label_book": "Hébreux", "id_book_emci": "hebreux", "id_book_topbible": "58", "id_book_biblecom": "HEB"}, "58": {"code_book": "jacques", "label_book": "Jacques", "id_book_emci": "jacques", "id_book_topbible": "59", "id_book_biblecom": "JAS"}, "59": {"code_book": "1-pierre", "label_book": "1 Pierre", "id_book_emci": "1-pierre", "id_book_topbible": "60", "id_book_biblecom": "1PE"}, "60": {"code_book": "2-pierre", "label_book": "2 Pierre", "id_book_emci": "2-pierre", "id_book_topbible": "61", "id_book_biblecom": "2PE"}, "61": {"code_book": "1-jean", "label_book": "1 Jean", "id_book_emci": "1-jean", "id_book_topbible": "62", "id_book_biblecom": "1JN"}, "62": {"code_book": "2-jean", "label_book": "2 Jean", "id_book_emci": "2-jean", "id_book_topbible": "63", "id_book_biblecom": "2JN"}, "63": {"code_book": "3-jean", "label_book": "3 Jean", "id_book_emci": "3-jean", "id_book_topbible": "64", "id_book_biblecom": "3JN"}, "64": {"code_book": "jude", "label_book": "Jude", "id_book_emci": "jude", "id_book_topbible": "65", "id_book_biblecom": "JUD"}, "65": {"code_book": "apocalypse", "label_book": "Apocalypse", "id_book_emci": "apocalypse", "id_book_topbible": "66", "id_book_biblecom": "REV"}}
        
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
    
