import sys
from pathlib import Path

IMAGE_FILES = []
VIDEO_FILES = []
DOCUMENT_FILES = []
AUDIO_FILES = []
ARCHIVE_FILES = []
UNKNOWN_FILES = []

REGISTER_EXTENSION = {
    'JPEG': IMAGE_FILES,
    'JPG': IMAGE_FILES,
    'PNG': IMAGE_FILES,
    'SVG': IMAGE_FILES,
    'AVI': VIDEO_FILES,
    'MP4': VIDEO_FILES,
    'MOV': VIDEO_FILES,
    'MKV': VIDEO_FILES,
    'DOC': DOCUMENT_FILES,
    'DOCX': DOCUMENT_FILES,
    'TXT': DOCUMENT_FILES,
    'PDF': DOCUMENT_FILES,
    'XLSX': DOCUMENT_FILES,
    'PPTX': DOCUMENT_FILES,
    'MP3': AUDIO_FILES,
    'OGG': AUDIO_FILES,
    'WAV': AUDIO_FILES,
    'AMR': AUDIO_FILES,
    'ZIP': ARCHIVE_FILES,
    'GZ': ARCHIVE_FILES,
    'TAR': ARCHIVE_FILES
}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()

def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper() if '.' in filename else ''

def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir() and item.name not in ('archives', 'videos', 'audio', 'documents', 'images', 'unknown'):
            FOLDERS.append(item)
            scan(item)
            continue

        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            UNKNOWN_FILES.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSION.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                UNKNOWN_FILES.append(fullname)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_to_scan = sys.argv[1]
        print(f'Starting in folder: {folder_to_scan}')
        scan(Path(folder_to_scan))
        print(f'Images (JPEG): {IMAGE_FILES}')
        print(f'Images (JPG): {IMAGE_FILES}')
        print(f'Images (PNG): {IMAGE_FILES}')
        print(f'Images (SVG): {IMAGE_FILES}')
        print(f'Videos (AVI): {VIDEO_FILES}')
        print(f'Videos (MP4): {VIDEO_FILES}')
        print(f'Videos (MOV): {VIDEO_FILES}')
        print(f'Videos (MKV): {VIDEO_FILES}')
        print(f'Documents (DOC): {DOCUMENT_FILES}')
        print(f'Documents (DOCX): {DOCUMENT_FILES}')
        print(f'Documents (TXT): {DOCUMENT_FILES}')
        print(f'Documents (PDF): {DOCUMENT_FILES}')
        print(f'Documents (XLSX): {DOCUMENT_FILES}')
        print(f'Documents (PPTX): {DOCUMENT_FILES}')
        print(f'Audio (MP3): {AUDIO_FILES}')
        print(f'Audio (OGG): {AUDIO_FILES}')
        print(f'Audio (WAV): {AUDIO_FILES}')
        print(f'Audio (AMR): {AUDIO_FILES}')
        print(f'Archives (ZIP): {ARCHIVE_FILES}')
        print(f'Archives (GZ): {ARCHIVE_FILES}')
        print(f'Archives (TAR): {ARCHIVE_FILES}')

        print(f'Types of files in folder: {EXTENSION}')
        print(f'Unknown file types: {UNKNOWN}')
        print(f'Unknown files: {UNKNOWN_FILES}')

        print(FOLDERS)
    else:
        print("Please provide a folder path as an argument.")
