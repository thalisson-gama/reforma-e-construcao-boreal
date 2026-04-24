"""
Converte os ativos visuais do projeto Boreal (base/) para WebP em assets/.
- Logo: PNG ja transparente, apenas corta o espaco vazio ao redor.
- Hero background: redimensionado para max 1920px de largura, qualidade 82.
- Especialista: redimensionado para max 1200px de largura, qualidade 85.
"""
from PIL import Image
from pathlib import Path

BASE = Path(__file__).parent
SRC = BASE / "base"
DST = BASE / "assets"
DST.mkdir(exist_ok=True)

def convert_logo():
    src = SRC / "logo-boreal.png"
    dst = DST / "logo-boreal.webp"
    img = Image.open(src).convert("RGBA")
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    img.save(dst, "WEBP", quality=95, method=6, lossless=False)
    print(f"[OK] Logo         -> {dst.name}  ({dst.stat().st_size // 1024} KB)  [{img.width}x{img.height}]")

def convert_hero():
    src = SRC / "hero-bg.jpg"
    dst = DST / "hero-bg.webp"
    img = Image.open(src)
    max_w = 1920
    if img.width > max_w:
        ratio = max_w / img.width
        img = img.resize((max_w, int(img.height * ratio)), Image.LANCZOS)
    img.save(dst, "WEBP", quality=82, method=6)
    print(f"[OK] Hero         -> {dst.name}  ({dst.stat().st_size // 1024} KB)  [{img.width}x{img.height}]")

def convert_especialista():
    src = SRC / "especialista-boreal.png"
    dst = DST / "especialista-boreal.webp"
    img = Image.open(src)
    if img.mode != "RGB":
        img = img.convert("RGB")
    max_w = 1200
    if img.width > max_w:
        ratio = max_w / img.width
        img = img.resize((max_w, int(img.height * ratio)), Image.LANCZOS)
    img.save(dst, "WEBP", quality=85, method=6)
    print(f"[OK] Especialista -> {dst.name}  ({dst.stat().st_size // 1024} KB)  [{img.width}x{img.height}]")

if __name__ == "__main__":
    convert_logo()
    convert_hero()
    convert_especialista()
    print("\nConversao concluida.")
