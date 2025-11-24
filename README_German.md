![Lizenz: Kostenlose Version MIT](https://img.shields.io/badge/License-Free%20MIT-green.svg)
![Lizenz: Pro-Version Proprietary](https://img.shields.io/badge/License-Proprietary-red.svg)
![Plattform: Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)
![Sprache: Python 3.10+](https://img.shields.io/badge/Language-Python_3.10+-yellow.svg)  

---

Dieses Projekt hat zwei Editionen:
- **Kostenlose Version**: MIT-lizenziert, Quellcode verfügbar  
- **Pro-Version**: Proprietär, Quellcode geschlossen

---

## README in anderen Sprachen

- [Englische Version (README.md)](README.md)
- [Japanische Version (README_Japanese.md)](README_Japanese.md)

---

## Wo Sie die Anwendung erhalten (Microsoft Store)

- [Path List (Kostenlose Version)] — Download-Link wird nach der Veröffentlichung hinzugefügt.  
- [Path List Pro (Pro-Version)](https://apps.microsoft.com/detail/9P3C6RXVNMSW)

---

# Path List / Path List Pro

This tool ist ein schlankes Tool, das vollständige Dateipfade (absolute Pfade) aus Ordnern schnell und einfach generiert.  
In der Pro-Version können Sie außerdem Ordnerinhalte in einer Baumstruktur extrahieren und die Ergebnisse nach Excel oder in ähnliche Formate exportieren.
  
Es unterstützt Unicode vollständig und stellt sicher, dass Zeichen jeder Sprache korrekt verarbeitet werden.  
Die Benutzeroberfläche der Anwendung ist auf Japanisch, Englisch und Deutsch verfügbar, weitere Sprachen sind geplant.

Diese App greift nicht auf das Web zu, zeigt keine Werbung an und ändert keine Registrierungseinträge.  
Sie kommuniziert nicht mit externen Servern und sammelt keine persönlichen Daten – vollständige Sicherheit und Datenschutz sind gewährleistet.

---

## Verwendung (Kostenlose und Pro-Versionen)

![UsageAndUI_DE](docs/UsageAndUI/UsageAndUI_DE.png)
1. Starten Sie die Anwendung.  
2. Ziehen Sie einen Ordner (oder dessen Verknüpfung) auf den angezeigten Dialog. Ob das Ziehen und Ablegen  abgeschlossen ist, erkennen Sie an der Anzeige im Dialog.
   - Wenn Sie eine Datei (oder deren Verknüpfung) ziehen und ablegen, wird das übergeordnete Verzeichnis  dieser Datei als Extraktionsziel verwendet.  
   - Sie können mehrere Ordner und mehrere Dateien gleichzeitig ziehen und ablegen. (Baummodus wird nicht unterstützt.)  
   Dieses Tool stellt sicher, dass derselbe Ordner nicht mehrfach in der Ausgabe erscheint.  
3. Wählen Sie im Dialog die gewünschten Ausgabeoptionen und klicken Sie auf **[OK]**.  
   - Wenn Sie die Standardeinstellungen verwenden möchten, drücken Sie einfach **[Enter]**.  
4. Nach Abschluss der Ausgabe wird eine Listen-Datei auf Ihrem Desktop erstellt.

---

## Screenshots (Deutsch)

Die Anzeigesprache der Anwendung wechselt automatisch entsprechend den Windows-Gebietsschemaeinstellungen.  
Beispiele für die Benutzeroberfläche in jeder Sprache sind in den jeweiligen sprachspezifischen README-Dateien aufgeführt.

- [Kostenlose Version UI](docs/Screenshot_03_German/11_Dialog_List_Free_Before.png)  
- [Pro-Version UI (Listenmodus)](docs/Screenshot_03_German/01_Dialog_List_Pro_Before.png)  
- [Pro-Version UI (Baummodus)](docs/Screenshot_03_German/03_Dialog_Tree_Pro.png)

---

## Ausgabebeispiele (Deutsch)

Beispiele für Ausgabedateien, die von der Anwendung erzeugt wurden.  
Bitte verwenden Sie diese Beispiele als Referenz, um den tatsächlichen Ausgabeinhalt und die Formatierung zu überprüfen.


- [Ausgabe der kostenlosen Version (Listenmodus)](docs/OutputSamples_03_German/01_List_Free.txt)  
- [Ausgabe der Pro-Version (Listenmodus)](docs/OutputSamples_03_German/02_List_Pro.xlsx)  
  - ※ Diese Excel-Datei wurde auf einem System **ohne installierte Microsoft Excel-Version** erzeugt.  
    Wenn Excel installiert ist, erfolgt die Ausgabe aufgrund der COM-Beschleunigung schneller.  
- [Ausgabe der Pro-Version (Baummodus)](docs/OutputSamples_03_German/03_Tree_Pro.txt)

---

## Über die kostenlose und die Pro-Version

Die kostenlose Version ist eine voll funktionsfähige App mit den Funktionen, die der Entwickler täglich verwendet.  
Um ein reibungsloses Erlebnis zu gewährleisten, werden keine Anzeigen angezeigt, keine Nutzungsbeschränkungen auferlegt und keine Aufforderungen zum Upgrade auf die Pro-Version angezeigt.

Die Pro-Version bietet die folgenden zusätzlichen Funktionen:  
Die baumstrukturierte Ansicht und die Excel-Ausgabefunktionen sind besonders nützlich.

1. Zusätzlich zur Pfadliste (Listenmodus) können Sie eine Ausgabe in Baumstruktur (Baummodus) erzeugen.  
2. Sie können Dateinamen und Ordnernamen (ohne Pfad) mit einem Suchbegriff filtern.  
   - Beispiel: Die Suche nach „.xlsx“ (Suffix-Übereinstimmung) extrahiert Excel-Dateien.  
3. Sie können die folgenden Informationen extrahieren:  
   - Datei-/Ordnername (ohne Pfad)  
   - Größe  
   - Zeitstempel (erstellt, geändert, zugegriffen)  
4. Ausgabeformatoptionen:  
   - `.txt`  
   - `.csv`  
   - `.csv` (Felder in doppelte Anführungszeichen gesetzt)  
   - `.xlsx`

---

## Funktionsliste (Listenmodus)

- Ziel: Dateien / Ordner  
- Unterordner einbeziehen: Ja / Nein  
- Suchbegriff (nur Pro-Version)  
- Größe (nur Pro-Version)  
- Datei-/Ordnername (ohne Pfad) (nur Pro-Version): mit/ohne Erweiterung  
- Zeitstempel (nur Pro-Version): erstellt / geändert / zugegriffen  
- Ausgabeformate (nur Pro-Version): Text / CSV / CSV (zitiert) / Excel  

  Hinweis: Excel-Dateien können auch erzeugt werden, wenn Microsoft Excel nicht installiert ist.

Hinweis: In der Eingabeaufforderung können Unicode-Zeichen (z. B. „Résumé“) auf dem Bildschirm korrekt angezeigt werden,  
aber in Ausgabedateien fehlerhaft erscheinen.  
Path List und Path List Pro unterstützen Unicode und geben Zeichen jeder Sprache korrekt aus.

Entsprechende Beispiele für die Eingabeaufforderung:  
```
dir /b /s /a-d > %USERPROFILE%\desktop\FileList.txt
```
```
dir /b /s /ad > %USERPROFILE%\desktop\FolderList.txt
```

---

## Funktionsliste (Baummodus) [Nur Pro-Version]

- Dateiinformationen abrufen: Ja / Nein (entspricht der Option `tree /f`)  
- Ausgabestil: Normal / ASCII-Zeichen (entspricht der Option `tree /a`)  

Hinweis: In englischen/deutschen Umgebungen beeinflusst die Option `/a` die Anzeige in der Eingabeaufforderung,  
aber die Dateiausgabe erfolgt immer im `/a`-Format. Path List Pro ermöglicht eine Ausgabe ohne `/a`,  
die der Bildschirmdarstellung entspricht.

Referenzbefehl:  
```
tree /f > %USERPROFILE%\desktop\FileTree.txt
```

---

## Weitere Details

- Die Benutzeroberfläche verwendet eine Schriftgröße, die 1 pt größer ist als der Systemstandard, für bessere Lesbarkeit.  
- Hohe DPI-Unterstützung: Kompatibel mit hochauflösenden Displays und Skalierungseinstellungen.

---

## Unterstützte Sprachen

- Deutsch, Englisch, Japanisch  
- Automatisches Umschalten entsprechend den Windows-Gebietsschemaeinstellungen („Sprache und Region“)  
- Für andere Sprachen als Japanisch und Deutsch wird Englisch verwendet.

---

## Entwicklungs- und Testumgebung

- Betriebssystem: Windows 11 Pro 24H2 (Japanisch), Windows 11 Home 24H2 (Englisch/Deutsch)  
- CPU: AMD Ryzen 7 8845HS  
- Arbeitsspeicher: 32 GB  
- Englische und deutsche Umgebungen wurden auf Hyper-V (virtuelle Maschinen) getestet.  
- Entwickelt für Windows 10 und 11 (Betrieb auf allen Editionen, z. B. SE oder Education, nicht garantiert).

---

## Test und Verifikation

- Diese Anwendung wurde einer detaillierten und umfassenden Test- und Verifikationsphase unterzogen.  
Bitte beziehen Sie sich auf Folgendes für die Testfälle und Beispielordner:
- [Liste der Testfälle (List_of_Test_Cases.xlsx)](docs/List_of_Test_Cases.xlsx)  
- [Beispielordner für einen einzelnen Ordner-Drop (TestFolder_01)](docs/TestFolder_01)  
- [Beispielordner für mehrere Ordner-Drops (TestFolder_02)](docs/TestFolder_02)

---

## Programmiersprache

1. **Python 3.10.11 (CPython)**  
2. **Standardbibliotheken:**  
   - `locale`: Gebietsschema (Sprache und Region) abrufen  
   - `sys`: Befehlszeilenargumente abrufen  
   - `os`: Pfadverarbeitung, Existenzprüfung, Auflistung  
   - `ctypes`: Windows API (hohe DPI-Unterstützung)  
   - `datetime`: Datum/Uhrzeit abrufen  
   - `threading`: Hintergrundverarbeitung (nur Pro-Version)  
   - `gc`: GC-Steuerung für COM-Freigabe (nur Pro-Version)  
3. **Externe Bibliotheken:**  
   - `wxPython`: GUI  
   - `pywin32 (win32com.client)`: `.lnk`-Ziele abrufen, COM-Operationen  
   - `openpyxl`: Excel-Ausgabe (nur Pro-Version, Lazy Loading)

---

## Versionsverlauf

### Free-Version

| Version | Datum       | Beschreibung                                                                 |
|---------|------------|----------------------------------------------------------------------------|
| 1.00    | 08.11.2025 | Erste Veröffentlichung                                                      |
| 1.10    | 24.11.2025 | Für die Verteilung im Microsoft Store optimiert (MSIX-Funktionalität verbessert) |

### Pro-Version

| Version | Datum       | Beschreibung                                                                 |
|---------|------------|----------------------------------------------------------------------------|
| 1.00    | 08.11.2025 | Erste Veröffentlichung                                                      |
| 1.10    | 24.11.2025 | Für die Verteilung im Microsoft Store optimiert (MSIX-Funktionalität verbessert) |

---

## Kontakt

- 📧 **s.sugawara.dev@gmail.com**  
- Bitte senden Sie Feedback, Wünsche oder Fehlerberichte an die oben genannte Adresse.
- Diese Anwendung unterstützt mehrere Sprachen in ihrer Benutzeroberfläche.  
Anfragen in anderen Sprachen als Japanisch werden mit KI-gestützter Übersetzung bearbeitet.  
Ich bemühe mich, auf jedes Feedback aufrichtig zu reagieren. Bitte haben Sie jedoch  Verständnis dafür, dass diese App von einer einzelnen Person entwickelt und betreut wird.  
Daher kann es zu Verzögerungen bei den Antworten kommen, und gelegentlich können Missverständnisse aufgrund der automatischen Übersetzung auftreten.

---

## Beiträge

Weitere Einzelheiten finden Sie im folgenden Dokument.

- [CONTRIBUTING_German.md](CONTRIBUTING_German.md)

---

## Unterstützung für Entwicklung und Support

- Wenn Sie die Weiterentwicklung und Pflege unterstützen möchten, können Sie dies hier tun.  
[Stripe Payment Links](https://buy.stripe.com/8x200lalBfsvfW13BO9sk03)  
- Wenn Sie die Pro-Version noch nicht gekauft haben, erwägen Sie bitte den Kauf anstelle einer Spende.

---

## Urheberrecht

- Alle Rechte an **Path List / Path List Pro** liegen beim Entwickler.  
- Der Binärcode/Quellcode der Pro-Version ist geschlossen.  
  Weitergabe, Modifikation, Dekompilierung und Reverse Engineering sind verboten.  
- Der Quellcode der kostenlosen Version wird unter der **MIT-Lizenz** veröffentlicht.  
[PathList_1.10.py auf GitHub ansehen](https://github.com/Shintaro-Sugawara/PathList/blob/master/src/PathList_1.10.py)
- Abgesehen von der Microsoft Store-Zahlung für die Pro-Version sind keine zusätzlichen Lizenzgebühren erforderlich.  
- © 2025 **S. Sugawara** Alle Rechte vorbehalten.
