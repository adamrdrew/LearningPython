from labler.lib import *

Scanner = MusicScanner(CONFIG["LibraryDirectory"])
Scanner.Debug = True
Scanner.ScanLibrary()

ArtScanner = AlbumArtScanner()
ArtScanner.ScanLibrary()