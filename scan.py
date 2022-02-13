from lib.config import CONFIG
from lib.scanners import MusicScanner, AlbumArtScanner

Scanner = MusicScanner(CONFIG["LibraryDirectory"])
Scanner.Debug = True
Scanner.ScanLibrary()

ArtScanner = AlbumArtScanner()
ArtScanner.Debug = True
ArtScanner.ScanLibrary()