# bible-api

Bible API library from JSON data

## Methods

+ **getBibleVersions()**: Get available Bible versions. 
+ **getBibleBooks()**: Get the Bible book list (Genesis, Exodus, Leviticus...) 
+ **getVersesFromBook(version, book)**: Get all verses Bible book.
+ **getVerse(version, book, chapter, num\_verse)**: Get a specific verse.
+ **getVersesFromSearch(pattern, version = '', book = '', chapter = '')**: Get verses from a search pattern

## How it works

+ Provide Bible data (books name's, versions name's, verses) from JSON collection files.
+ Caching process: Store verses result in a global python array

