import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEOS = []
MP4_VIDEOS = []
MOV_VIDEOS = []
MKV_VIDEOS = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []
UNKNOWN_FILES = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEOS,
    'MP4': MP4_VIDEOS,
    'MOV': MOV_VIDEOS,
    'MKV': MKV_VIDEOS,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES
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
        print(f'Images (JPEG): {JPEG_IMAGES}')
        print(f'Images (JPG): {JPG_IMAGES}')
        print(f'Images (PNG): {PNG_IMAGES}')
        print(f'Images (SVG): {SVG_IMAGES}')
        print(f'Videos (AVI): {AVI_VIDEOS}')
        print(f'Videos (MP4): {MP4_VIDEOS}')
        print(f'Videos (MOV): {MOV_VIDEOS}')
        print(f'Videos (MKV): {MKV_VIDEOS}')
        print(f'Documents (DOC): {DOC_DOCUMENTS}')
        print(f'Documents (DOCX): {DOCX_DOCUMENTS}')
        print(f'Documents (TXT): {TXT_DOCUMENTS}')
        print(f'Documents (PDF): {PDF_DOCUMENTS}')
        print(f'Documents (XLSX): {XLSX_DOCUMENTS}')
        print(f'Documents (PPTX): {PPTX_DOCUMENTS}')
        print(f'Audio (MP3): {MP3_AUDIO}')
        print(f'Audio (OGG): {OGG_AUDIO}')
        print(f'Audio (WAV): {WAV_AUDIO}')
        print(f'Audio (AMR): {AMR_AUDIO}')
        print(f'Archives (ZIP): {ZIP_ARCHIVES}')
        print(f'Archives (GZ): {GZ_ARCHIVES}')
        print(f'Archives (TAR): {TAR_ARCHIVES}')

        print(f'Types of files in folder: {EXTENSION}')
        print(f'Unknown file types: {UNKNOWN}')
        print(f'Unknown files: {UNKNOWN_FILES}')

        print(FOLDERS)
    else:
        print("Please provide a folder path as an argument.")
