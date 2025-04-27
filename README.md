# Elemzés - József Attila versei

József Attila válogatott versinek elemzése Python segítségével. Az elemzés az NLTK Python könyvtár 
segítségével készült:

```
Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
```

## Hogyan használjuk

Telepítsük a Python egy friss verzióját, pl `3.12`. Telepítsük a szükséges könyvtárakat:

```bash
python -m pip install -r requirements.txt
```

### Versek letöltése

A program a MEK oldaláról tölti le József Attila válogatott verseit. Ezek külön-külön és egyben is 
mentésre kerülnek szöveges fájlokba.

```bash
python scrape_verses.py
```

A versek a `verses` mappába kerülnek a script mellé.

### Magyar nyelvcsomag telepítése

Az NLTK-hoz használható magyar nyelvcsomag mellékelve van ide, `hungarian.pickle` néven. Ennek forrása:

- https://github.com/mhq/train_punkt/blob/master/hungarian.pickle

Ezt telepíteni és előkészíteni kell:

```bash
python install_hungarian_pack.py
```

### Versek elemzése

Az elemző scriptnek meg kell adni, hogy melyik versből olvasson be tartalmat. A lehetséges verseket a 
`verses` mappában találjuk. Például ha a `verse_0024.txt` tartalmát szeretnénk elemezni, akkor:

```bash
python analyze_verse.py verse_0024
```

Az eredmények a `results` mappába kerülnek. Ezek szintén szöveges fájlok, az egyszerűség kedvéért.