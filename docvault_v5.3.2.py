"""
╔══════════════════════════════════════════════════════════════╗
║  DocVault v3.0.0 – Dokumentenverwaltung für Windows 11      ║
║  Native Desktop-App · Kein Webserver · Kein localhost        ║
╚══════════════════════════════════════════════════════════════╝
Starten:  python docvault_v3.0.0.py
"""
VERSION = "5.3.2"

# ╔══════════════════════════════════════════════════════════════╗
# ║  LIZENZSCHUTZ: SHA-256 Hash mit Salt + Ablaufdatum          ║
# ║  Format: TIMESTAMP-SHA256(TIMESTAMP|Salt)[:16]              ║
# ╚══════════════════════════════════════════════════════════════╝
LIC_SALT = "THATSTHEBEGINNING"

# ═══════════════════════════════════════════════════════════════
# ZWEISPRACHIG (Deutsch / English)
# Spracherkennung: Nicht-deutsches Windows → Englisch
# Manuell umschaltbar in den Einstellungen
# ═══════════════════════════════════════════════════════════════
_LANG = "de"  # Wird beim Start gesetzt
_TR = {
    # ── Navigation ──
    "nav_backup":       {"de": "💾  Backup",          "en": "💾  Backup"},
    "nav_import":       {"de": "📥  Importieren",     "en": "📥  Import"},
    "nav_note":         {"de": "✏️  Neue Notiz",      "en": "✏️  New Note"},
    "nav_scanner":      {"de": "🖨️  Dokument einscannen", "en": "🖨️  Scan Document"},
    "nav_settings":     {"de": "⚙️  Einstellungen",   "en": "⚙️  Settings"},
    "nav_sync":         {"de": "🔄 Dokumente synchronisieren", "en": "🔄 Sync Documents"},
    "sync_title":       {"de": "Dokumente synchronisieren", "en": "Sync Documents"},
    "sync_scanning":    {"de": "Prüfe verknüpfte Dokumente...", "en": "Checking linked documents..."},
    "sync_found":       {"de": "{n} geänderte Dokumente gefunden", "en": "{n} changed documents found"},
    "sync_none":        {"de": "✅ Alle verknüpften Dokumente sind aktuell.", "en": "✅ All linked documents are up to date."},
    "sync_missing":     {"de": "⚠️ {n} Dateien nicht gefunden (verschoben/gelöscht)", "en": "⚠️ {n} files not found (moved/deleted)"},
    "sync_reindex":     {"de": "Jetzt neu indexieren", "en": "Re-index now"},
    "sync_progress":    {"de": "Indexiere {i}/{n}: {name}", "en": "Indexing {i}/{n}: {name}"},
    "sync_done":        {"de": "✅ {n} Dokumente neu indexiert", "en": "✅ {n} documents re-indexed"},
    "sync_license":     {"de": "Diese Funktion erfordert eine gültige Lizenznummer.\n\nAb einem Sponsoring von CHF 30.- erhalten Sie eine\nLizenznummer mit erweiterten Funktionen.", "en": "This feature requires a valid license key.\n\nWith a sponsorship of CHF 30 or more, you will receive\na license key with extended features."},
    "cat_header":       {"de": "KATEGORIEN",           "en": "CATEGORIES"},
    "all_docs":         {"de": "Alle Dokumente",       "en": "All Documents"},
    "favorites":        {"de": "⭐ Favoriten",         "en": "⭐ Favorites"},
    "no_docs":          {"de": "📭 Keine Dokumente",   "en": "📭 No documents"},
    "docs_singular":    {"de": "Dokument",             "en": "document"},
    "docs_plural":      {"de": "Dokumente",            "en": "documents"},
    "page":             {"de": "Seite",                "en": "Page"},
    "search_placeholder": {"de": "🔍 Suchen...",       "en": "🔍 Search..."},
    # ── Sortierung ──
    "sort_date_desc":   {"de": "Datum ↓ (neueste)",    "en": "Date ↓ (newest)"},
    "sort_date_asc":    {"de": "Datum ↑ (älteste)",    "en": "Date ↑ (oldest)"},
    "sort_size_desc":   {"de": "Grösse ↓",            "en": "Size ↓"},
    "sort_size_asc":    {"de": "Grösse ↑",            "en": "Size ↑"},
    "sort_pages_desc":  {"de": "Seiten ↓",            "en": "Pages ↓"},
    "sort_pages_asc":   {"de": "Seiten ↑",            "en": "Pages ↑"},
    "sort_name_az":     {"de": "Name A-Z",             "en": "Name A-Z"},
    "sort_name_za":     {"de": "Name Z-A",             "en": "Name Z-A"},
    "sort_star":        {"de": "★ Favoriten zuerst",   "en": "★ Favorites first"},
    "sort_updated":     {"de": "Zuletzt geändert",     "en": "Recently updated"},
    "sort_label":       {"de": "Sortierung:",          "en": "Sort:"},
    # ── Scanner ──
    "scan_title":       {"de": "🖨️ Scanner (NAPS2)",  "en": "🖨️ Scanner (NAPS2)"},
    "scan_btn":         {"de": "🖨️ Scannen",          "en": "🖨️ Scan"},
    "scan_search":      {"de": "🔄 Scanner suchen",   "en": "🔄 Find Scanners"},
    "scan_preview":     {"de": "Scan-Vorschau",        "en": "Scan Preview"},
    "scan_accept":      {"de": "✅ OK – Archivieren",  "en": "✅ OK – Archive"},
    "scan_cancel":      {"de": "❌ Verwerfen",         "en": "❌ Discard"},
    "scan_format":      {"de": "Speicherformat:",      "en": "Storage format:"},
    "scan_manual":      {"de": "Manuelle Scan-Einstellungen:", "en": "Manual scan settings:"},
    "scan_manual_off":  {"de": "Manuelle Scan-Einstellungen (deaktiviert – Profil aktiv):", "en": "Manual scan settings (disabled – profile active):"},
    # ── Import ──
    "import_title":     {"de": "📥 Importieren",      "en": "📥 Import"},
    "import_copy":      {"de": "Kopieren",             "en": "Copy"},
    "import_link":      {"de": "Nur verknüpfen",      "en": "Link only"},
    # ── Einstellungen ──
    "sett_title":       {"de": "⚙️ Einstellungen",    "en": "⚙️ Settings"},
    "sett_datapath":    {"de": "📁 DATENPFAD (gemeinsam für alle PCs)", "en": "📁 DATA PATH (shared across PCs)"},
    "sett_local":       {"de": "💻 LOKALE EINSTELLUNGEN (nur dieser PC)", "en": "💻 LOCAL SETTINGS (this PC only)"},
    "sett_shared":      {"de": "🌐 GEMEINSAME EINSTELLUNGEN (alle PCs)", "en": "🌐 SHARED SETTINGS (all PCs)"},
    "sett_searchidx":   {"de": "🔍 SUCHINDEX-EINSTELLUNGEN", "en": "🔍 SEARCH INDEX SETTINGS"},
    "sett_plugins":     {"de": "🔌 PLUGINS (Vorschau-Erweiterungen)", "en": "🔌 PLUGINS (Preview Extensions)"},
    "sett_sysinfo":     {"de": "ℹ️ SYSTEM-INFO",      "en": "ℹ️ SYSTEM INFO"},
    "sett_appearance":  {"de": "Darstellung:",         "en": "Appearance:"},
    "sett_dark":        {"de": "Dunkel",               "en": "Dark"},
    "sett_light":       {"de": "Hell",                 "en": "Light"},
    "sett_pagesize":    {"de": "Dokumente pro Seite:", "en": "Documents per page:"},
    "sett_ocrlang":     {"de": "OCR-Sprache:",         "en": "OCR Language:"},
    "sett_importmode":  {"de": "Standard-Import:",     "en": "Default import:"},
    "sett_language":    {"de": "🌐 SPRACHE / LANGUAGE", "en": "🌐 LANGUAGE / SPRACHE"},
    "sett_lang_de":     {"de": "Deutsch",              "en": "Deutsch"},
    "sett_lang_en":     {"de": "English",              "en": "English"},
    "sett_license":     {"de": "🔑 LIZENZ",            "en": "🔑 LICENSE"},
    "sett_ai_tags":     {"de": "🤖 KI-SCHLAGWÖRTER",  "en": "🤖 AI KEYWORDS"},
    "sett_ai_provider": {"de": "KI-Anbieter:",         "en": "AI Provider:"},
    "sett_ai_token":    {"de": "API-Token:",            "en": "API Token:"},
    "sett_ai_token_ph": {"de": "API-Schlüssel eingeben...", "en": "Enter API key..."},
    "sett_ai_active":   {"de": "✅ KI-Schlagwörter aktiv ({prov})", "en": "✅ AI keywords active ({prov})"},
    "sett_ai_inactive": {"de": "Kein API-Token gesetzt – Schlagwörter werden regelbasiert generiert", "en": "No API token set – keywords are generated rule-based"},
    "sett_ai_save":     {"de": "Speichern", "en": "Save"},
    "sett_ai_test":     {"de": "🧪 Testen", "en": "🧪 Test"},
    "sett_ai_hint":     {"de": "Optional: Generiert intelligente Schlagwörter per KI beim Importieren.\nSie benötigen einen eigenen API-Token vom gewählten Anbieter.", "en": "Optional: Generates smart keywords via AI when importing.\nYou need your own API token from the selected provider."},
    "nav_licenses":     {"de": "⚖️ Lizenzen & Urheberrechte", "en": "⚖️ Licenses & Copyright"},
    "sett_license_enter": {"de": "Lizenznummer eingeben:", "en": "Enter license key:"},
    "sett_license_activate": {"de": "Aktivieren",      "en": "Activate"},
    "sett_license_ok":  {"de": "✅ Lizenz gültig",     "en": "✅ License valid"},
    "sett_license_invalid": {"de": "❌ Ungültige oder abgelaufene Lizenznummer", "en": "❌ Invalid or expired license key"},
    "sett_license_free": {"de": "Kostenlose Version (unregistriert)", "en": "Free version (unregistered)"},
    "sett_license_expiry": {"de": "Pausenfreie Lizenz gültig bis {date}", "en": "Pause-free license valid until {date}"},
    # ── Löschen ──
    "del_title":        {"de": "⚠️ Endgültig löschen", "en": "⚠️ Delete permanently"},
    "del_confirm":      {"de": "Dokument(e) endgültig löschen?", "en": "Delete document(s) permanently?"},
    "del_file_warn":    {"de": "Datei(en) werden von der Festplatte gelöscht!", "en": "File(s) will be deleted from disk!"},
    "del_link_info":    {"de": "Verknüpfung(en) – Originaldateien bleiben erhalten.", "en": "Link(s) – original files will be kept."},
    "del_no_undo":      {"de": "Dieser Vorgang kann NICHT rückgängig gemacht werden!", "en": "This action CANNOT be undone!"},
    # ── Disclaimer ──
    "disclaimer_title": {"de": "DocVault – Nutzungsbedingungen", "en": "DocVault – Terms of Use"},
    "disclaimer_btn":   {"de": "Gelesen und akzeptiert", "en": "Read and accepted"},
    # ── Donation ──
    "donate_title":     {"de": "DocVault – Unterstützen Sie uns!", "en": "DocVault – Support us!"},
    "donate_text":      {"de": (
        "DocVault ist ein spendenfinanziertes Open-Source-Projekt.\n\n"
        "Die Weiterentwicklung, der Support und die Pflege dieses Programms\n"
        "sind nur durch Ihre Unterstützung möglich.\n\n"
        "Bitte erwägen Sie eine Spende,\n"
        "um die Zukunft von DocVault zu sichern.\n\n"
        "Ab einem Sponsoring von CHF 30.- erhalten Sie eine\n"
        "Lizenznummer. Damit entfallen diese Wartepause und\n"
        "die Weiterleitung auf die DocVault-Webseite.\n\n"
        "Vielen Dank für Ihre Unterstützung!\n\n"
        "CADTEC GmbH\nwww.cadtec.ch"
    ), "en": (
        "DocVault is a donation-funded open-source project.\n\n"
        "Continued development, support and maintenance of this program\n"
        "are only possible through your support.\n\n"
        "Please consider making a donation\n"
        "to secure the future of DocVault.\n\n"
        "With a sponsorship of CHF 30 or more, you will receive\n"
        "a license key. This will remove the waiting pause and\n"
        "the redirect to the DocVault website.\n\n"
        "Thank you for your support!\n\n"
        "CADTEC GmbH\nwww.cadtec.ch"
    )},
    "donate_close_in":  {"de": "Schliessen in {s}s...", "en": "Close in {s}s..."},
    "donate_close":     {"de": "Schliessen",           "en": "Close"},
    # ── Notiz-Editor ──
    "note_title":       {"de": "Notiz-Editor",         "en": "Note Editor"},
    "note_save":        {"de": "💾 Speichern",         "en": "💾 Save"},
    "note_print":       {"de": "🖨️ Drucken",          "en": "🖨️ Print"},
    "note_title_ph":    {"de": "Titel...",              "en": "Title..."},
    "note_link_title":  {"de": "Link einfügen",        "en": "Insert Link"},
    "note_link_url":    {"de": "URL (https://...):",    "en": "URL (https://...):"},
    # ── Kategorien-Manager ──
    "catmgr_title":     {"de": "Kategorien",            "en": "Categories"},
    "catmgr_hint":      {"de": "Hauptkategorien und Unterkategorien · ▲▼ zum Sortieren", "en": "Categories and subcategories · ▲▼ to sort"},
    "catmgr_new":       {"de": "➕ Neue Hauptkategorie", "en": "➕ New Main Category"},
    "catmgr_edit_title": {"de": "Kategorie",           "en": "Category"},
    "catmgr_save":      {"de": "Speichern",             "en": "Save"},
    "catmgr_no_cat":    {"de": "❓ Ohne Kategorie",     "en": "❓ Uncategorized"},
    "catmgr_manage":    {"de": "✏️  Kategorien verwalten", "en": "✏️  Manage Categories"},
    # ── Dokumentliste ──
    "doc_select_preview": {"de": "Dokument auswählen\nfür Vorschau", "en": "Select document\nfor preview"},
    "doc_no_preview":   {"de": "Keine Vorschau verfügbar", "en": "No preview available"},
    "doc_pages":        {"de": "Seiten",                "en": "pages"},
    "doc_meta_name":    {"de": "Name:",                 "en": "Name:"},
    "doc_meta_cat":     {"de": "Kategorie:",            "en": "Category:"},
    "doc_meta_tags":    {"de": "Tags:",                 "en": "Tags:"},
    "doc_meta_tags_ph": {"de": "Komma-getrennt",       "en": "Comma-separated"},
    "doc_meta_save":    {"de": "💾 Metadaten speichern", "en": "💾 Save Metadata"},
    "doc_ai_retag":     {"de": "🤖 KI-Tags vorschlagen", "en": "🤖 Suggest AI Tags"},
    "doc_meta_source":  {"de": "Quelle:",               "en": "Source:"},
    "doc_open":         {"de": "📂 Öffnen",            "en": "📂 Open"},
    "doc_backup":       {"de": "💾 Backup",            "en": "💾 Backup"},
    "doc_delete":       {"de": "🗑️ Löschen",          "en": "🗑️ Delete"},
    "doc_tags_ph":      {"de": "Tags mit Komma trennen...", "en": "Separate tags with comma..."},
    # ── Import ──
    "import_copy":      {"de": "Kopieren",              "en": "Copy"},
    "import_link":      {"de": "Nur verknüpfen",       "en": "Link only"},
    "import_cat":       {"de": "Kategorie beim Import:", "en": "Category on import:"},
    "import_auto":      {"de": "(Automatisch)",         "en": "(Automatic)"},
    "import_files_btn": {"de": "📂 Dateien...",        "en": "📂 Files..."},
    "import_drop":      {"de": "📎  Dateien oder Ordner hier ablegen\n(Unterordner werden rekursiv eingelesen)", "en": "📎  Drop files or folders here\n(Subfolders are read recursively)"},
    "import_drop_active": {"de": "📎  Dateien oder Ordner hierher ziehen\n(Unterordner werden rekursiv eingelesen)\nDrag & Drop aktiv ✓", "en": "📎  Drag files or folders here\n(Subfolders are read recursively)\nDrag & Drop active ✓"},
    "import_drop_click": {"de": "📎  Hier klicken für Datei-Dialog\n\nFür Drag & Drop: pip install windnd", "en": "📎  Click here for file dialog\n\nFor Drag & Drop: pip install windnd"},
    "import_phase1":    {"de": "📥 Phase 1: Dateien importieren", "en": "📥 Phase 1: Importing files"},
    "import_phase2":    {"de": "🔤 Phase 2: OCR & Kategorisierung", "en": "🔤 Phase 2: OCR & Categorization"},
    "import_wait":      {"de": "Dies kann einige Minuten dauern...", "en": "This may take a few minutes..."},
    # ── Scanner ──
    "scan_profiles_load": {"de": "🔄 Profile laden",  "en": "🔄 Load Profiles"},
    "scan_profile_hint": {"de": "Profil übersteuert manuelle Einstellungen", "en": "Profile overrides manual settings"},
    "scan_no_profile":  {"de": "(Kein Profil – manuelle Einstellungen)", "en": "(No profile – manual settings)"},
    "scan_searching":   {"de": "⏳ Suche Scanner...",  "en": "⏳ Searching scanners..."},
    "scan_none_found":  {"de": "Keine Scanner gefunden", "en": "No scanners found"},
    "scan_naps2_missing": {"de": "NAPS2 nicht installiert", "en": "NAPS2 not installed"},
    "scan_click_search": {"de": "Klicken Sie 'Scanner suchen'", "en": "Click 'Find Scanners'"},
    "scan_adf_hint":    {"de": "ADF: Alle Seiten automatisch\nFlachbett: Seiten einzeln sammeln", "en": "ADF: All pages automatically\nFlatbed: Collect pages one by one"},
    "scan_ocr_test":    {"de": "🔍 OCR testen",       "en": "🔍 Test OCR"},
    "scan_deskew":      {"de": "Automatisch gerade richten", "en": "Auto deskew"},
    "scan_webp_hint":   {"de": "WebP spart ~50% Speicher, PDF ist universell kompatibel", "en": "WebP saves ~50% space, PDF is universally compatible"},
    "scan_naps2_path":  {"de": "📂 NAPS2 Pfad...",    "en": "📂 NAPS2 Path..."},
    "scan_naps2_open":  {"de": "🖥️ NAPS2 öffnen",    "en": "🖥️ Open NAPS2"},
    # ── Flatbed Multi-Page ──
    "flat_title":       {"de": "Flachbett – Mehrseitiger Scan", "en": "Flatbed – Multi-Page Scan"},
    "flat_page_done":   {"de": "✅ Seite {n} gescannt", "en": "✅ Page {n} scanned"},
    "flat_next":        {"de": "📄 Nächste Seite scannen", "en": "📄 Scan Next Page"},
    "flat_finish":      {"de": "✅ Fertig – Archivieren", "en": "✅ Done – Archive"},
    "flat_scanning":    {"de": "⏳ Seite {n} wird gescannt...", "en": "⏳ Scanning page {n}..."},
    "flat_merging":     {"de": "📑 {n} Seiten zusammenführen...", "en": "📑 Merging {n} pages..."},
    "flat_collected":   {"de": "📑 {n} Seite(n) gesammelt", "en": "📑 {n} page(s) collected"},
    "flat_place_page":  {"de": "Legen Sie die nächste Seite auf\nden Scanner und klicken Sie\n'Nächste Seite scannen'.", "en": "Place the next page on the\nscanner and click\n'Scan Next Page'."},
    # ── ADF Multi-Batch ──
    "adf_title":        {"de": "ADF – Mehrstapel-Scan", "en": "ADF – Multi-Batch Scan"},
    "adf_batch_done":   {"de": "✅ Stapel {n}: {p} Seiten gescannt", "en": "✅ Batch {n}: {p} pages scanned"},
    "adf_next_batch":   {"de": "📄 Nächsten Stapel scannen", "en": "📄 Scan Next Batch"},
    "adf_finish":       {"de": "✅ Fertig – Archivieren", "en": "✅ Done – Archive"},
    "adf_scanning":     {"de": "⏳ Stapel {n} wird gescannt...", "en": "⏳ Scanning batch {n}..."},
    "adf_merging":      {"de": "📑 {n} Stapel zusammenführen...", "en": "📑 Merging {n} batches..."},
    "adf_collected":    {"de": "📑 {p} Seiten aus {n} Stapel(n)", "en": "📑 {p} pages from {n} batch(es)"},
    "adf_place_batch":  {"de": "Legen Sie den nächsten Stapel\nin den Einzug und klicken Sie\n'Nächsten Stapel scannen'.", "en": "Place the next batch\nin the feeder and click\n'Scan Next Batch'."},
    # ── Backup ──
    "backup_creating":  {"de": "💾 Backup wird erstellt...", "en": "💾 Creating backup..."},
    "backup_ok":        {"de": "✅ Backup erfolgreich!", "en": "✅ Backup successful!"},
    "backup_show":      {"de": "📂 Backup im Explorer anzeigen", "en": "📂 Show backup in Explorer"},
    "backup_fail":      {"de": "❌ Backup fehlgeschlagen", "en": "❌ Backup failed"},
    "backup_fail_hint": {"de": "Fehlerdetails wurden in die Konsole geschrieben.\nBitte prüfen Sie den Speicherplatz.", "en": "Error details have been written to the console.\nPlease check available disk space."},
    # ── OCR Dialog ──
    "ocr_naps2_missing": {"de": "❌ NAPS2 nicht gefunden – bitte installieren: naps2.com", "en": "❌ NAPS2 not found – please install: naps2.com"},
    "ocr_lang_import":  {"de": "OCR-Sprache für importierte Dokumente:", "en": "OCR language for imported documents:"},
    "ocr_running":      {"de": "OCR-Texterkennung",    "en": "OCR Text Recognition"},
    "ocr_extracting":   {"de": "🔤 Text wird extrahiert...", "en": "🔤 Extracting text..."},
    "ocr_modified_hint": {"de": "Scan wurde bearbeitet – Text wird neu gelesen.", "en": "Scan was modified – text is being re-read."},
    # ── Bulk Tags ──
    "tags_title":       {"de": "Tags",                  "en": "Tags"},
    "tags_add_hint":    {"de": "Diese Tags werden ZUSÄTZLICH zu bestehenden Tags hinzugefügt.\nMit Komma trennen.", "en": "These tags will be ADDED to existing tags.\nSeparate with comma."},
    "tags_add_ph":      {"de": "z.B. wichtig, 2024, steuer", "en": "e.g. important, 2024, tax"},
    "tags_add_btn":     {"de": "➕ Hinzufügen",        "en": "➕ Add"},
    "tags_replace_btn": {"de": "🔄 Ersetzen",         "en": "🔄 Replace"},
    "tags_edit":        {"de": "Tags bearbeiten",       "en": "Edit Tags"},
    # ── Suchfeld ──
    "search_for":       {"de": "für",                   "en": "for"},
    "search_prefix":    {"de": "🔍 Suche:",            "en": "🔍 Search:"},
    # ── Plugins Settings ──
    "plug_reload":      {"de": "🔄 Plugins neu laden", "en": "🔄 Reload Plugins"},
    "plug_folder":      {"de": "📂 Plugin-Ordner öffnen", "en": "📂 Open Plugin Folder"},
    "plug_none":        {"de": "Keine Plugins gefunden.\nLegen Sie .py-Dateien im plugins/-Ordner ab.", "en": "No plugins found.\nPlace .py files in the plugins/ folder."},
    # ── Einstellungen Details ──
    "sett_naps2_path":  {"de": "NAPS2-Pfad:",         "en": "NAPS2 Path:"},
    "sett_naps2_change": {"de": "Ändern...",           "en": "Change..."},
    "sett_scanner":     {"de": "Gespeicherter Scanner:", "en": "Saved Scanner:"},
    "sett_change_path": {"de": "📂 Datenpfad ändern...", "en": "📂 Change data path..."},
    "sett_datapath_hint": {"de": "Datenbank, Dokumente und Thumbnails liegen hier.\nFür Multi-PC: Gemeinsamen Netzwerkordner wählen (z.B. Z:\\DocVault).", "en": "Database, documents and thumbnails are stored here.\nFor multi-PC: Choose a shared network folder (e.g. Z:\\DocVault)."},
    "sett_datapath_dlg_title": {"de": "Datenpfad ändern", "en": "Change Data Path"},
    "sett_datapath_dlg_hint": {"de": "Hier liegen Datenbank, Dokumente und Thumbnails.\nBeispiel: D:\\Dropbox\\DocVault", "en": "Database, documents and thumbnails are stored here.\nExample: D:\\Dropbox\\DocVault"},
    # ── PDF/WebP Vorschau Fehler ──
    "prev_no_fitz":     {"de": "PDF-Vorschau nicht verfügbar\n(PyMuPDF/fitz nicht installiert)", "en": "PDF preview not available\n(PyMuPDF/fitz not installed)"},
    "prev_webp_error":  {"de": "WebP-Vorschau nicht lesbar", "en": "WebP preview not readable"},
    "prev_error":       {"de": "⚠️ Vorschau-Fehler:", "en": "⚠️ Preview error:"},
    # ── Dark/Light labels ──
    "mode_dark":        {"de": "Dunkel",                "en": "Dark"},
    "mode_light":       {"de": "Hell",                  "en": "Light"},
    # ── Duplikat ──
    "dup_detected":     {"de": "Duplikat erkannt.",     "en": "Duplicate detected."},
    # ── Settings Detail-Texte ──
    "sett_current":     {"de": "Aktuell:", "en": "Current:"},
    "sett_local_hint":  {"de": "Diese Einstellungen gelten nur für diesen Computer\nund werden neben dem Programm gespeichert:", "en": "These settings apply only to this computer\nand are stored next to the program:"},
    "sett_shared_hint": {"de": "Werden in {path} gespeichert.\nÄnderungen gelten für alle PCs die auf denselben Datenordner zugreifen.", "en": "Stored in {path}.\nChanges apply to all PCs accessing the same data folder."},
    "sett_idx_hint":    {"de": "Steuert wie viel Text pro Dokument gespeichert und indexiert wird.\nGrössere Werte = bessere Suche bei grossen Dokumenten, aber mehr Speicherplatz.", "en": "Controls how much text per document is stored and indexed.\nLarger values = better search for large documents, but more disk space."},
    "sett_max_chars":   {"de": "Max. Textzeichen (ocr_text):", "en": "Max. text chars (ocr_text):"},
    "sett_max_chars_h": {"de": "   Wie viele Zeichen Rohtext pro Dokument in der DB gespeichert werden. 400 Seiten ≈ 400'000 Zeichen.", "en": "   How many raw text characters per document are stored in the DB. 400 pages ≈ 400,000 chars."},
    "sett_max_words":   {"de": "Max. Index-Wörter (Suche):", "en": "Max. index words (search):"},
    "sett_max_words_h": {"de": "   Wie viele einzigartige Wörter pro Dokument im Suchindex landen. Typisch: Rechnung ≈ 50-200, Brief ≈ 100-500, Buch ≈ 5'000-30'000.", "en": "   How many unique words per document end up in the search index. Typical: invoice ≈ 50-200, letter ≈ 100-500, book ≈ 5,000-30,000."},
    "sett_min_wlen":    {"de": "Min. Wortlänge:", "en": "Min. word length:"},
    "sett_min_wlen_h":  {"de": "   Wörter kürzer als diese Länge werden nicht indexiert. Stoppwörter: {n} (de+en).", "en": "   Words shorter than this length are not indexed. Stop words: {n} (de+en)."},
    "sett_chars":       {"de": "Zeichen", "en": "chars"},
    "sett_plugin_dir":  {"de": "Plugin-Ordner:", "en": "Plugin folder:"},
    "sett_restart_hint": {"de": "(Neustart erforderlich)", "en": "(Restart required)"},
    "sett_ocr_mode":    {"de": "OCR-Modus:", "en": "OCR Mode:"},
    # ── Scanner/Vorschau Detail ──
    "scan_active":      {"de": "✓ Aktiv", "en": "✓ Active"},
    "scan_naps2_notfound": {"de": "❌ NAPS2 nicht gefunden", "en": "❌ NAPS2 not found"},
    "scan_wait_adf":    {"de": "Bitte warten – bei ADF werden alle Seiten eingezogen.", "en": "Please wait – ADF is feeding all pages."},
    "scan_profile_lbl": {"de": "Profil:", "en": "Profile:"},
    "scan_scanner_lbl": {"de": "Scanner:", "en": "Scanner:"},
    "scan_all_pages":   {"de": "Alle Seiten:", "en": "All pages:"},
    "scan_profiles_ok": {"de": "✅ {n} Profil(e) geladen aus: {path}", "en": "✅ {n} profile(s) loaded from: {path}"},
    "scan_no_profiles": {"de": "⚠️ Keine profiles.xml gefunden – bitte NAPS2 öffnen und Profil erstellen", "en": "⚠️ No profiles.xml found – please open NAPS2 and create a profile"},
    # ── Dynamische Texte ──
    "files":            {"de": "Dateien", "en": "files"},
    "page_of":          {"de": "Seite {a} / {b}", "en": "Page {a} / {b}"},
    "x_pages":          {"de": "{n} Seiten", "en": "{n} pages"},
    "error":            {"de": "Fehler:", "en": "Error:"},
    "keywords_comma":   {"de": "Schlüsselwörter (Komma)", "en": "Keywords (comma-separated)"},
    "folder_btn":       {"de": "📁 Ordner...", "en": "📁 Folder..."},
    "data_folder":      {"de": "Daten-Ordner", "en": "Data Folder"},
    "scan_preview_lbl": {"de": "Scan-Vorschau", "en": "Scan Preview"},
    # ── Kontextmenü ──
    "ctx_cut":          {"de": "✂️  Ausschneiden", "en": "✂️  Cut"},
    "ctx_copy":         {"de": "📋  Kopieren", "en": "📋  Copy"},
    "ctx_paste":        {"de": "📃  Einfügen", "en": "📃  Paste"},
    "ctx_ocr_lang":     {"de": "⚙️  OCR-Sprache:", "en": "⚙️  OCR Language:"},
    "ctx_ocr":          {"de": "🔤  OCR / Texterkennung", "en": "🔤  OCR / Text Recognition"},
    "ctx_fav_remove":   {"de": "☆  Fav. entfernen", "en": "☆  Remove Favorite"},
    "ctx_fav_add":      {"de": "★  Als Favorit", "en": "★  Add to Favorites"},
    "ctx_category":     {"de": "🏷️  Kategorie", "en": "🏷️  Category"},
    "ctx_tags":         {"de": "🏷️  Tags", "en": "🏷️  Tags"},
    "ctx_tags_edit":    {"de": "🏷️  Tags bearbeiten...", "en": "🏷️  Edit Tags..."},
    "ctx_delete":       {"de": "🗑️  Löschen", "en": "🗑️  Delete"},
    "ctx_ocr_settings": {"de": "OCR-Einstellungen", "en": "OCR Settings"},
    "ctx_clear_fmt":    {"de": "🧹  Formatierung löschen", "en": "🧹  Clear Formatting"},
    "ctx_ins_link":     {"de": "🔗  Link einfügen...", "en": "🔗  Insert Link..."},
    "ctx_ins_img":      {"de": "🖼️  Bild einfügen...", "en": "🖼️  Insert Image..."},
    "ctx_print":        {"de": "🖨️  Drucken", "en": "🖨️  Print"},
    "ctx_rotate180":    {"de": "🔄  180° drehen & speichern", "en": "🔄  Rotate 180° & save"},
    "ctx_clear_history": {"de": "🗑️ Historie löschen", "en": "🗑️ Clear History"},
    "import_n_files":   {"de": "📎  {n} Dateien werden importiert...", "en": "📎  Importing {n} files..."},
    "log_link":         {"de": "Verknüpfen", "en": "Link"},
    "log_copy":         {"de": "Kopieren", "en": "Copy"},
    "log_auto":         {"de": "Automatisch", "en": "Automatic"},
}

def _t(key):
    """Gibt die Übersetzung für den aktuellen Sprachmodus zurück."""
    entry = _TR.get(key)
    if not entry: return key
    return entry.get(_LANG, entry.get("de", key))

def _detect_language():
    """Erkennt die Windows-Sprache. Nicht-deutsch → Englisch."""
    try:
        if platform.system() == "Windows":
            import ctypes
            lid = ctypes.windll.kernel32.GetUserDefaultUILanguage()
            # Deutsch: 0x0407 (DE), 0x0807 (AT), 0x0C07 (CH)
            if (lid & 0xFF) == 0x07: return "de"
            return "en"
        else:
            import locale
            lang = locale.getdefaultlocale()[0] or ""
            return "de" if lang.startswith("de") else "en"
    except Exception:
        return "de"

def _set_language(lang):
    """Setzt die aktive Sprache."""
    global _LANG
    _LANG = lang if lang in ("de", "en") else "de"

def _check_license(key):
    """Prüft ob die Lizenznummer gültig ist.
    Format: TIMESTAMP-HASH16
    HASH16 = SHA256(TIMESTAMP + "|" + LIC_SALT)[:16] uppercase
    Gültig wenn: Hash stimmt UND aktuelle Zeit < Timestamp.
    """
    if not key or not key.strip():
        return False
    key = key.strip()
    if "-" not in key:
        return False
    parts = key.split("-", 1)
    if len(parts) != 2:
        return False
    ts_str, provided_hash = parts
    try:
        ts = int(ts_str)
    except ValueError:
        return False
    # Hash verifizieren
    import hashlib as _hl
    expected = _hl.sha256((ts_str + "|" + LIC_SALT).encode()).hexdigest().upper()[:16]
    if provided_hash.upper() != expected:
        return False
    # Ablaufdatum prüfen
    import time as _tm
    return _tm.time() < ts

def _get_license_expiry(key):
    """Gibt das Ablaufdatum als datetime zurück, oder None."""
    if not key or "-" not in key:
        return None
    try:
        ts = int(key.strip().split("-", 1)[0])
        return datetime.fromtimestamp(ts)
    except Exception:
        return None

def _is_licensed():
    """Prüft ob eine gültige Lizenz gespeichert ist."""
    lc = load_local()
    return _check_license(lc.get("license_key", ""))

import os,sys,json,sqlite3,hashlib,shutil,subprocess,re,platform
import threading,logging,io,base64,uuid,zipfile,configparser
from pathlib import Path
from datetime import datetime
from contextlib import contextmanager
# Konsolen-Fenster bei subprocess-Aufrufen ausblenden (Windows)
_NOCONSOLE = 0x08000000 if platform.system()=="Windows" else 0

def _decode_output(data):
    """Dekodiert Bytes mit Fallback-Kette: UTF-8 → cp1252 → latin-1."""
    if data is None: return ""
    if isinstance(data, str): return data
    for enc in ("utf-8", "cp1252", "latin-1"):
        try: return data.decode(enc)
        except (UnicodeDecodeError, AttributeError): continue
    return data.decode("utf-8", errors="replace")

def _run_subprocess(cmd, timeout=300, env=None):
    """Führt subprocess aus mit korrekter Umlaut-Behandlung."""
    result = subprocess.run(cmd, capture_output=True, timeout=timeout,
                            env=env, creationflags=_NOCONSOLE)
    return type('R', (), {
        'returncode': result.returncode,
        'stdout': _decode_output(result.stdout),
        'stderr': _decode_output(result.stderr)
    })()

def check_deps():
    m=[]
    try: import customtkinter
    except ImportError: m.append("customtkinter")
    try: from PIL import Image
    except ImportError: m.append("Pillow")
    try: import pdfplumber
    except ImportError: m.append("pdfplumber")
    if m:
        print(f"\nDocVault v{VERSION} – Fehlend: {', '.join(m)}")
        print(f"  python -m pip install {' '.join(m)}"); input("\nEnter..."); sys.exit(1)
check_deps()

import customtkinter as ctk
from PIL import Image,ImageTk,ImageGrab
import pdfplumber
from tkinter import filedialog,messagebox,colorchooser
import tkinter as tk

# PyMuPDF für PDF-Text-Extraktion
HAS_FITZ=False
try:
    import fitz  # PyMuPDF (alter Modulname)
    HAS_FITZ=True
except ImportError:
    try:
        import pymupdf as fitz  # PyMuPDF 1.24+ (neuer Modulname)
        HAS_FITZ=True
    except ImportError: pass

def _pix_to_pil(pix):
    """Konvertiert fitz.Pixmap zu PIL.Image – kompatibel mit PyMuPDF 1.18 bis 1.27+.
    Löst das Problem dass pix.samples ab PyMuPDF 1.23 ein memoryview zurückgibt
    und manche Pixmaps RGBA statt RGB haben (Alpha-Kanal)."""
    try:
        # Methode 1: tobytes("png") → universell sicher (PyMuPDF 1.19+)
        png_data = pix.tobytes("png")
        return Image.open(io.BytesIO(png_data)).convert("RGB")
    except Exception:
        pass
    try:
        # Methode 2: samples mit korrektem Modus
        mode = "RGBA" if pix.alpha else "RGB"
        img = Image.frombytes(mode, [pix.width, pix.height], bytes(pix.samples))
        return img.convert("RGB")
    except Exception:
        pass
    # Methode 3: Fallback über temporäre Datei
    try:
        import tempfile
        tmp = tempfile.mktemp(suffix=".png")
        pix.save(tmp)
        img = Image.open(tmp).convert("RGB")
        try: os.remove(tmp)
        except: pass
        return img
    except Exception:
        return None

# Bei PyInstaller-EXE zeigt __file__ auf einen Temp-Ordner (_MEIxxxxx).
# sys.executable zeigt auf die tatsächliche EXE-Datei.
if getattr(sys, 'frozen', False):
    # Ausgeführt als PyInstaller-EXE
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    # Ausgeführt als Python-Skript
    BASE_DIR = Path(__file__).resolve().parent
# ─── Konfigurierbarer Datenpfad ─────────────────────────────────
# Datei 'docvault_pfad.ini' neben dem Programm bestimmt wo die Daten liegen.
# So können mehrere PCs das gleiche Programm nutzen mit zentralen Daten.
_path_cfg_file = BASE_DIR / "docvault_pfad.ini"

# ═══ App-Icon (eingebettet als Base64 – keine externe Datei nötig) ═══
_ICON_B64_32 = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABSUlEQVR4nN2XP27CMBTGP1vsuQFLl8AFwtC9lXqAjpXgFEyBiVMEqWMPUCnsHcoFQpYuvkFOEAbkynWeE3CejdRvSfwn7/vl+dlRgDtLUJ1Pm/Y7lOFhIxZmW8Y0p+LLvsEYEJLqjAkh+szLHOlQoGONOv/wB+nUgI+2r3cGGAPBBuALwQrgA8EOcCvEZKxZljp3Ss0K8P7589U3/vby8HhtLC8AX4MhSQBQClmI4ENSCpk0G7HNAWsJlEI2neJIPcBZA+bLdmrABcFVA3amBQDMlm1LTa4KNCO8En0zX7knjT4HXMbPW6x1R1Vg5wIJcg6Y5rpd5hcIW9xLkNjmpsocOzsLQb4Ft+jfATSutabSHwLg14xqV0V3brRzwDQ3M9ELwC0KQgLAaS/IXzRuaVN9Pe3FX+NYmdDmgFWEsTJh+nR2QWgIO/4ZDRl6vp/GFJ4AAAAASUVORK5CYII="
_ICON_B64_48 = "iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAABu0lEQVR4nO2ZP07DMBTGP0fsvUEXlsIFwsDeShyAEQlO0SnJ1FO0EiMHQCo7Q3uBNguLb9AThMnBpLH9apI8O+JbKvlfvp/f87OlApFLuAbM82o3hBGbPnJxZ+ozAoRgvKk2kDOAEI03pYMkekcM5oHfPhPbwBhUA8Sy+0rK7xV1wjbDzOdD+xJl9uYzk6YE6H/3i8d+1p3n1W6wM9AXxKCHuA+IwatQ1xAsZbRLCLZ7oCsI1ousCwjyPeCrdOa8P8q/rB/9U8I7Aq/vX5+XjH96uL73/ZZN3gB9GbpU0adQAgBSIuU24iMpkY4jAkB8UVB+x1WFpEQ6nWLPaYgiPVvOIqA6qSBDqi3NjSkUEojtfAoAuHmuKtcihzVOXZrSNGk23L7QJ/f+mHNosiiwbDYe1lhRITirUKt5AFgUWFIhuFLIaF7XNnNDcNzEJPNAHQmrxvOUiFX/ANziADhtM6woA0OtQgABggrJmUJGCL3dVUaDfgvp5k2pRAbgkgsiAYDjRjj/L+aSbrqZTseNEFGUURtEDRByFIAfCPWr/EYRASXjGVAKPQpKuk+j4RArU9sGO3c8BBBbZnwDzsuZyD/BG/oAAAAASUVORK5CYII="

_app_icon_cache = {}  # Cache für PhotoImage-Objekte

def _get_icon_image(size=32):
    """Gibt ein PIL.Image des App-Icons zurück."""
    if size in _app_icon_cache:
        return _app_icon_cache[size]
    import base64, io
    b64 = _ICON_B64_48 if size > 32 else _ICON_B64_32
    data = base64.b64decode(b64)
    img = Image.open(io.BytesIO(data)).convert("RGBA")
    if img.size[0] != size:
        img = img.resize((size, size), Image.LANCZOS)
    _app_icon_cache[size] = img
    return img

def _set_window_icon(window):
    """Setzt das DocVault-Icon auf ein Fenster."""
    try:
        from PIL import ImageTk
        img = _get_icon_image(32)
        tk_icon = ImageTk.PhotoImage(img)
        window._dv_icon_ref = tk_icon  # Referenz halten
        window.iconphoto(False, tk_icon)
    except Exception: pass

def _generate_ico_file():
    """Generiert eine .ico-Datei aus den eingebetteten Icons (für PyInstaller)."""
    ico_path = BASE_DIR / "DocVault-Icon.ico"
    if ico_path.exists(): return str(ico_path)
    try:
        img = _get_icon_image(48)
        img.save(str(ico_path), format="ICO", sizes=[(32,32),(48,48)])
        return str(ico_path)
    except Exception: return None
def _read_data_path():
    if _path_cfg_file.exists():
        try:
            cfg=configparser.ConfigParser()
            cfg.read(str(_path_cfg_file),encoding="utf-8")
            p=cfg.get("pfade","daten_ordner",fallback="").strip()
            if p and Path(p).exists(): return Path(p)
        except Exception: pass
    # Standard: DocVault_Daten neben dem Programm
    # Aber: Falls das Programm bereits IN einem DocVault_Daten-Ordner liegt, nicht nochmal nesten
    default = BASE_DIR / "DocVault_Daten"
    if BASE_DIR.name == "DocVault_Daten":
        default = BASE_DIR  # Schon im richtigen Ordner
    return default

def _write_data_path(path):
    try:
        cfg=configparser.ConfigParser()
        if not cfg.has_section("pfade"): cfg.add_section("pfade")
        cfg.set("pfade","daten_ordner",str(path))
        with open(str(_path_cfg_file),"w",encoding="utf-8") as f: cfg.write(f)
    except PermissionError:
        # Fallback: INI in DATA_DIR speichern
        try:
            alt = Path(path) / "docvault_pfad.ini"
            with open(str(alt),"w",encoding="utf-8") as f: cfg.write(f)
        except Exception: pass

DATA_DIR=_read_data_path()
DOCS_DIR=DATA_DIR/"documents"
THUMB_DIR=DATA_DIR/"thumbnails"; NOTE_IMG_DIR=DATA_DIR/"note_images"
DB_PATH=DATA_DIR/"docvault.db"; INI_PATH=DATA_DIR/"docvault.ini"
try:
    for d in [DATA_DIR,DOCS_DIR,THUMB_DIR,NOTE_IMG_DIR]: d.mkdir(parents=True,exist_ok=True)
except PermissionError:
    # ═══ Schreibgeschütztes Verzeichnis (z.B. C:\Program Files\) ═══
    _fallback = Path(os.path.expandvars(r"%LOCALAPPDATA%")) / "DocVault" / "DocVault_Daten"
    _msg_de = (
        f"DocVault kann den Datenordner nicht erstellen:\n\n"
        f"   {DATA_DIR}\n\n"
        f"Das Verzeichnis ist schreibgeschützt (z.B. C:\\Program Files\\).\n\n"
        f"LÖSUNGEN:\n\n"
        f"1. DocVault in ein beschreibbares Verzeichnis verschieben,\n"
        f"   z.B. C:\\DocVault\\ oder D:\\DocVault\\\n\n"
        f"2. Oder: Erstellen Sie die Datei 'docvault_pfad.ini'\n"
        f"   neben der DocVault.exe mit folgendem Inhalt:\n\n"
        f"   [pfade]\n"
        f"   daten_ordner = {_fallback}\n\n"
        f"DocVault versucht nun den Fallback-Ordner zu verwenden:\n"
        f"   {_fallback}"
    )
    _msg_en = (
        f"DocVault cannot create the data folder:\n\n"
        f"   {DATA_DIR}\n\n"
        f"The directory is read-only (e.g. C:\\Program Files\\).\n\n"
        f"SOLUTIONS:\n\n"
        f"1. Move DocVault to a writable directory,\n"
        f"   e.g. C:\\DocVault\\ or D:\\DocVault\\\n\n"
        f"2. Or: Create the file 'docvault_pfad.ini'\n"
        f"   next to DocVault.exe with the following content:\n\n"
        f"   [pfade]\n"
        f"   daten_ordner = {_fallback}\n\n"
        f"DocVault will now try to use the fallback folder:\n"
        f"   {_fallback}"
    )
    try:
        import tkinter as _tk
        from tkinter import messagebox as _mb
        _root = _tk.Tk(); _root.withdraw()
        _msg = _msg_de if _detect_language() == "de" else _msg_en
        _mb.showwarning("DocVault – Schreibgeschütztes Verzeichnis", _msg)
        _root.destroy()
    except Exception:
        print(f"\n[FEHLER] {_msg_de}\n")
    # Fallback: %LOCALAPPDATA%\DocVault\DocVault_Daten
    try:
        DATA_DIR = _fallback
        DOCS_DIR = DATA_DIR / "documents"
        THUMB_DIR = DATA_DIR / "thumbnails"; NOTE_IMG_DIR = DATA_DIR / "note_images"
        DB_PATH = DATA_DIR / "docvault.db"; INI_PATH = DATA_DIR / "docvault.ini"
        for d in [DATA_DIR, DOCS_DIR, THUMB_DIR, NOTE_IMG_DIR]: d.mkdir(parents=True, exist_ok=True)
        print(f"[DocVault] Fallback-Datenordner: {DATA_DIR}")
    except Exception as e2:
        print(f"[FATAL] Auch Fallback-Ordner nicht erstellbar: {e2}")
        try:
            import tkinter as _tk2
            from tkinter import messagebox as _mb2
            _r2 = _tk2.Tk(); _r2.withdraw()
            _mb2.showerror("DocVault", f"Fatal: Cannot create data folder.\n\n{e2}\n\nDocVault will exit.")
            _r2.destroy()
        except Exception: pass
        sys.exit(1)

# ═══════ LOKALE EINSTELLUNGEN (pro PC, neben EXE/Skript) ═══════
# Getrennt von gemeinsamen Settings (DATA_DIR) für Multi-PC-Betrieb.
# Lokal: NAPS2-Pfad, Scanner, Darstellung, Fenster-Positionen
# Gemeinsam: OCR-Sprache, Import-Modus, Kategorien
# Falls BASE_DIR schreibgeschützt ist (z.B. Program Files): Fallback auf DATA_DIR
LOCAL_SETTINGS_PATH = BASE_DIR / "docvault_local.json"
try:
    # Schreibtest: Kann die Datei dort geschrieben werden?
    _test_path = BASE_DIR / ".docvault_write_test"
    _test_path.write_text("test"); _test_path.unlink()
except (PermissionError, OSError):
    LOCAL_SETTINGS_PATH = DATA_DIR / "docvault_local.json"

def _resolve_conflicted_settings():
    """Findet und löst Dropbox-Konflikte für docvault_local.json."""
    # Alle Konflikt-Kopien sammeln (auch wenn Hauptdatei existiert)
    candidates = list(BASE_DIR.glob("docvault_local*conflicted*.json"))
    if not candidates:
        if LOCAL_SETTINGS_PATH.exists(): return
        # Keine Konflikte, aber auch keine Hauptdatei → andere json suchen
        candidates = [c for c in BASE_DIR.glob("docvault_local*.json")
                      if c.exists() and c.name != "docvault_local.json"]
        if not candidates: return
    # Falls Hauptdatei fehlt: neueste Konfliktkopie wiederherstellen
    if not LOCAL_SETTINGS_PATH.exists():
        candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
        best = candidates[0]
        try:
            import shutil
            shutil.copy2(str(best), str(LOCAL_SETTINGS_PATH))
            print(f"[DocVault] Konfliktkopie wiederhergestellt: {best.name}")
        except Exception as e:
            print(f"[DocVault] Konfliktkopie Fehler: {e}")
    # Alle Konflikt-Kopien löschen (aufräumen)
    for cf in BASE_DIR.glob("docvault_local*conflicted*.json"):
        try:
            cf.unlink()
            print(f"[DocVault] Konfliktkopie gelöscht: {cf.name}")
        except Exception: pass

def load_local():
    """Lädt PC-lokale Einstellungen."""
    _resolve_conflicted_settings()
    try:
        if LOCAL_SETTINGS_PATH.exists():
            return json.loads(LOCAL_SETTINGS_PATH.read_text(encoding="utf-8"))
    except Exception: pass
    return {}

def save_local(data):
    """Speichert PC-lokale Einstellungen."""
    try: LOCAL_SETTINGS_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except Exception as e: logger.warning("Lokale Einstellungen: %s", e)

_local = load_local()

try:
    logging.basicConfig(level=logging.INFO,format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(),logging.FileHandler(DATA_DIR/"docvault.log",encoding="utf-8")])
except PermissionError:
    logging.basicConfig(level=logging.INFO,format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()])
logger=logging.getLogger("DocVault")

# ═══════ PLUGIN-SYSTEM ═══════
PLUGINS_DIR = BASE_DIR / "plugins"
_loaded_plugins = []  # Liste von {"info":{...}, "module":mod, "enabled":bool}

def _load_plugins():
    """Lädt alle Plugins aus dem plugins/-Ordner."""
    global _loaded_plugins
    _loaded_plugins = []
    if not PLUGINS_DIR.exists():
        try: PLUGINS_DIR.mkdir(parents=True, exist_ok=True)
        except Exception: pass
        return
    enabled_plugins = set(_local.get("enabled_plugins", []))
    # Sicherstellen dass Plugin-Imports Zugriff auf gebündelte Pakete haben
    plugins_str = str(PLUGINS_DIR)
    if plugins_str not in sys.path:
        sys.path.insert(0, plugins_str)
    # Alle .py-Dateien im plugins/-Ordner laden
    for pf in sorted(PLUGINS_DIR.glob("*.py")):
        if pf.name.startswith("_"): continue
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location(pf.stem, str(pf))
            if spec is None:
                logger.warning("Plugin %s: spec ist None", pf.name)
                continue
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            info = getattr(mod, "PLUGIN_INFO", None)
            if not info or "name" not in info: continue
            is_enabled = pf.stem in enabled_plugins if enabled_plugins else True
            _loaded_plugins.append({"info": info, "module": mod, "enabled": is_enabled, "file": pf.stem})
            logger.info("Plugin geladen: %s v%s (%s) [%s]",
                info.get("name"), info.get("version","?"),
                ", ".join(info.get("extensions",[])),
                "aktiv" if is_enabled else "inaktiv")
        except Exception as e:
            logger.warning("Plugin %s: %s", pf.name, e)

def get_plugins(): return _loaded_plugins

def plugin_render_preview(filepath, max_width=330):
    """Versucht eine Vorschau über ein Plugin zu rendern. Gibt dict oder None zurück."""
    ext = Path(filepath).suffix.lower()
    for p in _loaded_plugins:
        if not p["enabled"]: continue
        info = p["info"]
        mod = p["module"]
        # Prüfe ob Plugin zuständig: statische Extension-Liste ODER Prefix-Match
        in_list = ext in info.get("extensions", [])
        if not in_list:
            # Prefix-Match (z.B. ".ad_" für alle Alibre-Dateien)
            prefixes = info.get("extension_prefixes", [])
            in_list = any(ext.startswith(pf) for pf in prefixes)
        if not in_list: continue
        try:
            # can_preview darf ablehnen (z.B. zu grosse Datei), aber nicht allein matchen
            if hasattr(mod, "can_preview") and not mod.can_preview(filepath): continue
            if hasattr(mod, "render_preview"):
                result = mod.render_preview(filepath, max_width)
                if result:
                    result["plugin_name"] = info.get("name","Plugin")
                    return result
        except Exception as e:
            logger.warning("Plugin %s preview: %s", info.get("name"), e)
            return {"type": "error", "message": f"Plugin-Fehler: {e}"}
    return None

def plugin_extract_text(filepath):
    """Extrahiert Text über ein Plugin für die Datenbank/Suche. Gibt (text, pages) zurück."""
    ext = Path(filepath).suffix.lower()
    for p in _loaded_plugins:
        if not p["enabled"]: continue
        info = p["info"]
        mod = p["module"]
        # Prüfe ob Plugin zuständig: statische Extension-Liste ODER Prefix-Match
        in_list = ext in info.get("extensions", [])
        if not in_list:
            prefixes = info.get("extension_prefixes", [])
            in_list = any(ext.startswith(pf) for pf in prefixes)
        if not in_list: continue
        try:
            # Methode 1: Dedizierte extract_text Funktion
            if hasattr(mod, "extract_text"):
                result = mod.extract_text(filepath)
                if result and isinstance(result, tuple) and len(result) == 2:
                    text, pages = result
                    if text and len(text.strip()) > 0:
                        max_c = _get_index_settings()["max_ocr_chars"]
                        logger.info("Plugin '%s': %d Zeichen extrahiert", info.get("name"), len(text))
                        return text[:max_c], pages
            # Methode 2: Fallback auf render_preview (content-Feld nutzen)
            if hasattr(mod, "render_preview"):
                result = mod.render_preview(filepath, 9999)
                if result and result.get("type") in ("text", "html_text"):
                    content = result.get("content", "")
                    pages = result.get("pages", 1)
                    if content and len(content.strip()) > 0:
                        max_c = _get_index_settings()["max_ocr_chars"]
                        logger.info("Plugin '%s' (via preview): %d Zeichen", info.get("name"), len(content))
                        return content[:max_c], pages
        except Exception as e:
            logger.warning("Plugin %s extract_text: %s", info.get("name"), e)
    return None, 0

_load_plugins()

ALLOWED_EXT={".pdf",".png",".jpg",".jpeg",".tiff",".tif",".bmp",".gif",".webp"}
# Zusätzlich erlaubte Dateitypen (alle ausser System/Cache)
EXCLUDED_EXT={".tmp",".bak",".log",".lock",".lnk",".url",".ini",".sys",".dll",
              ".exe",".msi",".bat",".cmd",".com",".scr",".pif",".vbs",".js",
              ".db",".sqlite",".db-journal",".db-wal",".db-shm",
              ".thumbs.db",".ds_store",".spotlight-v100",".trashes",
              ".swp",".swo",".pyc",".pyo",".class",".o",".obj",".cache"}
EXCLUDED_PREFIXES=("~$","._",".~","~","thumbs","desktop.ini","__pycache__")

def _is_system_file(filepath):
    """Prüft ob eine Datei eine System-/Cache-/Hidden-Datei ist."""
    p=Path(filepath)
    name=p.name.lower()
    # Versteckte Dateien (beginnen mit .)
    if name.startswith(".") and name not in (".pdf",): return True
    # Bekannte Systemnamen
    for prefix in EXCLUDED_PREFIXES:
        if name.lower().startswith(prefix.lower()): return True
    # Bekannte Systemdateien
    if name in ("thumbs.db","desktop.ini",".ds_store","ntuser.dat","pagefile.sys",
                "hiberfil.sys","swapfile.sys","icon\r","iconr"): return True
    # Ausgeschlossene Erweiterungen
    if p.suffix.lower() in EXCLUDED_EXT: return True
    # Dateien ohne Erweiterung (oft System)
    if not p.suffix and p.stat().st_size == 0: return True
    return False

DEFAULT_CATS=[
    ("Rechnung","🧾","rechnung,invoice,rechnungsnummer,rechnungsdatum,zahlbar,fällig,netto,brutto,mwst,mehrwertsteuer,iban"),
    ("Vertrag","📝","vertrag,contract,vereinbarung,vertragspartner,laufzeit,kündigung,unterschrift"),
    ("Brief","✉️","sehr geehrte,mit freundlichen grüßen,betreff,absender,empfänger,dear,sincerely"),
    ("Steuer","🏛️","steuererklärung,finanzamt,steuernummer,steuer-id,einkommensteuer,lohnsteuer"),
    ("Versicherung","🛡️","versicherung,police,versicherungsnummer,deckung,prämie"),
    ("Bewerbung","👤","bewerbung,lebenslauf,curriculum vitae,berufserfahrung"),
    ("Medizin","🏥","diagnose,patient,arzt,rezept,befund,therapie,medikament"),
    ("Kontoauszug","🏦","kontoauszug,saldo,kontobewegung,buchungstag,wertstellung"),
    ("Quittung","🧾","quittung,kassenbon,receipt,bar bezahlt"),
    ("Notiz","📝",""),("Dokument","📄",""),
]

# ═══════ INI-Einstellungen ═══════
def load_ini():
    cfg=configparser.ConfigParser()
    if INI_PATH.exists():
        try: cfg.read(str(INI_PATH),encoding="utf-8")
        except Exception: pass
    return cfg

def save_ini(cfg):
    try:
        with open(str(INI_PATH),"w",encoding="utf-8") as f: cfg.write(f)
    except Exception: pass

def save_geometry(cfg,section,widget):
    if not cfg.has_section(section): cfg.add_section(section)
    cfg.set(section,"geometry",widget.geometry())
    save_ini(cfg)

def center_window(widget,width,height):
    """Zentriert ein Fenster auf dem Bildschirm."""
    widget.update_idletasks()
    sw=widget.winfo_screenwidth(); sh=widget.winfo_screenheight()
    x=(sw-width)//2; y=(sh-height)//2
    widget.geometry(f"{width}x{height}+{x}+{y}")

def restore_geometry(cfg,section,widget,default):
    if cfg.has_section(section):
        g=cfg.get(section,"geometry",fallback=default)
        try: widget.geometry(g)
        except Exception: widget.geometry(default)
    else:
        # Erster Start: zentrieren
        try:
            w,h=[int(x) for x in default.split("x")[:2]]
            center_window(widget,w,h)
        except Exception: widget.geometry(default)

# ═══════ DATENBANK ═══════
@contextmanager
def get_db():
    conn=sqlite3.connect(str(DB_PATH),timeout=60); conn.row_factory=sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL"); conn.execute("PRAGMA busy_timeout=30000")
    try: yield conn; conn.commit()
    except Exception: conn.rollback(); raise
    finally: conn.close()

def init_db():
    with get_db() as c:
        c.executescript("""
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL, original_name TEXT NOT NULL,
                file_path TEXT NOT NULL, file_size INTEGER DEFAULT 0,
                file_hash TEXT UNIQUE, mime_type TEXT,
                page_count INTEGER DEFAULT 0, ocr_text TEXT DEFAULT '',
                category TEXT DEFAULT 'Dokument', tags TEXT DEFAULT '[]',
                notes TEXT DEFAULT '', note_data TEXT DEFAULT '',
                confidence REAL DEFAULT 0.0, source TEXT DEFAULT 'import',
                thumbnail TEXT DEFAULT '',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                processed INTEGER DEFAULT 0, starred INTEGER DEFAULT 0,
                archived INTEGER DEFAULT 0);
            CREATE TABLE IF NOT EXISTS search_index (
                doc_id INTEGER PRIMARY KEY, terms TEXT,
                FOREIGN KEY (doc_id) REFERENCES documents(id) ON DELETE CASCADE);
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL, icon TEXT DEFAULT '📄',
                keywords TEXT DEFAULT '', sort_order INTEGER DEFAULT 100,
                parent_id INTEGER DEFAULT NULL);
            CREATE INDEX IF NOT EXISTS idx_cat ON documents(category);
            CREATE INDEX IF NOT EXISTS idx_star ON documents(starred);""")
        for col,df in [("thumbnail","''"),("note_data","''")]:
            try: c.execute(f"ALTER TABLE documents ADD COLUMN {col} TEXT DEFAULT {df}")
            except Exception: pass
        # Subcategory-Spalte nachrüsten
        try: c.execute("ALTER TABLE categories ADD COLUMN parent_id INTEGER DEFAULT NULL")
        except Exception: pass
        existing={r["name"] for r in c.execute("SELECT name FROM categories").fetchall()}
        for i,(n,ic,kw) in enumerate(DEFAULT_CATS):
            if n not in existing:
                c.execute("INSERT INTO categories (name,icon,keywords,sort_order) VALUES (?,?,?,?)",(n,ic,kw,i*10))

def get_categories(parent_id=None):
    """Gibt Kategorien zurück. parent_id=None für Hauptkategorien, id für Unterkategorien."""
    with get_db() as c:
        if parent_id is None:
            return [dict(r) for r in c.execute(
                "SELECT * FROM categories WHERE parent_id IS NULL ORDER BY sort_order,name").fetchall()]
        return [dict(r) for r in c.execute(
            "SELECT * FROM categories WHERE parent_id=? ORDER BY sort_order,name",(parent_id,)).fetchall()]
def get_all_categories():
    """Gibt ALLE Kategorien flach zurück."""
    with get_db() as c:
        return [dict(r) for r in c.execute("SELECT * FROM categories ORDER BY sort_order,name").fetchall()]
def get_cat_names():
    """Gibt alle Kategorienamen für Dropdowns zurück (flach, ohne Prefix)."""
    return [c["name"] for c in get_all_categories()]
def get_cat_names_hierarchical():
    """Gibt Kategorienamen mit Einrückung für Anzeige zurück."""
    cats=get_all_categories(); result=[]
    mains=[c for c in cats if not c.get("parent_id")]
    for m in mains:
        result.append(m["name"])
        subs=[c for c in cats if c.get("parent_id")==m["id"]]
        for s in subs: result.append(f"  ↳ {s['name']}")
    return result
def get_cat_dict():
    return {c["name"]:c for c in get_all_categories()}

def _ensure_category(name):
    """Stellt sicher dass eine Kategorie existiert. Erstellt sie falls nötig."""
    existing = get_cat_names()
    if name in existing:
        return name
    try:
        with get_db() as c:
            max_order = c.execute("SELECT MAX(sort_order) FROM categories").fetchone()[0] or 0
            c.execute("INSERT INTO categories (name, icon, keywords, sort_order) VALUES (?,?,?,?)",
                      (name, "📂", name.lower(), max_order + 10))
        logger.info("Neue KI-Kategorie erstellt: %s", name)
    except Exception as e:
        logger.warning("Kategorie '%s' erstellen fehlgeschlagen: %s", name, e)
        return "Dokument"
    return name

# ═══════ SUCHE ═══════
STOP={"der","die","das","den","dem","des","ein","eine","einer","eines","einem","einen",
      "und","oder","aber","doch","nicht","kein","keine","keinem","keinen","keiner",
      "mit","von","für","auf","ist","sind","war","hat","haben","wird","werden","wurde","wurden",
      "sich","ich","wir","sie","ihr","ihm","ihn","ihnen","er","es","mich","mir","uns",
      "auch","nach","bei","aus","wie","noch","nur","über","zum","zur","bis","vor","durch","unter",
      "wenn","weil","dass","dann","denn","doch","schon","sehr","mehr","viel","alle","allem",
      "allen","aller","alles","andere","anderen","anderer","anderes","bereits","dabei","dadurch",
      "dafür","dagegen","daher","dahin","damals","damit","danach","daneben","daran","darauf",
      "daraus","darf","darfst","darin","darum","darunter","darüber","davon","davor","dazu",
      "dein","deine","deinem","deinen","deiner","deren","derer","dessen","diese","diesem",
      "diesen","dieser","dieses","dort","drin","dritte","dritten","dritter","drittes",
      "du","dürfen","eben","ebenso","ehe","eher","eigenen","eigentlich","einige","einigen",
      "einiger","einiges","einmal","erst","etwa","etwas","euch","euer","eure","eurem",
      "euren","eurer","falls","fast","ganz","gar","gegen","gehen","geht","ging",
      "gewesen","gibt","ging","gleich","groß","große","großen","großer","großes",
      "hatte","hätte","hin","hinter","hoch","immer","indem","innen","ins","irgend",
      "jede","jedem","jeden","jeder","jedes","jedoch","jemals","jene","jenem","jenen",
      "jener","jenes","jetzt","kann","kannst","konnte","kurz","lang","lange","längst",
      "lässt","laut","lediglich","legen","legt","leid","lesen","liest","liegt","lässt",
      "machen","macht","manche","manchem","manchen","mancher","manchmal","mehr","mein",
      "meine","meinem","meinen","meiner","meist","meisten","mich","mindestens","mir",
      "möchte","mögen","möglich","muss","müssen","nach","nachdem","nachher","nächste",
      "neben","nehmen","nein","neu","neue","neuem","neuen","neuer","neues","neulich",
      "nichts","nie","niemand","nimmt","noch","nun","nur","nutzen","ober","oben",
      "obgleich","obwohl","ohne","per","pro","recht","rechts","rund","sagen","schlecht",
      "schließen","schlimm","schnell","schon","sehen","sehr","sein","seine","seinem",
      "seinen","seiner","seit","seitdem","selbst","sicher","so","sofort","sogar","solch",
      "solche","solchem","solchen","solcher","soll","sollen","sollte","sollten","solltest",
      "somit","sondern","sonst","sorgen","soviel","sowie","steht","stellen","stets",
      "trotz","trotzdem","tun","über","überhaupt","übrigens","uhr","um","ums",
      "und","uns","unser","unsere","unserem","unseren","unserer","unten","unter","viel",
      "viele","vielen","vielleicht","völlig","vom","von","vor","vorbei","vorher","vorn",
      "während","wann","warum","was","weder","weil","weit","weiter","weitere","weiterem",
      "weiteren","weiterer","weiteres","welch","welche","welchem","welchen","welcher",
      "welches","wem","wen","wenig","wenige","wenigen","weniger","wenigstens","wenn",
      "wer","werde","werden","werdet","weshalb","wessen","wie","wieder","wieso","will",
      "wir","wird","wirklich","wissen","wo","wohl","wollen","worden","worin","würde",
      "würden","ziemlich","zu","zum","zur","zurück","zusammen","zwar","zwischen",
      # Englisch
      "the","and","for","that","this","with","from","but","not","you","all","can","had",
      "her","was","one","our","out","are","has","have","been","will","would","could",
      "should","about","which","their","there","what","when","where","who","how","may",
      "also","than","then","them","these","those","into","over","such","your","some",
      "its","just","only","other","than","very","each","every","both","few","more",
      "most","much","many","any","own","same","after","before","between","here","does",
      "did","being","because","while","during","without","again","further","once","shall"}

# ═══ Index-Einstellungen (konfigurierbar) ═══
_INDEX_DEFAULTS = {"max_ocr_chars": 50000, "max_index_words": 5000, "min_word_len": 3}
def _get_index_settings():
    """Lädt Index-Einstellungen aus lokalen Settings."""
    return {
        "max_ocr_chars": _local.get("max_ocr_chars", _INDEX_DEFAULTS["max_ocr_chars"]),
        "max_index_words": _local.get("max_index_words", _INDEX_DEFAULTS["max_index_words"]),
        "min_word_len": _local.get("min_word_len", _INDEX_DEFAULTS["min_word_len"]),
    }

SYNONYMS={"arzt":["doktor","medizin","praxis","dr","ärztin"],"rechnung":["invoice","zahlung","faktura"],
    "vertrag":["vereinbarung","kontrakt"],"miete":["mietvertrag","vermieter","wohnung"],
    "steuer":["finanzamt","steuererklärung","elster"],"bank":["konto","kontoauszug","iban"],
    "gehalt":["lohn","lohnabrechnung","salär","einkommen"],"auto":["fahrzeug","kfz","pkw","wagen"],
    "haus":["wohnung","immobilie","gebäude"]}
def norm(t):
    if not t: return ""
    t=t.lower()
    for a,b in [("ß","ss"),("ä","ae"),("ö","oe"),("ü","ue")]: t=t.replace(a,b)
    return t
def tokenize(t):
    if not t: return []
    s = _get_index_settings()
    min_len = s["min_word_len"]
    return [w for w in re.sub(r'[^\w\s]',' ',t.lower()).split() if len(w)>=min_len and w not in STOP]
def tok_norm(t):
    toks=tokenize(t); res=list(toks)
    for tk in toks:
        n=norm(tk)
        if n!=tk: res.append(n)
    return list(set(res))
def expand(toks):
    exp=set(toks)
    for t in list(exp):
        n=norm(t)
        if n!=t: exp.add(n)
    for t in list(exp):
        for k,syns in SYNONYMS.items():
            if t==k or t in syns or norm(t)==norm(k): exp.add(k); exp.update(syns)
    return list(exp)
def index_document(did,text):
    s = _get_index_settings()
    max_words = s["max_index_words"]
    all_terms = list(set(tok_norm(text)))
    # Auf max_index_words begrenzen (häufigste/kürzeste bevorzugen)
    if len(all_terms) > max_words:
        # Kürzere Wörter zuerst (sind oft spezifischer: "IBAN", "CHF", "PDF")
        # dann alphabetisch für Reproduzierbarkeit
        all_terms.sort(key=lambda w: (len(w), w))
        all_terms = all_terms[:max_words]
        logger.info("Index #%d: %d → %d Wörter (begrenzt)", did, len(set(tok_norm(text))), max_words)
    terms = " ".join(all_terms)
    with get_db() as c: c.execute("INSERT OR REPLACE INTO search_index (doc_id,terms) VALUES (?,?)",(did,terms))
def search_docs(query,cat="",star=False,limit=200,exclude_cats=None,sort="date_desc"):
    toks=tokenize(query) if query else []; exp=expand(toks) if toks else []
    all_s=list(set(exp))
    for t in list(all_s):
        n=norm(t)
        if n not in all_s: all_s.append(n)
    sort_map={"date_desc":"d.created_at DESC","date_asc":"d.created_at ASC",
              "size_desc":"d.file_size DESC","size_asc":"d.file_size ASC",
              "pages_desc":"d.page_count DESC","pages_asc":"d.page_count ASC",
              "name_asc":"d.original_name ASC","name_desc":"d.original_name DESC",
              "star_desc":"d.starred DESC, d.created_at DESC",
              "updated_desc":"d.updated_at DESC"}
    order=sort_map.get(sort,"d.created_at DESC")
    with get_db() as c:
        w,p=["d.archived=0"],[]
        if all_s:
            conditions = []
            for t in all_s:
                conditions.append("(si.terms LIKE ? OR d.ocr_text LIKE ? OR d.original_name LIKE ?)")
                p.extend([f"%{t}%", f"%{t}%", f"%{t}%"])
            w.append(f"({' OR '.join(conditions)})")
        if cat=="__uncategorized__":
            w.append("(d.category IS NULL OR d.category='' OR d.category='Dokument')")
        elif cat:
            w.append("d.category=?"); p.append(cat)
        if star: w.append("d.starred=1")
        # Kategorien ausschliessen (bei "Alle Dokumente")
        if exclude_cats:
            placeholders=",".join(["?" for _ in exclude_cats])
            w.append(f"(d.category NOT IN ({placeholders}) OR d.category IS NULL)")
            p.extend(exclude_cats)
        p.append(limit)
        return [dict(r) for r in c.execute(f"SELECT DISTINCT d.* FROM documents d LEFT JOIN search_index si ON d.id=si.doc_id WHERE {' AND '.join(w)} ORDER BY {order} LIMIT ?",p).fetchall()]

# ═══════ OCR + KATEGORISIERUNG + THUMBNAIL ═══════
def extract_text_pdf(p):
    """Text aus PDF extrahieren (PyMuPDF → pdfplumber)."""
    if HAS_FITZ:
        try:
            doc = fitz.open(str(p)); pg = len(doc)
            tx = [page.get_text() for page in doc]; doc.close()
            result = "\n\n".join(t for t in tx if t.strip())
            logger.info("PyMuPDF: %d Seiten, %d Zeichen", pg, len(result))
            if result.strip(): return result, pg
        except Exception as e: logger.warning("PyMuPDF: %s", e)
    try:
        tx=[]; pg=0
        with pdfplumber.open(p) as pdf:
            pg=len(pdf.pages)
            for pa in pdf.pages:
                t=pa.extract_text()
                if t: tx.append(t)
        result="\n\n".join(tx)
        logger.info("pdfplumber: %d Seiten, %d Zeichen", pg, len(result))
        return result,pg
    except Exception as e:
        logger.warning("pdfplumber: %s",e)
        return "",0

def naps2_ocr(filepath, lang="deu"):
    """Lässt NAPS2 OCR auf einer Datei laufen (PDF oder Bild).
    Gibt OCR-Text direkt zurück (nicht Pfad)."""
    if not NAPS2_EXE:
        logger.warning("NAPS2 nicht verfügbar für OCR")
        return "", 0
    import tempfile, time
    ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    TEMP = tempfile.gettempdir()
    ocr_pdf = os.path.join(TEMP, f"docvault_ocr_{ts}.pdf")

    # Alte Temp-Datei löschen
    if os.path.exists(ocr_pdf):
        try: os.remove(ocr_pdf)
        except: pass

    cmd = [NAPS2_EXE, "-i", str(filepath), "--enableocr", "--ocrlang", lang,
           "-o", ocr_pdf, "--force"]
    logger.info("NAPS2 OCR: %s", " ".join(cmd))
    try:
        r = _run_subprocess(cmd, timeout=300, env=NAPS2_ENV)
        if (r.stdout or "").strip(): logger.info("NAPS2 OCR stdout: %s", r.stdout.strip()[:200])
        if (r.stderr or "").strip(): logger.info("NAPS2 OCR stderr: %s", r.stderr.strip()[:200])

        # Warte auf Datei
        for _ in range(30):
            if os.path.exists(ocr_pdf) and os.path.getsize(ocr_pdf) > 0: break
            time.sleep(0.5)

        if os.path.exists(ocr_pdf) and os.path.getsize(ocr_pdf) > 0:
            # Text mit PyMuPDF extrahieren (wie beim Scan)
            text = ""
            pg = 1
            if HAS_FITZ:
                doc = fitz.open(ocr_pdf)
                text = "".join([page.get_text() for page in doc])
                pg = len(doc)
                doc.close()
            else:
                try:
                    with pdfplumber.open(ocr_pdf) as pdf:
                        pg = len(pdf.pages)
                        text = "\n\n".join(p.extract_text() or "" for p in pdf.pages)
                except: pass
            logger.info("NAPS2 OCR: %d Seiten, %d Zeichen", pg, len(text))
            # Aufräumen
            try: os.remove(ocr_pdf)
            except: pass
            return text, pg
        else:
            logger.warning("NAPS2 OCR: keine Datei erstellt")
    except Exception as e:
        logger.error("NAPS2 OCR Fehler: %s", e)
    return "", 0

def run_ocr(fp, lang="deu", status_cb=None):
    """Text aus Datei extrahieren. Pipeline: 1) Direkt lesen, 2) NAPS2 OCR."""
    ext = Path(fp).suffix.lower()
    if status_cb: status_cb(f"Analysiere {Path(fp).name}...")

    # Text-basierte Dateien direkt lesen
    if ext in (".txt",".csv",".md",".rtf",".html",".htm",".xml",".json",".log"):
        max_c = _get_index_settings()["max_ocr_chars"]
        try:
            for enc in ("utf-8","cp1252","latin-1"):
                try:
                    text=Path(fp).read_text(encoding=enc)
                    return text[:max_c], 1
                except UnicodeDecodeError: continue
        except Exception: pass
        return "", 1

    # Schritt 1: Direkt Text extrahieren (nur für PDFs mit Text-Layer)
    if ext == ".pdf":
        if status_cb: status_cb("PDF-Text extrahieren...")
        text, pg = extract_text_pdf(fp)
        if len(text.strip()) > 30:
            return text, pg

    # Schritt 2: NAPS2 OCR (nur für PDFs und Bilder)
    if NAPS2_EXE and ext in (".pdf",".png",".jpg",".jpeg",".tiff",".tif",".bmp",".gif",".webp"):
        if status_cb: status_cb(f"NAPS2 OCR ({lang})...")
        text, pg = naps2_ocr(fp, lang)
        if text.strip():
            return text, pg

    # Schritt 3: Plugin-Textextraktion (DOCX, ODT, HTML etc.)
    plugin_text, plugin_pages = plugin_extract_text(fp)
    if plugin_text and len(plugin_text.strip()) > 0:
        if status_cb: status_cb(f"Plugin: {len(plugin_text)} Zeichen extrahiert")
        return plugin_text, plugin_pages or 1

    # Schritt 4: Seitenzahl trotzdem ermitteln
    pg = 1
    if ext == ".pdf":
        try:
            if HAS_FITZ:
                doc = fitz.open(str(fp)); pg = len(doc); doc.close()
            else:
                with pdfplumber.open(fp) as pdf: pg = len(pdf.pages)
        except Exception: pass

    return "", pg

# OCR-Sprache (aus Settings)
_ocr_lang = "deu"
def get_ocr_lang():
    global _ocr_lang
    return _ocr_lang
def set_ocr_lang(lang):
    global _ocr_lang
    _ocr_lang = lang

def categorize(text):
    if not text or len(text.strip())<10: return "Dokument",0.0,[]
    tl=text.lower(); tn=norm(text)
    cats=get_categories(); scores={}; tags_map={}
    for cat in cats:
        kws_s=cat.get("keywords","")
        if not kws_s: continue
        kws=[k.strip() for k in kws_s.split(",") if k.strip()]
        hits=[kw for kw in kws if kw in tl or norm(kw) in tn]
        if hits: scores[cat["name"]]=len(hits)/len(kws); tags_map[cat["name"]]=hits
    if not scores:
        tg=[]
        if re.findall(r'\d{1,2}[./]\d{1,2}[./]\d{2,4}',tl): tg.append("datum")
        return "Dokument",0.1,tg
    best=max(scores,key=scores.get); conf=min(scores[best]*1.5,1.0)
    tg=tags_map.get(best,[])
    if re.findall(r'\d{1,2}[./]\d{1,2}[./]\d{2,4}',tl): tg.append("datum")
    if re.findall(r'\d+[.,]\d{2}\s*(?:€|eur|chf|usd)',tl): tg.append("betrag")
    if re.search(r'[a-z]{2}\d{2}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{4}',tl): tg.append("iban")
    return best,round(conf,2),list(dict.fromkeys(tg))[:12]

def _call_ai_api(prompt):
    """Ruft die konfigurierte KI-API auf. Gibt Antwort-Text zurück oder ''."""
    lc = load_local()
    provider = lc.get("ai_provider", "")
    token = lc.get("ai_token", "")
    if not provider or not token: return ""

    try:
        import urllib.request, json as _json
        if provider == "DeepSeek":
            url = "https://api.deepseek.com/chat/completions"
            model = "deepseek-chat"
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            body = {"model": model, "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 300, "temperature": 0.2}
        elif provider == "OpenAI":
            url = "https://api.openai.com/v1/chat/completions"
            model = "gpt-4o-mini"
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            body = {"model": model, "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 300, "temperature": 0.2}
        elif provider == "Anthropic":
            url = "https://api.anthropic.com/v1/messages"
            model = "claude-haiku-4-5-20251001"
            headers = {"x-api-key": token, "Content-Type": "application/json",
                       "anthropic-version": "2023-06-01"}
            body = {"model": model, "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 300}
        else:
            return ""
        data = _json.dumps(body).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = _json.loads(resp.read().decode("utf-8"))
        if provider == "Anthropic":
            return result.get("content", [{}])[0].get("text", "")
        else:
            return result.get("choices", [{}])[0].get("message", {}).get("content", "")
    except Exception as e:
        logger.warning("AI API call failed (%s): %s", provider, e)
        return ""

def _ai_analyze_document(text, categories, filename=""):
    """KI-Analyse: Dokumentname, Kategorie und Tags in einem API-Call.
    Gibt dict zurück: {"name": str, "category": str, "tags": [str]}"""
    lc = load_local()
    if not lc.get("ai_provider") or not lc.get("ai_token") or not text or len(text.strip()) < 20:
        return {}

    snippet = text[:2000]
    cat_list = ", ".join(categories) if categories else "Dokument"

    prompt = (
        f"Analysiere diesen Dokumenttext und antworte NUR mit genau 3 Zeilen:\n"
        f"Zeile 1: Ein kurzer, beschreibender Dokumentname (max. 60 Zeichen, in der Sprache des Dokuments)\n"
        f"Zeile 2: Die passendste Kategorie. Bevorzugt aus dieser Liste: {cat_list} – "
        f"aber wenn keine passt, schlage eine neue kurze Kategorie vor (1-2 Wörter)\n"
        f"Zeile 3: 5-8 Schlagwörter als komma-getrennte Liste (Sprache des Dokuments)\n\n"
        f"Kein anderer Text, keine Erklärung, keine Nummerierung.\n"
    )
    if filename:
        prompt += f"Dateiname: {filename}\n"
    prompt += f"\nDokumenttext:\n{snippet}"

    raw = _call_ai_api(prompt)
    if not raw:
        return {}

    lines = [l.strip() for l in raw.strip().split("\n") if l.strip()]
    result = {}
    if len(lines) >= 1:
        name = lines[0].strip().strip('"').strip("'")
        # Präfixe wie "1:" oder "Name:" entfernen
        for prefix in ["1:", "1.", "Name:", "Dokumentname:", "Document name:"]:
            if name.lower().startswith(prefix.lower()):
                name = name[len(prefix):].strip()
        if 3 <= len(name) <= 80:
            result["name"] = name
    if len(lines) >= 2:
        cat = lines[1].strip().strip('"').strip("'")
        for prefix in ["2:", "2.", "Kategorie:", "Category:"]:
            if cat.lower().startswith(prefix.lower()):
                cat = cat[len(prefix):].strip()
        if 1 <= len(cat) <= 40:
            result["category"] = cat
            # Neue Kategorie erstellen falls nötig
            if cat not in categories:
                result["new_category"] = True
    if len(lines) >= 3:
        tag_line = lines[2]
        for prefix in ["3:", "3.", "Tags:", "Schlagwörter:", "Keywords:"]:
            if tag_line.lower().startswith(prefix.lower()):
                tag_line = tag_line[len(prefix):].strip()
        tags = [t.strip().lower() for t in tag_line.split(",") if t.strip()]
        tags = [t for t in tags if 2 <= len(t) <= 40]
        if tags:
            result["tags"] = tags[:8]

    return result

def _generate_ai_tags(text, max_tags=8):
    """Fallback: Nur Tags generieren (für Test-Button)."""
    result = _ai_analyze_document(text, get_cat_names())
    return result.get("tags", [])
def gen_thumb(fp,did):
    tp=THUMB_DIR/f"{did}.png"
    if tp.exists(): return str(tp)
    try:
        ext=Path(fp).suffix.lower(); img=None
        if ext==".pdf" and HAS_FITZ:
            doc=fitz.open(str(fp))
            if len(doc)>0:
                page=doc[0]; pix=page.get_pixmap(dpi=72)
                img=_pix_to_pil(pix)
            doc.close()
        elif ext==".webp":
            img=Image.open(fp).convert("RGB")
        elif ext in ALLOWED_EXT: img=Image.open(fp)
        if img: img.thumbnail((80,110),Image.LANCZOS); img.save(str(tp),"PNG"); return str(tp)
    except Exception: pass
    return ""

def pdf_to_webp(pdf_path, quality=80):
    """Konvertiert ein mehrseitiges PDF in eine mehrseitige WebP-Datei.
    Gibt den Pfad der WebP-Datei zurück oder None bei Fehler."""
    if not HAS_FITZ:
        logger.warning("PDF→WebP: PyMuPDF nicht verfügbar")
        return None
    try:
        pdf = fitz.open(pdf_path)
        frames = []
        for i in range(len(pdf)):
            pix = pdf[i].get_pixmap(dpi=150)
            frames.append(_pix_to_pil(pix))
        pdf.close()
        if not frames: return None
        webp_path = str(Path(pdf_path).with_suffix(".webp"))
        if len(frames) == 1:
            frames[0].save(webp_path, "WebP", quality=quality, method=4)
        else:
            frames[0].save(webp_path, "WebP", quality=quality, method=4,
                           save_all=True, append_images=frames[1:], duration=0, loop=0)
        pdf_size = os.path.getsize(pdf_path)
        try: os.remove(pdf_path)
        except OSError: pass
        webp_size = os.path.getsize(webp_path)
        saving = (1 - webp_size/pdf_size)*100 if pdf_size else 0
        logger.info("PDF→WebP: %s (%.0fKB → %.0fKB, %.0f%% kleiner, %d Seiten)",
            Path(webp_path).name, pdf_size/1024, webp_size/1024, saving, len(frames))
        return webp_path
    except Exception as e:
        logger.error("PDF→WebP Fehler: %s", e)
        return None

def webp_page_count(filepath):
    """Zählt Seiten in einer WebP-Datei."""
    try:
        img = Image.open(filepath); n = 0
        try:
            while True: n += 1; img.seek(n)
        except EOFError: pass
        return n
    except Exception: return 1

def webp_get_page(filepath, page_idx, max_width=None):
    """Extrahiert eine Seite aus einer mehrseitigen WebP-Datei als PIL.Image."""
    try:
        img = Image.open(filepath); img.seek(page_idx)
        frame = img.copy().convert("RGB")
        if max_width and frame.width > max_width:
            s = max_width / frame.width
            frame = frame.resize((max_width, int(frame.height * s)), Image.LANCZOS)
        return frame
    except Exception: return None

# ═══════ IMPORT + VERARBEITUNG ═══════
def compute_hash(p):
    sha=hashlib.sha256()
    with open(p,"rb") as f:
        for ch in iter(lambda:f.read(8192),b""): sha.update(ch)
    return sha.hexdigest()
def import_file(src,link_only=False):
    source=Path(src)
    if not source.exists(): return None,"Nicht gefunden"
    if _is_system_file(source): return None,f"Systemdatei übersprungen"
    fh=compute_hash(source)
    with get_db() as c:
        dup=c.execute("SELECT id FROM documents WHERE file_hash=?",(fh,)).fetchone()
        if dup: return None,f"Duplikat (#{dup['id']})"
    if link_only: fp,fn,st=str(source.resolve()),source.name,"link"
    else:
        ts=datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        safe=re.sub(r'[^\w.\-]','_',source.name); fn=f"{ts}_{safe}"; dest=DOCS_DIR/fn
        shutil.copy2(source,dest); fp,st=str(dest),"import"
    mime={".pdf":"application/pdf",".png":"image/png",".jpg":"image/jpeg",".jpeg":"image/jpeg",
          ".tiff":"image/tiff",".tif":"image/tiff",".bmp":"image/bmp",".gif":"image/gif",".webp":"image/webp",
          ".doc":"application/msword",".docx":"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
          ".xls":"application/vnd.ms-excel",".xlsx":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
          ".ppt":"application/vnd.ms-powerpoint",".pptx":"application/vnd.openxmlformats-officedocument.presentationml.presentation",
          ".odt":"application/vnd.oasis.opendocument.text",".ods":"application/vnd.oasis.opendocument.spreadsheet",
          ".txt":"text/plain",".csv":"text/csv",".md":"text/markdown",".rtf":"application/rtf",
          ".html":"text/html",".htm":"text/html",".xml":"text/xml",".json":"application/json",
          ".zip":"application/zip",".rar":"application/x-rar-compressed",".7z":"application/x-7z-compressed",
          ".mp3":"audio/mpeg",".wav":"audio/wav",".mp4":"video/mp4",".avi":"video/x-msvideo",
          ".ppp":"application/x-pageplus",
          }.get(source.suffix.lower(),"application/octet-stream")
    with get_db() as c:
        cur=c.execute("INSERT INTO documents (filename,original_name,file_path,file_size,file_hash,mime_type,source) VALUES (?,?,?,?,?,?,?)",
            (fn,source.name,fp,source.stat().st_size,fh,mime,st))
        return cur.lastrowid,None
def process_document(did, callback=None, status_cb=None, lang=None, pre_ocr_text=None, force_category=None):
    try:
        with get_db() as c:
            doc=c.execute("SELECT * FROM documents WHERE id=?",(did,)).fetchone()
            if not doc: return
        ocr_lang = lang or get_ocr_lang()
        if status_cb: status_cb(f"Verarbeite #{did}: {doc['original_name']}")
        if pre_ocr_text and len(pre_ocr_text.strip()) > 10:
            text = pre_ocr_text
            pg = 1
            try:
                if HAS_FITZ:
                    d=fitz.open(str(doc["file_path"])); pg=len(d); d.close()
                else:
                    with pdfplumber.open(doc["file_path"]) as pdf: pg=len(pdf.pages)
            except Exception: pass
            logger.info("OCR #%d: %d Zeichen (vorgegeben), %d Seiten", did, len(text), pg)
        else:
            logger.info("Starte OCR #%d: %s (Sprache: %s)", did, doc['original_name'], ocr_lang)
            text,pg=run_ocr(doc["file_path"], ocr_lang, status_cb)
            logger.info("OCR #%d: %d Zeichen, %d Seiten", did, len(text), pg)
        if status_cb: status_cb(f"Kategorisiere #{did}...")
        if force_category:
            cat=force_category; conf=1.0; tags=[]
        else:
            cat,conf,tags=categorize(text)
        # KI-Analyse: Name, Kategorie und Tags (wenn API-Token gesetzt)
        ai = _ai_analyze_document(text, get_cat_names(), doc.get("original_name",""))
        if ai:
            if ai.get("tags"):
                tags = list(dict.fromkeys(tags + ai["tags"]))[:12]
            if ai.get("category") and not force_category:
                cat = _ensure_category(ai["category"]); conf = 0.95
            if ai.get("name"):
                with get_db() as c:
                    c.execute("UPDATE documents SET original_name=? WHERE id=?", (ai["name"], did))
            if status_cb:
                parts = []
                if ai.get("name"): parts.append(f"📝 {ai['name']}")
                if ai.get("category"): parts.append(f"📂 {ai['category']}")
                if ai.get("tags"): parts.append(f"🏷 {len(ai['tags'])} Tags")
                status_cb(f"🤖 KI: {', '.join(parts)}")
        if status_cb: status_cb(f"Thumbnail #{did}...")
        thumb=gen_thumb(doc["file_path"],did)
        # Text-Limit anwenden
        idx_s = _get_index_settings()
        max_chars = idx_s["max_ocr_chars"]
        stored_text = text[:max_chars] if len(text) > max_chars else text
        with get_db() as c:
            c.execute("UPDATE documents SET ocr_text=?,page_count=?,category=?,confidence=?,tags=?,thumbnail=?,processed=1,updated_at=CURRENT_TIMESTAMP WHERE id=?",
                (stored_text,pg,cat,conf,json.dumps(tags),thumb,did))
        index_document(did,f"{doc['original_name']} {cat} {' '.join(tags)} {text}")
        if status_cb: status_cb(f"✅ #{did}: {cat} ({int(conf*100)}%)")
        logger.info("Verarbeitet #%d: %s (%d%%), %d/%d Zeichen OCR, Index-Max: %d Wörter",
                     did,cat,int(conf*100),len(stored_text),len(text),idx_s["max_index_words"])
    except Exception as e:
        logger.error("Fehler #%d: %s",did,e,exc_info=True)
        if status_cb: status_cb(f"❌ #{did}: {e}")
    if callback: callback()
def delete_doc_complete(did):
    """Löscht ein Dokument komplett: DB-Eintrag, physische Datei, Thumbnail, Notiz-Bilder."""
    with get_db() as c:
        row=c.execute("SELECT * FROM documents WHERE id=?",(did,)).fetchone()
        if not row: return
        doc=dict(row)
        fp = doc.get("file_path","")
        src = doc.get("source","import")
        # Physische Datei löschen (nur wenn kopiert/gescannt, NICHT bei Verknüpfungen)
        if src != "link" and fp and os.path.isfile(fp):
            try:
                os.remove(fp)
                logger.info("Datei gelöscht: %s", fp)
            except OSError as e:
                logger.warning("Datei löschen fehlgeschlagen: %s (%s)", fp, e)
        elif src == "link":
            logger.info("Verknüpfung entfernt (Originaldatei bleibt): %s", fp)
        # Thumbnail löschen
        try: os.remove(str(THUMB_DIR/f"{did}.png"))
        except OSError: pass
        # Notiz-Bilder löschen
        nd=doc.get("note_data","")
        if nd:
            try:
                for img in json.loads(nd).get("images",[]):
                    try: os.remove(str(NOTE_IMG_DIR/img.get("file","")))
                    except OSError: pass
                    # Original-Datei auch löschen
                    iid = img.get("id","")
                    if iid:
                        try: os.remove(str(NOTE_IMG_DIR/f"{iid}_orig.png"))
                        except OSError: pass
            except Exception: pass
        # Aus Datenbank löschen
        c.execute("DELETE FROM search_index WHERE doc_id=?",(did,))
        c.execute("DELETE FROM documents WHERE id=?",(did,))
        logger.info("Dokument #%d gelöscht: %s (Quelle: %s)", did, doc.get("original_name",""), src)

def create_backup(progress_cb=None):
    ts=datetime.now().strftime("%Y%m%d_%H%M%S")
    bp=filedialog.asksaveasfilename(title="Backup speichern",initialfile=f"DocVault_Backup_{ts}.zip",
        defaultextension=".zip",filetypes=[("ZIP","*.zip")])
    if not bp: return None
    all_files=[]
    for root,dirs,files in os.walk(str(DATA_DIR)):
        for f in files: all_files.append(Path(root)/f)
    # Lokale Einstellungen und Pfad-Konfiguration mit sichern
    local_extras = []
    for lf in [LOCAL_SETTINGS_PATH, _path_cfg_file]:
        if lf.exists(): local_extras.append(lf)
    total=len(all_files) + len(local_extras)
    try:
        with zipfile.ZipFile(bp,'w',zipfile.ZIP_DEFLATED) as zf:
            for i,fp in enumerate(all_files):
                zf.write(fp,fp.relative_to(DATA_DIR.parent))
                if progress_cb: progress_cb(i+1,total)
            # Lokale Dateien in Unterordner "_lokal_PC/"
            for j,lf in enumerate(local_extras):
                zf.write(lf, f"_lokal_PC/{lf.name}")
                if progress_cb: progress_cb(len(all_files)+j+1,total)
        logger.info("Backup erstellt: %s (%d Dateien + %d lokale)", bp, len(all_files), len(local_extras))
        return bp
    except Exception as e:
        logger.error("Backup fehlgeschlagen: %s", e, exc_info=True)
        return None


# ═══════ SCANNER: NAPS2 (ADF + OCR integriert) ═══════
# NAPS2 ist kostenlos, Open Source und unterstützt ADF zuverlässig.
# Download: https://www.naps2.com/ → NAPS2.Console.exe
NAPS2_PATHS = [
    r"C:\NAPS2-Portable\App\NAPS2.Console.exe",
    r"C:\Program Files\NAPS2\NAPS2.Console.exe",
    r"C:\Program Files (x86)\NAPS2\NAPS2.Console.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Programs\NAPS2\NAPS2.Console.exe"),
]

def _find_naps2():
    """Sucht NAPS2.Console.exe – LOKALER gespeicherter Pfad zuerst."""
    # 1. Lokale Einstellung (pro PC)
    saved = _local.get("naps2_path", "")
    if saved and os.path.isfile(saved):
        return saved
    # 2. Bekannte Installationspfade
    for p in NAPS2_PATHS:
        if os.path.isfile(p): return p
    # 3. Im PATH suchen
    import shutil as _sh
    found = _sh.which("NAPS2.Console")
    if found: return found
    return None

NAPS2_EXE = _find_naps2()

def set_naps2_path(path):
    """Setzt und speichert den NAPS2-Pfad LOKAL (pro PC)."""
    global NAPS2_EXE, NAPS2_ENV, _local
    if not os.path.isfile(path):
        return False
    NAPS2_EXE = path
    _local["naps2_path"] = path
    save_local(_local)
    # Components-Fix neu ausführen
    NAPS2_ENV = None
    _fix_naps2_components()
    logger.info("NAPS2 Pfad gesetzt (lokal): %s", path)
    return True

# ═══ FIX: NAPS2 OCR-Komponenten-Pfad mit Sonderzeichen (z.B. André → é) ═══
# Tesseract innerhalb von NAPS2 scheitert wenn der Pfad Sonderzeichen enthält.
# Lösung: Components in einen sauberen Pfad kopieren.
NAPS2_ENV = None  # Umgebungsvariablen für NAPS2 subprocess-Aufrufe

def _fix_naps2_components():
    """Prüft und repariert den NAPS2 Components-Pfad."""
    global NAPS2_ENV
    if not NAPS2_EXE or platform.system() != "Windows":
        return

    # Original-Pfad: %APPDATA%\NAPS2\Components oder neben der Portable-EXE
    appdata = os.environ.get("APPDATA", "")
    orig_comp = os.path.join(appdata, "NAPS2", "components")
    
    # Bei Portable-Version: Components neben der EXE
    naps2_dir = os.path.dirname(NAPS2_EXE)
    portable_comp = os.path.join(naps2_dir, "components")
    if os.path.isdir(portable_comp):
        # Portable hat eigenen Components-Ordner → prüfe ob DIESER Pfad OK ist
        try:
            naps2_dir.encode("ascii")
            logger.info("NAPS2 Portable Components OK: %s", portable_comp)
            return  # Kein Fix nötig
        except UnicodeEncodeError:
            orig_comp = portable_comp  # Portable-Pfad hat auch Sonderzeichen

    # Prüfe ob Pfad Nicht-ASCII-Zeichen enthält
    try:
        appdata.encode("ascii")
        # Alles ASCII → kein Problem
        logger.info("NAPS2 Components-Pfad OK (ASCII): %s", orig_comp)
        return
    except UnicodeEncodeError:
        pass

    logger.warning("NAPS2 Components-Pfad enthält Sonderzeichen: %s", appdata)

    # Sauberer Pfad ohne Sonderzeichen
    clean_base = r"C:\ProgramData\NAPS2"
    clean_comp = os.path.join(clean_base, "components")

    # Components kopieren wenn nötig
    if os.path.isdir(orig_comp):
        try:
            os.makedirs(clean_base, exist_ok=True)
            if not os.path.isdir(clean_comp):
                shutil.copytree(orig_comp, clean_comp)
                logger.info("NAPS2 Components kopiert: %s → %s", orig_comp, clean_comp)
            else:
                # Aktualisieren falls Original neuer
                for item in os.listdir(orig_comp):
                    s = os.path.join(orig_comp, item)
                    d = os.path.join(clean_comp, item)
                    if os.path.isdir(s):
                        if not os.path.isdir(d):
                            shutil.copytree(s, d)
                    else:
                        if not os.path.isfile(d) or os.path.getmtime(s) > os.path.getmtime(d):
                            shutil.copy2(s, d)
                logger.info("NAPS2 Components aktualisiert: %s", clean_comp)
        except Exception as e:
            logger.warning("NAPS2 Components kopieren: %s", e)
            return

    # Auch die NAPS2-Konfiguration kopieren (OCR-Einstellungen)
    orig_naps2 = os.path.join(appdata, "NAPS2")
    clean_naps2 = clean_base
    for cfg_file in ["config.xml", "appsettings.xml"]:
        src = os.path.join(orig_naps2, cfg_file)
        dst = os.path.join(clean_naps2, cfg_file)
        if os.path.isfile(src) and not os.path.isfile(dst):
            try: shutil.copy2(src, dst)
            except: pass

    # Umgebungsvariablen: NAPS2 soll den sauberen Pfad verwenden
    NAPS2_ENV = os.environ.copy()
    NAPS2_ENV["NAPS2_COMPONENTS"] = clean_comp
    # Auch APPDATA auf kurzen 8.3-Pfad setzen (Fallback)
    try:
        import ctypes
        buf = ctypes.create_unicode_buffer(500)
        ctypes.windll.kernel32.GetShortPathNameW(appdata, buf, 500)
        short_appdata = buf.value
        if short_appdata and short_appdata != appdata:
            NAPS2_ENV["APPDATA"] = short_appdata
            logger.info("APPDATA → Kurzpfad: %s", short_appdata)
    except Exception as e:
        logger.info("Kurzpfad: %s", e)

    logger.info("NAPS2 Umgebung angepasst: Components=%s", clean_comp)

_fix_naps2_components()

def naps2_find_profiles_xml():
    """Findet profiles.xml – alle möglichen Pfade für installiert und portable."""
    search_paths = []
    if NAPS2_EXE:
        naps2_dir = os.path.dirname(NAPS2_EXE)
        # Portable: Data neben App-Ordner (z.B. C:\NAPS2-Portable\Data\)
        parent = os.path.dirname(naps2_dir)
        search_paths.append(os.path.join(parent, "Data", "profiles.xml"))
        # Direkt neben EXE
        search_paths.append(os.path.join(naps2_dir, "profiles.xml"))
        # Portable: Data neben EXE
        search_paths.append(os.path.join(naps2_dir, "Data", "profiles.xml"))
        # Zwei Ebenen hoch (falls App\NAPS2.Console.exe)
        grandparent = os.path.dirname(parent)
        search_paths.append(os.path.join(grandparent, "Data", "profiles.xml"))
    appdata = os.environ.get("APPDATA", "")
    if appdata:
        search_paths.append(os.path.join(appdata, "NAPS2", "profiles.xml"))
    for pp in search_paths:
        if os.path.isfile(pp):
            logger.info("NAPS2 profiles.xml gefunden: %s", pp)
            return pp
    logger.info("NAPS2 profiles.xml nicht gefunden. Gesucht: %s", search_paths)
    return None

def naps2_list_profiles():
    """Liest NAPS2-Profile mit Details aus profiles.xml."""
    import xml.etree.ElementTree as ET
    pp = naps2_find_profiles_xml()
    if not pp: return [], None
    profiles = []  # Liste von {"name":..., "device":..., "dpi":..., "bitdepth":..., "source":...}
    try:
        tree = ET.parse(pp); root = tree.getroot()
        for prof in root.iter():
            if not prof.tag.endswith("ScanProfile"): continue
            info = {"name":"","device":"","dpi":"","bitdepth":"","source":"","driver":""}
            for child in prof.iter():
                tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
                if tag=="DisplayName" and child.text: info["name"]=child.text.strip()
                elif tag=="Device":
                    for dc in child.iter():
                        dtag = dc.tag.split("}")[-1] if "}" in dc.tag else dc.tag
                        if dtag=="Name" and dc.text: info["device"]=dc.text.strip()
                elif tag=="BitDepth" and child.text: info["bitdepth"]=child.text.strip()
                elif tag=="Resolution" and child.text: info["dpi"]=child.text.strip()
                elif tag=="PaperSource" and child.text: info["source"]=child.text.strip()
                elif tag=="DriverName" and child.text: info["driver"]=child.text.strip()
            if info["name"] and info["name"] not in [p["name"] for p in profiles]:
                profiles.append(info)
        if profiles:
            logger.info("NAPS2 Profile: %s", [p["name"] for p in profiles])
    except Exception as e:
        logger.info("NAPS2 profiles.xml parsen: %s", e)
    return profiles, pp

def naps2_find_gui():
    """Findet NAPS2.exe (GUI) neben der Console-EXE."""
    if not NAPS2_EXE: return None
    naps2_dir = os.path.dirname(NAPS2_EXE)
    for name in ["NAPS2.exe", "NAPS2.Desktop.exe"]:
        p = os.path.join(naps2_dir, name)
        if os.path.isfile(p): return p
    return None

def naps2_list_scanners():
    """Listet alle verfügbaren Scanner über NAPS2."""
    if not NAPS2_EXE:
        logger.warning("NAPS2 nicht gefunden")
        return []
    try:
        r = _run_subprocess(
            [NAPS2_EXE, "--driver", "wia", "--listdevices"],
            timeout=30, env=NAPS2_ENV)
        lines = (r.stdout or "").strip().split("\n")
        devices = [l.strip() for l in lines if l.strip() and not l.startswith("---")]
        logger.info("NAPS2 Scanner: %s", devices)
        return devices
    except Exception as e:
        logger.error("NAPS2 Scannerliste: %s", e)
        return []

def naps2_scan(scanner_name, dpi=150, color="color", source="feeder", fmt="pdf",
               ocr_lang="deu", enable_ocr=True, ocr_fast=False, deskew=False,
               profile=None):
    """Scannt über NAPS2. Bei profile= wird das NAPS2-Profil verwendet.
    
    Gibt (dateipfad, ocr_text, fehler) zurück.
    """
    import tempfile, time
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    if not NAPS2_EXE:
        return None, "", "NAPS2.Console.exe nicht gefunden!"

    TEMP_DIR = tempfile.gettempdir()
    SCAN_TEMP = os.path.join(TEMP_DIR, f"docvault_scan_{ts}.pdf")
    if os.path.exists(SCAN_TEMP):
        try: os.remove(SCAN_TEMP)
        except: pass

    if profile:
        # ═══ PROFIL-MODUS – MIT OCR (Text wird sofort extrahiert) ═══
        cmd = [NAPS2_EXE, "--profile", profile,
               "--enableocr", "--ocrlang", ocr_lang,
               "-o", SCAN_TEMP, "--force"]
        logger.info("NAPS2 Profil: '%s' (mit OCR, Sprache: %s)", profile, ocr_lang)
        extra_args = []
        attempts = [cmd]
    else:
        # ═══ PARAMETER-MODUS – MIT OCR ═══
        cmd = [
            NAPS2_EXE,
            "--noprofile",
            "--driver", "wia",
            "--device", scanner_name,
            "--source", source,
            "--pagesize", "a4",
            "--bitdepth", color,
            "--dpi", str(dpi),
            "--enableocr", "--ocrlang", ocr_lang,
        ]
        extra_args = []
        if ocr_fast: extra_args.extend(["--ocrmode", "fast"])
        if deskew: extra_args.append("--deskew")
        cmd_with_extras = cmd + extra_args + ["-o", SCAN_TEMP, "--force"]
        cmd_basic = cmd + ["-o", SCAN_TEMP, "--force"]
        attempts = [cmd_with_extras, cmd_basic] if extra_args else [cmd_basic]

    for attempt, try_cmd in enumerate(attempts):
        logger.info("NAPS2 (Versuch %d): %s", attempt+1, " ".join(try_cmd))

        # Alte Temp-Datei löschen
        if os.path.exists(SCAN_TEMP):
            try: os.remove(SCAN_TEMP)
            except: pass

        try:
            result = _run_subprocess(try_cmd, timeout=600, env=NAPS2_ENV)
            
            stdout = (result.stdout or "").strip()
            stderr = (result.stderr or "").strip()
            if stdout: logger.info("NAPS2 stdout: %s", stdout[:500])
            if stderr: logger.info("NAPS2 stderr: %s", stderr[:500])
            logger.info("NAPS2 returncode: %d", result.returncode)

            # Prüfe ob Scan fehlgeschlagen (returncode != 0 oder unbekannte Optionen)
            if result.returncode != 0 and attempt == 0 and extra_args:
                logger.warning("NAPS2 mit erweiterten Optionen fehlgeschlagen – versuche ohne...")
                continue  # Nächster Versuch ohne Extras

            # Auf Datei warten
            found = False
            for _ in range(20):
                if os.path.exists(SCAN_TEMP) and os.path.getsize(SCAN_TEMP) > 0:
                    found = True; break
                time.sleep(0.5)

            if found:
                logger.info("✔ Scan-Datei: %s (%.0f KB)", SCAN_TEMP, os.path.getsize(SCAN_TEMP)/1024)

                # OCR-Text direkt aus dem gescannten PDF extrahieren
                ocr_text = ""
                page_count = 1
                if HAS_FITZ:
                    try:
                        doc = fitz.open(SCAN_TEMP)
                        ocr_text = "".join([page.get_text() for page in doc])
                        page_count = len(doc)
                        doc.close()
                        logger.info("✔ OCR: %d Seiten, %d Zeichen", page_count, len(ocr_text))
                    except Exception: pass
                # pdfplumber Fallback
                if len(ocr_text.strip()) < 10:
                    try:
                        with pdfplumber.open(SCAN_TEMP) as pdf:
                            pt = "\n\n".join(p.extract_text() or "" for p in pdf.pages)
                            if len(pt.strip()) > len(ocr_text.strip()):
                                ocr_text = pt
                    except Exception: pass

                # Datei verschieben
                final_name = f"Scan_{ts}.pdf"
                final_path = str(DOCS_DIR / final_name)
                shutil.move(SCAN_TEMP, final_path)
                logger.info("✔ Verschoben: %s (%d Zeichen OCR)", final_path, len(ocr_text))
                return final_path, ocr_text, ""
            else:
                err_msg = stderr or stdout or "Keine Datei erstellt"
                # ADF-Papierfehler erkennen
                adf_hints = ["no paper","no document","feeder empty","paper jam",
                              "kein papier","no pages","adf","empty",
                              "zuführung","zufuehrung","keine seiten","einzug"]
                is_adf = any(h in err_msg.lower() for h in adf_hints)
                # Auch wenn returncode != 0 und keine Datei: wahrscheinlich kein Papier im ADF
                if not is_adf and result.returncode != 0 and source == "feeder":
                    is_adf = True
                if is_adf:
                    err_msg = "Vermutlich kein Papier im Einzug (ADF).\n\nBitte Papier einlegen und erneut versuchen."
                if attempt == 0 and extra_args:
                    continue
                logger.error("❌ Scan fehlgeschlagen: %s", err_msg)
                return None, "", err_msg

        except subprocess.TimeoutExpired:
            logger.error("NAPS2: Timeout (600s)")
            return None, "", "Timeout – Scan dauerte zu lange (>10 Min.)"
        except Exception as e:
            logger.error("NAPS2 Fehler: %s", e, exc_info=True)
            return None, "", str(e)

    return None, "", "Scan fehlgeschlagen nach allen Versuchen"

def _convert_pdf_to_image(pdf_path, ts, fmt):
    """Konvertiert einzelseitige PDF → WebP/JPEG via PyMuPDF."""
    try:
        if HAS_FITZ:
            doc = fitz.open(str(pdf_path))
            if len(doc) > 0:
                page = doc[0]; pix = page.get_pixmap(dpi=150)
                img = _pix_to_pil(pix)
                doc.close()
                if fmt == "webp":
                    out = DATA_DIR / f"scan_{ts}.webp"
                    img.save(str(out), "WEBP", quality=85)
                elif fmt == "jpeg":
                    out = DATA_DIR / f"scan_{ts}.jpg"
                    img.save(str(out), "JPEG", quality=90)
                else:
                    return str(pdf_path)
                pdf_path.unlink()
                logger.info("Konvertiert: %s", out.name)
                return str(out)
            doc.close()
        return str(pdf_path)
    except Exception as e:
        logger.warning("Konvertierung: %s", e)
        return str(pdf_path)




# ═══════ ERWEITERTER NOTIZ-EDITOR ═══════
# Fonts, Farben, Ausrichtung, Listen, Tabellen, Drucken

FONTS_WEBSAFE = ["Segoe UI","Arial","Helvetica","Times New Roman","Georgia",
    "Verdana","Tahoma","Trebuchet MS","Courier New","Consolas","Lucida Console"]
FONT_SIZES = [8,9,10,11,12,14,16,18,20,24,28,32,36,48]

class NoteEditor(ctk.CTkToplevel):
    def __init__(self,master,on_save=None,edit_doc=None):
        super().__init__(master)
        self.title(f"DocVault v{VERSION} – {_t('note_title')}")
        _set_window_icon(self)
        self.transient(master); self.on_save_cb=on_save; self.edit_doc=edit_doc
        self._images={}; self._link_urls={}
        self._cur_font="Segoe UI"; self._cur_size=12
        self._cfg=load_ini(); restore_geometry(self._cfg,"note_editor",self,"1050x750")
        self._build()
        if edit_doc: self._load(edit_doc)
        self.protocol("WM_DELETE_WINDOW",self._on_close)

    def _on_close(self):
        save_geometry(self._cfg,"note_editor",self); self.destroy()

    # ═══ TOOLTIP HELPER ═══
    def _tip(self, widget, text):
        """Tooltip für ein Widget."""
        tip_win = [None]
        def show(ev):
            if tip_win[0]: return
            tw = tk.Toplevel(widget); tw.wm_overrideredirect(True)
            tw.wm_geometry(f"+{ev.x_root+12}+{ev.y_root+16}")
            lbl = tk.Label(tw, text=text, background="#ffffe0", foreground="#333",
                relief="solid", borderwidth=1, font=("Segoe UI", 9), padx=6, pady=2)
            lbl.pack()
            tip_win[0] = tw
        def hide(ev):
            if tip_win[0]: tip_win[0].destroy(); tip_win[0] = None
        widget.bind("<Enter>", show); widget.bind("<Leave>", hide)

    def _build(self):
        # ═══ Titel ═══
        top=ctk.CTkFrame(self,fg_color="transparent"); top.pack(fill="x",padx=12,pady=(10,2))
        self.title_var=ctk.StringVar(value="Neue Notiz" if _LANG=="de" else "New Note")
        ctk.CTkEntry(top,textvariable=self.title_var,font=ctk.CTkFont(size=16,weight="bold"),
            height=38,corner_radius=8,placeholder_text=_t("note_title_ph")).pack(fill="x")

        # ═══ Toolbar Zeile 1: Font, Grösse, Formate, Farben ═══
        tb1=ctk.CTkFrame(self,height=36,fg_color=("gray90","#21242f"),corner_radius=6)
        tb1.pack(fill="x",padx=12,pady=(6,1))
        self.font_var=ctk.StringVar(value=self._cur_font)
        font_om=ctk.CTkOptionMenu(tb1,values=FONTS_WEBSAFE,variable=self.font_var,width=140,height=28,
            font=ctk.CTkFont(size=11),command=self._apply_font,
            fg_color=("#e8eef8","#353a4a"),text_color=("gray10","gray90"),
            dropdown_text_color=("gray10","gray90"),dropdown_fg_color=("#f8faff","#2a2e3b"))
        font_om.pack(side="left",padx=(6,2),pady=3)
        self._tip(font_om, "Font" if _LANG=="en" else "Schriftart")
        self.size_var=ctk.StringVar(value="12")
        size_om=ctk.CTkOptionMenu(tb1,values=[str(s) for s in FONT_SIZES],variable=self.size_var,
            width=60,height=28,font=ctk.CTkFont(size=11),command=self._apply_size,
            fg_color=("#e8eef8","#353a4a"),text_color=("gray10","gray90"),
            dropdown_text_color=("gray10","gray90"),dropdown_fg_color=("#f8faff","#2a2e3b"))
        size_om.pack(side="left",padx=2,pady=3)
        self._tip(size_om, "Font Size" if _LANG=="en" else "Schriftgrösse")
        self._sep(tb1)
        # Format-Buttons mit Tooltips
        bs={"width":32,"height":28,"corner_radius":5,"font":ctk.CTkFont(size=13,weight="bold"),
            "fg_color":"transparent","hover_color":("gray80","#353a4a"),"text_color":("gray20","gray80")}
        self._fmt_btns={}
        fmt_items = [
            ("B", self._bold,    "Bold (Ctrl+B)" if _LANG=="en" else "Fett (Strg+B)"),
            ("I", self._italic,  "Italic (Ctrl+I)" if _LANG=="en" else "Kursiv (Strg+I)"),
            ("U", self._underline, "Underline (Ctrl+U)" if _LANG=="en" else "Unterstrichen (Strg+U)"),
            ("S", self._strike,  "Strikethrough" if _LANG=="en" else "Durchgestrichen"),
            ("x²",self._superscript, "Superscript" if _LANG=="en" else "Hochgestellt"),
            ("x₂",self._subscript, "Subscript" if _LANG=="en" else "Tiefgestellt"),
        ]
        for txt,cmd,tip in fmt_items:
            b=ctk.CTkButton(tb1,text=txt,command=cmd,**bs); b.pack(side="left",padx=1,pady=3)
            self._fmt_btns[txt]=b; self._tip(b,tip)
        self._sep(tb1)
        # Farben
        fg_btn=ctk.CTkButton(tb1,text="A",command=self._color_fg,width=32,height=28,corner_radius=5,
            font=ctk.CTkFont(size=14,weight="bold"),fg_color="transparent",
            hover_color=("gray80","#353a4a"),text_color=("red","#ef4444"))
        fg_btn.pack(side="left",padx=1,pady=3); self._tip(fg_btn, "Text Color" if _LANG=="en" else "Textfarbe")
        bg_btn=ctk.CTkButton(tb1,text="🖌",command=self._color_bg,width=32,height=28,corner_radius=5,
            font=ctk.CTkFont(size=13),fg_color="transparent",
            hover_color=("gray80","#353a4a"),text_color=("gray20","gray80"))
        bg_btn.pack(side="left",padx=1,pady=3); self._tip(bg_btn, "Highlight Color" if _LANG=="en" else "Hintergrundfarbe")
        self._sep(tb1)
        clr_btn=ctk.CTkButton(tb1,text="🧹",command=self._clear_fmt,width=32,height=28,corner_radius=5,
            font=ctk.CTkFont(size=13),fg_color="transparent",
            hover_color=("gray80","#353a4a"),text_color=("gray20","gray80"))
        clr_btn.pack(side="left",padx=1,pady=3); self._tip(clr_btn, "Clear Formatting" if _LANG=="en" else "Formatierung löschen")
        self._sep(tb1)
        # Undo/Redo
        undo_btn=ctk.CTkButton(tb1,text="↩",command=self._undo,**bs); undo_btn.pack(side="left",padx=1,pady=3)
        self._tip(undo_btn, "Undo (Ctrl+Z)" if _LANG=="en" else "Rückgängig (Strg+Z)")
        redo_btn=ctk.CTkButton(tb1,text="↪",command=self._redo,**bs); redo_btn.pack(side="left",padx=1,pady=3)
        self._tip(redo_btn, "Redo (Ctrl+Y)" if _LANG=="en" else "Wiederherstellen (Strg+Y)")

        # ═══ Toolbar Zeile 2: Ausrichtung, Listen, Einzug, Überschriften, Einfügen ═══
        tb2=ctk.CTkFrame(self,height=36,fg_color=("gray90","#21242f"),corner_radius=6)
        tb2.pack(fill="x",padx=12,pady=(1,2))
        align_items = [
            ("⬅",self._align_left, "Align Left" if _LANG=="en" else "Linksbündig"),
            ("⬌",self._align_center, "Center" if _LANG=="en" else "Zentriert"),
            ("➡",self._align_right, "Align Right" if _LANG=="en" else "Rechtsbündig"),
        ]
        for txt,cmd,tip in align_items:
            b=ctk.CTkButton(tb2,text=txt,command=cmd,**bs); b.pack(side="left",padx=1,pady=3); self._tip(b,tip)
        self._sep(tb2)
        list_items = [
            ("• ",self._list_bullet, "Bullet List" if _LANG=="en" else "Aufzählung"),
            ("1.",self._list_number, "Numbered List" if _LANG=="en" else "Nummerierung"),
        ]
        for txt,cmd,tip in list_items:
            b=ctk.CTkButton(tb2,text=txt,command=cmd,**bs); b.pack(side="left",padx=1,pady=3); self._tip(b,tip)
        self._sep(tb2)
        indent_items = [
            ("→",self._indent, "Indent" if _LANG=="en" else "Einrücken"),
            ("←",self._outdent, "Outdent" if _LANG=="en" else "Ausrücken"),
        ]
        for txt,cmd,tip in indent_items:
            b=ctk.CTkButton(tb2,text=txt,command=cmd,**bs); b.pack(side="left",padx=1,pady=3); self._tip(b,tip)
        self._sep(tb2)
        h_items = [
            ("H1",self._h1, "Heading 1" if _LANG=="en" else "Überschrift 1"),
            ("H2",self._h2, "Heading 2" if _LANG=="en" else "Überschrift 2"),
        ]
        for txt,cmd,tip in h_items:
            b=ctk.CTkButton(tb2,text=txt,command=cmd,**bs); b.pack(side="left",padx=1,pady=3)
            self._fmt_btns[txt]=b; self._tip(b,tip)
        self._sep(tb2)
        ins_items = [
            ("🔗",self._ins_link, "Insert Link (Ctrl+K)" if _LANG=="en" else "Link einfügen (Strg+K)"),
            ("🖼️",self._ins_img, "Insert Image" if _LANG=="en" else "Bild einfügen"),
            ("📋",self._paste_img, "Paste Image" if _LANG=="en" else "Bild aus Zwischenablage"),
            ("─",self._ins_hr, "Horizontal Rule" if _LANG=="en" else "Trennlinie"),
        ]
        for txt,cmd,tip in ins_items:
            b=ctk.CTkButton(tb2,text=txt,command=cmd,**bs); b.pack(side="left",padx=1,pady=3); self._tip(b,tip)
        self._sep(tb2)
        # Suchen
        find_btn=ctk.CTkButton(tb2,text="🔍",command=self._find_replace,**bs)
        find_btn.pack(side="left",padx=1,pady=3); self._tip(find_btn, "Find & Replace (Ctrl+F)" if _LANG=="en" else "Suchen & Ersetzen (Strg+F)")
        self._sep(tb2)
        pr_btn=ctk.CTkButton(tb2,text=_t("note_print"),width=90,height=28,corner_radius=5,
            font=ctk.CTkFont(size=11),fg_color=("gray80","#353a4a"),
            text_color=("gray20","gray80"),command=self._print)
        pr_btn.pack(side="left",padx=4,pady=3)
        ctk.CTkButton(tb2,text=_t("note_save"),width=100,height=28,corner_radius=5,
            font=ctk.CTkFont(size=12,weight="bold"),command=self._save).pack(side="right",padx=6,pady=3)

        # ═══ Status-Leiste ═══
        self._status=ctk.CTkLabel(self,text="",font=ctk.CTkFont(size=10),
            text_color=("gray50","gray55"),anchor="w")
        self._status.pack(fill="x",padx=14,pady=(0,1))

        # ═══ Text-Widget ═══
        ef=ctk.CTkFrame(self,fg_color="transparent"); ef.pack(fill="both",expand=True,padx=12,pady=(0,10))
        self.text=tk.Text(ef,wrap="word",undo=True,maxundo=50,font=(self._cur_font,self._cur_size),
            bg="#ffffff",fg="#1a1a1a",insertbackground="#1a1a1a",selectbackground="#4f8ff7",
            relief="flat",padx=16,pady=12,tabs="40")
        sb=ctk.CTkScrollbar(ef,command=self.text.yview); self.text.configure(yscrollcommand=sb.set)
        sb.pack(side="right",fill="y"); self.text.pack(fill="both",expand=True)

        # ═══ Tags definieren ═══
        f=self._cur_font; sz=self._cur_size
        # Bold/Italic/Size werden über dynamische Combined-Tags gelöst (siehe _apply_font_style)
        self.text.tag_configure("underline",underline=True)
        self.text.tag_configure("strike",overstrike=True)
        self.text.tag_configure("superscript",offset=6,font=(f,max(8,sz-3)))
        self.text.tag_configure("subscript",offset=-4,font=(f,max(8,sz-3)))
        self.text.tag_configure("h1",font=(f,24,"bold"),spacing1=8,spacing3=4)
        self.text.tag_configure("h2",font=(f,18,"bold"),spacing1=6,spacing3=3)
        self.text.tag_configure("link",foreground="#4f8ff7",underline=True)
        self.text.tag_configure("hr",font=(f,2),foreground="#bbbbbb",spacing1=4,spacing3=4)
        self.text.tag_configure("align_left",justify="left")
        self.text.tag_configure("align_center",justify="center")
        self.text.tag_configure("align_right",justify="right")
        for lvl in range(1,6):
            self.text.tag_configure(f"indent_{lvl}",lmargin1=lvl*40,lmargin2=lvl*40)
        self.text.tag_raise("h1"); self.text.tag_raise("h2")

        self.text.tag_bind("link","<Button-1>",self._click_link)
        # Tastenkürzel
        for k,c in [("<Control-b>",self._bold),("<Control-i>",self._italic),
            ("<Control-u>",self._underline),("<Control-s>",self._save),
            ("<Control-k>",lambda e=None:self._ins_link()),
            ("<Control-f>",lambda e=None:self._find_replace()),
            ("<Control-p>",lambda e=None:self._print()),
            ("<Control-z>",lambda e=None:self._undo()),
            ("<Control-y>",lambda e=None:self._redo())]:
            self.text.bind(k,lambda e,fn=c:fn())
        self.text.bind("<Control-v>",self._on_paste)
        self.text.bind("<Control-Shift-V>",self._paste_plain)
        self.text.bind("<Control-Shift-v>",self._paste_plain)
        self.text.bind("<KeyRelease>",self._update_status)
        self.text.bind("<ButtonRelease-1>",self._update_status)
        # Rechtsklick-Menü
        self.text.bind("<Button-3>",self._ctx_menu)
        self.text.bind("<Double-Button-1>",self._on_dblclick)

    def _sep(self,parent):
        ctk.CTkFrame(parent,width=1,height=20,fg_color=("gray75","#353a4a")).pack(side="left",padx=3,pady=6)

    # ═══════ UNDO / REDO ═══════
    def _undo(self):
        try: self.text.edit_undo()
        except tk.TclError: pass
    def _redo(self):
        try: self.text.edit_redo()
        except tk.TclError: pass

    # ═══════ DYNAMISCHES COMBINED-TAG-SYSTEM ═══════
    # Löst das Tk-Problem dass font= immer ALLE Font-Eigenschaften überschreibt.
    # Jede Kombination von Family+Size+Weight+Slant bekommt einen eigenen Tag.
    # Tag-Name: fs_{family}_{size}_{bi}  (b=bold, i=italic, bi=beides, n=normal)

    def _get_sel_range(self):
        try: return self.text.index("sel.first"), self.text.index("sel.last")
        except tk.TclError: return None, None

    def _cur_font_state(self, idx=None):
        """Liest den aktuellen Font-Zustand an Position idx (oder sel.first)."""
        if idx is None:
            idx = self._get_sel_range()[0]
            if not idx: idx = self.text.index("insert")
        tags = self.text.tag_names(idx)
        family = self._cur_font
        size = self._cur_size
        bold = False
        italic = False
        for t in tags:
            if t.startswith("fs_"):
                # Parse: fs_{family}_{size}_{style}
                parts = t.split("_")
                if len(parts) >= 4:
                    family = parts[1].replace("~", " ")
                    try: size = int(parts[2])
                    except: pass
                    style = parts[3] if len(parts) > 3 else "n"
                    bold = "b" in style
                    italic = "i" in style
        return family, size, bold, italic

    def _make_font_tag(self, family, size, bold, italic):
        """Erstellt/konfiguriert einen Combined-Font-Tag und gibt seinen Namen zurück."""
        style = ("b" if bold else "") + ("i" if italic else "") or "n"
        safe_family = family.replace(" ", "~")
        tag_name = f"fs_{safe_family}_{size}_{style}"
        # Font-String bauen
        weight = "bold" if bold else "normal"
        slant = "italic" if italic else "roman"
        font_tuple = (family, size, f"{weight} {slant}".strip())
        self.text.tag_configure(tag_name, font=font_tuple)
        return tag_name

    def _remove_font_tags(self, s, e):
        """Entfernt alle font-bezogenen Tags von der Selektion."""
        # Alle Tags im gesamten Bereich sammeln
        all_tags = set()
        idx = s
        while self.text.compare(idx, "<", e):
            for t in self.text.tag_names(idx):
                if t.startswith("fs_") or t.startswith("font_") or t.startswith("sz_"):
                    all_tags.add(t)
            idx = self.text.index(f"{idx}+1c")
        for t in all_tags:
            self.text.tag_remove(t, s, e)
        # Alte Kompatibilitäts-Tags entfernen
        for t in ("bold", "italic", "bold_italic"):
            self.text.tag_remove(t, s, e)

    def _apply_font_style(self, toggle_bold=None, toggle_italic=None, new_family=None, new_size=None):
        """Wendet Font-Änderung an. Erhält alle anderen Eigenschaften."""
        s, e = self._get_sel_range()
        if not s: return
        family, size, is_bold, is_italic = self._cur_font_state(s)
        # Gewünschte Änderung anwenden
        if toggle_bold is not None:
            is_bold = not is_bold
        if toggle_italic is not None:
            is_italic = not is_italic
        if new_family is not None:
            family = new_family
        if new_size is not None:
            size = new_size
        # Alten Font-Tag entfernen, neuen setzen
        self._remove_font_tags(s, e)
        new_tag = self._make_font_tag(family, size, is_bold, is_italic)
        self.text.tag_add(new_tag, s, e)

    def _bold(self):
        self._apply_font_style(toggle_bold=True)

    def _italic(self):
        self._apply_font_style(toggle_italic=True)

    def _toggle(self,tag):
        s, e = self._get_sel_range()
        if not s: return
        if tag in self.text.tag_names(s): self.text.tag_remove(tag,s,e)
        else: self.text.tag_add(tag,s,e)

    def _underline(self): self._toggle("underline")
    def _strike(self): self._toggle("strike")
    def _superscript(self):
        s, e = self._get_sel_range()
        if not s: return
        self.text.tag_remove("subscript",s,e); self._toggle("superscript")
    def _subscript(self):
        s, e = self._get_sel_range()
        if not s: return
        self.text.tag_remove("superscript",s,e); self._toggle("subscript")

    # ═══════ SCHRIFT ═══════
    def _apply_font(self,_=None):
        self._cur_font=self.font_var.get()
        self._apply_font_style(new_family=self._cur_font)
    def _apply_size(self,_=None):
        self._cur_size=int(self.size_var.get())
        self._apply_font_style(new_size=self._cur_size)

    # ═══════ FARBEN ═══════
    def _color_fg(self):
        c=colorchooser.askcolor(title="Text Color" if _LANG=="en" else "Textfarbe")[1]
        if not c: return
        s, e = self._get_sel_range()
        if not s: return
        tag=f"clr_{c}"; self.text.tag_configure(tag,foreground=c); self.text.tag_add(tag,s,e)
    def _color_bg(self):
        c=colorchooser.askcolor(title="Highlight" if _LANG=="en" else "Hintergrundfarbe")[1]
        if not c: return
        s, e = self._get_sel_range()
        if not s: return
        tag=f"bg_{c}"; self.text.tag_configure(tag,background=c); self.text.tag_add(tag,s,e)

    # ═══════ AUSRICHTUNG ═══════
    def _set_align(self,align):
        try: s=self.text.index("sel.first linestart"); e=self.text.index("sel.last lineend")
        except tk.TclError: s=self.text.index("insert linestart"); e=self.text.index("insert lineend")
        for a in ["align_left","align_center","align_right"]: self.text.tag_remove(a,s,e)
        self.text.tag_add(f"align_{align}",s,e)
    def _align_left(self): self._set_align("left")
    def _align_center(self): self._set_align("center")
    def _align_right(self): self._set_align("right")

    # ═══════ LISTEN (mit Undo-Unterstützung) ═══════
    def _list_bullet(self):
        try: s=self.text.index("sel.first linestart"); e=self.text.index("sel.last lineend")
        except tk.TclError: s=self.text.index("insert linestart"); e=self.text.index("insert lineend")
        self.text.edit_separator()
        lines=self.text.get(s,e).split("\n"); self.text.delete(s,e)
        result = []
        for l in lines:
            clean=l.lstrip("•●○0123456789.) \t")
            if l.lstrip().startswith("•"):
                result.append(clean)  # Toggle off: remove bullet
            else:
                result.append("  • " + clean)
        self.text.insert(s, "\n".join(result))
        self.text.edit_separator()

    def _list_number(self):
        try: s=self.text.index("sel.first linestart"); e=self.text.index("sel.last lineend")
        except tk.TclError: s=self.text.index("insert linestart"); e=self.text.index("insert lineend")
        self.text.edit_separator()
        lines=self.text.get(s,e).split("\n"); self.text.delete(s,e)
        result = []
        has_numbers = any(l.lstrip()[:2].rstrip(". ").isdigit() for l in lines if l.strip())
        for i,l in enumerate(lines):
            clean=l.lstrip("•●○0123456789.) \t")
            if has_numbers:
                result.append(clean)  # Toggle off: remove numbers
            else:
                result.append(f"  {i+1}. " + clean)
        self.text.insert(s, "\n".join(result))
        self.text.edit_separator()

    # ═══════ EINZUG ═══════
    def _indent(self):
        try: s=self.text.index("sel.first linestart"); e=self.text.index("sel.last lineend")
        except tk.TclError: s=self.text.index("insert linestart"); e=self.text.index("insert lineend")
        cur=0
        for t in self.text.tag_names(s):
            if t.startswith("indent_"): cur=int(t.split("_")[1]); break
        new_lvl=min(cur+1,5)
        for lvl in range(1,6): self.text.tag_remove(f"indent_{lvl}",s,e)
        if new_lvl>0: self.text.tag_add(f"indent_{new_lvl}",s,e)

    def _outdent(self):
        try: s=self.text.index("sel.first linestart"); e=self.text.index("sel.last lineend")
        except tk.TclError: s=self.text.index("insert linestart"); e=self.text.index("insert lineend")
        cur=0
        for t in self.text.tag_names(s):
            if t.startswith("indent_"): cur=int(t.split("_")[1]); break
        new_lvl=max(cur-1,0)
        for lvl in range(1,6): self.text.tag_remove(f"indent_{lvl}",s,e)
        if new_lvl>0: self.text.tag_add(f"indent_{new_lvl}",s,e)

    # ═══════ ÜBERSCHRIFTEN (mit bold_italic Unterstützung) ═══════
    def _heading(self,tag,other):
        try: s,e=self.text.index("sel.first linestart"),self.text.index("sel.last lineend")
        except tk.TclError: s,e=self.text.index("insert linestart"),self.text.index("insert lineend")
        is_active = tag in self.text.tag_names(s)
        for t in ("h1","h2"): self.text.tag_remove(t,s,e)
        if not is_active:
            self.text.tag_add(tag, s, e)
    def _h1(self): self._heading("h1","h2")
    def _h2(self): self._heading("h2","h1")

    # ═══════ TRENNLINIE ═══════
    def _ins_hr(self):
        """Trennlinie als dünne Textzeile (speicher- und ladbar)."""
        hr_text = "─" * 120  # Genug Zeichen um bei Wortumbruch die volle Breite zu füllen
        self.text.insert("insert", "\n")
        start = self.text.index("insert")
        self.text.insert("insert", hr_text)
        end = self.text.index("insert")
        self.text.tag_add("hr", start, end)
        self.text.insert("insert", "\n")

    # ═══════ FORMATIERUNG LÖSCHEN ═══════
    def _clear_fmt(self):
        s, e = self._get_sel_range()
        if not s: return
        # Alle Tags im gesamten Bereich sammeln
        all_tags = set()
        idx = s
        while self.text.compare(idx, "<", e):
            for t in self.text.tag_names(idx):
                if t not in ("sel","find_highlight"):
                    all_tags.add(t)
            idx = self.text.index(f"{idx}+1c")
        for tag in all_tags:
            self.text.tag_remove(tag, s, e)

    # ═══════ LINKS ═══════
    def _ins_link(self):
        dlg=ctk.CTkToplevel(self); dlg.title("Link" if _LANG=="en" else "Link einfügen")
        _set_window_icon(dlg); dlg.transient(self); dlg.grab_set(); center_window(dlg, 440, 200)
        ctk.CTkLabel(dlg, text="URL:", font=ctk.CTkFont(size=12,weight="bold")).pack(anchor="w",padx=16,pady=(12,2))
        url_var = ctk.StringVar(value="https://")
        ctk.CTkEntry(dlg, textvariable=url_var, width=400, height=32).pack(padx=16,pady=(0,8))
        # Anzeigetext
        try: sel_text = self.text.get("sel.first","sel.last")
        except tk.TclError: sel_text = ""
        ctk.CTkLabel(dlg, text="Text:" if _LANG=="en" else "Anzeigetext:", font=ctk.CTkFont(size=12,weight="bold")).pack(anchor="w",padx=16,pady=(4,2))
        text_var = ctk.StringVar(value=sel_text)
        ctk.CTkEntry(dlg, textvariable=text_var, width=400, height=32,
            placeholder_text="(URL as text)" if _LANG=="en" else "(URL als Text)").pack(padx=16,pady=(0,8))
        def _do_insert():
            url = url_var.get().strip()
            if not url: dlg.destroy(); return
            display = text_var.get().strip() or url
            dlg.destroy()
            # Bestehende Selektion ersetzen oder an Cursor einfügen
            try:
                s = self.text.index("sel.first"); e = self.text.index("sel.last")
                self.text.delete(s, e)
            except tk.TclError:
                s = self.text.index("insert")
            self.text.insert(s, display)
            e = self.text.index(f"{s}+{len(display)}c")
            lt = f"lnk_{uuid.uuid4().hex[:8]}"
            self.text.tag_configure(lt, foreground="#4f8ff7", underline=True)
            self.text.tag_add("link", s, e)
            self.text.tag_add(lt, s, e)
            self._link_urls[lt] = url
        ctk.CTkButton(dlg, text="OK", width=100, height=32, command=_do_insert).pack(pady=(4,12))

    def _click_link(self,ev):
        idx=self.text.index(f"@{ev.x},{ev.y}")
        for tag in self.text.tag_names(idx):
            if tag in self._link_urls: import webbrowser; webbrowser.open(self._link_urls[tag]); return

    def _edit_link(self, ev=None):
        """Link an der Cursor-Position bearbeiten (via Rechtsklick-Menü)."""
        idx = self.text.index("insert")
        link_tag = None; old_url = ""
        for tag in self.text.tag_names(idx):
            if tag in self._link_urls:
                link_tag = tag; old_url = self._link_urls[tag]; break
        if not link_tag:
            msg = "No link at cursor position." if _LANG=="en" else "Kein Link an der Cursor-Position."
            messagebox.showinfo("DocVault", msg); return
        # Link-Bereich finden
        ranges = self.text.tag_ranges(link_tag)
        if len(ranges) < 2: return
        s, e = str(ranges[0]), str(ranges[1])
        old_text = self.text.get(s, e)
        # Edit-Dialog
        dlg=ctk.CTkToplevel(self); dlg.title("Edit Link" if _LANG=="en" else "Link bearbeiten")
        _set_window_icon(dlg); dlg.transient(self); dlg.grab_set(); center_window(dlg, 440, 240)
        ctk.CTkLabel(dlg, text="URL:", font=ctk.CTkFont(size=12,weight="bold")).pack(anchor="w",padx=16,pady=(12,2))
        url_var = ctk.StringVar(value=old_url)
        ctk.CTkEntry(dlg, textvariable=url_var, width=400, height=32).pack(padx=16,pady=(0,8))
        ctk.CTkLabel(dlg, text="Text:", font=ctk.CTkFont(size=12,weight="bold")).pack(anchor="w",padx=16,pady=(4,2))
        text_var = ctk.StringVar(value=old_text)
        ctk.CTkEntry(dlg, textvariable=text_var, width=400, height=32).pack(padx=16,pady=(0,8))
        btn_fr = ctk.CTkFrame(dlg, fg_color="transparent"); btn_fr.pack(pady=(4,12))
        def _do_save():
            new_url = url_var.get().strip(); new_text = text_var.get().strip() or new_url
            self._link_urls[link_tag] = new_url
            if new_text != old_text:
                self.text.delete(s, e); self.text.insert(s, new_text)
                ne = self.text.index(f"{s}+{len(new_text)}c")
                self.text.tag_add("link", s, ne); self.text.tag_add(link_tag, s, ne)
            dlg.destroy()
        def _do_remove():
            self.text.tag_remove("link", s, e); self.text.tag_remove(link_tag, s, e)
            del self._link_urls[link_tag]; dlg.destroy()
        ctk.CTkButton(btn_fr, text="OK", width=100, height=32, command=_do_save).pack(side="left",padx=4)
        rm_txt = "Remove Link" if _LANG=="en" else "Link entfernen"
        ctk.CTkButton(btn_fr, text=rm_txt, width=120, height=32,
            fg_color=("gray75","#353a4a"), text_color=("gray30","gray80"),
            command=_do_remove).pack(side="left",padx=4)

    def _on_dblclick(self, ev):
        """Doppelklick: wenn auf Bild → Skalieren-Dialog."""
        idx = self.text.index(f"@{ev.x},{ev.y}")
        iid = self._find_image_at_pos(idx)
        if iid:
            self._scale_image(iid)
            return "break"

    # ═══════ BILDER ═══════
    def _ins_img(self):
        p=filedialog.askopenfilename(filetypes=[("Images" if _LANG=="en" else "Bilder","*.png *.jpg *.jpeg *.gif *.bmp")])
        if p: self._embed(Image.open(p))
    def _paste_img(self):
        try:
            img=ImageGrab.grabclipboard()
            if isinstance(img,Image.Image): self._embed(img)
        except Exception: pass
    def _on_paste(self,ev):
        try:
            img=ImageGrab.grabclipboard()
            if isinstance(img,Image.Image): self._embed(img); return "break"
        except Exception: pass
    def _paste_plain(self,ev=None):
        """Fügt Clipboard-Inhalt als unformatierten Text ein."""
        try:
            txt = self.clipboard_get()
            if txt:
                self.text.insert("insert", txt)
                return "break"
        except tk.TclError: pass
    def _embed(self, pil, iid=None, at_pos=None):
        """Bild einbetten. Original wird separat als {iid}_orig.png gespeichert."""
        orig_pil = pil.copy()
        display_pil = pil.copy()
        if display_pil.width > 560:
            r = 560 / display_pil.width
            display_pil = display_pil.resize((560, int(display_pil.height * r)), Image.LANCZOS)
        if not iid:
            iid = uuid.uuid4().hex[:12]
        # Original immer separat speichern (wird nie überschrieben)
        orig_path = NOTE_IMG_DIR / f"{iid}_orig.png"
        if not orig_path.exists():
            orig_pil.save(str(orig_path), "PNG")
        # Anzeige-Version speichern
        display_path = NOTE_IMG_DIR / f"{iid}.png"
        display_pil.save(str(display_path), "PNG")
        tk_img = ImageTk.PhotoImage(display_pil)
        self._images[iid] = {"tk": tk_img, "file": f"{iid}.png",
                             "pil": display_pil, "orig_pil": orig_pil,
                             "width": display_pil.width, "height": display_pil.height}
        pos = at_pos or "insert"
        self.text.image_create(pos, image=tk_img, name=iid)
        if not at_pos:
            self.text.insert("insert", "\n")

    def _find_image_at_pos(self, idx):
        """Prüft ob an Position idx ein eingebettetes Bild ist. Gibt iid zurück oder None."""
        for iid in self._images:
            try:
                img_idx = self.text.index(iid)
                if img_idx == self.text.index(idx):
                    return iid
            except tk.TclError:
                continue
        return None

    def _scale_image(self, iid):
        """Dialog zum Skalieren eines eingebetteten Bildes."""
        info = self._images.get(iid)
        if not info: return

        # Original IMMER von Datei laden (nie aus Memory-State vertrauen)
        orig_path = NOTE_IMG_DIR / f"{iid}_orig.png"
        display_path = NOTE_IMG_DIR / info["file"]
        if orig_path.exists():
            orig = Image.open(str(orig_path))
        elif display_path.exists():
            orig = Image.open(str(display_path))
            # Nachträglich Original sichern
            orig.save(str(orig_path), "PNG")
        else:
            return
        info["orig_pil"] = orig

        cur_w = info.get("width", orig.width)
        cur_h = info.get("height", orig.height)
        aspect = orig.width / orig.height if orig.height > 0 else 1

        dlg = ctk.CTkToplevel(self)
        ttl = "Scale Image" if _LANG == "en" else "Bild skalieren"
        dlg.title(ttl); _set_window_icon(dlg)
        dlg.transient(self); dlg.grab_set()
        center_window(dlg, 500, 530)

        # Info-Zeile
        orig_lbl = f"Original: {orig.width} × {orig.height} px"
        cur_lbl_txt = f"Current: {cur_w} × {cur_h} px" if _LANG == "en" else f"Aktuell: {cur_w} × {cur_h} px"
        ctk.CTkLabel(dlg, text=orig_lbl, font=ctk.CTkFont(size=11),
            text_color=("gray50", "gray55")).pack(pady=(12, 0))
        ctk.CTkLabel(dlg, text=cur_lbl_txt, font=ctk.CTkFont(size=10),
            text_color=("gray50", "gray55")).pack(pady=(0, 4))

        # Vorschau
        preview_lbl = ctk.CTkLabel(dlg, text="", width=300, height=200)
        preview_lbl.pack(pady=(4, 8))
        dlg._preview_ref = None

        # Breite-Slider
        sf = ctk.CTkFrame(dlg, fg_color="transparent"); sf.pack(fill="x", padx=24, pady=(4, 2))
        w_lbl = "Width:" if _LANG == "en" else "Breite:"
        ctk.CTkLabel(sf, text=w_lbl, width=60, anchor="w").pack(side="left")
        w_var = tk.IntVar(value=cur_w)
        w_display = ctk.CTkLabel(sf, text=f"{cur_w} px", width=80, anchor="e",
            font=ctk.CTkFont(size=12, weight="bold"))
        w_display.pack(side="right")

        # Bereich: 32px bis Original-Breite
        max_w = max(orig.width, 64)
        min_w = 32
        slider = ctk.CTkSlider(dlg, from_=min_w, to=max_w,
            number_of_steps=max(1, (max_w - min_w) // 2),
            variable=w_var, width=420, command=lambda v: _on_slider(v))
        slider.pack(padx=24, pady=(0, 4))
        slider.set(min(cur_w, max_w))

        # Höhe-Anzeige
        hf = ctk.CTkFrame(dlg, fg_color="transparent"); hf.pack(fill="x", padx=24, pady=(0, 6))
        h_lbl_t = "Height:" if _LANG == "en" else "Höhe:"
        ctk.CTkLabel(hf, text=h_lbl_t, width=60, anchor="w").pack(side="left")
        h_display = ctk.CTkLabel(hf, text=f"{cur_h} px", width=80, anchor="e",
            font=ctk.CTkFont(size=12))
        h_display.pack(side="right")

        # Prozent-Schnellwahl
        pf = ctk.CTkFrame(dlg, fg_color="transparent"); pf.pack(pady=(0, 6))
        for pct in [25, 50, 75, 100]:
            pw = max(min_w, int(orig.width * pct / 100))
            ctk.CTkButton(pf, text=f"{pct}%", width=55, height=28, corner_radius=6,
                fg_color=("gray80", "#353a4a"), text_color=("gray20", "gray80"),
                font=ctk.CTkFont(size=10),
                command=lambda p=pw: (slider.set(p), _on_slider(p))).pack(side="left", padx=3)

        # Checkbox: Datei in neuer Grösse speichern
        resample_var = ctk.BooleanVar(value=True)
        rs_txt = "Bilddatei in neuer Auflösung speichern\n(schärfer, angepasste Dateigrösse)" if _LANG == "de" else "Save image file at new resolution\n(sharper, adjusted file size)"
        ctk.CTkCheckBox(dlg, text=rs_txt, variable=resample_var,
            font=ctk.CTkFont(size=10), checkbox_width=18, checkbox_height=18).pack(padx=24, pady=(0, 8), anchor="w")

        def _update_preview(w):
            w = max(min_w, int(float(w)))
            h = max(1, int(w / aspect))
            w_display.configure(text=f"{w} px")
            h_display.configure(text=f"{h} px")
            preview = orig.copy()
            preview.thumbnail((min(w, 300), min(h, 200)), Image.LANCZOS)
            tk_prev = ImageTk.PhotoImage(preview)
            dlg._preview_ref = tk_prev
            preview_lbl.configure(image=tk_prev, text="")

        _update_timer = [None]
        def _on_slider(v):
            if _update_timer[0]:
                dlg.after_cancel(_update_timer[0])
            _update_timer[0] = dlg.after(50, lambda: _update_preview(v))

        _update_preview(cur_w)

        # Buttons
        bf = ctk.CTkFrame(dlg, fg_color="transparent"); bf.pack(pady=(4, 16))

        def _apply():
            new_w = max(min_w, int(w_var.get()))
            new_h = max(1, int(new_w / aspect))
            # Immer vom Original skalieren (scharf)
            new_pil = orig.resize((new_w, new_h), Image.LANCZOS)
            # Anzeige-Datei aktualisieren (Original bleibt unangetastet)
            if resample_var.get():
                new_pil.save(str(display_path), "PNG")
            # Tk-Bild ersetzen
            new_tk = ImageTk.PhotoImage(new_pil)
            info["tk"] = new_tk
            info["pil"] = new_pil
            info["width"] = new_w
            info["height"] = new_h
            # Im Text-Widget ersetzen
            try:
                pos = self.text.index(iid)
                self.text.delete(pos)
                self.text.image_create(pos, image=new_tk, name=iid)
            except tk.TclError:
                pass
            dlg.destroy()
            if resample_var.get():
                sz = display_path.stat().st_size
                sz_str = f"{sz/1024:.0f} KB" if sz < 1048576 else f"{sz/1048576:.1f} MB"
                self._status.configure(text=f"✅ {new_w}×{new_h} px, {sz_str}")
            else:
                self._status.configure(text=f"✅ {new_w}×{new_h} px")

        ok_txt = "Apply" if _LANG == "en" else "Anwenden"
        ctk.CTkButton(bf, text=ok_txt, width=120, height=34,
            font=ctk.CTkFont(size=12, weight="bold"), command=_apply).pack(side="left", padx=6)
        cancel_txt = "Cancel" if _LANG == "en" else "Abbrechen"
        ctk.CTkButton(bf, text=cancel_txt, width=100, height=34,
            fg_color=("gray75", "#353a4a"), text_color=("gray30", "gray80"),
            command=dlg.destroy).pack(side="left", padx=6)

    # ═══════ SUCHEN & ERSETZEN ═══════
    def _find_replace(self):
        dlg=ctk.CTkToplevel(self)
        dlg.title("Find & Replace" if _LANG=="en" else "Suchen & Ersetzen")
        _set_window_icon(dlg); dlg.transient(self)
        center_window(dlg, 420, 195); dlg.attributes("-topmost", True)

        # ═══ Suchzeile ═══
        fr=ctk.CTkFrame(dlg,fg_color="transparent"); fr.pack(fill="x",padx=12,pady=(12,4))
        ctk.CTkLabel(fr,text="Find:" if _LANG=="en" else "Suchen:",width=80,anchor="w").grid(row=0,column=0,padx=4,pady=4)
        find_var=ctk.StringVar()
        find_entry=ctk.CTkEntry(fr,textvariable=find_var,width=280)
        find_entry.grid(row=0,column=1,padx=4,pady=4)

        # ═══ Ersetzen-Zeile mit Checkbox ═══
        repl_enabled = ctk.BooleanVar(value=False)
        repl_var = ctk.StringVar()
        repl_row = ctk.CTkFrame(fr, fg_color="transparent")
        repl_row.grid(row=1, column=0, columnspan=2, sticky="w", padx=4, pady=4)
        repl_cb = ctk.CTkCheckBox(repl_row, text="Replace:" if _LANG=="en" else "Ersetzen:",
            variable=repl_enabled, width=80, font=ctk.CTkFont(size=12),
            checkbox_width=18, checkbox_height=18,
            command=lambda: _toggle_replace())
        repl_cb.pack(side="left")
        repl_entry = ctk.CTkEntry(repl_row, textvariable=repl_var, width=280, state="disabled",
            fg_color=("gray90","#1a1d26"))
        repl_entry.pack(side="left", padx=(8, 0))

        def _toggle_replace():
            if repl_enabled.get():
                repl_entry.configure(state="normal", fg_color=("white","#2a2e3b"))
                repl_btn.configure(state="normal"); all_btn.configure(state="normal")
            else:
                repl_entry.configure(state="disabled", fg_color=("gray90","#1a1d26"))
                repl_btn.configure(state="disabled"); all_btn.configure(state="disabled")

        # ═══ Status ═══
        status_lbl=ctk.CTkLabel(dlg,text="",font=ctk.CTkFont(size=10),text_color=("gray50","gray55"))
        status_lbl.pack()

        # ═══ Buttons ═══
        bf=ctk.CTkFrame(dlg,fg_color="transparent"); bf.pack(pady=(4,12))
        self._find_pos = "1.0"

        # Highlight-Tag
        self.text.tag_configure("find_highlight", background="#4f8ff7", foreground="white")
        self.text.tag_raise("find_highlight")

        def _clear_highlights():
            self.text.tag_remove("find_highlight", "1.0", "end")

        def _find_next(ev=None):
            term = find_var.get()
            if not term: return
            _clear_highlights()
            self.text.tag_remove("sel", "1.0", "end")
            pos = self.text.search(term, self._find_pos, stopindex="end", nocase=True)
            if pos:
                end_pos = f"{pos}+{len(term)}c"
                self.text.tag_add("find_highlight", pos, end_pos)
                self.text.tag_add("sel", pos, end_pos)
                self.text.mark_set("insert", end_pos)
                # Zum Treffer scrollen und sichtbar machen
                self.text.see(pos)
                self.text.after(50, lambda: self.text.see(pos))
                self._find_pos = end_pos
                n = "Found" if _LANG=="en" else "Gefunden"
                status_lbl.configure(text=f"✓ {n}: Ln {pos.split('.')[0]}")
            else:
                self._find_pos = "1.0"
                n = "Not found – restarting from top" if _LANG=="en" else "Nicht gefunden – Suche von oben"
                status_lbl.configure(text=f"✗ {n}")

        def _replace_one():
            if not repl_enabled.get(): return
            term=find_var.get(); repl=repl_var.get()
            try:
                s=self.text.index("sel.first"); e=self.text.index("sel.last")
                if self.text.get(s,e).lower()==term.lower():
                    self.text.delete(s,e); self.text.insert(s,repl)
            except tk.TclError: pass
            _find_next()

        def _replace_all():
            if not repl_enabled.get(): return
            term=find_var.get(); repl=repl_var.get()
            if not term: return
            _clear_highlights()
            count=0; pos="1.0"
            while True:
                pos=self.text.search(term,pos,stopindex="end",nocase=True)
                if not pos: break
                end_pos=f"{pos}+{len(term)}c"
                self.text.delete(pos,end_pos); self.text.insert(pos,repl)
                pos=f"{pos}+{len(repl)}c"; count+=1
            lbl = f"Replaced {count}" if _LANG=="en" else f"{count} ersetzt"
            status_lbl.configure(text=f"✓ {lbl}")

        def _on_close_find():
            _clear_highlights(); dlg.destroy()
        dlg.protocol("WM_DELETE_WINDOW", _on_close_find)

        find_lbl = "Find" if _LANG=="en" else "Suchen"
        repl_lbl = "Replace" if _LANG=="en" else "Ersetzen"
        all_lbl = "All" if _LANG=="en" else "Alle"
        ctk.CTkButton(bf,text=f"🔍 {find_lbl}",width=90,height=30,command=_find_next).pack(side="left",padx=3)
        repl_btn = ctk.CTkButton(bf,text=f"↔ {repl_lbl}",width=90,height=30,command=_replace_one,state="disabled")
        repl_btn.pack(side="left",padx=3)
        all_btn = ctk.CTkButton(bf,text=f"↔ {all_lbl}",width=80,height=30,command=_replace_all,state="disabled")
        all_btn.pack(side="left",padx=3)

        # Fokus auf Suchfeld + Enter-Taste
        dlg.after(100, find_entry.focus_set)
        find_entry.bind("<Return>", _find_next)

    # ═══════ RECHTSKLICK-MENÜ ═══════
    def _ctx_menu(self,ev):
        # Cursor an Klick-Position setzen
        self.text.mark_set("insert", f"@{ev.x},{ev.y}")
        m=tk.Menu(self,tearoff=0,font=("Segoe UI",10))
        m.add_command(label=_t("ctx_cut"),command=lambda:self.text.event_generate("<<Cut>>"))
        m.add_command(label=_t("ctx_copy"),command=lambda:self.text.event_generate("<<Copy>>"))
        m.add_command(label=_t("ctx_paste"),command=lambda:self.text.event_generate("<<Paste>>"))
        paste_plain_lbl = "📝  Paste as Plain Text" if _LANG=="en" else "📝  Als reinen Text einfügen"
        m.add_command(label=paste_plain_lbl,command=self._paste_plain)
        m.add_separator()
        sel_all = "Select All" if _LANG=="en" else "Alles markieren"
        m.add_command(label=sel_all,command=lambda:self.text.tag_add("sel","1.0","end"))
        m.add_separator()
        b = "B  Bold" if _LANG=="en" else "B  Fett"
        i = "I  Italic" if _LANG=="en" else "I  Kursiv"
        u = "U  Underline" if _LANG=="en" else "U  Unterstrichen"
        s = "S  Strikethrough" if _LANG=="en" else "S  Durchgestrichen"
        m.add_command(label=b,command=self._bold)
        m.add_command(label=i,command=self._italic)
        m.add_command(label=u,command=self._underline)
        m.add_command(label=s,command=self._strike)
        m.add_separator()
        fg = "A  Text Color..." if _LANG=="en" else "A  Textfarbe..."
        bg = "🖌  Highlight..." if _LANG=="en" else "🖌  Hintergrundfarbe..."
        m.add_command(label=fg,command=self._color_fg)
        m.add_command(label=bg,command=self._color_bg)
        m.add_command(label=_t("ctx_clear_fmt"),command=self._clear_fmt)
        m.add_separator()
        align_m=tk.Menu(m,tearoff=0)
        al = "Left" if _LANG=="en" else "Links"
        ac = "Center" if _LANG=="en" else "Zentriert"
        ar = "Right" if _LANG=="en" else "Rechts"
        align_m.add_command(label=al,command=self._align_left)
        align_m.add_command(label=ac,command=self._align_center)
        align_m.add_command(label=ar,command=self._align_right)
        align_lbl = "Alignment" if _LANG=="en" else "Ausrichtung"
        m.add_cascade(label=align_lbl,menu=align_m)
        list_m=tk.Menu(m,tearoff=0)
        bl = "• Bullets" if _LANG=="en" else "• Aufzählung"
        nl = "1. Numbered" if _LANG=="en" else "1. Nummerierung"
        list_m.add_command(label=bl,command=self._list_bullet)
        list_m.add_command(label=nl,command=self._list_number)
        list_lbl = "List" if _LANG=="en" else "Liste"
        m.add_cascade(label=list_lbl,menu=list_m)
        ind = "→  Indent" if _LANG=="en" else "→  Einrücken"
        oud = "←  Outdent" if _LANG=="en" else "←  Ausrücken"
        m.add_command(label=ind,command=self._indent)
        m.add_command(label=oud,command=self._outdent)
        m.add_separator()
        m.add_command(label=_t("ctx_ins_link"),command=self._ins_link)
        # "Link bearbeiten" nur anzeigen wenn Cursor auf einem Link steht
        cursor_on_link = any(tag in self._link_urls for tag in self.text.tag_names("insert"))
        if cursor_on_link:
            edit_link_lbl = "✏️  Edit Link..." if _LANG=="en" else "✏️  Link bearbeiten..."
            m.add_command(label=edit_link_lbl,command=self._edit_link)
        m.add_command(label=_t("ctx_ins_img"),command=self._ins_img)
        # Bild skalieren - nur wenn Cursor auf einem Bild steht
        img_at_cursor = self._find_image_at_pos("insert")
        if img_at_cursor:
            scale_lbl = "📐  Scale Image..." if _LANG=="en" else "📐  Bild skalieren..."
            m.add_command(label=scale_lbl, command=lambda iid=img_at_cursor: self._scale_image(iid))
        m.add_separator()
        m.add_command(label=_t("ctx_print"),command=self._print)
        m.post(ev.x_root,ev.y_root)

    # ═══════ STATUS-LEISTE ═══════
    def _update_status(self,ev=None):
        try:
            idx=self.text.index("insert")
            tags=[t for t in self.text.tag_names(idx) if t not in ("sel","find_highlight")]
            parts=[]
            # Bold/Italic aus fs_-Tags erkennen
            is_bold = False; is_italic = False; fs_family = ""; fs_size = 0
            for t in tags:
                if t.startswith("fs_"):
                    p = t.split("_")
                    if len(p) >= 4:
                        fs_family = p[1].replace("~"," ")
                        try: fs_size = int(p[2])
                        except: pass
                        style = p[3]
                        is_bold = "b" in style
                        is_italic = "i" in style
                # Alte Tags auch erkennen (Kompatibilität)
                if t in ("bold","bold_italic"): is_bold = True
                if t in ("italic","bold_italic"): is_italic = True
            if is_bold: parts.append("Bold")
            if is_italic: parts.append("Italic")
            if fs_family: parts.append(fs_family)
            if fs_size: parts.append(f"{fs_size}pt")
            for t in tags:
                if t in ("underline","strike","superscript","subscript",
                         "h1","h2","align_left","align_center","align_right"):
                    parts.append(t.replace("_"," ").title())
                elif t.startswith("clr_"):
                    lbl = "Color" if _LANG=="en" else "Farbe"
                    parts.append(f"{lbl}:{t[4:]}")
                elif t.startswith("bg_"):
                    lbl = "Bg" if _LANG=="en" else "Hg"
                    parts.append(f"{lbl}:{t[3:]}")
                elif t.startswith("indent_"):
                    lbl = "Indent" if _LANG=="en" else "Einzug"
                    parts.append(f"{lbl}:{t[7:]}")
            ln,col=idx.split(".")
            total_chars = len(self.text.get("1.0", "end-1c"))
            ln_lbl = "Line" if _LANG=="en" else "Zeile"
            col_lbl = "Col" if _LANG=="en" else "Spalte"
            char_lbl = "Chars" if _LANG=="en" else "Zeichen"
            status=f"{ln_lbl} {ln}, {col_lbl} {col}  |  {total_chars} {char_lbl}"
            if parts: status+=f"  |  {', '.join(parts)}"
            self._status.configure(text=status)
            # Toolbar-Buttons hervorheben
            if "B" in self._fmt_btns:
                self._fmt_btns["B"].configure(fg_color=("#c0d8f0","#4a5a7a") if is_bold else "transparent")
            if "I" in self._fmt_btns:
                self._fmt_btns["I"].configure(fg_color=("#c0d8f0","#4a5a7a") if is_italic else "transparent")
            active_tags=set(tags)
            for txt,tag_list in [("U",("underline",)),("S",("strike",)),
                            ("x²",("superscript",)),("x₂",("subscript",)),
                            ("H1",("h1",)),("H2",("h2",))]:
                if txt in self._fmt_btns:
                    btn=self._fmt_btns[txt]
                    if any(t in active_tags for t in tag_list):
                        btn.configure(fg_color=("#c0d8f0","#4a5a7a"))
                    else:
                        btn.configure(fg_color="transparent")
        except Exception: pass

    # ═══════ DRUCKEN ═══════
    def _text_to_html(self):
        """Konvertiert den formatierten Text-Widget-Inhalt in HTML mit Bildern."""
        html_parts = []
        tw = self.text
        idx = "1.0"
        end = tw.index("end-1c")
        prev_tags = set()
        open_spans = []

        while tw.compare(idx, "<", end):
            has_img = False
            for iid, info in self._images.items():
                try:
                    img_idx = tw.index(iid)
                    if img_idx == idx:
                        img_path = NOTE_IMG_DIR / info["file"]
                        if img_path.exists():
                            import base64 as b64mod
                            with open(str(img_path), "rb") as imgf:
                                b64 = b64mod.b64encode(imgf.read()).decode()
                            ext = img_path.suffix.lower().strip(".")
                            if ext == "jpg": ext = "jpeg"
                            html_parts.append(f'<img src="data:image/{ext};base64,{b64}" style="max-width:100%;">')
                        has_img = True; break
                except tk.TclError: pass

            if has_img: idx = tw.index(f"{idx}+1c"); continue
            ch = tw.get(idx, f"{idx}+1c")
            cur_tags = set(t for t in tw.tag_names(idx) if t != "sel")

            if cur_tags != prev_tags:
                for _ in open_spans: html_parts.append("</span>")
                open_spans.clear()
                styles = []
                for t in cur_tags:
                    if t.startswith("fs_"):
                        p = t.split("_")
                        if len(p) >= 4:
                            fam = p[1].replace("~"," ")
                            styles.append(f"font-family:'{fam}'")
                            try: styles.append(f"font-size:{int(p[2])}pt")
                            except: pass
                            st = p[3]
                            if "b" in st: styles.append("font-weight:bold")
                            if "i" in st: styles.append("font-style:italic")
                    elif t in ("bold","bold_italic"): styles.append("font-weight:bold")
                    elif t in ("italic","bold_italic"): styles.append("font-style:italic")
                    elif t == "underline": styles.append("text-decoration:underline")
                    elif t == "strike": styles.append("text-decoration:line-through")
                    elif t == "superscript": styles.append("vertical-align:super;font-size:0.8em")
                    elif t == "subscript": styles.append("vertical-align:sub;font-size:0.8em")
                    elif t in ("h1","h1_italic"): styles.append("font-size:24pt;font-weight:bold")
                    elif t in ("h2","h2_italic"): styles.append("font-size:18pt;font-weight:bold")
                    elif t.startswith("clr_"): styles.append(f"color:{t[4:]}")
                    elif t.startswith("bg_"): styles.append(f"background-color:{t[3:]}")
                    elif t.startswith("font_"): styles.append(f"font-family:'{t[5:].replace('_',' ')}'")
                    elif t.startswith("sz_"): styles.append(f"font-size:{t[3:]}pt")
                    elif t == "link": styles.append("color:#4f8ff7;text-decoration:underline")
                if styles:
                    html_parts.append(f'<span style="{";".join(styles)}">')
                    open_spans.append(True)
            prev_tags = cur_tags
            if ch == "\n": html_parts.append("<br>")
            elif ch == "<": html_parts.append("&lt;")
            elif ch == ">": html_parts.append("&gt;")
            elif ch == "&": html_parts.append("&amp;")
            else: html_parts.append(ch)
            idx = tw.index(f"{idx}+1c")
        for _ in open_spans: html_parts.append("</span>")
        raw_html = "".join(html_parts)
        lines = raw_html.split("<br>")
        final_lines = []
        for i, line in enumerate(lines):
            line_idx = f"{i+1}.0"
            try: tags = tw.tag_names(line_idx)
            except: tags = ()
            bstyle = ""
            for t in tags:
                if t == "align_center": bstyle += "text-align:center;"
                elif t == "align_right": bstyle += "text-align:right;"
                elif t.startswith("indent_"): bstyle += f"margin-left:{int(t.split('_')[1])*40}px;"
            if bstyle: final_lines.append(f'<div style="{bstyle}">{line}</div>')
            else: final_lines.append(line + "<br>")
        return "\n".join(final_lines)

    def _print(self):
        import tempfile
        title = self.title_var.get().strip() or "Notiz"
        body_html = self._text_to_html()
        html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>{title}</title>
<style>
body {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 12pt; margin: 2cm;
       line-height: 1.6; color: #1a1a1a; }}
img {{ max-width: 100%; height: auto; margin: 8px 0; }}
table {{ border-collapse: collapse; margin: 1em 0; }}
td, th {{ border: 1px solid #ccc; padding: 6px 12px; }}
th {{ background-color: #e8eef8; }}
@media print {{ body {{ margin: 1.5cm; }} }}
</style></head><body>
<h1>{title}</h1>
{body_html}
<script>window.onload=function(){{window.print()}}</script></body></html>"""
        tmp = os.path.join(tempfile.gettempdir(), "docvault_print.html")
        with open(tmp, "w", encoding="utf-8") as f: f.write(html)
        if platform.system() == "Windows":
            try: os.startfile(tmp)
            except OSError: import webbrowser; webbrowser.open(tmp)
        else: subprocess.Popen(["xdg-open", tmp])

    # ═══════ SERIALISIERUNG ═══════
    def _serialize(self):
        content = self.text.get("1.0", "end-1c")
        tag_data=[]; tag_cfgs={}
        for tag in self.text.tag_names():
            if tag in ("sel",): continue
            ranges=self.text.tag_ranges(tag)
            for i in range(0,len(ranges),2):
                tag_data.append({"tag":tag,"start":str(ranges[i]),"end":str(ranges[i+1])})
            if any(tag.startswith(p) for p in ("clr_","bg_","lnk_","font_","sz_","indent_","fs_")):
                cfg={}
                for prop in ("foreground","background","underline","overstrike","font",
                             "offset","justify","lmargin1","lmargin2"):
                    try:
                        v=self.text.tag_cget(tag,prop)
                        if v: cfg[prop]=v
                    except Exception: pass
                if cfg: tag_cfgs[tag]=cfg
        img_data=[]
        for iid,info in self._images.items():
            try: pos=self.text.index(iid); img_data.append({"id":iid,"file":info["file"],"pos":pos})
            except tk.TclError: pass
        return json.dumps({"text":content,"tags":tag_data,"tag_configs":tag_cfgs,
            "images":img_data,"links":self._link_urls},ensure_ascii=False)

    def _load(self,doc):
        self.title_var.set(doc.get("original_name","Notiz"))
        nd=doc.get("note_data","")
        if nd:
            try: self._restore(json.loads(nd)); return
            except Exception: pass
        content=doc.get("ocr_text","") or doc.get("notes","")
        if content: self.text.insert("1.0",content)

    def _restore(self,nd):
        self.text.insert("1.0",nd.get("text",""))
        # Bilder wiederherstellen
        for img in sorted(nd.get("images",[]),key=lambda x:x["pos"],reverse=True):
            ip=NOTE_IMG_DIR/img["file"]
            if ip.exists():
                try:
                    display_pil=Image.open(str(ip))
                    # Original laden (separate Datei)
                    iid=img["id"]
                    orig_path = NOTE_IMG_DIR / f"{iid}_orig.png"
                    if orig_path.exists():
                        orig_pil = Image.open(str(orig_path))
                    else:
                        orig_pil = display_pil.copy()
                        # Nachträglich Original-Datei anlegen
                        orig_pil.save(str(orig_path), "PNG")
                    tk_img=ImageTk.PhotoImage(display_pil)
                    self._images[iid]={"tk":tk_img,"file":img["file"],
                                       "pil":display_pil,"orig_pil":orig_pil,
                                       "width":display_pil.width,"height":display_pil.height}
                    try: self.text.image_create(img["pos"],image=tk_img,name=iid)
                    except tk.TclError: self.text.image_create("end",image=tk_img,name=iid)
                except Exception: pass
        # Tag-Konfigurationen wiederherstellen
        for tag,cfg in nd.get("tag_configs",{}).items(): self.text.tag_configure(tag,**cfg)
        for td in nd.get("tags",[]):
            if td["tag"]=="sel": continue
            try: self.text.tag_add(td["tag"],td["start"],td["end"])
            except tk.TclError: pass
        self._link_urls=nd.get("links",{})

    def _save(self):
        title=self.title_var.get().strip() or ("Untitled Note" if _LANG=="en" else "Unbenannte Notiz")
        content=self.text.get("1.0","end-1c").strip()
        if not content:
            msg = "Note is empty." if _LANG=="en" else "Notiz ist leer."
            messagebox.showwarning("DocVault", msg); return
        try:
            nd_json=self._serialize()
            ts=datetime.now().strftime("%Y%m%d_%H%M%S")
            fn=f"notiz_{ts}.txt"
            fp=DOCS_DIR/fn
            fp.write_text(content,encoding="utf-8")
            ch=hashlib.sha256(f"{content}_{ts}_{uuid.uuid4().hex[:8]}".encode()).hexdigest()
            if self.edit_doc:
                did=self.edit_doc["id"]
                conn=sqlite3.connect(str(DB_PATH),timeout=10)
                conn.execute("UPDATE documents SET original_name=?,ocr_text=?,note_data=?,file_path=?,file_hash=?,updated_at=CURRENT_TIMESTAMP WHERE id=?",
                    (title,content,nd_json,str(fp),ch,did))
                conn.commit(); conn.close()
                index_document(did,f"{title} Notiz {content}")
                logger.info("Notiz aktualisiert: #%d '%s'", did, title)
            else:
                conn=sqlite3.connect(str(DB_PATH),timeout=10)
                cat = "Note" if _LANG=="en" else "Notiz"
                cur=conn.execute("INSERT INTO documents (filename,original_name,file_path,file_size,file_hash,mime_type,source,category,processed,ocr_text,note_data) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (fn,title,str(fp),len(content.encode()),ch,"text/plain","note",cat,1,content,nd_json))
                did=cur.lastrowid; conn.commit(); conn.close()
                index_document(did,f"{title} Notiz {content}")
                logger.info("Notiz gespeichert: #%d '%s'", did, title)
                # Ab jetzt ist es ein bestehendes Dokument (Update statt Insert)
                self.edit_doc = {"id": did, "original_name": title}
        except Exception as e:
            logger.error("Notiz speichern: %s", e)
            msg = f"Could not save note:\n{e}" if _LANG=="en" else f"Notiz konnte nicht gespeichert werden:\n{e}"
            messagebox.showerror("Error" if _LANG=="en" else "Fehler", msg); return
        # Status anzeigen statt schliessen
        saved_msg = "✅ Saved" if _LANG=="en" else "✅ Gespeichert"
        self._status.configure(text=f"{saved_msg}: {title}")
        # Liste im Hauptfenster aktualisieren
        if self.on_save_cb:
            try: self.on_save_cb()
            except Exception: pass

# ═══════ KATEGORIEN-MANAGER ═══════
class CatMgr(ctk.CTkToplevel):
    def __init__(self,master,on_change=None):
        super().__init__(master)
        self.title(f"DocVault v{VERSION} – {_t('catmgr_title')}"); self.transient(master)
        _set_window_icon(self)
        self.on_change=on_change; self._cfg=load_ini()
        restore_geometry(self._cfg,"cat_mgr",self,"600x550")
        self._build(); self.protocol("WM_DELETE_WINDOW",self._close)
    def _close(self): save_geometry(self._cfg,"cat_mgr",self); self.destroy()
    def _build(self):
        ctk.CTkLabel(self,text=_t("catmgr_title"),font=ctk.CTkFont(size=18,weight="bold")).pack(padx=16,pady=(16,4),anchor="w")
        ctk.CTkLabel(self,text=_t("catmgr_hint"),
            font=ctk.CTkFont(size=11),text_color=("gray50","gray55")).pack(padx=16,anchor="w")
        self.sc=ctk.CTkScrollableFrame(self,fg_color="transparent"); self.sc.pack(fill="both",expand=True,padx=12,pady=4)
        bf=ctk.CTkFrame(self,fg_color="transparent"); bf.pack(fill="x",padx=16,pady=(4,16))
        ctk.CTkButton(bf,text=_t("catmgr_new"),width=180,command=lambda:self._edit_dlg(None,None)).pack(side="left")
        self._refresh()
    def _refresh(self):
        for w in self.sc.winfo_children(): w.destroy()
        self._render_mgr_tree(None, 0)
    def _render_mgr_tree(self, parent_id, depth):
        """Rekursiv: Kategorien im Manager rendern mit beliebiger Tiefe."""
        cats = get_categories(parent_id=parent_id)
        for i, cat in enumerate(cats):
            indent = depth * 20
            f = ctk.CTkFrame(self.sc, corner_radius=8,
                fg_color=("white", "#21242f") if depth == 0 else ("#f5f5ff", "#1a1d27"), height=34)
            f.pack(fill="x", pady=1, padx=(indent, 0)); f.pack_propagate(False)
            prefix = "  ↳ " * min(depth, 1) if depth > 0 else ""
            ctk.CTkLabel(f, text=f"{prefix}{cat['icon']} {cat['name']}",
                font=ctk.CTkFont(size=12 if depth == 0 else 11,
                weight="bold" if depth == 0 else "normal")).pack(side="left", padx=8)
            # Sortierung innerhalb Geschwister
            if i > 0:
                ctk.CTkButton(f, text="▲", width=26, height=22, fg_color="transparent",
                    text_color=("gray50", "gray60"), hover_color=("gray90", "#353a4a"),
                    command=lambda c=cat, idx=i: self._move(c, idx, -1, depth > 0)).pack(side="right", padx=1)
            if i < len(cats) - 1:
                ctk.CTkButton(f, text="▼", width=26, height=22, fg_color="transparent",
                    text_color=("gray50", "gray60"), hover_color=("gray90", "#353a4a"),
                    command=lambda c=cat, idx=i: self._move(c, idx, 1, depth > 0)).pack(side="right", padx=1)
            if cat["name"] not in ("Dokument", "Notiz"):
                ctk.CTkButton(f, text="🗑️", width=26, height=22, fg_color="transparent",
                    text_color=("gray50", "gray60"), hover_color=("gray90", "#353a4a"),
                    command=lambda c=cat: self._del(c)).pack(side="right", padx=1)
            ctk.CTkButton(f, text="✏️", width=26, height=22, fg_color="transparent",
                text_color=("gray50", "gray60"), hover_color=("gray90", "#353a4a"),
                command=lambda c=cat: self._edit_dlg(c, cat.get("parent_id"))).pack(side="right", padx=1)
            # + Unterkategorie
            ctk.CTkButton(f, text="＋", width=26, height=22, fg_color="transparent",
                text_color=("gray50", "gray60"), hover_color=("gray90", "#353a4a"),
                command=lambda c=cat: self._edit_dlg(None, c["id"])).pack(side="right", padx=1)
            # Kinder rekursiv
            self._render_mgr_tree(cat["id"], depth + 1)
    def _move(self,cat,idx,direction,is_sub):
        pid=cat.get("parent_id")
        siblings=get_categories(parent_id=pid)
        new_idx=idx+direction
        if new_idx<0 or new_idx>=len(siblings): return
        other=siblings[new_idx]
        with get_db() as c:
            c.execute("UPDATE categories SET sort_order=? WHERE id=?",(other["sort_order"],cat["id"]))
            c.execute("UPDATE categories SET sort_order=? WHERE id=?",(cat["sort_order"],other["id"]))
        self._refresh()
        if self.on_change: self.on_change()
    def _edit_dlg(self,cat,parent_id):
        dlg=ctk.CTkToplevel(self); dlg.title("Kategorie"); dlg.transient(self); dlg.grab_set()
        center_window(dlg,460,350)
        ctk.CTkLabel(dlg,text="Name",font=ctk.CTkFont(size=11,weight="bold")).pack(anchor="w",padx=16,pady=(16,2))
        nv=ctk.StringVar(value=cat["name"] if cat else ""); ctk.CTkEntry(dlg,textvariable=nv).pack(fill="x",padx=16)
        ctk.CTkLabel(dlg,text="Icon",font=ctk.CTkFont(size=11,weight="bold")).pack(anchor="w",padx=16,pady=(8,2))
        iv=ctk.StringVar(value=cat["icon"] if cat else "📄"); ctk.CTkEntry(dlg,textvariable=iv,width=80).pack(anchor="w",padx=16)
        # Übergeordnete Kategorie – alle Kategorien ausser sich selbst + Nachfahren
        ctk.CTkLabel(dlg,text="Übergeordnet",font=ctk.CTkFont(size=11,weight="bold")).pack(anchor="w",padx=16,pady=(8,2))
        # Alle Kategorien flach laden und Nachfahren ausschliessen
        all_cats=get_all_categories()
        def get_descendants(cid):
            """Gibt IDs aller Nachfahren zurück."""
            result=set()
            for c in all_cats:
                if c.get("parent_id")==cid:
                    result.add(c["id"]); result|=get_descendants(c["id"])
            return result
        exclude_ids=set()
        if cat: exclude_ids={cat["id"]}|get_descendants(cat["id"])
        # Hierarchische Liste aufbauen
        parent_opts=["(Hauptkategorie)"]
        parent_map={}  # label → id
        def add_opts(pid, depth):
            for c in all_cats:
                if c.get("parent_id")==pid and c["id"] not in exclude_ids:
                    prefix="  " * depth
                    label=f"{prefix}{c['icon']} {c['name']}"
                    parent_opts.append(label); parent_map[label]=c["id"]
                    add_opts(c["id"], depth+1)
        add_opts(None, 0)
        pv=ctk.StringVar(value="(Hauptkategorie)")
        if parent_id:
            for label,cid in parent_map.items():
                if cid==parent_id: pv.set(label); break
        ctk.CTkOptionMenu(dlg,values=parent_opts,variable=pv,width=300).pack(anchor="w",padx=16)
        ctk.CTkLabel(dlg,text=_t("keywords_comma"),font=ctk.CTkFont(size=11,weight="bold")).pack(anchor="w",padx=16,pady=(8,2))
        kb=ctk.CTkTextbox(dlg,height=50); kb.pack(fill="x",padx=16)
        if cat: kb.insert("1.0",cat.get("keywords",""))
        def save():
            n=nv.get().strip(); ic=iv.get().strip() or "📄"; kws=kb.get("1.0","end-1c").strip()
            if not n: return
            sel=pv.get(); pid=parent_map.get(sel)  # None für Hauptkategorie
            with get_db() as c:
                if cat:
                    c.execute("UPDATE categories SET name=?,icon=?,keywords=?,parent_id=? WHERE id=?",(n,ic,kws,pid,cat["id"]))
                    if n!=cat["name"]: c.execute("UPDATE documents SET category=? WHERE category=?",(n,cat["name"]))
                else: c.execute("INSERT INTO categories (name,icon,keywords,sort_order,parent_id) VALUES (?,?,?,?,?)",(n,ic,kws,999,pid))
            dlg.destroy(); self._refresh()
            if self.on_change: self.on_change()
        ctk.CTkButton(dlg,text=_t("catmgr_save"),command=save).pack(pady=12)
    def _del(self,cat):
        with get_db() as c:
            cnt=c.execute("SELECT COUNT(*) FROM documents WHERE category=?",(cat["name"],)).fetchone()[0]
            sub_cnt=c.execute("SELECT COUNT(*) FROM categories WHERE parent_id=?",(cat["id"],)).fetchone()[0]
        msg=f"'{cat['name']}' löschen?"
        if cnt: msg+=f"\n{cnt} Dok. werden auf 'Dokument' umgestellt."
        if sub_cnt: msg+=f"\n{sub_cnt} Unterkategorie(n) werden zu Hauptkategorien."
        if not messagebox.askyesno("Löschen",msg): return
        with get_db() as c:
            c.execute("UPDATE documents SET category='Dokument' WHERE category=?",(cat["name"],))
            c.execute("UPDATE categories SET parent_id=NULL WHERE parent_id=?",(cat["id"],))
            c.execute("DELETE FROM categories WHERE id=?",(cat["id"],))
        self._refresh()
        if self.on_change: self.on_change()

# ═══════ DISCLAIMER & SPENDEN-DIALOG ═══════
DISCLAIMER_TEXT_DE = """NUTZUNGSBEDINGUNGEN / HAFTUNGSAUSSCHLUSS

DocVault wird von der CADTEC GmbH entwickelt und bereitgestellt.

CADTEC GmbH
Chlupfwiesstrasse 31
CH-8165 Zürich-Oberweningen
Schweiz

Tel: +41 (0)44 585 30 31
Web: www.cadtec.ch
Frage stellen: https://www.cad-schweiz.ch/FRAGE-ANTWORT/
Quellcode: https://github.com/cadcam-etik/DocVault

HAFTUNGSAUSSCHLUSS:
DocVault wird „wie besehen" ohne jegliche Gewährleistung bereitgestellt. \
Die Nutzung erfolgt auf eigenes Risiko. CADTEC GmbH haftet nicht \
für Datenverlust, Schäden oder Folgeschäden, die durch die Nutzung dieses \
Programms entstehen.

Der Benutzer ist selbst dafür verantwortlich, regelmässige Backups seiner \
Dokumente und Daten zu erstellen.

LIZENZ / SPENDE:
DocVault darf kostenlos genutzt werden. Für professionellen Einsatz und \
Support empfehlen wir uns eine angemessende Spende zukommen zu lassen.

Spenden-Link:
https://www.cadtec.ch/Quick-Bestellung/cla/index.php?search=docvault

© CADTEC GmbH – Alle Rechte vorbehalten."""

DISCLAIMER_TEXT_EN = """TERMS OF USE / DISCLAIMER

DocVault is developed and provided by CADTEC GmbH.

CADTEC GmbH
Chlupfwiesstrasse 31
CH-8165 Zürich-Oberweningen
Switzerland

Phone: +41 (0)44 585 30 31
Web: www.cadtec.ch
Ask a question: https://www.cad-schweiz.ch/FRAGE-ANTWORT/
Source code: https://github.com/cadcam-etik/DocVault

DISCLAIMER:
DocVault is provided "as is" without any warranty. Use at your own risk. \
CADTEC GmbH is not liable for any data loss, damages or \
consequential damages arising from the use of this program.

The user is solely responsible for creating regular backups of their \
documents and data.

LICENSE / DONATION:
DocVault may be used free of charge. For professional use and support, \
we recommend making an appropriate donation.

Donation link:
https://www.cadtec.ch/Quick-Bestellung/cla/index.php?search=docvault

© CADTEC GmbH – All rights reserved."""

SHOP_URL = "https://www.cadtec.ch/Quick-Bestellung/cla/product.php?id=prod_69afd68e21778_1773131406"
DONATE_URL = "https://www.cadtec.ch/Quick-Bestellung/cla/index.php?search=docvault"

def _show_about(parent):
    """Zeigt Info-Dialog mit Disclaimer und Spendenhinweis."""
    dlg = ctk.CTkToplevel(parent)
    dlg.title(f"DocVault v{VERSION}")
    _set_window_icon(dlg)
    dlg.transient(parent); dlg.grab_set()
    center_window(dlg, 560, 560)

    # ═══ Header ═══
    hdr = ctk.CTkFrame(dlg, fg_color="transparent")
    hdr.pack(fill="x", padx=20, pady=(16, 4))
    try:
        _about_img = _get_icon_image(48)
        _about_ctk = ctk.CTkImage(light_image=_about_img, dark_image=_about_img, size=(48, 48))
        dlg._about_icon_ref = _about_ctk
        ctk.CTkLabel(hdr, text="", image=_about_ctk, width=48).pack(side="left", padx=(0, 12))
    except Exception:
        pass
    info_fr = ctk.CTkFrame(hdr, fg_color="transparent")
    info_fr.pack(side="left")
    ctk.CTkLabel(info_fr, text="DocVault", font=ctk.CTkFont(size=26, weight="bold")).pack(anchor="w")
    ctk.CTkLabel(info_fr, text=f"Version {VERSION}",
        font=ctk.CTkFont(size=12), text_color=("gray50", "gray55")).pack(anchor="w")
    mode = "EXE" if getattr(sys, 'frozen', False) else "Python"
    lic_text = "Free"
    if _is_licensed():
        exp = _get_license_expiry(load_local().get("license_key", ""))
        if exp:
            lic_text = f"Licensed · {exp.strftime('%d.%m.%Y')}"
        else:
            lic_text = "Licensed"
    ctk.CTkLabel(info_fr, text=f"{mode} · {lic_text}" +
        (" · PyMuPDF" if HAS_FITZ else ""),
        font=ctk.CTkFont(size=10), text_color=("gray50", "gray55")).pack(anchor="w")

    # ═══ Disclaimer Text ═══
    txt = DISCLAIMER_TEXT_DE if _LANG == "de" else DISCLAIMER_TEXT_EN
    tb = ctk.CTkTextbox(dlg, height=280, font=ctk.CTkFont(size=11), corner_radius=8,
        fg_color=("gray95", "#171921"))
    tb.pack(fill="both", expand=True, padx=16, pady=(8, 6))
    tb.insert("1.0", txt); tb.configure(state="disabled")

    # ═══ Spendenhinweis ═══
    donate_fr = ctk.CTkFrame(dlg, corner_radius=10, fg_color=("#fff8ee", "#2a2518"))
    donate_fr.pack(fill="x", padx=16, pady=(4, 8))
    donate_lbl = "❤️ DocVault ist spendenfinanziert – bitte unterstützen Sie uns!" if _LANG == "de" else \
                 "❤️ DocVault is donation-funded – please support us!"
    ctk.CTkLabel(donate_fr, text=donate_lbl,
        font=ctk.CTkFont(size=12, weight="bold"),
        text_color=("#d63031", "#e74c3c")).pack(padx=12, pady=(8, 2))
    ctk.CTkLabel(donate_fr, text=DONATE_URL,
        font=ctk.CTkFont(size=10), text_color=("gray50", "gray55")).pack(padx=12, pady=(0, 4))
    donate_btn_text = "🌐 Spenden-Seite öffnen" if _LANG == "de" else "🌐 Open Donation Page"
    ctk.CTkButton(donate_fr, text=donate_btn_text, width=200, height=30,
        font=ctk.CTkFont(size=11),
        command=lambda: __import__('webbrowser').open(DONATE_URL)).pack(pady=(2, 8))

    # ═══ Schliessen ═══
    close_text = "Schliessen" if _LANG == "de" else "Close"
    ctk.CTkButton(dlg, text=close_text, width=120, height=34,
        command=dlg.destroy).pack(pady=(0, 12))


def _show_disclaimer_view(parent):
    """Zeigt den Disclaimer-Text als lesbaren Dialog (nicht der Erststart-Dialog)."""
    dlg = ctk.CTkToplevel(parent)
    ttl = "Nutzungsbedingungen / Haftungsausschluss" if _LANG == "de" else "Terms of Use / Disclaimer"
    dlg.title(ttl)
    _set_window_icon(dlg)
    dlg.transient(parent); dlg.grab_set()
    center_window(dlg, 580, 500)

    ctk.CTkLabel(dlg, text="📜 " + ttl,
        font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(16, 8))

    txt = DISCLAIMER_TEXT_DE if _LANG == "de" else DISCLAIMER_TEXT_EN
    tb = ctk.CTkTextbox(dlg, font=ctk.CTkFont(size=11), corner_radius=8,
        fg_color=("gray95", "#171921"))
    tb.pack(fill="both", expand=True, padx=16, pady=(4, 8))
    tb.insert("1.0", txt); tb.configure(state="disabled")

    close_text = "Schliessen" if _LANG == "de" else "Close"
    ctk.CTkButton(dlg, text=close_text, width=120, height=34,
        command=dlg.destroy).pack(pady=(0, 14))


def _show_whats_new(parent):
    """Zeigt die WHATS_NEW.md Datei als lesbaren Dialog."""
    dlg = ctk.CTkToplevel(parent)
    dlg.title(f"DocVault v{VERSION} – What's New")
    _set_window_icon(dlg)
    dlg.transient(parent); dlg.grab_set()
    center_window(dlg, 640, 560)

    ctk.CTkLabel(dlg, text="🆕 What's New",
        font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(16, 4))
    ctk.CTkLabel(dlg, text=f"DocVault v{VERSION}",
        font=ctk.CTkFont(size=11), text_color=("gray50", "gray55")).pack(pady=(0, 8))

    # tk.Text statt CTkTextbox (CTkTextbox verbietet font in tag_config)
    tf = ctk.CTkFrame(dlg, corner_radius=8, fg_color=("gray95", "#171921"))
    tf.pack(fill="both", expand=True, padx=16, pady=(4, 8))
    tb = tk.Text(tf, wrap="word", font=("Consolas", 11), bg="#f5f5f5", fg="#1a1a1a",
        relief="flat", padx=14, pady=10, highlightthickness=0, borderwidth=0)
    sb = ctk.CTkScrollbar(tf, command=tb.yview); tb.configure(yscrollcommand=sb.set)
    sb.pack(side="right", fill="y", padx=(0,2), pady=2)
    tb.pack(fill="both", expand=True, padx=2, pady=2)

    # WHATS_NEW.md laden
    content = ""
    for base in [BASE_DIR, Path(__file__).resolve().parent if not getattr(sys, 'frozen', False) else BASE_DIR]:
        wn_path = base / "WHATS_NEW.md"
        if wn_path.exists():
            try: content = wn_path.read_text(encoding="utf-8")
            except Exception: content = wn_path.read_text(encoding="latin-1")
            break
    if not content:
        content = "WHATS_NEW.md not found.\n\nExpected location:\n" + str(BASE_DIR / "WHATS_NEW.md")

    # Tags für Markdown-Rendering
    tb.tag_configure("h1", font=("Segoe UI", 17, "bold"), spacing1=6, spacing3=4)
    tb.tag_configure("h2", font=("Segoe UI", 14, "bold"), foreground="#2563eb", spacing1=8, spacing3=2)
    tb.tag_configure("h3", font=("Segoe UI", 12, "bold"), spacing1=4, spacing3=2)
    tb.tag_configure("bold_text", font=("Consolas", 11, "bold"))
    tb.tag_configure("hr", foreground="#bbbbbb", font=("Consolas", 6), spacing1=4, spacing3=4)
    tb.tag_configure("bullet", lmargin1=16, lmargin2=28)

    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.startswith("## "):
            tb.insert("end", stripped[3:] + "\n", "h2")
        elif stripped.startswith("### "):
            tb.insert("end", stripped[4:] + "\n", "h3")
        elif stripped.startswith("# "):
            tb.insert("end", stripped[2:] + "\n", "h1")
        elif stripped == "---":
            tb.insert("end", "─" * 70 + "\n", "hr")
        elif stripped.startswith("- **") and "**" in stripped[4:]:
            bold_end = stripped.index("**", 4)
            bold_part = stripped[4:bold_end]
            rest = stripped[bold_end+2:]
            start = tb.index("end-1c")
            tb.insert("end", "  • ")
            tb.insert("end", bold_part, "bold_text")
            tb.insert("end", rest + "\n")
            tb.tag_add("bullet", start, "end-1c")
        elif stripped.startswith("- "):
            start = tb.index("end-1c")
            tb.insert("end", "  • " + stripped[2:] + "\n")
            tb.tag_add("bullet", start, "end-1c")
        else:
            tb.insert("end", line + "\n")

    tb.configure(state="disabled")

    close_text = "Schliessen" if _LANG == "de" else "Close"
    ctk.CTkButton(dlg, text=close_text, width=120, height=34,
        command=dlg.destroy).pack(pady=(0, 14))


_OSS_LICENSES_DE = """══════════════════════════════════════════════════════
  Open-Source-Lizenzen & Quellen
  DocVault verwendet die folgenden Open-Source-Komponenten
══════════════════════════════════════════════════════

── PyMuPDF (fitz/pymupdf) ──────────────────────────
  Beschreibung: PDF-Rendering, Text-Extraktion, Thumbnails
  Lizenz:       GNU Affero General Public License v3.0 (AGPL-3.0)
  Autor:        Artifex Software, Inc.
  Quelle:       https://github.com/pymupdf/PyMuPDF
  Hinweis:      AGPL erfordert, dass der Quellcode dieser Anwendung
                verfügbar gemacht wird. DocVault wird als
                spendenbasierte Open-Source-Software veröffentlicht.
                Quellcode: https://github.com/cadcam-etik/DocVault

── CustomTkinter ───────────────────────────────────
  Beschreibung: Moderne GUI-Bibliothek basierend auf Tkinter
  Lizenz:       MIT License
  Autor:        Tom Schimansky
  Quelle:       https://github.com/TomSchimansky/CustomTkinter

── pdfplumber ──────────────────────────────────────
  Beschreibung: PDF-Textextraktion und Tabellenanalyse
  Lizenz:       MIT License
  Autor:        Jeremy Singer-Vine
  Quelle:       https://github.com/jsvine/pdfplumber

── Pillow (PIL) ────────────────────────────────────
  Beschreibung: Bildverarbeitung (Thumbnails, Konvertierung, Skalierung)
  Lizenz:       HPND License (Historical Permission Notice and Disclaimer)
  Autor:        Jeffrey A. Clark (Alex) und Mitwirkende
  Quelle:       https://github.com/python-pillow/Pillow

── python-docx ─────────────────────────────────────
  Beschreibung: DOCX-Vorschau und Textextraktion
  Lizenz:       MIT License
  Autor:        Steve Canny
  Quelle:       https://github.com/python-openxml/python-docx

── openpyxl ────────────────────────────────────────
  Beschreibung: Excel-Datei-Vorschau (XLSX)
  Lizenz:       MIT License
  Autor:        Eric Gazoni, Charlie Clark
  Quelle:       https://github.com/theorchard/openpyxl

── lxml ────────────────────────────────────────────
  Beschreibung: XML/HTML-Verarbeitung
  Lizenz:       BSD License (3-Clause)
  Autor:        lxml Projekt
  Quelle:       https://github.com/lxml/lxml

── windnd ──────────────────────────────────────────
  Beschreibung: Drag & Drop Unterstützung für Windows
  Lizenz:       MIT License
  Autor:        nicegist
  Quelle:       https://github.com/nicegist/windnd

── Python ──────────────────────────────────────────
  Beschreibung: Programmiersprache und Standardbibliothek
  Lizenz:       PSF License (Python Software Foundation License)
  Quelle:       https://www.python.org

── Tkinter / Tcl/Tk ────────────────────────────────
  Beschreibung: GUI-Toolkit (Basis von CustomTkinter)
  Lizenz:       Tcl/Tk License (BSD-ähnlich)
  Quelle:       https://www.tcl.tk

── SQLite ──────────────────────────────────────────
  Beschreibung: Eingebettete Datenbank
  Lizenz:       Public Domain (gemeinfrei)
  Quelle:       https://www.sqlite.org

── PyInstaller ─────────────────────────────────────
  Beschreibung: EXE-Erstellung für Windows
  Lizenz:       GPL v2 mit Bootloader-Ausnahme
  Hinweis:      Die Bootloader-Ausnahme erlaubt die Verteilung
                von nicht-GPL-Anwendungen als EXE.
  Quelle:       https://github.com/pyinstaller/pyinstaller

── NAPS2 (Not Another PDF Scanner 2) ──────────────
  Beschreibung: Scanner-Software für Dokumentenerfassung und OCR
  Lizenz:       GNU General Public License v2.0 (oder später)
  Autor:        Ben Olden-Cooligan
  Quelle:       https://github.com/cyanfish/naps2
  Website:      https://www.naps2.com
  Hinweis:      NAPS2 wird als separates Programm mitgeliefert
                und von DocVault als externer Prozess aufgerufen.

══════════════════════════════════════════════════════
  DocVault © CADTEC GmbH – www.cadtec.ch
  Vertrieb auf freiwilliger Spendenbasis.
  Quellcode: https://github.com/cadcam-etik/DocVault
══════════════════════════════════════════════════════"""

_OSS_LICENSES_EN = """══════════════════════════════════════════════════════
  Open Source Licenses & Sources
  DocVault uses the following open source components
══════════════════════════════════════════════════════

── PyMuPDF (fitz/pymupdf) ──────────────────────────
  Description: PDF rendering, text extraction, thumbnails
  License:     GNU Affero General Public License v3.0 (AGPL-3.0)
  Author:      Artifex Software, Inc.
  Source:      https://github.com/pymupdf/PyMuPDF
  Note:        AGPL requires that the source code of this
               application is made available. DocVault is
               published as donation-based open source software.
               Source: https://github.com/cadcam-etik/DocVault

── CustomTkinter ───────────────────────────────────
  Description: Modern GUI library based on Tkinter
  License:     MIT License
  Author:      Tom Schimansky
  Source:      https://github.com/TomSchimansky/CustomTkinter

── pdfplumber ──────────────────────────────────────
  Description: PDF text extraction and table analysis
  License:     MIT License
  Author:      Jeremy Singer-Vine
  Source:      https://github.com/jsvine/pdfplumber

── Pillow (PIL) ────────────────────────────────────
  Description: Image processing (thumbnails, conversion, scaling)
  License:     HPND License (Historical Permission Notice and Disclaimer)
  Author:      Jeffrey A. Clark (Alex) and contributors
  Source:      https://github.com/python-pillow/Pillow

── python-docx ─────────────────────────────────────
  Description: DOCX preview and text extraction
  License:     MIT License
  Author:      Steve Canny
  Source:      https://github.com/python-openxml/python-docx

── openpyxl ────────────────────────────────────────
  Description: Excel file preview (XLSX)
  License:     MIT License
  Author:      Eric Gazoni, Charlie Clark
  Source:      https://github.com/theorchard/openpyxl

── lxml ────────────────────────────────────────────
  Description: XML/HTML processing
  License:     BSD License (3-Clause)
  Author:      lxml project
  Source:      https://github.com/lxml/lxml

── windnd ──────────────────────────────────────────
  Description: Drag & drop support for Windows
  License:     MIT License
  Author:      nicegist
  Source:      https://github.com/nicegist/windnd

── Python ──────────────────────────────────────────
  Description: Programming language and standard library
  License:     PSF License (Python Software Foundation License)
  Source:      https://www.python.org

── Tkinter / Tcl/Tk ────────────────────────────────
  Description: GUI toolkit (base of CustomTkinter)
  License:     Tcl/Tk License (BSD-like)
  Source:      https://www.tcl.tk

── SQLite ──────────────────────────────────────────
  Description: Embedded database
  License:     Public Domain
  Source:      https://www.sqlite.org

── PyInstaller ─────────────────────────────────────
  Description: EXE creation for Windows
  License:     GPL v2 with Bootloader Exception
  Note:        The bootloader exception permits distribution
               of non-GPL applications as EXE files.
  Source:      https://github.com/pyinstaller/pyinstaller

── NAPS2 (Not Another PDF Scanner 2) ──────────────
  Description: Scanner software for document capture and OCR
  License:     GNU General Public License v2.0 (or later)
  Author:      Ben Olden-Cooligan
  Source:      https://github.com/cyanfish/naps2
  Website:     https://www.naps2.com
  Note:        NAPS2 is bundled as a separate program and
               called by DocVault as an external process.

══════════════════════════════════════════════════════
  DocVault © CADTEC GmbH – www.cadtec.ch
  Distributed on a voluntary donation basis.
  Source code: https://github.com/cadcam-etik/DocVault
══════════════════════════════════════════════════════"""


def _show_licenses(parent):
    """Zeigt alle Open-Source-Lizenzen in einem separaten Fenster."""
    dlg = ctk.CTkToplevel(parent)
    ttl = "Open-Source-Lizenzen & Quellen" if _LANG == "de" else "Open Source Licenses & Sources"
    dlg.title(ttl)
    _set_window_icon(dlg)
    dlg.transient(parent); dlg.grab_set()
    center_window(dlg, 680, 580)

    ctk.CTkLabel(dlg, text="⚖️ " + ttl,
        font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(16, 4))
    ctk.CTkLabel(dlg, text=f"DocVault v{VERSION}",
        font=ctk.CTkFont(size=11), text_color=("gray50", "gray55")).pack(pady=(0, 8))

    tf = ctk.CTkFrame(dlg, corner_radius=8, fg_color=("gray95", "#171921"))
    tf.pack(fill="both", expand=True, padx=16, pady=(4, 8))
    tb = tk.Text(tf, wrap="word", font=("Consolas", 10), bg="#f5f5f5", fg="#1a1a1a",
        relief="flat", padx=14, pady=10, highlightthickness=0, borderwidth=0)
    sb = ctk.CTkScrollbar(tf, command=tb.yview); tb.configure(yscrollcommand=sb.set)
    sb.pack(side="right", fill="y", padx=(0, 2), pady=2)
    tb.pack(fill="both", expand=True, padx=2, pady=2)

    # Tags für Hervorhebung
    tb.tag_configure("header", font=("Consolas", 10, "bold"), foreground="#2563eb")
    tb.tag_configure("license", font=("Consolas", 10, "bold"), foreground="#d35400")
    tb.tag_configure("agpl", font=("Consolas", 10, "bold"), foreground="#e74c3c",
        background="#fff5f5")

    content = _OSS_LICENSES_DE if _LANG == "de" else _OSS_LICENSES_EN
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.startswith("── ") and stripped.endswith("──"):
            tb.insert("end", line + "\n", "header")
        elif "AGPL" in line and ("Lizenz:" in line or "License:" in line):
            tb.insert("end", line + "\n", "agpl")
        elif "Lizenz:" in stripped or "License:" in stripped:
            tb.insert("end", line + "\n", "license")
        elif stripped.startswith("══"):
            tb.insert("end", line + "\n", "header")
        else:
            tb.insert("end", line + "\n")

    tb.configure(state="disabled")

    close_text = "Schliessen" if _LANG == "de" else "Close"
    ctk.CTkButton(dlg, text=close_text, width=120, height=34,
        command=dlg.destroy).pack(pady=(0, 14))


def _show_disclaimer(parent):
    """Zeigt Disclaimer beim allerersten Start. Muss bestätigt werden."""
    dlg = ctk.CTkToplevel(parent)
    dlg.title(_t("disclaimer_title"))
    _set_window_icon(dlg)
    dlg.transient(parent); dlg.grab_set()
    center_window(dlg, 620, 520)
    dlg.protocol("WM_DELETE_WINDOW", lambda: None)  # Nicht schliessbar

    ctk.CTkLabel(dlg, text="DocVault", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(16, 4))
    ctk.CTkLabel(dlg, text=f"Version {VERSION}", font=ctk.CTkFont(size=12),
        text_color=("gray50", "gray55")).pack()

    txt = DISCLAIMER_TEXT_DE if _LANG == "de" else DISCLAIMER_TEXT_EN
    tb = ctk.CTkTextbox(dlg, height=340, font=ctk.CTkFont(size=11), corner_radius=8,
        fg_color=("gray95", "#171921"))
    tb.pack(fill="both", expand=True, padx=16, pady=(12, 8))
    tb.insert("1.0", txt); tb.configure(state="disabled")

    accepted = [False]
    def _accept():
        accepted[0] = True
        dlg.destroy()

    ctk.CTkButton(dlg, text=_t("disclaimer_btn"), width=250, height=40,
        font=ctk.CTkFont(size=14, weight="bold"), command=_accept).pack(pady=(4, 16))

    parent.wait_window(dlg)
    return accepted[0]


def _show_donation_dialog(parent):
    """Zeigt Spendenhinweis beim Beenden (unlizenziert). 15s Countdown."""
    dlg = ctk.CTkToplevel(parent)
    dlg.title(_t("donate_title"))
    _set_window_icon(dlg)
    dlg.transient(parent)
    center_window(dlg, 540, 470)
    dlg.protocol("WM_DELETE_WINDOW", lambda: None)  # Während Countdown nicht schliessbar

    ctk.CTkLabel(dlg, text="❤️ DocVault", font=ctk.CTkFont(size=22, weight="bold"),
        text_color=("#d63031", "#e74c3c")).pack(pady=(16, 8))

    tb = ctk.CTkTextbox(dlg, height=200, font=ctk.CTkFont(size=12), corner_radius=8,
        fg_color=("gray95", "#171921"))
    tb.pack(fill="both", expand=True, padx=16, pady=(4, 4))
    tb.insert("1.0", _t("donate_text")); tb.configure(state="disabled")

    # Sponsoring-Button
    sponsor_txt = "❤️ Sponsoringbeitrag geben..." if _LANG=="de" else "❤️ Make a sponsorship contribution..."
    ctk.CTkButton(dlg, text=sponsor_txt, width=300, height=36,
        font=ctk.CTkFont(size=13, weight="bold"), cursor="hand2",
        fg_color=("#2e86c1", "#2e86c1"), hover_color=("#2471a3", "#2471a3"),
        command=lambda: __import__('webbrowser').open(DONATE_URL)).pack(pady=(0, 8))

    btn_var = [None]
    countdown = [15]

    def _update():
        if countdown[0] > 0:
            if btn_var[0]:
                btn_var[0].configure(text=_t("donate_close_in").format(s=countdown[0]),
                    state="disabled")
            countdown[0] -= 1
            dlg.after(1000, _update)
        else:
            if btn_var[0]:
                btn_var[0].configure(text=_t("donate_close"), state="normal")
            dlg.protocol("WM_DELETE_WINDOW", _close)

    def _close():
        dlg.destroy()
        # Shop-Seite öffnen
        try:
            import webbrowser
            webbrowser.open(SHOP_URL)
        except Exception: pass

    btn = ctk.CTkButton(dlg, text=_t("donate_close_in").format(s=15), width=200, height=38,
        font=ctk.CTkFont(size=13), state="disabled", command=_close)
    btn.pack(pady=(4, 16))
    btn_var[0] = btn

    dlg.after(1000, _update)
    parent.wait_window(dlg)


# ═══════ HAUPTFENSTER ═══════
class DocVaultApp(ctk.CTk):
    def __init__(self, search_query=None):
        super().__init__()
        # ═══ Sprache erkennen / setzen ═══
        _lc_temp = load_local()
        saved_lang = _lc_temp.get("language", "")
        if saved_lang in ("de", "en"):
            _set_language(saved_lang)
        else:
            _set_language(_detect_language())

        self.title(f"DocVault v{VERSION}")
        _set_window_icon(self)
        ctk.set_default_color_theme("blue")
        # ═══ Settings: LOKAL (pro PC) + GEMEINSAM (DATA_DIR) ═══
        self._sp=DATA_DIR/"settings.json"   # Gemeinsame Settings
        self._s=self._load_s()              # Gemeinsam: ocr_lang, link_only
        self._lc=load_local()               # Lokal: appearance, scanner, fenster
        ctk.set_appearance_mode(self._lc.get("appearance","dark"))
        self._cfg=load_ini(); restore_geometry(self._cfg,"main",self,"1320x850")

        # ═══ Disclaimer beim allerersten Start ═══
        if not self._lc.get("disclaimer_accepted"):
            self.update()  # Fenster kurz anzeigen
            if _show_disclaimer(self):
                self._lc["disclaimer_accepted"] = True
                self._lc["disclaimer_date"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                save_local(self._lc)
            else:
                os._exit(0)  # Nicht akzeptiert → Programm beenden

        self.current_cat=""; self.current_star=False; self.search_aid=None; self._hist_aid=None
        self._missing_link_ids = set()
        self._suppress_search=False
        self._page_size=self._lc.get("page_size",10)
        self._page=0
        self._preview_doc=None
        self._preview_page=0
        self._sort=self._lc.get("sort","date_desc")
        self.import_link=tk.IntVar(value=1 if self._s.get("link_only") else 0)
        self._tc={}; self.sel_ids=set(); self.last_click_idx=None; self._doc_list=[]
        self._cards={}; self._dbl_timer=None
        self._licensed = _is_licensed()
        self._build(); self.refresh_list(); self.refresh_stats()
        set_ocr_lang(self._s.get("ocr_lang","deu"))
        self.protocol("WM_DELETE_WINDOW",self._quit)
        # Suchbegriff von Kommandozeile setzen
        if search_query:
            self.after(200, lambda: self._apply_search_query(search_query))

    def _apply_search_query(self, query):
        """Setzt einen Suchbegriff (z.B. von der Kommandozeile)."""
        self._suppress_search = True
        self.sv.set(query)
        self._suppress_search = False
        self.lhdr.configure(text=f"{_t('search_prefix')} {query}")
        self._page = 0
        self.refresh_list()
        self.title(f"DocVault v{VERSION} – Suche: {query}")
    def _quit(self):
        try: save_geometry(self._cfg,"main",self)
        except Exception: pass
        # ═══ Spendenhinweis für unlizenzierte Versionen ═══
        if not self._licensed:
            try:
                _show_donation_dialog(self)
            except Exception: pass
        # Datenbank optimieren (VACUUM)
        try:
            import time; t0=time.time()
            with get_db() as c: c.execute("VACUUM")
            logger.info("DB VACUUM: %.1f ms", (time.time()-t0)*1000)
        except Exception as e:
            logger.warning("DB VACUUM: %s", e)
        # Alle after-Callbacks abbrechen
        try:
            for aid in self.tk.call('after','info'):
                try: self.after_cancel(aid)
                except Exception: pass
        except Exception: pass
        # Destroy mit Fehlerbehandlung (customtkinter/Thonny-Kompatibilität)
        try: self.quit()
        except Exception: pass
        try: self.destroy()
        except Exception: pass
        # Falls alles fehlschlägt, hart beenden
        os._exit(0)
    def _load_s(self):
        """Lädt GEMEINSAME Settings (DATA_DIR – für alle PCs gleich)."""
        try:
            if self._sp.exists(): return json.loads(self._sp.read_text(encoding="utf-8"))
        except Exception: pass
        return {"link_only":True,"ocr_lang":"deu"}
    def _save_s(self):
        """Speichert GEMEINSAME Settings."""
        try: self._sp.write_text(json.dumps(self._s,indent=2),encoding="utf-8")
        except Exception: pass
    def _save_lc(self):
        """Speichert LOKALE Settings (pro PC, neben EXE/Skript)."""
        global _local
        _local = self._lc
        save_local(self._lc)
    def _build(self):
        sb_w=self._lc.get("sidebar_width",260)
        self.grid_columnconfigure(0,weight=0,minsize=sb_w)
        self.grid_columnconfigure(1,weight=1); self.grid_rowconfigure(0,weight=1)
        self._sb=ctk.CTkFrame(self,corner_radius=0,fg_color=("#e8e8e8","#1a1d27"))
        self._sb.grid(row=0,column=0,sticky="nsew")
        # Sidebar Resize-Handle (rechter Rand)
        handle=ctk.CTkFrame(self._sb,width=5,fg_color=("gray75","#2a2e3b"),cursor="sb_h_double_arrow")
        handle.pack(side="right",fill="y")
        handle.bind("<B1-Motion>",self._resize_sidebar)
        handle.bind("<Enter>",lambda e:handle.configure(fg_color=("#4f8ff7","#4f8ff7")))
        handle.bind("<Leave>",lambda e:handle.configure(fg_color=("gray75","#2a2e3b")))
        logo=ctk.CTkFrame(self._sb,fg_color="transparent",cursor="hand2"); logo.pack(fill="x",padx=16,pady=(16,4))
        logo.bind("<Button-1>", lambda e: _show_about(self))
        # Icon im Sidebar-Logo (eingebettet)
        try:
            _logo_img = _get_icon_image(32)
            self._logo_ctk = ctk.CTkImage(light_image=_logo_img, dark_image=_logo_img, size=(32, 32))
            logo_row=ctk.CTkFrame(logo,fg_color="transparent",cursor="hand2"); logo_row.pack(anchor="w")
            logo_row.bind("<Button-1>", lambda e: _show_about(self))
            _icon_lbl=ctk.CTkLabel(logo_row,text="",image=self._logo_ctk,width=32)
            _icon_lbl.pack(side="left",padx=(0,8))
            _icon_lbl.bind("<Button-1>", lambda e: _show_about(self))
            _text_lbl=ctk.CTkLabel(logo_row,text="DocVault",font=ctk.CTkFont(size=22,weight="bold"))
            _text_lbl.pack(side="left")
            _text_lbl.bind("<Button-1>", lambda e: _show_about(self))
        except Exception:
            _fb_lbl=ctk.CTkLabel(logo,text="📄 DocVault",font=ctk.CTkFont(size=22,weight="bold"))
            _fb_lbl.pack(anchor="w")
            _fb_lbl.bind("<Button-1>", lambda e: _show_about(self))
        _ver_lbl=ctk.CTkLabel(logo,text=f"v{VERSION}",font=ctk.CTkFont(size=11),text_color=("gray50","gray60"),cursor="hand2")
        _ver_lbl.pack(anchor="w")
        _ver_lbl.bind("<Button-1>", lambda e: _show_about(self))
        # ═══ Info-Buttons: Disclaimer + What's New ═══
        info_btns=ctk.CTkFrame(logo,fg_color="transparent"); info_btns.pack(anchor="w",pady=(4,0))
        _bs_info={"height":24,"corner_radius":6,"font":ctk.CTkFont(size=10),
            "fg_color":("gray82","#2a3040"),"hover_color":("gray75","#353f55"),
            "text_color":("gray40","gray70")}
        disc_txt="📜 Disclaimer" if _LANG=="en" else "📜 Nutzungsbedingungen"
        ctk.CTkButton(info_btns,text=disc_txt,width=130,command=lambda:_show_disclaimer_view(self),
            **_bs_info).pack(side="left",padx=(0,4))
        ctk.CTkButton(info_btns,text="🆕 What's New",width=100,command=lambda:_show_whats_new(self),
            **_bs_info).pack(side="left")
        # Zweite Zeile: Lizenzen
        info_btns2=ctk.CTkFrame(logo,fg_color="transparent"); info_btns2.pack(anchor="w",pady=(2,0))
        ctk.CTkButton(info_btns2,text=_t("nav_licenses"),width=210,command=lambda:_show_licenses(self),
            **_bs_info).pack(side="left")
        # Lizenz-Ablaufdatum in der Sidebar
        if self._licensed:
            _lic_exp = _get_license_expiry(self._lc.get("license_key",""))
            if _lic_exp:
                _lic_txt = _t("sett_license_expiry").format(date=_lic_exp.strftime("%d.%m.%Y"))
                ctk.CTkLabel(logo, text=_lic_txt, font=ctk.CTkFont(size=9),
                    text_color=("#27ae60","#2ecc71")).pack(anchor="w", pady=(2,0))
        ctk.CTkFrame(self._sb,height=1,fg_color=("gray75","#2a2e3b")).pack(fill="x",padx=16,pady=(10,6))
        for key,tkey in [("backup","nav_backup"),("upload","nav_import"),
                          ("notes","nav_note"),("scanner","nav_scanner"),
                          ("settings","nav_settings")]:
            btn=ctk.CTkButton(self._sb,text=_t(tkey),anchor="w",font=ctk.CTkFont(size=13),
                fg_color="transparent",text_color=("gray20","gray80"),hover_color=("gray80","#282c3a"),
                height=34,corner_radius=8,command=lambda k=key:self._nav(k))
            btn.pack(fill="x",padx=8,pady=1)
        # Sync-Button (alle Dokumente prüfen)
        sync_btn=ctk.CTkButton(self._sb,text=_t("nav_sync"),anchor="w",font=ctk.CTkFont(size=12),
            fg_color="transparent",text_color=("gray20","gray80"),hover_color=("gray80","#282c3a"),
            height=30,corner_radius=8,command=self._sync_docs)
        sync_btn.pack(fill="x",padx=8,pady=(4,1))
        ctk.CTkFrame(self._sb,height=1,fg_color=("gray75","#2a2e3b")).pack(fill="x",padx=16,pady=(8,4))
        ctk.CTkLabel(self._sb,text=_t("cat_header"),font=ctk.CTkFont(size=10,weight="bold"),
            text_color=("gray50","gray55")).pack(anchor="w",padx=20,pady=(2,2))
        self.cat_sc=ctk.CTkScrollableFrame(self._sb,fg_color="transparent")
        self.cat_sc.pack(fill="both",expand=True,padx=8); self._rebuild_cats()
        # Kategorien verwalten
        ctk.CTkButton(self._sb,text=_t("catmgr_manage"),anchor="w",font=ctk.CTkFont(size=11),
            fg_color="transparent",text_color=("gray50","gray60"),hover_color=("gray80","#282c3a"),
            height=26,corner_radius=6,command=lambda:self._nav("catmgr")).pack(fill="x",padx=8,pady=(2,4))
        self.stat_lbl=ctk.CTkLabel(self._sb,text="",font=ctk.CTkFont(size=11),text_color=("gray50","gray55"))
        self.stat_lbl.pack(side="bottom",padx=16,pady=(4,14))
        mf=ctk.CTkFrame(self._sb,fg_color="transparent"); mf.pack(side="bottom",fill="x",padx=16,pady=(0,4))
        ctk.CTkLabel(mf,text="☀️",font=ctk.CTkFont(size=13)).pack(side="left")
        self.msw=ctk.CTkSwitch(mf,text="",width=40,onvalue="dark",offvalue="light",command=self._tog_app)
        if self._lc.get("appearance","dark")=="dark": self.msw.select()
        else: self.msw.deselect()
        self.msw.pack(side="right")
        self.mlbl=ctk.CTkLabel(mf,text=_t("mode_dark") if self._lc.get("appearance","dark")=="dark" else _t("mode_light"),
            font=ctk.CTkFont(size=11),text_color=("gray50","gray55"))
        self.mlbl.pack(side="right",padx=(0,6))
        # Main
        main=ctk.CTkFrame(self,corner_radius=0,fg_color=("gray95","#0f1117"))
        main.grid(row=0,column=1,sticky="nsew"); main.grid_columnconfigure(0,weight=1); main.grid_rowconfigure(1,weight=1)
        bar=ctk.CTkFrame(main,height=56,corner_radius=0,fg_color=("white","#1a1d27"))
        bar.grid(row=0,column=0,sticky="ew"); bar.grid_columnconfigure(1,weight=1)
        ctk.CTkButton(bar,text=_t("nav_backup"),width=90,height=38,
            font=ctk.CTkFont(size=13),fg_color=("gray80","#353a4a"),text_color=("gray20","gray80"),
            hover_color=("gray70","#454a5a"),command=self._do_backup).grid(row=0,column=0,padx=(16,8),pady=9)
        self.sv=ctk.StringVar(); self.sv.trace_add("write",self._on_search)
        sf=ctk.CTkFrame(bar,fg_color="transparent"); sf.grid(row=0,column=1,sticky="ew",padx=4,pady=9)
        sf.grid_columnconfigure(0,weight=1)
        self._search_entry=ctk.CTkEntry(sf,placeholder_text=_t("search_placeholder"),
            textvariable=self.sv,font=ctk.CTkFont(size=14),height=38,corner_radius=10,
            border_color=("gray75","#2a2e3b"))
        self._search_entry.grid(row=0,column=0,sticky="ew")
        self._search_entry.bind("<Return>",lambda e:self._save_search_term())
        self._search_clear=ctk.CTkButton(sf,text="✕",width=32,height=32,corner_radius=8,
            fg_color="transparent",hover_color=("gray80","#353a4a"),
            text_color=("gray50","gray60"),font=ctk.CTkFont(size=14),
            command=lambda:self.sv.set(""))
        self._search_clear.grid(row=0,column=1,padx=(2,0))
        self._search_hist_btn=ctk.CTkButton(sf,text="▾",width=32,height=32,corner_radius=8,
            fg_color="transparent",hover_color=("gray80","#353a4a"),
            text_color=("gray50","gray60"),font=ctk.CTkFont(size=14),
            command=self._show_search_history)
        self._search_hist_btn.grid(row=0,column=2,padx=(0,2))
        self._search_history=self._lc.get("search_history",[])
        ctk.CTkButton(bar,text=_t("nav_import"),width=90,height=38,command=lambda:self._nav("upload")
        ).grid(row=0,column=2,padx=4,pady=9)
        ctk.CTkButton(bar,text="✏️ Notiz",width=80,height=38,fg_color=("gray75","#353a4a"),
            text_color=("gray20","gray80"),command=lambda:self._open_note()
        ).grid(row=0,column=3,padx=(4,16),pady=9)
        self.content=ctk.CTkFrame(main,fg_color="transparent")
        self.content.grid(row=1,column=0,sticky="nsew")
        self.content.grid_columnconfigure(0,weight=1); self.content.grid_rowconfigure(0,weight=1)
        self._build_list(); self._build_import(); self._build_scanner(); self._build_settings()
        self._restore_scan_settings()  # Gespeicherte Scanner-Einstellungen laden
        self._show("list")
    def _rebuild_cats(self):
        for w in self.cat_sc.winfo_children(): w.destroy()
        # Dokumentzahlen laden
        cat_counts={}; total=0; starred=0; uncategorized=0
        try:
            with get_db() as c:
                for row in c.execute("SELECT category, COUNT(*) as cnt FROM documents WHERE archived=0 GROUP BY category"):
                    cat_counts[row["category"]]=row["cnt"]
                total=c.execute("SELECT COUNT(*) FROM documents WHERE archived=0").fetchone()[0]
                starred=c.execute("SELECT COUNT(*) FROM documents WHERE archived=0 AND starred=1").fetchone()[0]
                uncategorized=c.execute("SELECT COUNT(*) FROM documents WHERE archived=0 AND (category IS NULL OR category='' OR category='Dokument')").fetchone()[0]
        except Exception: pass
        if not hasattr(self,"_excluded_cats"): self._excluded_cats=set(self._lc.get("excluded_cats",[]))
        # Expand-State laden (Dict: cat_id → bool)
        if not hasattr(self,"_tree_expanded"):
            self._tree_expanded=set(self._lc.get("tree_expanded",[]))

        # ═══ Alle Dokumente + Favoriten (immer sichtbar) ═══
        ctk.CTkButton(self.cat_sc,text=f"📁  {_t('all_docs')} ({total})",anchor="w",
            font=ctk.CTkFont(size=12,weight="bold"),fg_color="transparent",text_color=("gray20","gray80"),
            hover_color=("gray80","#282c3a"),height=30,corner_radius=8,
            command=lambda:self._nav("all")).pack(fill="x")
        ctk.CTkButton(self.cat_sc,text=f"⭐  {_t('favorites')} ({starred})",anchor="w",
            font=ctk.CTkFont(size=12),fg_color="transparent",text_color=("gray30","gray75"),
            hover_color=("gray80","#282c3a"),height=28,corner_radius=8,
            command=lambda:self._nav("starred")).pack(fill="x")
        ctk.CTkFrame(self.cat_sc,height=1,fg_color=("gray80","#2a2e3b")).pack(fill="x",padx=4,pady=3)

        # ═══ Rekursiver Kategoriebaum ═══
        self._render_cat_tree(None, 0, cat_counts)

        # ═══ Ohne Kategorie ═══
        ctk.CTkFrame(self.cat_sc,height=1,fg_color=("gray80","#2a2e3b")).pack(fill="x",padx=4,pady=3)
        ctk.CTkButton(self.cat_sc,text=f"❓  {_t('catmgr_no_cat')[2:]} ({uncategorized})",anchor="w",
            font=ctk.CTkFont(size=11),fg_color="transparent",text_color=("gray50","gray60"),
            hover_color=("gray80","#282c3a"),height=26,corner_radius=8,
            command=self._filt_uncategorized).pack(fill="x")

    def _render_cat_tree(self, parent_id, depth, cat_counts):
        """Rendert Kategorien rekursiv als Baum mit beliebiger Tiefe."""
        cats = get_categories(parent_id=parent_id)
        for cat in cats:
            cid = str(cat["id"])
            cnt = cat_counts.get(cat["name"], 0)
            children = get_categories(parent_id=cat["id"])
            has_children = len(children) > 0
            is_expanded = cid in self._tree_expanded
            is_excluded = cat["name"] in self._excluded_cats
            indent = depth * 16  # Pixel pro Ebene

            # Zeile: [▸/▾] [Icon Name (cnt)] [👁]
            f = ctk.CTkFrame(self.cat_sc, fg_color="transparent", height=26 if depth > 0 else 28)
            f.pack(fill="x", padx=(indent, 0)); f.pack_propagate(False)

            # Expand/Collapse Toggle
            if has_children:
                arrow = "−" if is_expanded else "+"
                ctk.CTkButton(f, text=arrow, width=22, height=22,
                    font=ctk.CTkFont(size=14, weight="bold"), fg_color=("gray85","#2a2e3b"),
                    text_color=("gray30", "gray70"), hover_color=("gray75", "#3a3f4f"),
                    corner_radius=4,
                    command=lambda c=cid: self._tree_toggle(c)).pack(side="left", padx=(0,2))
            else:
                # Platzhalter für Ausrichtung
                ctk.CTkFrame(f, width=20, fg_color="transparent").pack(side="left")

            # Kategorie-Name (auch Drop-Target für DnD)
            font_size = 12 if depth == 0 else 11
            font_weight = "bold" if depth == 0 else "normal"
            tc = ("gray30", "gray75") if depth == 0 else ("gray45", "gray60")
            cat_btn=ctk.CTkButton(f, text=f"{cat['icon']}  {cat['name']} ({cnt})", anchor="w",
                font=ctk.CTkFont(size=font_size, weight=font_weight),
                fg_color="transparent", text_color=tc,
                hover_color=("gray80", "#282c3a"), height=26 if depth > 0 else 28,
                corner_radius=6,
                command=lambda c=cat["name"]: self._filt_cat(c))
            cat_btn.pack(side="left", fill="x", expand=True)
            # Drop-Target: wenn Maus hier losgelassen wird während Drag aktiv
            cat_btn.bind("<ButtonRelease-1>",lambda e,c=cat["name"]:self._cat_drop(c),add="+")
            cat_btn.configure(cursor="hand2")

            # Ausschluss-Toggle (nur Hauptkategorien)
            if depth == 0:
                eye = "👁" if not is_excluded else "🚫"
                ctk.CTkButton(f, text=eye, width=22, height=20, font=ctk.CTkFont(size=9),
                    fg_color="transparent", hover_color=("gray85", "#353a4a"),
                    text_color=("gray50", "gray55") if not is_excluded else ("red", "#ef4444"),
                    command=lambda c=cat["name"]: self._toggle_cat_exclude(c)).pack(side="right", padx=(0, 2))

            # Kinder rekursiv rendern (nur wenn aufgeklappt)
            if has_children and is_expanded:
                self._render_cat_tree(cat["id"], depth + 1, cat_counts)

    def _tree_toggle(self, cat_id):
        """Klappt eine Kategorie im Baum auf/zu und speichert den Zustand."""
        if cat_id in self._tree_expanded:
            self._tree_expanded.discard(cat_id)
        else:
            self._tree_expanded.add(cat_id)
        self._lc["tree_expanded"] = list(self._tree_expanded)
        self._save_lc()
        self._rebuild_cats()

    def _toggle_cat_exclude(self,cat_name):
        """Kategorie aus/einschliessen bei 'Alle Dokumente'."""
        if not hasattr(self,"_excluded_cats"): self._excluded_cats=set()
        if cat_name in self._excluded_cats:
            self._excluded_cats.discard(cat_name)
        else:
            self._excluded_cats.add(cat_name)
        self._lc["excluded_cats"]=list(self._excluded_cats)
        self._save_lc()
        self._rebuild_cats()
        if not self.current_cat and not self.current_star:
            self.refresh_list()  # "Alle Dokumente" aktualisieren

    def _filt_uncategorized(self):
        self._suppress_search=True; self.sv.set(""); self._suppress_search=False
        self.current_cat="__uncategorized__"; self.current_star=False; self._page=0
        self.lhdr.configure(text=_t("catmgr_no_cat"))
        self._show("list"); self.refresh_list()
    def _tog_app(self):
        m=self.msw.get(); ctk.set_appearance_mode(m); self._lc["appearance"]=m
        self._save_lc()
        self.mlbl.configure(text=_t("mode_dark") if m=="dark" else _t("mode_light"))
    def _resize_sidebar(self,ev):
        """Sidebar-Breite per Drag ändern."""
        new_w=max(180,min(500,ev.x_root-self.winfo_rootx()))
        self.grid_columnconfigure(0,minsize=new_w)
        self._lc["sidebar_width"]=new_w
        # Verzögertes Speichern (nicht bei jedem Pixel)
        if hasattr(self,"_sb_save_aid") and self._sb_save_aid:
            self.after_cancel(self._sb_save_aid)
        self._sb_save_aid=self.after(500,self._save_lc)
    def _resize_preview(self,ev):
        """Vorschau-Breite per Drag ändern."""
        split_right=self._split.winfo_rootx()+self._split.winfo_width()
        new_w=max(200,min(700,split_right-ev.x_root))
        self._split.grid_columnconfigure(1,minsize=new_w)
        self._preview_fr.configure(width=new_w)
        self._lc["preview_width"]=new_w
        if hasattr(self,"_pv_save_aid") and self._pv_save_aid:
            self.after_cancel(self._pv_save_aid)
        self._pv_save_aid=self.after(500,self._save_lc)
    def _build_list(self):
        self.lp=ctk.CTkFrame(self.content,fg_color="transparent")
        # Header (nur Titel + Untertitel)
        self.lhdr=ctk.CTkLabel(self.lp,text=_t("all_docs"),font=ctk.CTkFont(size=20,weight="bold"),anchor="w")
        self.lhdr.pack(fill="x",padx=20,pady=(12,0))
        self.lsub=ctk.CTkLabel(self.lp,text="",font=ctk.CTkFont(size=12),text_color=("gray50","gray55"),anchor="w")
        self.lsub.pack(fill="x",padx=20,pady=(0,4))
        # Split: Liste links + Vorschau rechts
        self._split=ctk.CTkFrame(self.lp,fg_color="transparent")
        self._split.pack(fill="both",expand=True,padx=12,pady=(0,4))
        self._split.grid_columnconfigure(0,weight=1)
        self._split.grid_rowconfigure(0,weight=1)
        left=ctk.CTkFrame(self._split,fg_color="transparent")
        left.grid(row=0,column=0,sticky="nsew",padx=(0,4))
        # ═══ Sortierung direkt über der Liste ═══
        sort_bar=ctk.CTkFrame(left,fg_color="transparent",height=28)
        sort_bar.pack(fill="x",pady=(2,2))
        sort_opts=[_t("sort_date_desc"),_t("sort_date_asc"),_t("sort_size_desc"),_t("sort_size_asc"),_t("sort_pages_desc"),_t("sort_pages_asc"),_t("sort_name_az"),_t("sort_name_za"),_t("sort_star"),_t("sort_updated")]
        sort_keys=["date_desc","date_asc","size_desc","size_asc","pages_desc","pages_asc","name_asc","name_desc","star_desc","updated_desc"]
        self._sort_map=dict(zip(sort_opts,sort_keys))
        self._sort_rmap=dict(zip(sort_keys,sort_opts))
        ctk.CTkLabel(sort_bar,text=_t("sort_label"),font=ctk.CTkFont(size=10),
            text_color=("gray50","gray55")).pack(side="left",padx=(4,4))
        self._sort_om=ctk.CTkOptionMenu(sort_bar,values=sort_opts,width=140,height=24,
            font=ctk.CTkFont(size=10),fg_color=("gray85","#353a4a"),
            text_color=("gray10","gray90"),dropdown_text_color=("gray10","gray90"),
            dropdown_fg_color=("#f8faff","#2a2e3b"),corner_radius=6,
            command=self._on_sort_change)
        self._sort_om.set(self._sort_rmap.get(self._sort,"Datum ↓"))
        self._sort_om.pack(side="left")
        # Dokumentenliste
        self.dscroll=ctk.CTkScrollableFrame(left,fg_color="transparent")
        self.dscroll.pack(fill="both",expand=True); self.dscroll.grid_columnconfigure(0,weight=1)
        self._page_bar=ctk.CTkFrame(left,fg_color="transparent",height=36)
        self._page_bar.pack(fill="x",pady=(4,0))
        # Vorschau rechts (resizable)
        prev_w=self._lc.get("preview_width",350)
        self._split.grid_columnconfigure(1,weight=0,minsize=prev_w)
        pf=ctk.CTkFrame(self._split,fg_color="transparent")
        pf.grid(row=0,column=1,sticky="nsew")
        # Resize-Handle links der Vorschau
        ph=ctk.CTkFrame(pf,width=5,fg_color=("gray75","#2a2e3b"),cursor="sb_h_double_arrow")
        ph.pack(side="left",fill="y")
        ph.bind("<B1-Motion>",self._resize_preview)
        ph.bind("<Enter>",lambda e:ph.configure(fg_color=("#4f8ff7","#4f8ff7")))
        ph.bind("<Leave>",lambda e:ph.configure(fg_color=("gray75","#2a2e3b")))
        self._preview_fr=ctk.CTkFrame(pf,width=prev_w,corner_radius=10,
            fg_color=("white","#21242f"),border_width=1,border_color=("gray80","#2a2e3b"))
        self._preview_fr.pack(side="left",fill="both",expand=True)
        self._preview_fr.pack_propagate(False)
        self._preview_lbl=ctk.CTkLabel(self._preview_fr,text=_t("doc_select_preview"),
            font=ctk.CTkFont(size=12),text_color=("gray50","gray55"))
        self._preview_lbl.pack(expand=True)
        self._preview_img_ref=None
        # Keyboard Navigation
        self.bind("<Up>",self._key_nav_up)
        self.bind("<Down>",self._key_nav_down)

    def _on_sort_change(self,val):
        self._sort=self._sort_map.get(val,"date_desc")
        self._lc["sort"]=self._sort; self._save_lc()
        self._page=0; self.refresh_list()

    def _key_nav_up(self,ev=None):
        """Cursortaste hoch: vorheriges Dokument."""
        self._key_nav(-1)
    def _key_nav_down(self,ev=None):
        """Cursortaste runter: nächstes Dokument."""
        self._key_nav(1)
    def _key_nav(self,delta):
        if not self._doc_list: return
        ids=[d["id"] for d in self._doc_list]
        # Aktuelles Dokument finden
        start=self._page*self._page_size
        cur_idx=start  # Default: erstes der Seite
        if self.sel_ids:
            sel_id=list(self.sel_ids)[0]
            if sel_id in ids: cur_idx=ids.index(sel_id)
        new_idx=max(0,min(len(ids)-1,cur_idx+delta))
        # Seitenwechsel wenn nötig
        new_page=new_idx//self._page_size
        if new_page!=self._page:
            self._page=new_page; self.refresh_list()
        doc=self._doc_list[new_idx]
        self.sel_ids={doc["id"]}; self.last_click_idx=doc["id"]
        self._update_sel_visuals()
        self._show_preview(doc)
    def _build_import(self):
        self.ip=ctk.CTkFrame(self.content,fg_color="transparent")
        ctk.CTkLabel(self.ip,text=_t("import_title"),font=ctk.CTkFont(size=20,weight="bold"),anchor="w").pack(fill="x",padx=20,pady=(16,8))
        mb=ctk.CTkFrame(self.ip,corner_radius=10,fg_color=("white","#21242f")); mb.pack(fill="x",padx=16,pady=(0,8))
        ctk.CTkRadioButton(mb,text=_t("import_copy"),variable=self.import_link,value=0,
            command=lambda:self._save_im()).pack(anchor="w",padx=20,pady=(12,4))
        ctk.CTkRadioButton(mb,text=_t("import_link"),variable=self.import_link,value=1,
            command=lambda:self._save_im()).pack(anchor="w",padx=20,pady=(0,12))
        # Kategorie-Vorgabe beim Import
        cat_fr=ctk.CTkFrame(self.ip,corner_radius=10,fg_color=("white","#21242f")); cat_fr.pack(fill="x",padx=16,pady=(0,8))
        ctk.CTkLabel(cat_fr,text=_t("import_cat"),font=ctk.CTkFont(size=11,weight="bold")).pack(anchor="w",padx=12,pady=(8,4))
        self._import_cat_var=ctk.StringVar(value=_t("import_auto"))
        cat_vals=[_t("import_auto"),"(Keine Kategorie)"]+get_cat_names()
        self._import_cat_om=ctk.CTkOptionMenu(cat_fr,values=cat_vals,variable=self._import_cat_var,
            width=250,height=28,font=ctk.CTkFont(size=11),
            fg_color=("#e8eef8","#353a4a"),text_color=("gray10","gray90"),
            dropdown_text_color=("gray10","gray90"),dropdown_fg_color=("#f8faff","#2a2e3b"))
        self._import_cat_om.pack(anchor="w",padx=12,pady=(0,10))
        br=ctk.CTkFrame(self.ip,fg_color="transparent"); br.pack(fill="x",padx=16,pady=(0,4))
        ctk.CTkButton(br,text=_t("import_files_btn"),height=38,width=140,command=self._import_files).pack(side="left",padx=(0,8))
        ctk.CTkButton(br,text=_t("folder_btn"),height=38,width=140,fg_color=("gray75","#353a4a"),
            text_color=("gray20","gray80"),command=self._import_folder).pack(side="left")
        # ═══ Drag & Drop Bereich ═══
        self.drop_frame=ctk.CTkFrame(self.ip,corner_radius=12,
            fg_color=("#e8f0fe","#1a2235"),border_width=3,
            border_color=("#a0b4d0","#3a4a6a"),height=120)
        self.drop_frame.pack(fill="x",padx=16,pady=(10,4))
        self.drop_frame.pack_propagate(False)
        self.drop_label=ctk.CTkLabel(self.drop_frame,
            text=_t("import_drop"),
            font=ctk.CTkFont(size=14),text_color=("gray40","gray55"),justify="center")
        self.drop_label.pack(expand=True)
        # Klick auf Drop-Bereich = Datei-Dialog
        self.drop_frame.bind("<Button-1>", lambda e: self._import_files())
        self.drop_label.bind("<Button-1>", lambda e: self._import_files())
        # DnD registrieren
        self._setup_dnd()
        # Log
        self.ilog=ctk.CTkTextbox(self.ip,height=160,font=ctk.CTkFont(family="Consolas",size=11),
            fg_color=("gray95","#171921"),corner_radius=10)
        self.ilog.pack(fill="both",expand=True,padx=16,pady=(4,12))
    def _save_im(self): self._s["link_only"]=bool(self.import_link.get()); self._save_s()
    def _build_scanner(self):
        self.sp_=ctk.CTkFrame(self.content,fg_color="transparent")
        ctk.CTkLabel(self.sp_,text=_t("scan_title"),font=ctk.CTkFont(size=20,weight="bold"),anchor="w").pack(fill="x",padx=20,pady=(16,4))
        # NAPS2-Pfad + GUI starten
        naps2_fr=ctk.CTkFrame(self.sp_,fg_color="transparent"); naps2_fr.pack(fill="x",padx=20,pady=(0,8))
        self.naps2_status_lbl=ctk.CTkLabel(naps2_fr,text="",font=ctk.CTkFont(size=11),anchor="w")
        self.naps2_status_lbl.pack(side="left",fill="x",expand=True)
        ctk.CTkButton(naps2_fr,text=_t("scan_naps2_path"),width=120,height=26,
            font=ctk.CTkFont(size=11),fg_color=("gray85","#353a4a"),
            text_color=("gray20","gray80"),command=self._change_naps2_path).pack(side="right",padx=(4,0))
        ctk.CTkButton(naps2_fr,text=_t("scan_naps2_open"),width=120,height=26,
            font=ctk.CTkFont(size=11),fg_color=("gray85","#353a4a"),
            text_color=("gray20","gray80"),command=self._open_naps2_gui).pack(side="right",padx=(4,0))
        self._update_naps2_status()
        # Scanner-Liste
        self.slist=ctk.CTkFrame(self.sp_,corner_radius=10,fg_color=("white","#21242f"))
        self.slist.pack(fill="x",padx=16,pady=(0,8))
        ctk.CTkLabel(self.slist,text=_t("scan_click_search"),text_color=("gray50","gray55")).pack(pady=12)
        # NAPS2 Profil (übersteuert Einstellungen)
        prof_fr=ctk.CTkFrame(self.sp_,corner_radius=10,fg_color=("#f0f5ff","#21242f"))
        prof_fr.pack(fill="x",padx=16,pady=(0,8))
        prof_top=ctk.CTkFrame(prof_fr,fg_color="transparent"); prof_top.pack(fill="x",padx=12,pady=(8,2))
        ctk.CTkLabel(prof_top,text="NAPS2:",font=ctk.CTkFont(size=11,weight="bold"),
            text_color=("gray30","gray70")).pack(side="left")
        self.scan_profile=ctk.CTkOptionMenu(prof_top,values=["(Kein Profil – manuelle Einstellungen)"],
            width=300,font=ctk.CTkFont(size=11),fg_color=("#e8eef8","#353a4a"),
            text_color=("gray10","gray90"),dropdown_text_color=("gray10","gray90"),
            dropdown_fg_color=("#f8faff","#2a2e3b"),
            command=self._on_profile_change)
        self.scan_profile.set("(Kein Profil – manuelle Einstellungen)")
        self.scan_profile.pack(side="left",padx=8)
        ctk.CTkButton(prof_top,text=_t("scan_profiles_load"),width=110,height=28,
            font=ctk.CTkFont(size=11),fg_color=("gray85","#353a4a"),
            text_color=("gray20","gray80"),
            command=self._refresh_profiles).pack(side="left",padx=4)
        ctk.CTkLabel(prof_top,text=_t("scan_profile_hint"),
            font=ctk.CTkFont(size=10),text_color=("gray50","gray55")).pack(side="left",padx=8)
        # Profil-Details Anzeige
        self._prof_detail_lbl=ctk.CTkLabel(prof_fr,text="",font=ctk.CTkFont(size=10),
            text_color=("gray50","gray55"),anchor="w")
        self._prof_detail_lbl.pack(fill="x",padx=16,pady=(0,6))
        self._profile_data=[]  # Gespeicherte Profil-Details
        # Scan-Optionen (als Fallback wenn kein Profil)
        self._manual_opts_lbl=ctk.CTkLabel(self.sp_,text=_t("scan_manual"),
            font=ctk.CTkFont(size=11,weight="bold"),text_color=("gray30","gray70"),anchor="w")
        self._manual_opts_lbl.pack(fill="x",padx=20,pady=(4,0))
        self._manual_opts=ctk.CTkFrame(self.sp_,corner_radius=10,fg_color=("#f0f5ff","#21242f"))
        self._manual_opts.pack(fill="x",padx=16,pady=(0,12)); self._manual_opts.grid_columnconfigure((0,1,2,3),weight=1)
        opts=self._manual_opts
        for i,(lbl,vals,df) in enumerate([("Auflösung",["150","200","300","600"],"150"),
            ("Farbe",["Farbe","Graustufen","SW"],"Farbe"),
            ("Quelle",["Einzug (ADF)","Flachbett"],"Einzug (ADF)"),
            ("Format",["PDF","WebP (klein)"],"PDF")]):
            ctk.CTkLabel(opts,text=lbl,font=ctk.CTkFont(size=10,weight="bold"),
                text_color=("gray30","gray70")).grid(row=0,column=i,padx=8,pady=(10,2),sticky="w")
            om=ctk.CTkOptionMenu(opts,values=vals,font=ctk.CTkFont(size=11),width=130,
                fg_color=("#e8eef8","#353a4a"),button_color=("#d0daf0","#454a5a"),
                text_color=("gray10","gray90"),dropdown_text_color=("gray10","gray90"),
                dropdown_fg_color=("#f8faff","#2a2e3b"),
                command=lambda v: self._save_scan_settings())
            om.set(df); om.grid(row=1,column=i,padx=8,pady=(0,10),sticky="ew")
            if i==0: self.scan_dpi=om
            elif i==1: self.scan_color=om
            elif i==2: self.scan_source=om
            else: self.scan_fmt=om
        br=ctk.CTkFrame(self.sp_,fg_color="transparent"); br.pack(fill="x",padx=16,pady=(0,8))
        ctk.CTkButton(br,text=_t("scan_search"),width=150,height=38,
            fg_color=("gray80","#353a4a"),text_color=("gray20","gray80"),
            command=self._refresh_scanners).pack(side="left",padx=(0,8))
        ctk.CTkButton(br,text=_t("scan_btn"),width=200,height=44,
            font=ctk.CTkFont(size=15,weight="bold"),
            command=self._do_scan).pack(side="left",padx=(0,12))
        ctk.CTkLabel(br,text=_t("scan_adf_hint"),
            font=ctk.CTkFont(size=11),text_color=("gray50","gray55"),justify="left").pack(side="left")
        self.scan_status=ctk.CTkLabel(self.sp_,text="",font=ctk.CTkFont(size=12),
            text_color=("gray50","gray55"),anchor="w")
        self.scan_status.pack(fill="x",padx=20,pady=(4,8))
        # OCR-Sprache + erweiterte Einstellungen
        ocr_fr=ctk.CTkFrame(self.sp_,fg_color="transparent"); ocr_fr.pack(fill="x",padx=20,pady=(0,4))
        ctk.CTkLabel(ocr_fr,text=_t("sett_ocrlang"),font=ctk.CTkFont(size=11)).pack(side="left")
        self.scan_ocr_lang=ctk.CTkOptionMenu(ocr_fr,values=["deu","eng","fra","ita","deu+eng"],
            width=100,font=ctk.CTkFont(size=11),fg_color=("#e8eef8","#353a4a"),
            text_color=("gray10","gray90"),dropdown_text_color=("gray10","gray90"),
            dropdown_fg_color=("#f8faff","#2a2e3b"),
            command=lambda v: self._save_scan_settings())
        self.scan_ocr_lang.set("deu"); self.scan_ocr_lang.pack(side="left",padx=8)
        ctk.CTkLabel(ocr_fr,text=_t("sett_ocr_mode"),font=ctk.CTkFont(size=11)).pack(side="left",padx=(12,0))
        self.scan_ocr_mode=ctk.CTkOptionMenu(ocr_fr,values=["Am besten","Schnell"],
            width=110,font=ctk.CTkFont(size=11),fg_color=("#e8eef8","#353a4a"),
            text_color=("gray10","gray90"),dropdown_text_color=("gray10","gray90"),
            dropdown_fg_color=("#f8faff","#2a2e3b"),
            command=lambda v: self._save_scan_settings())
        self.scan_ocr_mode.set("Am besten"); self.scan_ocr_mode.pack(side="left",padx=4)
        ctk.CTkButton(ocr_fr,text=_t("scan_ocr_test"),width=110,height=28,
            fg_color=("gray85","#353a4a"),text_color=("gray20","gray80"),
            font=ctk.CTkFont(size=11),command=self._test_naps2_ocr).pack(side="left",padx=8)
        # Bildkorrekturen
        corr_fr=ctk.CTkFrame(self.sp_,fg_color="transparent"); corr_fr.pack(fill="x",padx=20,pady=(0,8))
        self.scan_deskew=ctk.CTkCheckBox(corr_fr,text=_t("scan_deskew"),
            font=ctk.CTkFont(size=11),command=self._save_scan_settings)
        self.scan_deskew.pack(side="left")
        self.sel_scanner_name = self._lc.get("scanner_name","")
        # Auto-load Scanner beim Start
        if NAPS2_EXE:
            self.after(500, self._refresh_scanners)
    def _show(self,page):
        for p in [self.lp,self.ip,self.sp_,self.sett_p]: p.grid_forget()
        {"list":self.lp,"import":self.ip,"scanner":self.sp_,"settings":self.sett_p}.get(page,self.lp).grid(row=0,column=0,sticky="nsew")
    def _nav(self,k):
        if k in ("all","starred","upload","scanner","settings","catmgr","backup","notes"):
            self._suppress_search=True
            self.sv.set("")  # Suchfeld leeren ohne refresh auszulösen
            self._suppress_search=False
        if k=="all": self.current_cat="";self.current_star=False;self._page=0;self.lhdr.configure(text=_t("all_docs"));self._show("list");self.refresh_list()
        elif k=="starred": self.current_cat="";self.current_star=True;self._page=0;self.lhdr.configure(text=_t("favorites"));self._show("list");self.refresh_list()
        elif k=="upload": self._show("import")
        elif k=="notes": self._open_note()
        elif k=="scanner": self._show("scanner")
        elif k=="catmgr": CatMgr(self,on_change=lambda:(self._rebuild_cats(),self.refresh_list()))
        elif k=="backup": self._do_backup()
        elif k=="settings": self._show("settings"); self._refresh_settings()
    def _change_data_path(self):
        """Dialog um den Daten-Ordner zu ändern (für zentrale Speicherung auf NAS etc.)."""
        dlg=ctk.CTkToplevel(self); dlg.title("Datenpfad ändern")
        dlg.transient(self); dlg.grab_set()
        center_window(dlg,550,320)
        ctk.CTkLabel(dlg,text=_t("data_folder"),font=ctk.CTkFont(size=18,weight="bold")).pack(padx=16,pady=(16,4),anchor="w")
        ctk.CTkLabel(dlg,text=_t("sett_datapath_dlg_hint"),
            font=ctk.CTkFont(size=12),text_color=("gray50","gray55"),wraplength=500,justify="left"
        ).pack(padx=16,anchor="w",pady=(0,12))
        ctk.CTkLabel(dlg,text=f"{_t('sett_current')}",font=ctk.CTkFont(size=11,weight="bold"),
            text_color=("gray50","gray55")).pack(padx=16,anchor="w")
        ctk.CTkLabel(dlg,text=str(DATA_DIR),font=ctk.CTkFont(size=12),wraplength=500).pack(padx=16,anchor="w",pady=(2,12))
        path_var=ctk.StringVar(value=str(DATA_DIR))
        row=ctk.CTkFrame(dlg,fg_color="transparent"); row.pack(fill="x",padx=16)
        ctk.CTkEntry(row,textvariable=path_var,font=ctk.CTkFont(size=12)).pack(side="left",fill="x",expand=True,padx=(0,8))
        ctk.CTkButton(row,text="📂",width=40,command=lambda:path_var.set(
            filedialog.askdirectory(title="Daten-Ordner wählen") or path_var.get())).pack(side="right")
        def save():
            new_path=path_var.get().strip()
            if not new_path: return
            p=Path(new_path)
            try: p.mkdir(parents=True,exist_ok=True)
            except Exception as e:
                messagebox.showerror("Fehler",f"Ordner kann nicht erstellt werden:\n{e}"); return
            # Prüfe ob dort bereits eine Datenbank existiert
            existing_db = p / "docvault.db"
            existing_docs = p / "documents"
            if existing_db.exists():
                n_docs = 0
                try:
                    import sqlite3 as sq
                    c2 = sq.connect(str(existing_db), timeout=5)
                    n_docs = c2.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
                    c2.close()
                except Exception: pass
                msg = (f"Im gewählten Ordner existiert bereits eine DocVault-Datenbank!\n\n"
                       f"  Pfad: {p}\n"
                       f"  Dokumente: {n_docs}\n\n"
                       f"Die bestehenden Daten werden NICHT überschrieben.\n"
                       f"DocVault wird diese Datenbank beim nächsten Start verwenden.\n\n"
                       f"Fortfahren?")
                if not messagebox.askyesno("Bestehende Daten gefunden", msg):
                    return
            elif existing_docs.exists() and any(existing_docs.iterdir()):
                msg = (f"Im gewählten Ordner existiert bereits ein 'documents'-Ordner mit Dateien.\n\n"
                       f"  Pfad: {p}\n\n"
                       f"Bestehende Dateien werden NICHT überschrieben.\n"
                       f"Fortfahren?")
                if not messagebox.askyesno("Bestehende Daten gefunden", msg):
                    return
            _write_data_path(p)
            messagebox.showinfo("DocVault",f"Datenpfad geändert auf:\n{p}\n\nBitte DocVault neu starten.")
            dlg.destroy()
        ctk.CTkButton(dlg,text=_t("catmgr_save"),font=ctk.CTkFont(weight="bold"),
            command=save).pack(pady=16)
    def _filt_cat(self,c):
        self._suppress_search=True; self.sv.set(""); self._suppress_search=False
        self.current_cat=c;self.current_star=False;self._page=0;cd=get_cat_dict()
        self.lhdr.configure(text=f"{cd.get(c,{}).get('icon','📄')} {c}");self._show("list");self.refresh_list()
    def _on_search(self,*a):
        if self._suppress_search: return
        if self.search_aid: self.after_cancel(self.search_aid)
        self._page=0  # Bei neuer Suche: Seite 1
        self.search_aid=self.after(400,self.refresh_list)
        if hasattr(self,"_hist_aid") and self._hist_aid:
            self.after_cancel(self._hist_aid)
        self._hist_aid=self.after(5000,self._save_search_term)
    def _save_search_term(self):
        q=self.sv.get().strip()
        if q and len(q)>=3:
            if q in self._search_history: self._search_history.remove(q)
            self._search_history.insert(0,q)
            self._search_history=self._search_history[:30]
            self._lc["search_history"]=self._search_history
            self._save_lc()
    def _show_search_history(self):
        if not self._search_history: return
        m=tk.Menu(self,tearoff=0,font=("Segoe UI",10))
        for term in self._search_history[:30]:
            m.add_command(label=term,command=lambda t=term:self.sv.set(t))
        if self._search_history:
            m.add_separator()
            m.add_command(label=_t("ctx_clear_history"),command=self._clear_search_history)
        try:
            x=self._search_hist_btn.winfo_rootx()
            y=self._search_hist_btn.winfo_rooty()+self._search_hist_btn.winfo_height()
            m.post(x,y)
        except Exception: pass
    def _clear_search_history(self):
        self._search_history=[]
        self._lc["search_history"]=[]
        self._save_lc()
    def refresh_list(self):
        q=self.sv.get().strip()
        excl=None
        if not self.current_cat and not self.current_star:
            if hasattr(self,"_excluded_cats") and self._excluded_cats:
                excl=list(self._excluded_cats)
        # Spezialfilter: Fehlende Verknüpfungen
        if self.current_cat == "__missing_links__" and hasattr(self, "_missing_link_ids") and self._missing_link_ids:
            with get_db() as c:
                placeholders = ",".join(["?" for _ in self._missing_link_ids])
                docs = [dict(r) for r in c.execute(
                    f"SELECT * FROM documents WHERE id IN ({placeholders})",
                    list(self._missing_link_ids)).fetchall()]
        else:
            docs=search_docs(q,self.current_cat,self.current_star,limit=5000,exclude_cats=excl,sort=self._sort)
        self._doc_list=docs
        self._total_docs=len(docs)
        n_docs = len(docs)
        self._max_page=max(0,(n_docs-1)//self._page_size) if n_docs > 0 else 0
        if self._page>self._max_page: self._page=self._max_page
        start=self._page*self._page_size
        end=start+self._page_size
        page_docs=docs[start:end]
        # Info-Zeile
        n = len(docs)
        doc_word = _t('docs_plural') if n != 1 else _t('docs_singular')
        info=f"{n} {doc_word}"
        if q: info+=f' {_t("search_for")} "{q}"'
        if n_docs > self._page_size:
            info+=f" · {_t('page')} {self._page+1}/{self._max_page+1}"
        self.lsub.configure(text=info)
        self._render_docs(page_docs)
        self._render_page_bar()
        try: self.dscroll._parent_canvas.yview_moveto(0)
        except Exception: pass

    def _render_page_bar(self):
        """Rendert die Seitennavigation unter der Liste."""
        for w in self._page_bar.winfo_children(): w.destroy()
        if self._total_docs <= self._page_size: return  # Keine Pagination nötig
        bs={"height":28,"corner_radius":6,"font":ctk.CTkFont(size=11),
            "fg_color":("gray80","#353a4a"),"text_color":("gray20","gray80")}
        ctk.CTkButton(self._page_bar,text="◀◀",width=40,
            command=lambda:self._go_page(0),**bs).pack(side="left",padx=2)
        ctk.CTkButton(self._page_bar,text="◀",width=36,
            command=lambda:self._go_page(self._page-1),**bs).pack(side="left",padx=2)
        ctk.CTkLabel(self._page_bar,
            text=_t('page_of').format(a=self._page+1, b=self._max_page+1),
            font=ctk.CTkFont(size=11)).pack(side="left",padx=10)
        ctk.CTkButton(self._page_bar,text="▶",width=36,
            command=lambda:self._go_page(self._page+1),**bs).pack(side="left",padx=2)
        ctk.CTkButton(self._page_bar,text="▶▶",width=40,
            command=lambda:self._go_page(self._max_page),**bs).pack(side="left",padx=2)

    def _go_page(self,page):
        self._page=max(0,min(page,self._max_page))
        self.refresh_list()
    def _get_thumb(self,doc):
        did=doc["id"]
        if did in self._tc: return self._tc[did]
        tp=doc.get("thumbnail","")
        if tp and os.path.isfile(tp):
            try:
                img=Image.open(tp); ci=ctk.CTkImage(light_image=img,dark_image=img,size=(40,55))
                self._tc[did]=ci; return ci
            except Exception: pass
        return None
    def _render_docs(self,docs):
        for w in self.dscroll.winfo_children(): w.destroy()
        self._cards={}
        if not docs:
            ctk.CTkLabel(self.dscroll,text=_t("no_docs"),font=ctk.CTkFont(size=14),
                text_color=("gray50","gray55")).grid(row=0,column=0,pady=40)
            return
        for i,doc in enumerate(docs): self._card(doc,i)
    def _show_preview(self, doc):
        """Zeigt die Vorschau eines Dokuments im rechten Panel."""
        self._preview_doc = doc
        self._preview_page = 0
        self._render_preview()
    def _render_preview(self):
        """Rendert Vorschau + editierbare Metadaten."""
        for w in self._preview_fr.winfo_children(): w.destroy()
        doc = self._preview_doc
        if not doc:
            ctk.CTkLabel(self._preview_fr,text=_t("doc_select_preview"),
                font=ctk.CTkFont(size=12),text_color=("gray50","gray55")).pack(expand=True)
            return
        fp = doc.get("file_path","")
        name = doc.get("original_name","")
        pw = self._preview_fr.cget("width") or 350
        img_w = max(200, pw - 20)
        # Scrollbarer Container
        sc = ctk.CTkScrollableFrame(self._preview_fr,fg_color="transparent")
        sc.pack(fill="both",expand=True,padx=4,pady=4)
        ctk.CTkLabel(sc,text=name,font=ctk.CTkFont(size=11,weight="bold"),
            wraplength=img_w).pack(padx=4,pady=(4,4),anchor="w")

        try:
            self._render_preview_content(sc, doc, fp, img_w)
        except Exception as e:
            logger.error("Vorschau-Fehler: %s", e, exc_info=True)
            ctk.CTkLabel(sc,text=f"{_t('prev_error')}\n{e}",font=ctk.CTkFont(size=10),
                text_color=("red","#ef4444"),wraplength=img_w).pack(pady=8)

        # ═══ Editierbare Metadaten ═══
        try:
            self._render_preview_meta(sc, doc, fp, img_w)
        except Exception as e:
            logger.error("Metadaten-Fehler: %s", e)

    def _render_preview_content(self, sc, doc, fp, img_w):
        """Rendert den Vorschau-Inhalt (Bild/Text/Plugin)."""
        source = doc.get("source","")

        # ═══ Notizen: direkt den gespeicherten Text anzeigen ═══
        if source == "note":
            ocr = doc.get("ocr_text","")
            if ocr:
                tb = ctk.CTkTextbox(sc, height=min(400, max(100, ocr.count("\n")*16 + 40)),
                    font=ctk.CTkFont(size=11), corner_radius=6,
                    fg_color=("gray95","#171921"))
                tb.pack(fill="x", padx=4, pady=4)
                tb.insert("1.0", ocr[:5000]); tb.configure(state="disabled")
            else:
                ctk.CTkLabel(sc,text="(empty)" if _LANG=="en" else "(Leere Notiz)",font=ctk.CTkFont(size=11),
                    text_color=("gray50","gray55")).pack(pady=12)
            return

        # ═══ PDF-Vorschau ═══
        if fp.lower().endswith(".pdf") and os.path.isfile(fp):
            if HAS_FITZ:
                pdf = fitz.open(fp)
                total_pages = len(pdf)
                if self._preview_page >= total_pages: self._preview_page = total_pages - 1
                if self._preview_page < 0: self._preview_page = 0
                page = pdf[self._preview_page]
                scale = img_w / (page.rect.width or 1)
                mat = fitz.Matrix(scale, scale)
                pix = page.get_pixmap(matrix=mat)
                img = _pix_to_pil(pix)
                pdf.close()
                from PIL import ImageTk
                tk_img = ImageTk.PhotoImage(img)
                self._preview_img_ref = tk_img
                ctk.CTkLabel(sc, text="", image=tk_img).pack(padx=4, pady=2)
                if total_pages > 1:
                    nav = ctk.CTkFrame(sc, fg_color="transparent"); nav.pack(pady=2)
                    bs2={"height":24,"corner_radius":4,"font":ctk.CTkFont(size=10),
                        "fg_color":("gray85","#353a4a"),"text_color":("gray20","gray80")}
                    ctk.CTkButton(nav,text="◀",width=30,command=lambda:self._preview_nav(-1),**bs2).pack(side="left",padx=2)
                    ctk.CTkLabel(nav,text=f"{self._preview_page+1}/{total_pages}",font=ctk.CTkFont(size=10)).pack(side="left",padx=6)
                    ctk.CTkButton(nav,text="▶",width=30,command=lambda:self._preview_nav(1),**bs2).pack(side="left",padx=2)
            else:
                ctk.CTkLabel(sc,text=_t("prev_no_fitz"),
                    font=ctk.CTkFont(size=11),text_color=("gray50","gray55")).pack(pady=20)
            return

        # ═══ WebP-Vorschau (mehrseitig) ═══
        if fp.lower().endswith(".webp") and os.path.isfile(fp):
            total_pages = webp_page_count(fp)
            if self._preview_page >= total_pages: self._preview_page = total_pages - 1
            if self._preview_page < 0: self._preview_page = 0
            img = webp_get_page(fp, self._preview_page, max_width=img_w)
            if img:
                from PIL import ImageTk
                tk_img = ImageTk.PhotoImage(img)
                self._preview_img_ref = tk_img
                ctk.CTkLabel(sc, text="", image=tk_img).pack(padx=4, pady=2)
                if total_pages > 1:
                    nav = ctk.CTkFrame(sc, fg_color="transparent"); nav.pack(pady=2)
                    bs2={"height":24,"corner_radius":4,"font":ctk.CTkFont(size=10),
                        "fg_color":("gray85","#353a4a"),"text_color":("gray20","gray80")}
                    ctk.CTkButton(nav,text="◀",width=30,command=lambda:self._preview_nav(-1),**bs2).pack(side="left",padx=2)
                    ctk.CTkLabel(nav,text=f"{self._preview_page+1}/{total_pages}",font=ctk.CTkFont(size=10)).pack(side="left",padx=6)
                    ctk.CTkButton(nav,text="▶",width=30,command=lambda:self._preview_nav(1),**bs2).pack(side="left",padx=2)
            else:
                ctk.CTkLabel(sc,text=_t("prev_webp_error"),
                    font=ctk.CTkFont(size=11),text_color=("gray50","gray55")).pack(pady=20)
            return

        # ═══ Bild-Vorschau ═══
        if os.path.isfile(fp) and fp.lower().split(".")[-1] in ("png","jpg","jpeg","gif","webp","bmp"):
            img = Image.open(fp)
            s = img_w / (img.width or 1)
            img = img.resize((img_w, int(img.height * s)), Image.LANCZOS)
            from PIL import ImageTk
            tk_img = ImageTk.PhotoImage(img)
            self._preview_img_ref = tk_img
            ctk.CTkLabel(sc, text="", image=tk_img).pack(padx=4, pady=4)
            return

        # ═══ Plugin-Vorschau ═══
        if os.path.isfile(fp):
            plugin_result = plugin_render_preview(fp, img_w)
            if plugin_result:
                ptype = plugin_result.get("type","")
                if ptype == "text":
                    txt = plugin_result.get("content","")[:5000]
                    tb = ctk.CTkTextbox(sc, height=min(300, max(100, txt.count("\n")*16)),
                        font=ctk.CTkFont(family="Consolas",size=10), corner_radius=6,
                        fg_color=("gray95","#171921"))
                    tb.pack(fill="x", padx=4, pady=4)
                    tb.insert("1.0", txt); tb.configure(state="disabled")
                    pg = plugin_result.get("pages",0)
                    if pg: ctk.CTkLabel(sc,text=_t("x_pages").format(n=pg),font=ctk.CTkFont(size=9),
                        text_color=("gray50","gray55")).pack(anchor="w",padx=4)
                elif ptype == "image":
                    pil_img = plugin_result.get("image")
                    if pil_img:
                        from PIL import ImageTk
                        tk_img = ImageTk.PhotoImage(pil_img)
                        self._preview_img_ref = tk_img
                        ctk.CTkLabel(sc, text="", image=tk_img).pack(padx=4, pady=4)
                elif ptype == "html_text":
                    txt = plugin_result.get("content","")[:5000]
                    tb = ctk.CTkTextbox(sc, height=min(300, max(100, txt.count("\n")*16)),
                        font=ctk.CTkFont(size=10), corner_radius=6,
                        fg_color=("gray95","#171921"))
                    tb.pack(fill="x", padx=4, pady=4)
                    tb.insert("1.0", txt); tb.configure(state="disabled")
                elif ptype == "error":
                    ctk.CTkLabel(sc,text=f"⚠️ {plugin_result.get('message','')}",
                        font=ctk.CTkFont(size=10),text_color=("red","#ef4444"),
                        wraplength=img_w).pack(pady=8)
                pname = plugin_result.get("plugin_name","Plugin")
                ctk.CTkLabel(sc,text=f"via {pname}",font=ctk.CTkFont(size=8),
                    text_color=("gray60","gray50")).pack(anchor="w",padx=4)
                return

        # ═══ Keine Vorschau ═══
        ctk.CTkLabel(sc,text=_t("doc_no_preview"),font=ctk.CTkFont(size=11),
            text_color=("gray50","gray55")).pack(pady=20)

    def _render_preview_meta(self, sc, doc, fp, img_w):
        """Rendert die editierbaren Metadaten unter der Vorschau."""
        # ═══ Editierbare Metadaten ═══
        ctk.CTkFrame(sc,height=1,fg_color=("gray80","#2a2e3b")).pack(fill="x",padx=4,pady=6)
        ef={"height":28,"font":ctk.CTkFont(size=11),"corner_radius":6}
        # Name
        self._meta_name=ctk.StringVar(value=doc.get("original_name",""))
        r=ctk.CTkFrame(sc,fg_color="transparent"); r.pack(fill="x",padx=4,pady=1)
        ctk.CTkLabel(r,text=_t("doc_meta_name"),font=ctk.CTkFont(size=10,weight="bold"),width=65,anchor="w").pack(side="left")
        ctk.CTkEntry(r,textvariable=self._meta_name,**ef).pack(side="left",fill="x",expand=True)
        # Kategorie
        self._meta_cat=ctk.StringVar(value=doc.get("category","Dokument"))
        r=ctk.CTkFrame(sc,fg_color="transparent"); r.pack(fill="x",padx=4,pady=1)
        ctk.CTkLabel(r,text=_t("doc_meta_cat"),font=ctk.CTkFont(size=10,weight="bold"),width=65,anchor="w").pack(side="left")
        ctk.CTkOptionMenu(r,values=get_cat_names(),variable=self._meta_cat,height=28,
            font=ctk.CTkFont(size=11),fg_color=("#e8eef8","#353a4a"),
            text_color=("gray10","gray90"),dropdown_text_color=("gray10","gray90"),
            dropdown_fg_color=("#f8faff","#2a2e3b")).pack(side="left",fill="x",expand=True)
        # Tags
        tags=json.loads(doc.get("tags","[]")) if isinstance(doc.get("tags"),str) else []
        self._meta_tags=ctk.StringVar(value=", ".join(tags))
        r=ctk.CTkFrame(sc,fg_color="transparent"); r.pack(fill="x",padx=4,pady=1)
        ctk.CTkLabel(r,text=_t("doc_meta_tags"),font=ctk.CTkFont(size=10,weight="bold"),width=65,anchor="w").pack(side="left")
        ctk.CTkEntry(r,textvariable=self._meta_tags,placeholder_text=_t("doc_meta_tags_ph"),**ef).pack(side="left",fill="x",expand=True)
        # Info
        sz=doc.get("file_size",0)
        sz_txt=f"{sz/1048576:.1f} MB" if sz>1048576 else f"{sz/1024:.0f} KB"
        pg=doc.get("page_count",0)
        dt=doc.get("created_at","")[:19] if doc.get("created_at") else ""
        src=doc.get("source","")
        parts=[sz_txt]
        if pg: parts.append(f"{pg} Seiten")
        if dt: parts.append(dt)
        if src: parts.append(f"Quelle: {src}")
        ctk.CTkLabel(sc,text=" · ".join(parts),font=ctk.CTkFont(size=9),
            text_color=("gray50","gray55"),wraplength=img_w).pack(padx=4,pady=(4,1),anchor="w")
        ctk.CTkLabel(sc,text=fp,font=ctk.CTkFont(size=8),
            text_color=("gray60","gray50"),wraplength=img_w).pack(padx=4,pady=(0,4),anchor="w")
        # Buttons: KI-Tags + Speichern
        btn_row=ctk.CTkFrame(sc,fg_color="transparent"); btn_row.pack(fill="x",padx=4,pady=(4,8))
        ctk.CTkButton(btn_row,text=_t("doc_ai_retag"),height=30,width=160,
            font=ctk.CTkFont(size=11),fg_color=("gray82","#2a3040"),
            hover_color=("gray75","#353f55"),text_color=("gray30","gray80"),
            command=lambda:self._ai_retag_doc(doc)).pack(side="left",padx=(0,4))
        ctk.CTkButton(btn_row,text=_t("doc_meta_save"),height=30,
            font=ctk.CTkFont(size=11),command=lambda:self._save_meta(doc)).pack(side="left",fill="x",expand=True)
    def _preview_nav(self, delta):
        """Blättert in der Vorschau."""
        self._preview_page += delta
        self._render_preview()
    def _ai_retag_doc(self, doc):
        """KI-Tags vorschlagen, in Dialog anzeigen, optional übernehmen."""
        lc = load_local()
        if not lc.get("ai_provider") or not lc.get("ai_token"):
            messagebox.showinfo("🤖 KI-Tags",
                "Kein API-Token gesetzt.\n\n"
                "Bitte unter Einstellungen → 🤖 KI-Schlagwörter\n"
                "einen Anbieter und API-Token eingeben." if _LANG == "de" else
                "No API token set.\n\n"
                "Please enter a provider and API token under\n"
                "Settings → 🤖 AI Keywords.")
            return

        text = doc.get("ocr_text", "")
        if not text or len(text.strip()) < 20:
            messagebox.showwarning("🤖 KI-Tags",
                "Zu wenig Text für KI-Analyse." if _LANG == "de" else
                "Not enough text for AI analysis.")
            return

        # Vorhandene Tags laden
        existing_tags = json.loads(doc.get("tags", "[]")) if isinstance(doc.get("tags"), str) else doc.get("tags", [])

        # KI aufrufen (in Thread)
        dlg = ctk.CTkToplevel(self)
        dlg.title("🤖 KI-Tags vorschlagen" if _LANG == "de" else "🤖 Suggest AI Tags")
        _set_window_icon(dlg); dlg.transient(self); dlg.grab_set()
        center_window(dlg, 480, 360)

        ctk.CTkLabel(dlg, text="🤖 KI-Tags",
            font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(14, 4))
        status_lbl = ctk.CTkLabel(dlg, text="⏳ KI analysiert Dokument..." if _LANG == "de" else "⏳ AI analyzing document...",
            font=ctk.CTkFont(size=12), text_color=("gray40", "gray60"))
        status_lbl.pack(pady=(0, 8))

        # Vorhandene Tags anzeigen
        if existing_tags:
            ctk.CTkLabel(dlg, text=f"Vorhandene Tags: {', '.join(existing_tags)}" if _LANG == "de" else f"Existing tags: {', '.join(existing_tags)}",
                font=ctk.CTkFont(size=10), text_color=("gray50", "gray55"),
                wraplength=440).pack(padx=16, pady=(0, 8), anchor="w")

        # Frame für neue Tags
        tags_fr = ctk.CTkFrame(dlg, fg_color=("gray95", "#171921"), corner_radius=8)
        tags_fr.pack(fill="both", expand=True, padx=16, pady=(0, 8))
        new_tags_lbl = ctk.CTkLabel(tags_fr, text="", font=ctk.CTkFont(size=12),
            wraplength=420, justify="left")
        new_tags_lbl.pack(padx=12, pady=12, anchor="w")

        # AI-Name und Kategorie anzeigen
        ai_info_lbl = ctk.CTkLabel(dlg, text="", font=ctk.CTkFont(size=10),
            text_color=("gray50", "gray55"), wraplength=440)
        ai_info_lbl.pack(padx=16, pady=(0, 4), anchor="w")

        # Buttons (initial deaktiviert)
        btn_fr = ctk.CTkFrame(dlg, fg_color="transparent"); btn_fr.pack(pady=(4, 14))
        accept_txt = "✅ Übernehmen" if _LANG == "de" else "✅ Accept"
        reject_txt = "❌ Verwerfen" if _LANG == "de" else "❌ Reject"
        accept_btn = ctk.CTkButton(btn_fr, text=accept_txt, width=140, height=34,
            font=ctk.CTkFont(size=12, weight="bold"), state="disabled")
        accept_btn.pack(side="left", padx=6)
        ctk.CTkButton(btn_fr, text=reject_txt, width=120, height=34,
            fg_color=("gray75", "#353a4a"), text_color=("gray30", "gray80"),
            command=dlg.destroy).pack(side="left", padx=6)

        ai_result = [None]

        def _fetch():
            ai = _ai_analyze_document(text, get_cat_names(), doc.get("original_name", ""))
            ai_result[0] = ai

            def _show():
                if not ai or not ai.get("tags"):
                    status_lbl.configure(text="❌ KI konnte keine Tags generieren." if _LANG == "de" else "❌ AI could not generate tags.")
                    return

                new_tags = ai.get("tags", [])
                # Duplikate mit vorhandenen Tags entfernen
                unique_new = [t for t in new_tags if t.lower() not in [e.lower() for e in existing_tags]]

                if not unique_new:
                    status_lbl.configure(text="ℹ️ Alle vorgeschlagenen Tags sind bereits vorhanden." if _LANG == "de" else "ℹ️ All suggested tags already exist.")
                    new_tags_lbl.configure(text=", ".join(new_tags))
                    return

                status_lbl.configure(text=f"🤖 {len(unique_new)} neue Tags vorgeschlagen:" if _LANG == "de" else f"🤖 {len(unique_new)} new tags suggested:")
                new_tags_lbl.configure(text=", ".join(unique_new),
                    font=ctk.CTkFont(size=13, weight="bold"))

                # Name und Kategorie als Info
                info_parts = []
                if ai.get("name") and ai["name"] != doc.get("original_name", ""):
                    info_parts.append(f"📝 Name: {ai['name']}")
                if ai.get("category"):
                    info_parts.append(f"📂 Kategorie: {ai['category']}")
                if info_parts:
                    ai_info_lbl.configure(text=" · ".join(info_parts))

                def _accept():
                    # Neue Tags an vorhandene anhängen
                    merged = existing_tags + unique_new
                    merged = list(dict.fromkeys(merged))[:12]
                    # In DB speichern
                    with get_db() as c:
                        c.execute("UPDATE documents SET tags=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
                            (json.dumps(merged), doc["id"]))
                    doc["tags"] = json.dumps(merged)
                    # Name aktualisieren wenn KI einen vorschlägt
                    if ai.get("name"):
                        with get_db() as c:
                            c.execute("UPDATE documents SET original_name=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
                                (ai["name"], doc["id"]))
                        doc["original_name"] = ai["name"]
                    # Kategorie aktualisieren
                    if ai.get("category"):
                        cat_name = _ensure_category(ai["category"])
                        with get_db() as c:
                            c.execute("UPDATE documents SET category=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
                                (cat_name, doc["id"]))
                        doc["category"] = cat_name
                    dlg.destroy()
                    # UI aktualisieren
                    self._preview_doc = doc
                    self._render_preview()
                    self.refresh_list(); self._rebuild_cats(); self.refresh_stats()

                accept_btn.configure(state="normal", command=_accept)

            self.after(0, _show)

        threading.Thread(target=_fetch, daemon=True).start()

    def _save_meta(self, doc):
        """Speichert editierte Metadaten aus der Vorschau."""
        did=doc["id"]
        new_name=self._meta_name.get().strip()
        new_cat=self._meta_cat.get().strip()
        new_tags=[t.strip() for t in self._meta_tags.get().replace(";",",").split(",") if t.strip()]
        with get_db() as c:
            c.execute("UPDATE documents SET original_name=?,category=?,tags=? WHERE id=?",
                (new_name or doc["original_name"], new_cat or "Dokument", json.dumps(new_tags), did))
        # Lokalen doc-dict aktualisieren
        doc["original_name"]=new_name; doc["category"]=new_cat; doc["tags"]=json.dumps(new_tags)
        index_document(did, f"{new_name} {new_cat} {' '.join(new_tags)}")
        logger.info("Meta gespeichert: #%d name=%s cat=%s tags=%s", did, new_name, new_cat, new_tags)
        self.refresh_list(); self._rebuild_cats(); self.refresh_stats()
        # Vorschau aktualisieren wenn dieses Dokument angezeigt wird
        if self._preview_doc and self._preview_doc["id"] == did:
            self._render_preview()
    def _card(self,doc,row):
        sel=doc["id"] in self.sel_ids
        card_h=70
        # Quelle-basierte Farben (Pastelltöne)
        src=doc.get("source","import")
        src_colors={
            "scan":   ("#eef6ff","#1a2333"),  # Hellblau
            "import": ("#eefaee","#1a2a1a"),  # Hellgrün
            "link":   ("#fff8ee","#2a2518"),  # Hellgelb
            "note":   ("#f5eeff","#221a2e"),  # Helllila
        }
        card_bg=src_colors.get(src,("#f5f5f5","#21242f"))
        card=ctk.CTkFrame(self.dscroll,corner_radius=10,height=card_h,fg_color=card_bg,
            border_width=2 if sel else 1,border_color=("#4f8ff7","#4f8ff7") if sel else ("gray80","#2a2e3b"))
        card.grid(row=row,column=0,sticky="ew",pady=2,padx=4)
        card.grid_columnconfigure(2,weight=1); card.grid_propagate(False)
        self._cards[doc["id"]]=card

        def bind_all(widget):
            widget.bind("<Button-1>",lambda e,d=doc:self._click(e,d))
            widget.bind("<Double-Button-1>",lambda e,d=doc:self._dbl_click(d))
            widget.bind("<Button-3>",lambda e,d=doc:self._ctx(e,d))
            widget.bind("<B1-Motion>",lambda e:self._start_drag(e))
        bind_all(card)

        thumb=self._get_thumb(doc)
        if thumb:
            tl=ctk.CTkLabel(card,text="",image=thumb,width=40)
            tl.grid(row=0,column=0,rowspan=2,padx=(8,4),pady=6)
        else:
            src_icons={"scan":"🖨️","import":"📄","link":"🔗","note":"✏️"}
            ic=src_icons.get(src,"📄")
            tl=ctk.CTkLabel(card,text=ic,width=40,height=40,font=ctk.CTkFont(size=18),
                fg_color=("gray95","#353a4a"),corner_radius=8)
            tl.grid(row=0,column=0,rowspan=2,padx=(8,4),pady=6)
        bind_all(tl)
        # Quell-Badge (kleines Symbol)
        src_badge={"scan":"🖨","import":"📥","link":"🔗","note":"✏"}
        badge=src_badge.get(src,"")
        if badge:
            ctk.CTkLabel(card,text=badge,width=14,font=ctk.CTkFont(size=9),
                text_color=("gray50","gray55")).grid(row=0,column=1,sticky="nw",pady=(8,0))
        # Dateiname + Tags in einer Zeile
        name=doc["original_name"]
        if len(name)>55: name=name[:52]+"..."
        tags=json.loads(doc.get("tags","[]")) if isinstance(doc.get("tags"),str) else []
        tag_text="  🏷 "+" · ".join(tags[:4]) if tags else ""
        name_fr=ctk.CTkFrame(card,fg_color="transparent"); name_fr.grid(row=0,column=2,sticky="w",pady=(6,0))
        nl=ctk.CTkLabel(name_fr,text=name,font=ctk.CTkFont(size=13,weight="bold"),anchor="w")
        nl.pack(side="left"); bind_all(nl)
        if tag_text:
            tgl=ctk.CTkLabel(name_fr,text=tag_text,font=ctk.CTkFont(size=9),
                text_color=("#6b7280","#9ca3af"),fg_color="transparent",anchor="w",cursor="hand2")
            tgl.pack(side="left",padx=(2,0))
            tgl.bind("<Button-1>",lambda e,d=doc:self._quick_tag(d))
            bind_all(tgl)
        bind_all(name_fr)
        sz=f"{doc['file_size']/1048576:.1f}MB" if doc['file_size']>1048576 else f"{doc['file_size']/1024:.0f}KB"
        dt=doc["created_at"][:10] if doc.get("created_at") else ""
        pg=doc.get("page_count",0)
        pg_txt=f" · {pg}S." if pg and pg>0 else ""
        src_labels={"scan":"🖨 Scan","import":"📥 Import","link":"🔗 Verknüpft","note":"✏ Notiz"}
        src_lbl=src_labels.get(src,"")
        ml=ctk.CTkLabel(card,text=f"{src_lbl} · {sz}{pg_txt} · {dt}",font=ctk.CTkFont(size=10),text_color=("gray50","gray55"),anchor="w")
        ml.grid(row=1,column=2,sticky="w",pady=0); bind_all(ml)
        cv=ctk.StringVar(value=doc.get("category","Dokument"))
        ctk.CTkOptionMenu(card,values=get_cat_names(),variable=cv,width=115,height=24,
            font=ctk.CTkFont(size=10),corner_radius=6,fg_color=("gray85","#353a4a"),
            button_color=("gray75","#454a5a"),text_color=("gray10","gray90"),
            dropdown_text_color=("gray10","gray90"),dropdown_fg_color=("white","#2a2e3b"),
            command=lambda v,d=doc:self._upd_cat(d["id"],v)).grid(row=0,column=3,padx=4,pady=(8,0))
        star="★" if doc.get("starred") else "☆"
        sc=("#d97706","#f59e0b") if doc.get("starred") else ("gray60","gray50")
        ctk.CTkButton(card,text=star,width=28,height=24,font=ctk.CTkFont(size=14),
            fg_color="transparent",text_color=sc,hover_color=("gray90","#282c3a"),
            command=lambda d=doc:self._tog_star(d)).grid(row=1,column=3)
    # ─── Click-Logik (SCHNELL – kein Rebuild) ───
    def _click(self,ev,doc):
        ctrl=ev.state & 0x4; shift=ev.state & 0x1
        did=doc["id"]
        if shift and self.last_click_idx is not None:
            ids=[d["id"] for d in self._doc_list]
            try:
                cur_idx=ids.index(did); last_idx=ids.index(self.last_click_idx)
                lo,hi=min(cur_idx,last_idx),max(cur_idx,last_idx)
                for i in range(lo,hi+1): self.sel_ids.add(ids[i])
            except ValueError: self.sel_ids={did}
        elif ctrl:
            if did in self.sel_ids: self.sel_ids.discard(did)
            else: self.sel_ids.add(did)
        else:
            self.sel_ids={did}
        self.last_click_idx=did
        self._drag_active=False
        self._update_sel_visuals()
        if len(self.sel_ids)==1:
            self._show_preview(doc)

    def _start_drag(self,ev):
        """Startet Drag-Modus wenn Dokumente selektiert sind."""
        if not self.sel_ids: return
        self._drag_active=True
        try: self.configure(cursor="plus")
        except Exception: pass
        # Global ButtonRelease binden um Drag zu beenden
        self.bind("<ButtonRelease-1>",self._end_drag,add="+")

    def _end_drag(self,ev=None):
        """Beendet Drag und setzt Cursor zurück."""
        if not getattr(self,"_drag_active",False): return
        self._drag_active=False
        try: self.configure(cursor="")
        except Exception: pass
        self.unbind("<ButtonRelease-1>")

    def _cat_drop(self,cat_name):
        """Drop-Handler: selektierte Dokumente in Kategorie verschieben."""
        if not getattr(self,"_drag_active",False) or not self.sel_ids: return
        n=len(self.sel_ids)
        self._drag_active=False
        try: self.configure(cursor="")
        except Exception: pass
        with get_db() as c:
            for did in self.sel_ids:
                c.execute("UPDATE documents SET category=? WHERE id=?",(cat_name,did))
        logger.info("DnD: %d Dok. → Kategorie '%s'", n, cat_name)
        self.sel_ids.clear(); self.refresh_list(); self._rebuild_cats()

    def _dbl_click(self,doc):
        self._open_file(doc)

    def _update_sel_visuals(self):
        """Nur Rahmenfarbe aktualisieren – KEIN Widget-Rebuild."""
        sel_bc=("#4f8ff7","#4f8ff7"); norm_bc=("gray80","#2a2e3b")
        for did,card in self._cards.items():
            try:
                if did in self.sel_ids:
                    card.configure(border_width=2,border_color=sel_bc)
                else:
                    card.configure(border_width=1,border_color=norm_bc)
            except Exception: pass

    def _ctx(self,ev,doc):
        if doc["id"] not in self.sel_ids:
            self.sel_ids={doc["id"]}; self._update_sel_visuals()
        menu=tk.Menu(self,tearoff=0); n=len(self.sel_ids)
        if n==1:
            menu.add_command(label="📂  Öffnen",command=lambda:self._open_file(doc))
            menu.add_command(label=_t("ctx_print"),command=lambda:self._print_doc(doc))
            if doc.get("source")=="note":
                menu.add_command(label="✏️  Edit Note" if _LANG=="en" else "✏️  Notiz bearbeiten",command=lambda:self._open_note(doc))
            if platform.system()=="Windows" and doc.get("source")!="note":
                show_expl = "📁  Show in Explorer" if _LANG=="en" else "📁  Im Explorer zeigen"
                menu.add_command(label=show_expl,command=lambda:self._show_explorer(doc))
            menu.add_command(label="🔍  Details",command=lambda:self._show_detail(doc))
            if doc.get("file_path","").lower().endswith(".pdf"):
                menu.add_command(label=_t("ctx_rotate180"),command=lambda:self._rotate_pdf(doc))
            menu.add_command(label=_t("ctx_tags_edit"),command=lambda:self._quick_tag(doc))
            menu.add_separator()
        # OCR-Untermenü
        ocr_menu=tk.Menu(menu,tearoff=0)
        ocr_lbl = f"🔄  OCR erneut starten ({n} Dok.)" if n>1 else "🔄  OCR erneut starten"
        ocr_menu.add_command(label=ocr_lbl,command=lambda:self._reprocess_with_progress(list(self.sel_ids)))
        ocr_menu.add_separator()
        ocr_menu.add_command(label=f"{_t('ctx_ocr_lang')} {get_ocr_lang()}",command=self._ocr_settings)
        menu.add_cascade(label=_t("ctx_ocr"),menu=ocr_menu)
        menu.add_separator()
        star_lbl=_t("ctx_fav_remove") if any(d.get("starred") for d in self._doc_list if d["id"] in self.sel_ids) else _t("ctx_fav_add")
        menu.add_command(label=star_lbl,command=self._bulk_star)
        cm=tk.Menu(menu,tearoff=0)
        for c in get_cat_names(): cm.add_command(label=c,command=lambda c=c:self._bulk_cat(c))
        menu.add_cascade(label=_t("ctx_category"),menu=cm)
        # Bulk Tag
        tag_lbl=f"{_t('ctx_tags')} ({n})" if n>1 else _t('ctx_tags_edit')
        menu.add_command(label=tag_lbl,command=lambda:self._bulk_tag())
        menu.add_separator()
        menu.add_command(label=f"{_t('ctx_delete')} ({n})" if n>1 else _t('ctx_delete'),command=self._bulk_del)
        menu.tk_popup(ev.x_root,ev.y_root)

    def _ocr_settings(self):
        """Dialog zum Einstellen der OCR-Sprache (NAPS2)."""
        dlg=ctk.CTkToplevel(self); dlg.title(_t("ctx_ocr_settings")); dlg.geometry("450x300")
        dlg.transient(self); dlg.grab_set()
        ctk.CTkLabel(dlg,text=_t("ocr_running"),font=ctk.CTkFont(size=18,weight="bold")).pack(padx=16,pady=(16,8),anchor="w")
        if NAPS2_EXE:
            ctk.CTkLabel(dlg,text=f"✅ NAPS2: {NAPS2_EXE}",
                font=ctk.CTkFont(size=12),text_color=("green","#34d399")).pack(padx=16,anchor="w")
        else:
            ctk.CTkLabel(dlg,text=_t("ocr_naps2_missing"),
                font=ctk.CTkFont(size=12),text_color=("red","#ef4444")).pack(padx=16,anchor="w")
        ctk.CTkLabel(dlg,text="\n" + _t("sett_language").split("/")[0].strip().split(" ")[-1],font=ctk.CTkFont(size=10,weight="bold"),
            text_color=("gray50","gray55")).pack(padx=16,anchor="w")
        ctk.CTkLabel(dlg,text=_t("ocr_lang_import"),
            font=ctk.CTkFont(size=12)).pack(padx=16,anchor="w")
        lang_var=ctk.StringVar(value=get_ocr_lang())
        ctk.CTkEntry(dlg,textvariable=lang_var,font=ctk.CTkFont(size=14),height=36).pack(fill="x",padx=16,pady=(4,8))
        presets=ctk.CTkFrame(dlg,fg_color="transparent"); presets.pack(fill="x",padx=16,pady=(0,12))
        for lbl,val in [("Deutsch","deu"),("Englisch","eng"),("Französisch","fra"),
                         ("Italienisch","ita"),("Deu+Eng","deu+eng")]:
            ctk.CTkButton(presets,text=lbl,width=80,height=28,font=ctk.CTkFont(size=11),
                fg_color=("gray85","#353a4a"),text_color=("gray10","gray90"),
                command=lambda v=val:lang_var.set(v)).pack(side="left",padx=2)
        def save():
            new_lang=lang_var.get().strip()
            if new_lang:
                set_ocr_lang(new_lang)
                self._s["ocr_lang"]=new_lang; self._save_s()
                messagebox.showinfo("OCR",f"Sprache: {new_lang}")
            dlg.destroy()
        ctk.CTkButton(dlg,text=_t("catmgr_save"),font=ctk.CTkFont(weight="bold"),command=save).pack(pady=12)

    def _reprocess_with_progress(self,doc_ids):
        """OCR für ausgewählte Dokumente mit Fortschrittsanzeige."""
        if not doc_ids: return
        pw=ctk.CTkToplevel(self); pw.title("OCR-Verarbeitung")
        pw.geometry("500x200"); pw.transient(self)

        ctk.CTkLabel(pw,text=f"OCR: {len(doc_ids)} {_t('docs_plural')}",
            font=ctk.CTkFont(size=14,weight="bold")).pack(pady=(16,4))
        self._ocr_status_lbl=ctk.CTkLabel(pw,text="Starte...",font=ctk.CTkFont(size=12),
            text_color=("gray50","gray55"))
        self._ocr_status_lbl.pack(pady=(0,8))
        pb=ctk.CTkProgressBar(pw,width=440); pb.pack(padx=16); pb.set(0)
        count_lbl=ctk.CTkLabel(pw,text="",font=ctk.CTkFont(size=11))
        count_lbl.pack(pady=4)

        lang=get_ocr_lang()

        def do():
            total=len(doc_ids)
            for i,did in enumerate(doc_ids):
                def status(msg,_i=i):
                    self.after(0,lambda:self._ocr_status_lbl.configure(text=msg))
                    self.after(0,lambda:pb.set((_i+0.5)/total))
                    self.after(0,lambda:count_lbl.configure(text=f"{_i+1}/{total}"))

                with get_db() as c:
                    c.execute("UPDATE documents SET processed=0 WHERE id=?",(did,))
                process_document(did,
                    callback=lambda:self.after(0,self.refresh_list),
                    status_cb=status, lang=lang)
                self.after(0,lambda v=(i+1)/total:pb.set(v))

            self.after(0,lambda:self._ocr_status_lbl.configure(text=f"✅ {total} {_t('docs_plural')}"))
            self.after(0,lambda:pb.set(1.0))
            self.after(0,self.refresh_list)
            self.after(0,self.refresh_stats)
            self.after(2000,pw.destroy)

        threading.Thread(target=do,daemon=True).start()
    # ═══════ DOKUMENTE SYNCHRONISIEREN ═══════
    def _sync_docs(self):
        """Prüft alle Dokumente (verknüpft, importiert, gescannt) auf Änderungen."""
        # ═══ Lizenzprüfung ═══
        if not _is_licensed():
            dlg = ctk.CTkToplevel(self)
            dlg.title("🔒 " + _t("sync_title"))
            _set_window_icon(dlg); dlg.transient(self); dlg.grab_set()
            center_window(dlg, 480, 260)
            ctk.CTkLabel(dlg, text="🔒", font=ctk.CTkFont(size=36)).pack(pady=(20, 8))
            ctk.CTkLabel(dlg, text=_t("sync_license"),
                font=ctk.CTkFont(size=12), justify="center",
                text_color=("gray30", "gray70")).pack(padx=24, pady=(0, 12))
            sponsor_txt = "❤️ Sponsoringbeitrag geben..." if _LANG == "de" else "❤️ Make a sponsorship contribution..."
            ctk.CTkButton(dlg, text=sponsor_txt, width=280, height=36,
                font=ctk.CTkFont(size=12, weight="bold"), cursor="hand2",
                fg_color=("#2e86c1", "#2e86c1"), hover_color=("#2471a3", "#2471a3"),
                command=lambda: __import__('webbrowser').open(DONATE_URL)).pack(pady=(0, 8))
            close_txt = "Schliessen" if _LANG == "de" else "Close"
            ctk.CTkButton(dlg, text=close_txt, width=100, height=30,
                fg_color=("gray75", "#353a4a"), text_color=("gray30", "gray80"),
                command=dlg.destroy).pack(pady=(0, 16))
            return

        # ═══ Sync-Dialog ═══
        dlg = ctk.CTkToplevel(self)
        dlg.title(_t("sync_title"))
        _set_window_icon(dlg); dlg.transient(self); dlg.grab_set()
        center_window(dlg, 700, 640)

        ctk.CTkLabel(dlg, text="🔄 " + _t("sync_title"),
            font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(14, 2))
        desc_txt = "Prüft alle Dokumente auf Änderungen (verknüpft, importiert, gescannt)" if _LANG == "de" else "Checks all documents for changes (linked, imported, scanned)"
        ctk.CTkLabel(dlg, text=desc_txt,
            font=ctk.CTkFont(size=10), text_color=("gray50", "gray55")).pack(pady=(0, 6))
        status_lbl = ctk.CTkLabel(dlg, text=_t("sync_scanning"),
            font=ctk.CTkFont(size=12), text_color=("gray40", "gray60"))
        status_lbl.pack(pady=(0, 4))

        pb = ctk.CTkProgressBar(dlg, width=620, mode="determinate")
        pb.pack(padx=24, pady=(0, 4)); pb.set(0)
        progress_detail = ctk.CTkLabel(dlg, text="", font=ctk.CTkFont(size=10),
            text_color=("gray50", "gray55"))
        progress_detail.pack(pady=(0, 6))

        rf = ctk.CTkFrame(dlg, fg_color="transparent"); rf.pack(fill="both", expand=True, padx=16, pady=(0, 4))
        result_tb = tk.Text(rf, wrap="word", font=("Consolas", 10), bg="#f5f5f5", fg="#1a1a1a",
            relief="flat", padx=10, pady=8, highlightthickness=0)
        result_sb = ctk.CTkScrollbar(rf, command=result_tb.yview)
        result_tb.configure(yscrollcommand=result_sb.set)
        result_sb.pack(side="right", fill="y")
        result_tb.pack(fill="both", expand=True)
        result_tb.tag_configure("changed", foreground="#d35400", font=("Consolas", 10, "bold"))
        result_tb.tag_configure("changed_detail", foreground="#b07020")
        result_tb.tag_configure("missing", foreground="#e74c3c")
        result_tb.tag_configure("missing_detail", foreground="#c0392b", font=("Consolas", 9))
        result_tb.tag_configure("ok", foreground="#27ae60")
        result_tb.tag_configure("header", font=("Segoe UI", 12, "bold"))
        result_tb.tag_configure("subheader", font=("Segoe UI", 10, "bold"), foreground="#555")

        btn_fr = ctk.CTkFrame(dlg, fg_color="transparent"); btn_fr.pack(pady=(4, 14))
        reindex_btn = ctk.CTkButton(btn_fr, text=f"🔄 {_t('sync_reindex')}", width=220, height=36,
            font=ctk.CTkFont(size=12, weight="bold"), state="disabled",
            command=lambda: _do_reindex())
        reindex_btn.pack(side="left", padx=6)
        filter_missing_txt = "🔍 Fehlende anzeigen" if _LANG == "de" else "🔍 Show missing"
        filter_btn = ctk.CTkButton(btn_fr, text=filter_missing_txt, width=160, height=36,
            font=ctk.CTkFont(size=11), state="disabled",
            fg_color=("#e74c3c", "#c0392b"), hover_color=("#c0392b", "#a93226"),
            command=lambda: _show_missing())
        filter_btn.pack(side="left", padx=6)
        close_txt = "Schliessen" if _LANG == "de" else "Close"
        ctk.CTkButton(btn_fr, text=close_txt, width=100, height=36,
            fg_color=("gray75", "#353a4a"), text_color=("gray30", "gray80"),
            command=dlg.destroy).pack(side="left", padx=6)

        changed_docs = []
        missing_docs = []

        def _log(text, tag=""):
            self.after(0, lambda: (result_tb.configure(state="normal"),
                                   result_tb.insert("end", text + "\n", tag),
                                   result_tb.see("end"),
                                   result_tb.configure(state="disabled")))

        def _scan():
            with get_db() as c:
                all_docs = [dict(r) for r in c.execute(
                    "SELECT * FROM documents WHERE source IN ('link','import','scan') AND archived=0").fetchall()]

            total = len(all_docs)
            if total == 0:
                self.after(0, lambda: status_lbl.configure(text=_t("sync_none")))
                self.after(0, lambda: pb.pack_forget())
                self.after(0, lambda: progress_detail.pack_forget())
                return

            n_ok = 0; n_changed = 0; n_missing = 0

            for i, doc in enumerate(all_docs):
                fp = doc.get("file_path", "")
                name = doc.get("original_name", Path(fp).name if fp else "?")
                old_hash = doc.get("file_hash", "")

                self.after(0, lambda idx=i, nm=name, t=total: (
                    pb.set((idx + 0.5) / t),
                    progress_detail.configure(text=f"{idx+1}/{t}: {nm[:60]}")
                ))

                if not os.path.isfile(fp):
                    n_missing += 1
                    missing_docs.append(doc)
                    continue

                try:
                    new_hash = compute_hash(fp)
                    new_size = os.path.getsize(fp)
                except Exception:
                    n_missing += 1
                    missing_docs.append(doc)
                    continue

                if new_hash != old_hash:
                    n_changed += 1
                    doc["_new_size"] = new_size
                    changed_docs.append(doc)
                else:
                    n_ok += 1

            def _show_results():
                pb.set(1.0)
                progress_detail.configure(text="")
                result_tb.configure(state="normal"); result_tb.delete("1.0", "end")

                total_lbl = "Documents checked" if _LANG == "en" else "Dokumente geprüft"
                result_tb.insert("end", f"{total_lbl}: {total}\n\n", "header")

                src_icons = {"link": "🔗", "import": "📥", "scan": "🖨"}

                if changed_docs:
                    ch_hdr = f"⚡ {'Changed' if _LANG=='en' else 'Geändert'} ({n_changed}):\n"
                    result_tb.insert("end", ch_hdr, "subheader")
                    for doc in changed_docs:
                        nm = doc.get("original_name", "?")
                        old_sz = doc.get("file_size", 0)
                        new_sz = doc.get("_new_size", 0)
                        icon = src_icons.get(doc.get("source", ""), "📄")
                        result_tb.insert("end", f"  {icon} {nm}\n", "changed")
                        result_tb.insert("end", f"     {old_sz/1024:.0f} KB → {new_sz/1024:.0f} KB\n", "changed_detail")
                        result_tb.insert("end", f"     {doc.get('file_path','')}\n\n", "changed_detail")
                    reindex_btn.configure(state="normal")

                if missing_docs:
                    ms_hdr = f"✗ {'Missing' if _LANG=='en' else 'Nicht gefunden'} ({n_missing}):\n"
                    result_tb.insert("end", ms_hdr, "subheader")
                    for doc in missing_docs:
                        nm = doc.get("original_name", "?")
                        icon = src_icons.get(doc.get("source", ""), "📄")
                        result_tb.insert("end", f"  {icon} ✗ {nm}\n", "missing")
                        result_tb.insert("end", f"     {doc.get('file_path','')}\n\n", "missing_detail")
                    filter_btn.configure(state="normal")

                result_tb.insert("end", "\n", "")
                sum_hdr = "Summary:" if _LANG == "en" else "Zusammenfassung:"
                result_tb.insert("end", f"{sum_hdr}\n", "subheader")
                result_tb.insert("end", f"  ✅ {'Up to date' if _LANG=='en' else 'Aktuell'}: {n_ok}\n", "ok")
                if n_changed:
                    result_tb.insert("end", f"  ⚡ {'Changed' if _LANG=='en' else 'Geändert'}: {n_changed}\n", "changed")
                if n_missing:
                    result_tb.insert("end", f"  ✗ {'Missing' if _LANG=='en' else 'Fehlt'}: {n_missing}\n", "missing")

                result_tb.configure(state="disabled")
                result_tb.see("1.0")

                if not n_changed and not n_missing:
                    status_lbl.configure(text=_t("sync_none"))
                    pb.pack_forget()
                elif n_changed:
                    status_lbl.configure(text=_t("sync_found").format(n=n_changed))
                else:
                    status_lbl.configure(text=_t("sync_missing").format(n=n_missing))

            self.after(0, _show_results)

        def _do_reindex():
            if not changed_docs: return
            reindex_btn.configure(state="disabled"); filter_btn.configure(state="disabled")
            pb.configure(mode="determinate"); pb.set(0)
            lang = get_ocr_lang()

            def _reindex():
                total = len(changed_docs)
                for i, doc in enumerate(changed_docs):
                    did = doc["id"]; fp = doc.get("file_path", "")
                    name = doc.get("original_name", "?")

                    self.after(0, lambda idx=i, nm=name, t=total: (
                        status_lbl.configure(text=_t("sync_progress").format(i=idx+1, n=t, name=nm[:40])),
                        pb.set((idx + 0.5) / t),
                        progress_detail.configure(text=f"OCR + Index: {nm[:50]}")
                    ))

                    try:
                        new_hash = compute_hash(fp)
                        new_size = os.path.getsize(fp)
                        with get_db() as c:
                            c.execute("UPDATE documents SET file_hash=?, file_size=?, processed=0, updated_at=CURRENT_TIMESTAMP WHERE id=?",
                                (new_hash, new_size, did))
                    except Exception as e:
                        logger.warning("Sync hash update #%d: %s", did, e)

                    process_document(did,
                        callback=lambda: None,
                        status_cb=lambda msg: None,
                        lang=lang)

                    self.after(0, lambda v=(i+1)/total: pb.set(v))
                    logger.info("Sync re-indexed: #%d %s", did, name)

                def _done():
                    pb.set(1.0)
                    status_lbl.configure(text=_t("sync_done").format(n=total))
                    progress_detail.configure(text="")
                    self._sort = "updated_desc"
                    self._lc["sort"] = self._sort; self._save_lc()
                    try: self._sort_om.set(self._sort_rmap.get("updated_desc", _t("sort_updated")))
                    except Exception: pass
                    self.current_cat = ""; self.current_star = False; self._page = 0
                    self.lhdr.configure(text=_t("all_docs"))
                    self._show("list")
                    self.refresh_list(); self._rebuild_cats(); self.refresh_stats()
                    result_tb.configure(state="normal")
                    sort_hint = "Sorted by: Recently updated" if _LANG == "en" else "Sortierung: Zuletzt geändert"
                    result_tb.insert("end", f"\n\n✅ {total} {'documents re-indexed' if _LANG=='en' else 'Dokumente neu indexiert'}\n", "ok")
                    result_tb.insert("end", f"📋 {sort_hint}\n", "ok")
                    result_tb.configure(state="disabled")
                    result_tb.see("end")

                self.after(0, _done)

            threading.Thread(target=_reindex, daemon=True).start()

        def _show_missing():
            self._missing_link_ids = {d["id"] for d in missing_docs}
            dlg.destroy()
            self.current_cat = "__missing_links__"
            self.current_star = False
            self._page = 0
            hdr = "🔍 Missing Files" if _LANG == "en" else "🔍 Fehlende Dateien"
            self.lhdr.configure(text=hdr)
            self._show("list")
            self.refresh_list()

        threading.Thread(target=_scan, daemon=True).start()

    def _bulk_star(self):
        changed_ids = set(self.sel_ids)
        with get_db() as c:
            for did in self.sel_ids:
                d=c.execute("SELECT starred FROM documents WHERE id=?",(did,)).fetchone()
                if d: c.execute("UPDATE documents SET starred=? WHERE id=?",(0 if d["starred"] else 1,did))
        # Lokale doc_list aktualisieren
        for d in self._doc_list:
            if d["id"] in changed_ids:
                d["starred"] = 0 if d.get("starred") else 1
        self.sel_ids.clear()
        self.refresh_list()
        self._rebuild_cats()
        # Vorschau aktualisieren wenn betroffen
        if self._preview_doc and self._preview_doc["id"] in changed_ids:
            self._render_preview()
    def _bulk_cat(self,cat):
        changed_ids = set(self.sel_ids)
        with get_db() as c:
            for did in self.sel_ids: c.execute("UPDATE documents SET category=? WHERE id=?",(cat,did))
        # Lokale doc_list aktualisieren
        for d in self._doc_list:
            if d["id"] in changed_ids:
                d["category"] = cat
        self.sel_ids.clear()
        self.refresh_list()
        self._rebuild_cats()
        self.refresh_stats()
        # Vorschau aktualisieren wenn betroffen
        if self._preview_doc and self._preview_doc["id"] in changed_ids:
            self._preview_doc["category"] = cat
            self._render_preview()
    def _bulk_tag(self):
        """Tags für mehrere Dokumente gleichzeitig bearbeiten."""
        n=len(self.sel_ids)
        dlg=ctk.CTkToplevel(self); dlg.title(f"Tags – {n} Dokument(e)")
        dlg.transient(self); dlg.grab_set(); center_window(dlg,450,200)
        ctk.CTkLabel(dlg,text=f"{_t('tags_edit')}: {n} {_t('docs_plural')}",
            font=ctk.CTkFont(size=14,weight="bold")).pack(padx=12,pady=(12,4))
        ctk.CTkLabel(dlg,text=_t("tags_add_hint"),
            font=ctk.CTkFont(size=11),text_color=("gray50","gray55")).pack(padx=12)
        tv=ctk.StringVar()
        e=ctk.CTkEntry(dlg,textvariable=tv,font=ctk.CTkFont(size=12),height=34,
            placeholder_text=_t("tags_add_ph"))
        e.pack(fill="x",padx=12,pady=8); e.focus()
        bf=ctk.CTkFrame(dlg,fg_color="transparent"); bf.pack(pady=6)
        def add_tags():
            new=[t.strip() for t in tv.get().replace(";",",").split(",") if t.strip()]
            if not new: dlg.destroy(); return
            with get_db() as c:
                for did in self.sel_ids:
                    row=c.execute("SELECT tags FROM documents WHERE id=?",(did,)).fetchone()
                    existing=json.loads(row["tags"] or "[]") if row else []
                    merged=list(dict.fromkeys(existing+new))  # Deduplizieren, Reihenfolge beibehalten
                    c.execute("UPDATE documents SET tags=? WHERE id=?",(json.dumps(merged),did))
            dlg.destroy(); self.refresh_list()
        def replace_tags():
            new=[t.strip() for t in tv.get().replace(";",",").split(",") if t.strip()]
            with get_db() as c:
                for did in self.sel_ids:
                    c.execute("UPDATE documents SET tags=? WHERE id=?",(json.dumps(new),did))
            dlg.destroy(); self.refresh_list()
        e.bind("<Return>",lambda ev:add_tags())
        ctk.CTkButton(bf,text=_t("tags_add_btn"),width=130,height=32,command=add_tags).pack(side="left",padx=4)
        ctk.CTkButton(bf,text=_t("tags_replace_btn"),width=130,height=32,
            fg_color=("gray80","#353a4a"),text_color=("gray20","gray80"),
            command=replace_tags).pack(side="left",padx=4)
    def _bulk_del(self):
        n=len(self.sel_ids)
        if n==0: return
        # Details sammeln für die Sicherheitsabfrage
        docs_to_del = [d for d in self._doc_list if d["id"] in self.sel_ids]
        copied = [d for d in docs_to_del if d.get("source") not in ("link","note")]
        linked = [d for d in docs_to_del if d.get("source") == "link"]
        notes  = [d for d in docs_to_del if d.get("source") == "note"]
        # Dateinamen für Anzeige (max 8)
        names = [d.get("original_name","?") for d in docs_to_del[:8]]
        if n > 8: names.append(f"... und {n-8} weitere")
        name_list = "\n".join(f"  • {nm}" for nm in names)
        # Warntext
        warn_parts = [f"{n} Dokument(e) endgültig löschen?\n"]
        warn_parts.append(name_list)
        warn_parts.append("")
        if copied:
            warn_parts.append(f"⚠️ {len(copied)} Datei(en) werden von der Festplatte gelöscht!")
        if linked:
            warn_parts.append(f"🔗 {len(linked)} Verknüpfung(en) – Originaldateien bleiben erhalten.")
        if notes:
            warn_parts.append(f"✏️ {len(notes)} Notiz(en) werden gelöscht.")
        warn_parts.append("\nDieser Vorgang kann NICHT rückgängig gemacht werden!")
        warn_msg = "\n".join(warn_parts)
        # Sicherheitsabfrage: Ja/Nein/Abbrechen (Abbrechen=Backup)
        ans = messagebox.askyesnocancel("⚠️ Endgültig löschen", warn_msg)
        if ans is None: return  # Abbrechen
        if ans is False:
            # "Nein" = Zuerst Backup, dann nochmal fragen
            self._do_backup()
            if not messagebox.askyesno("Löschen nach Backup",
                f"Backup erstellt.\n\nJetzt {n} Dokument(e) endgültig löschen?"):
                return
        # UI sofort aktualisieren
        for did in list(self.sel_ids):
            if did in self._cards:
                try: self._cards[did].destroy()
                except Exception: pass
                del self._cards[did]
        ids_to_del=list(self.sel_ids)
        self.sel_ids.clear()
        self._doc_list=[d for d in self._doc_list if d["id"] not in ids_to_del]
        def do_del():
            for did in ids_to_del: delete_doc_complete(did)
            self.after(0,self.refresh_stats)
            self.after(0,self._rebuild_cats)
        threading.Thread(target=do_del,daemon=True).start()
    def _upd_cat(self,did,v):
        with get_db() as c: c.execute("UPDATE documents SET category=? WHERE id=?",(v,did))
        # Lokale doc_list aktualisieren
        for d in self._doc_list:
            if d["id"] == did: d["category"] = v; break
        self._rebuild_cats(); self.refresh_stats()
        # Vorschau aktualisieren wenn betroffen
        if self._preview_doc and self._preview_doc["id"] == did:
            self._preview_doc["category"] = v
            self._render_preview()
    def _upd_tags(self,did,tags_str):
        """Speichert benutzerdefinierte Tags für ein Dokument."""
        tags=[t.strip() for t in tags_str.replace(";",",").split(",") if t.strip()]
        with get_db() as c:
            c.execute("UPDATE documents SET tags=? WHERE id=?",(json.dumps(tags),did))
        index_document(did, " ".join(tags))
        return tags
    def _quick_tag(self,doc):
        """Schnell-Tag-Editor als Popup."""
        tags=json.loads(doc.get("tags","[]")) if isinstance(doc.get("tags"),str) else []
        dlg=ctk.CTkToplevel(self); dlg.title("Tags bearbeiten")
        dlg.transient(self); dlg.grab_set()
        center_window(dlg,400,130)
        ctk.CTkLabel(dlg,text=f"Tags: {doc['original_name'][:40]}",
            font=ctk.CTkFont(size=13,weight="bold")).pack(padx=12,pady=(10,4),anchor="w")
        tv=ctk.StringVar(value=", ".join(tags))
        e=ctk.CTkEntry(dlg,textvariable=tv,font=ctk.CTkFont(size=12),height=34,
            placeholder_text=_t("doc_tags_ph"))
        e.pack(fill="x",padx=12,pady=4); e.focus()
        def save(ev=None):
            new_tags=self._upd_tags(doc["id"],tv.get())
            doc["tags"]=json.dumps(new_tags)
            dlg.destroy(); self.refresh_list()
        e.bind("<Return>",save)
        ctk.CTkButton(dlg,text=_t("catmgr_save"),width=100,height=30,command=save).pack(pady=6)
    def _tog_star(self,doc):
        new_val=0 if doc.get("starred") else 1
        doc["starred"]=new_val
        with get_db() as c: c.execute("UPDATE documents SET starred=? WHERE id=?",(new_val,doc["id"]))
        self.refresh_list()
        self._rebuild_cats()
        if self._preview_doc and self._preview_doc["id"] == doc["id"]:
            self._render_preview()
    def _open_file(self,doc):
        if doc.get("source")=="note": self._open_note(doc); return
        p=doc.get("file_path","")
        if not os.path.isfile(p):
            messagebox.showerror("Fehler",f"Nicht gefunden:\n{p}"); return
        # WebP → interner Viewer (Windows kann mehrseitige WebP nicht nativ)
        if p.lower().endswith(".webp"):
            self._view_webp(doc); return
        if platform.system()=="Windows": os.startfile(p)
        else: subprocess.Popen(["xdg-open",p])
    def _show_explorer(self,doc):
        p=doc.get("file_path","")
        if os.path.isfile(p):
            p = os.path.normpath(p)
            subprocess.Popen(f'explorer /select,"{p}"')
    def _rotate_pdf(self,doc):
        """PDF 180° drehen und speichern."""
        fp=doc.get("file_path","")
        if not fp or not os.path.isfile(fp):
            messagebox.showerror("Fehler","Datei nicht gefunden."); return
        if not HAS_FITZ:
            messagebox.showerror("Fehler","PyMuPDF nicht installiert."); return
        is_link = doc.get("source")=="link"
        if is_link:
            if not messagebox.askyesno("Verknüpfte Datei",
                f"Diese Datei ist nur verknüpft und liegt ausserhalb von DocVault:\n\n"
                f"{fp}\n\nDie Original-Datei wird überschrieben!\nFortfahren?"):
                return
        try:
            pdf=fitz.open(fp)
            for page in pdf:
                page.set_rotation((page.rotation + 180) % 360)
            pdf.save(fp, incremental=True, encryption=0)
            pdf.close()
            # Thumbnail neu erstellen
            tp=THUMB_DIR/f"{doc['id']}.png"
            if tp.exists():
                try: tp.unlink()
                except: pass
            gen_thumb(fp,doc["id"])
            logger.info("PDF gedreht (180°): %s", Path(fp).name)
            self.refresh_list()
            # OCR erneut ausführen?
            if messagebox.askyesno("PDF gedreht",
                f"✅ PDF wurde 180° gedreht:\n{Path(fp).name}\n\n"
                f"OCR-Texterkennung erneut ausführen?\n"
                f"(Empfohlen – verbessert die Textqualität nach Drehung)"):
                self._reprocess_with_progress([doc["id"]])
        except Exception as e:
            logger.error("PDF drehen: %s",e,exc_info=True)
            messagebox.showerror("Fehler",f"PDF konnte nicht gedreht werden:\n{e}")

    def _print_doc(self,doc):
        """Dokument drucken."""
        p=doc.get("file_path","")
        if doc.get("source")=="note":
            import tempfile
            title=doc.get("original_name","Notiz")
            content=doc.get("ocr_text","")
            html=f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title>
<style>body{{font-family:'Segoe UI',Arial;font-size:12pt;margin:2cm;line-height:1.6;}}
h1{{font-size:20pt;border-bottom:1px solid #ccc;padding-bottom:8px;}}
</style></head><body><h1>{title}</h1>
<pre style="font-family:inherit;white-space:pre-wrap;">{content.replace('<','&lt;')}</pre>
<script>window.onload=function(){{window.print()}}</script></body></html>"""
            tmp=os.path.join(tempfile.gettempdir(),"docvault_print.html")
            with open(tmp,"w",encoding="utf-8") as f: f.write(html)
            if platform.system()=="Windows":
                try: os.startfile(tmp)
                except OSError: import webbrowser; webbrowser.open(tmp)
        elif os.path.isfile(p) and p.lower().endswith(".webp"):
            self._print_webp(p, doc.get("original_name","WebP"))
        elif os.path.isfile(p):
            if platform.system()=="Windows":
                try: os.startfile(p,"print")
                except OSError: os.startfile(p)

    def _print_webp(self, filepath, title="WebP"):
        """Druckt ein mehrseitiges WebP als HTML – eine Seite pro Bild, keine Leerseiten."""
        import tempfile, base64 as b64mod
        from io import BytesIO
        n = webp_page_count(filepath)
        img_tags = []
        for i in range(n):
            pil = webp_get_page(filepath, i)
            if pil:
                buf = BytesIO(); pil.save(buf, "PNG"); buf.seek(0)
                b64 = b64mod.b64encode(buf.read()).decode()
                # Nur zwischen Seiten umbrechen, nicht nach der letzten
                cls = "page" if i < n - 1 else "page last"
                img_tags.append(f'<div class="{cls}"><img src="data:image/png;base64,{b64}"></div>')
        html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title>
<style>
@page {{ margin: 5mm; }}
* {{ margin: 0; padding: 0; }}
body {{ margin: 0; padding: 0; }}
.page {{ page-break-after: always; display: flex; justify-content: center; align-items: flex-start; }}
.page.last {{ page-break-after: avoid; }}
.page img {{ max-width: 100%; max-height: 100vh; width: auto; height: auto; display: block; }}
</style></head><body>
{"".join(img_tags)}
<script>window.onload=function(){{window.print()}}</script></body></html>"""
        tmp = os.path.join(tempfile.gettempdir(), "docvault_webp_print.html")
        with open(tmp, "w", encoding="utf-8") as f: f.write(html)
        if platform.system() == "Windows":
            try: os.startfile(tmp)
            except OSError: import webbrowser; webbrowser.open(tmp)
        else: subprocess.Popen(["xdg-open", tmp])
    def _view_webp(self, doc):
        """Vollbild-Viewer für mehrseitige WebP-Dokumente."""
        fp = doc.get("file_path", "")
        if not os.path.isfile(fp): return
        total = webp_page_count(fp)
        name = doc.get("original_name", Path(fp).name)

        vw = ctk.CTkToplevel(self)
        vw.title(f"DocVault – {name}")
        _set_window_icon(vw)
        vw.transient(self)
        center_window(vw, 820, 700)
        vw.grid_rowconfigure(1, weight=1)
        vw.grid_columnconfigure(0, weight=1)

        # State
        cur_page = [0]
        zoom = [1.0]
        vw._img_ref = None

        # ═══ Toolbar ═══
        tb = ctk.CTkFrame(vw, height=40, fg_color=("gray90", "#21242f"), corner_radius=0)
        tb.grid(row=0, column=0, sticky="ew")
        bs = {"height": 30, "corner_radius": 6, "font": ctk.CTkFont(size=11),
              "fg_color": ("gray80", "#353a4a"), "text_color": ("gray20", "gray80")}

        ctk.CTkButton(tb, text="◀◀", width=36, command=lambda: _go(0), **bs).pack(side="left", padx=(8,2), pady=5)
        ctk.CTkButton(tb, text="◀", width=36, command=lambda: _go(cur_page[0]-1), **bs).pack(side="left", padx=2, pady=5)
        page_lbl = ctk.CTkLabel(tb, text=f"1 / {total}", font=ctk.CTkFont(size=12, weight="bold"), width=80)
        page_lbl.pack(side="left", padx=6, pady=5)
        ctk.CTkButton(tb, text="▶", width=36, command=lambda: _go(cur_page[0]+1), **bs).pack(side="left", padx=2, pady=5)
        ctk.CTkButton(tb, text="▶▶", width=36, command=lambda: _go(total-1), **bs).pack(side="left", padx=2, pady=5)

        # Separator
        ctk.CTkFrame(tb, width=1, height=22, fg_color=("gray70", "#454a5a")).pack(side="left", padx=8, pady=9)

        # Zoom
        ctk.CTkButton(tb, text="−", width=32, command=lambda: _zoom(-0.2), **bs).pack(side="left", padx=2, pady=5)
        zoom_lbl = ctk.CTkLabel(tb, text="100%", font=ctk.CTkFont(size=11), width=50)
        zoom_lbl.pack(side="left", padx=4, pady=5)
        ctk.CTkButton(tb, text="+", width=32, command=lambda: _zoom(0.2), **bs).pack(side="left", padx=2, pady=5)
        fit_txt = "Fit" if _LANG == "en" else "Einpassen"
        ctk.CTkButton(tb, text=fit_txt, width=60, command=lambda: _fit(), **bs).pack(side="left", padx=4, pady=5)

        ctk.CTkFrame(tb, width=1, height=22, fg_color=("gray70", "#454a5a")).pack(side="left", padx=8, pady=9)

        # Print + Info
        pr_txt = "🖨 Print" if _LANG == "en" else "🖨 Drucken"
        ctk.CTkButton(tb, text=pr_txt, width=80, command=lambda: self._print_webp(fp, name), **bs).pack(side="left", padx=4, pady=5)

        info_lbl = ctk.CTkLabel(tb, text=f"{total} {'pages' if _LANG=='en' else 'Seiten'}",
            font=ctk.CTkFont(size=10), text_color=("gray50", "gray55"))
        info_lbl.pack(side="right", padx=12, pady=5)

        # ═══ Canvas für Bild-Anzeige mit Scrollbars ═══
        canvas_fr = ctk.CTkFrame(vw, fg_color=("gray85", "#0f1117"), corner_radius=0)
        canvas_fr.grid(row=1, column=0, sticky="nsew")
        canvas_fr.grid_rowconfigure(0, weight=1)
        canvas_fr.grid_columnconfigure(0, weight=1)

        canvas = tk.Canvas(canvas_fr, bg="#2a2d37", highlightthickness=0)
        h_scroll = tk.Scrollbar(canvas_fr, orient="horizontal", command=canvas.xview)
        v_scroll = tk.Scrollbar(canvas_fr, orient="vertical", command=canvas.yview)
        canvas.configure(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)
        canvas.grid(row=0, column=0, sticky="nsew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        h_scroll.grid(row=1, column=0, sticky="ew")

        # ═══ Seite rendern ═══
        def _render():
            pil = webp_get_page(fp, cur_page[0])
            if not pil: return
            # Zoom anwenden
            zw = max(32, int(pil.width * zoom[0]))
            zh = max(32, int(pil.height * zoom[0]))
            pil_z = pil.resize((zw, zh), Image.LANCZOS)
            tk_img = ImageTk.PhotoImage(pil_z)
            vw._img_ref = tk_img
            canvas.delete("all")
            canvas.create_image(zw // 2, zh // 2, image=tk_img, anchor="center")
            canvas.configure(scrollregion=(0, 0, zw, zh))
            page_lbl.configure(text=f"{cur_page[0]+1} / {total}")
            zoom_lbl.configure(text=f"{int(zoom[0]*100)}%")

        def _go(page):
            cur_page[0] = max(0, min(page, total - 1))
            _render()

        def _zoom(delta):
            zoom[0] = max(0.1, min(zoom[0] + delta, 5.0))
            _render()

        def _fit():
            pil = webp_get_page(fp, cur_page[0])
            if not pil: return
            cw = canvas.winfo_width() or 780
            ch = canvas.winfo_height() or 600
            scale_w = cw / pil.width if pil.width > 0 else 1
            scale_h = ch / pil.height if pil.height > 0 else 1
            zoom[0] = min(scale_w, scale_h, 3.0)
            _render()

        # Tastatur-Navigation
        def _on_key(ev):
            if ev.keysym in ("Left", "Prior"): _go(cur_page[0] - 1)
            elif ev.keysym in ("Right", "Next"): _go(cur_page[0] + 1)
            elif ev.keysym == "Home": _go(0)
            elif ev.keysym == "End": _go(total - 1)
            elif ev.keysym == "plus" or ev.keysym == "KP_Add": _zoom(0.2)
            elif ev.keysym == "minus" or ev.keysym == "KP_Subtract": _zoom(-0.2)
        vw.bind("<Key>", _on_key)

        # Mausrad zum Scrollen / Zoom mit Ctrl
        def _on_mousewheel(ev):
            if ev.state & 0x4:  # Ctrl gedrückt
                _zoom(0.1 if ev.delta > 0 else -0.1)
            else:
                canvas.yview_scroll(-1 if ev.delta > 0 else 1, "units")
        canvas.bind("<MouseWheel>", _on_mousewheel)

        # Erste Seite rendern (verzögert damit Canvas-Grösse bekannt ist)
        vw.after(100, _fit)

    def _open_note(self,doc=None):
        NoteEditor(self,on_save=lambda:(self.refresh_list(),self.refresh_stats()),edit_doc=doc)
    def _show_detail(self,doc):
        with get_db() as c:
            f=c.execute("SELECT * FROM documents WHERE id=?",(doc["id"],)).fetchone()
            if not f: return
            doc=dict(f)
        win=ctk.CTkToplevel(self); win.title(f"Details: {doc['original_name']}")
        _set_window_icon(win)
        win.transient(self)
        cfg=load_ini(); restore_geometry(cfg,"detail",win,"700x600")
        win.protocol("WM_DELETE_WINDOW",lambda:(save_geometry(cfg,"detail",win),win.destroy()))
        sc=ctk.CTkScrollableFrame(win,fg_color="transparent"); sc.pack(fill="both",expand=True,padx=16,pady=16)
        ctk.CTkLabel(sc,text=doc["original_name"],font=ctk.CTkFont(size=16,weight="bold"),wraplength=650).pack(anchor="w")
        sz=f"{doc['file_size']/1048576:.1f}MB" if doc['file_size']>1048576 else f"{doc['file_size']/1024:.0f}KB"
        src={"link":"🔗 Verknüpft","note":"✏️ Notiz"}.get(doc.get("source",""),"📋 Kopiert")
        ctk.CTkLabel(sc,text=f"{src} · {sz} · {doc['created_at'][:16]}",font=ctk.CTkFont(size=11),
            text_color=("gray50","gray55")).pack(anchor="w",pady=(4,2))
        ctk.CTkLabel(sc,text=f"📂 {doc.get('file_path','')}",font=ctk.CTkFont(size=10),
            text_color=("gray50","gray50"),wraplength=650).pack(anchor="w",pady=(0,12))
        bf=ctk.CTkFrame(sc,fg_color="transparent"); bf.pack(fill="x",pady=(0,12))
        ctk.CTkButton(bf,text=_t("doc_open"),width=80,command=lambda:self._open_file(doc)).pack(side="left",padx=(0,6))
        ctk.CTkButton(bf,text=_t("doc_backup"),width=80,fg_color=("gray75","#353a4a"),text_color=("gray20","gray80"),
            command=self._do_backup).pack(side="left",padx=(0,6))
        def _del_from_detail():
            src = doc.get("source","import")
            name = doc.get("original_name","?")
            msg = f"Dokument endgültig löschen?\n\n  {name}\n\n"
            if src != "link":
                msg += "⚠️ Die Datei wird von der Festplatte gelöscht!\n"
            else:
                msg += "🔗 Verknüpfung wird entfernt (Originaldatei bleibt).\n"
            msg += "\nDieser Vorgang kann NICHT rückgängig gemacht werden!"
            if not messagebox.askyesno("⚠️ Endgültig löschen", msg): return
            delete_doc_complete(doc["id"]); win.destroy()
            self.refresh_list(); self.refresh_stats(); self._rebuild_cats()
        ctk.CTkButton(bf,text=_t("doc_delete"),width=80,fg_color=("#fecaca","#3b2020"),text_color=("#dc2626","#ef4444"),
            command=_del_from_detail).pack(side="left")
        # Kategorie in Detail
        ctk.CTkLabel(sc,text=_t("doc_meta_cat").upper().rstrip(":"),font=ctk.CTkFont(size=10,weight="bold"),text_color=("gray50","gray55")).pack(anchor="w",pady=(8,2))
        cv=ctk.StringVar(value=doc.get("category","Dokument"))
        ctk.CTkOptionMenu(sc,values=get_cat_names(),variable=cv,width=200,
            fg_color=("#e8eef8","#353a4a"),button_color=("#d0daf0","#454a5a"),
            text_color=("gray10","gray90"),dropdown_text_color=("gray10","gray90"),
            dropdown_fg_color=("#f8faff","#2a2e3b"),
            command=lambda v:self._upd_cat(doc["id"],v)).pack(anchor="w")
        conf=doc.get("confidence",0)
        if conf: ctk.CTkLabel(sc,text=f"Konfidenz: {int(conf*100)}%",font=ctk.CTkFont(size=11),
            text_color=("gray50","gray55")).pack(anchor="w",pady=(2,0))
        tags=json.loads(doc.get("tags","[]")) if isinstance(doc.get("tags"),str) else []
        ctk.CTkLabel(sc,text="TAGS",font=ctk.CTkFont(size=10,weight="bold"),
            text_color=("gray50","gray55")).pack(anchor="w",pady=(8,2))
        tag_fr=ctk.CTkFrame(sc,fg_color="transparent"); tag_fr.pack(fill="x")
        tag_var=ctk.StringVar(value=", ".join(tags))
        tag_entry=ctk.CTkEntry(tag_fr,textvariable=tag_var,font=ctk.CTkFont(size=11),
            height=30,placeholder_text=_t("doc_tags_ph"))
        tag_entry.pack(side="left",fill="x",expand=True)
        def save_tags(ev=None):
            new_tags=self._upd_tags(doc["id"],tag_var.get())
            tag_var.set(", ".join(new_tags))
        tag_entry.bind("<Return>",save_tags)
        tag_entry.bind("<FocusOut>",save_tags)
        ctk.CTkButton(tag_fr,text="💾",width=32,height=30,fg_color=("gray85","#353a4a"),
            text_color=("gray20","gray80"),command=save_tags).pack(side="right",padx=(4,0))
        ctk.CTkLabel(sc,text="OCR-TEXT",font=ctk.CTkFont(size=10,weight="bold"),text_color=("gray50","gray55")).pack(anchor="w",pady=(8,2))
        ob=ctk.CTkTextbox(sc,height=250,font=ctk.CTkFont(family="Consolas",size=11),
            corner_radius=8,fg_color=("gray95","#171921")); ob.pack(fill="both",expand=True)
        ob.insert("1.0",(doc.get("ocr_text","") or "(Kein Text)")[:10000]); ob.configure(state="disabled")
    def _reprocess(self,doc):
        self._reprocess_with_progress([doc["id"]])
    def refresh_stats(self):
        with get_db() as c:
            t=c.execute("SELECT COUNT(*) FROM documents WHERE archived=0").fetchone()[0]
            s=c.execute("SELECT COALESCE(SUM(file_size),0) FROM documents WHERE archived=0").fetchone()[0]
        self.stat_lbl.configure(text=f"{t} Dok · {s/(1024*1024):.1f} MB")
    def _do_backup(self):
        # Erst Dateianzahl zählen für realistische Fortschrittsanzeige
        file_count=sum(1 for _,_,files in os.walk(str(DATA_DIR)) for f in files)
        for lf in [LOCAL_SETTINGS_PATH, _path_cfg_file]:
            if lf.exists(): file_count+=1
        size_mb=sum(fp.stat().st_size for fp in DATA_DIR.rglob("*") if fp.is_file())/(1024*1024)

        pw=ctk.CTkToplevel(self); pw.title("Backup")
        pw.transient(self); pw.grab_set()
        center_window(pw,480,200)
        ctk.CTkLabel(pw,text=_t("backup_creating"),
            font=ctk.CTkFont(size=16,weight="bold")).pack(pady=(16,4))
        info_lbl=ctk.CTkLabel(pw,text=f"{file_count} {_t('files')} · {size_mb:.1f} MB",
            font=ctk.CTkFont(size=11),text_color=("gray50","gray55"))
        info_lbl.pack()
        pb=ctk.CTkProgressBar(pw,width=400); pb.pack(padx=20,pady=(10,4)); pb.set(0)
        status_lbl=ctk.CTkLabel(pw,text="Starte...",font=ctk.CTkFont(size=11),
            text_color=("gray50","gray55")); status_lbl.pack()

        def prog(cur,total):
            v=cur/total if total else 0
            self.after(0,lambda:pb.set(v))
            self.after(0,lambda:status_lbl.configure(text=f"{int(v*100)}%  ({cur}/{total} {_t('files')})"))

        def do():
            p=create_backup(progress_cb=prog)
            self.after(0,lambda: self._backup_done(pw,p))

        threading.Thread(target=do,daemon=True).start()

    def _backup_done(self,pw,backup_path):
        """Zeigt Backup-Ergebnis mit 'Ordner öffnen' Button."""
        for w in pw.winfo_children(): w.destroy()
        if backup_path:
            size_mb=os.path.getsize(backup_path)/(1024*1024)
            ctk.CTkLabel(pw,text=_t("backup_ok"),
                font=ctk.CTkFont(size=16,weight="bold"),
                text_color=("green","#34d399")).pack(pady=(16,4))
            ctk.CTkLabel(pw,text=f"{backup_path}\n({size_mb:.1f} MB)",
                font=ctk.CTkFont(size=11),text_color=("gray50","gray55"),
                wraplength=440).pack(padx=16)
            btn_fr=ctk.CTkFrame(pw,fg_color="transparent"); btn_fr.pack(pady=16)
            ctk.CTkButton(btn_fr,text=_t("backup_show"),width=220,height=36,
                command=lambda: self._show_in_explorer(backup_path)).pack(side="left",padx=6)
            ctk.CTkButton(btn_fr,text="OK",width=80,height=36,
                fg_color=("gray75","#353a4a"),text_color=("gray20","gray80"),
                command=pw.destroy).pack(side="left",padx=6)
        else:
            ctk.CTkLabel(pw,text=_t("backup_fail"),
                font=ctk.CTkFont(size=16,weight="bold"),
                text_color=("red","#ef4444")).pack(pady=(16,4))
            ctk.CTkLabel(pw,text=_t("backup_fail_hint"),
                font=ctk.CTkFont(size=11),text_color=("gray50","gray55"),wraplength=400).pack(padx=16)
            ctk.CTkButton(pw,text="OK",width=80,height=36,command=pw.destroy).pack(pady=16)

    def _show_in_explorer(self, filepath):
        """Öffnet den Explorer und markiert die Datei."""
        if platform.system()=="Windows":
            fp = os.path.normpath(filepath)
            subprocess.Popen(f'explorer /select,"{fp}"')
        else:
            subprocess.Popen(["xdg-open",os.path.dirname(filepath)])
    # Import
    def _setup_dnd(self):
        """Drag & Drop registrieren – windnd mit thread-sicherer Queue."""
        import queue
        self._drop_queue = queue.Queue()

        try:
            import windnd
            # windnd Callback läuft in COM-Thread → KEINE Tkinter-Aufrufe!
            # Nur in Queue schreiben, Hauptthread pollt.
            def on_drop(paths):
                str_paths = []
                for p in paths:
                    if isinstance(p, bytes):
                        # Windows: Pfade kommen in System-Codepage (oft cp1252/cp850)
                        for enc in ["utf-8", "cp1252", "cp850", "latin-1"]:
                            try:
                                decoded = p.decode(enc)
                                if os.path.exists(decoded):
                                    p = decoded; break
                            except (UnicodeDecodeError, OSError): continue
                        else:
                            p = p.decode("utf-8", errors="replace")
                    p = str(p).strip().strip('"').strip("'")
                    if p: str_paths.append(p)
                logger.info("DnD: %d Pfade empfangen: %s", len(str_paths),
                    [os.path.basename(p) for p in str_paths[:5]])
                self._drop_queue.put(str_paths)

            windnd.hook_dropfiles(self, func=on_drop)
            self._poll_drop_queue()  # Polling starten
            logger.info("Drag & Drop: windnd aktiv")
            self.drop_label.configure(text=_t("import_drop_active"))
            return
        except ImportError: pass
        except Exception as e: logger.info("windnd: %s", e)
        logger.info("Drag & Drop: Kein DnD-Paket – Klick-Fallback")
        self.drop_label.configure(text=_t("import_drop_click"))

    def _poll_drop_queue(self):
        """Pollt die Drop-Queue im Hauptthread (thread-sicher für Tkinter)."""
        try:
            while not self._drop_queue.empty():
                paths = self._drop_queue.get_nowait()
                self._process_dropped(paths)
        except Exception: pass
        self.after(200, self._poll_drop_queue)  # Alle 200ms prüfen

    def _process_dropped(self, paths):
        """Verarbeitet per Drag & Drop abgelegte Dateien/Ordner."""
        self._show("import")
        all_files = []
        for p in paths:
            p = str(p).strip().strip('"').strip("'").replace("\r","").replace("\n","")
            logger.info("DnD prüfe: '%s' (exists=%s, isdir=%s)", p, os.path.exists(p), os.path.isdir(p))
            if os.path.isdir(p):
                all_files.extend(self._collect_files_recursive(p))
            elif os.path.isfile(p):
                if not _is_system_file(p):
                    all_files.append(p)
                else:
                    logger.info("DnD: Systemdatei übersprungen: %s", Path(p).name)
        logger.info("DnD: %d unterstützte Dateien gefunden", len(all_files))
        if all_files:
            # Visuelles Feedback
            self.drop_label.configure(text=_t("import_n_files").format(n=len(all_files)))
            self._proc_imp(all_files)
            self.after(2000, lambda: self.drop_label.configure(
                text=_t("import_drop")))
        else:
            messagebox.showinfo("Import","Keine importierbaren Dateien gefunden.\n\n"
                "Systemdateien (.tmp, .dll, .exe, versteckte Dateien etc.) werden übersprungen.")

    def _collect_files_recursive(self, folder):
        """Sammelt alle Dateien aus Ordner und Unterordnern (ohne Systemdateien)."""
        files = []
        try:
            for root, dirs, filenames in os.walk(folder):
                # Versteckte/System-Ordner überspringen
                dirs[:] = [d for d in dirs if not d.startswith(".") and d.lower() not in
                    ("__pycache__",".git",".svn","node_modules","$recycle.bin",
                     "system volume information",".thumbnails",".cache","thumbs")]
                for fn in sorted(filenames):
                    fp=os.path.join(root, fn)
                    if not _is_system_file(fp):
                        files.append(fp)
            logger.info("Ordner %s: %d Dateien (rekursiv)", folder, len(files))
        except Exception as e:
            logger.warning("Ordner lesen: %s", e)
        return files

    def _import_files(self):
        ps=filedialog.askopenfilenames(title="Dokumente importieren",filetypes=[
            ("Alle Dateien","*.*"),
            ("PDF","*.pdf"),("Bilder","*.png *.jpg *.jpeg *.tiff *.bmp *.webp"),
            ("Office","*.doc *.docx *.xls *.xlsx *.ppt *.pptx *.odt *.ods *.odp"),
            ("Desktop Publishing","*.ppp"),
            ("Text","*.txt *.csv *.md *.rtf *.html")])
        if ps: self._show("import"); self._proc_imp(list(ps))
    def _import_folder(self):
        f=filedialog.askdirectory(title="Ordner importieren (rekursiv)")
        if not f: return
        files=self._collect_files_recursive(f)
        if files: self._show("import"); self._proc_imp(files)
        else: messagebox.showinfo("Import",f"Keine importierbaren Dateien in:\n{f}")
    def _proc_imp(self,paths):
        lo=bool(self.import_link.get())
        total=len(paths)
        imp_cat=self._import_cat_var.get()
        force_cat=None
        if imp_cat=="(Keine Kategorie)": force_cat="Dokument"
        elif imp_cat!=_t("import_auto"): force_cat=imp_cat
        # Progress-Dialog (bleibt über beide Phasen)
        pw=ctk.CTkToplevel(self); pw.title("Import & Verarbeitung")
        pw.transient(self); center_window(pw,520,220); pw.grab_set()
        self._imp_phase=ctk.CTkLabel(pw,text=_t("import_phase1"),
            font=ctk.CTkFont(size=14,weight="bold"))
        self._imp_phase.pack(pady=(14,2))
        self._imp_file_lbl=ctk.CTkLabel(pw,text="",font=ctk.CTkFont(size=11),
            text_color=("gray50","gray55"),wraplength=480)
        self._imp_file_lbl.pack()
        self._imp_pb=ctk.CTkProgressBar(pw,width=460); self._imp_pb.pack(padx=20,pady=(8,4)); self._imp_pb.set(0)
        self._imp_status=ctk.CTkLabel(pw,text="0%",font=ctk.CTkFont(size=11),
            text_color=("gray50","gray55")); self._imp_status.pack()
        self._imp_detail=ctk.CTkLabel(pw,text="",font=ctk.CTkFont(size=10),
            text_color=("gray50","gray55")); self._imp_detail.pack(pady=(2,8))
        self.ilog.configure(state="normal")
        cat_info=f" · {_t('doc_meta_cat')} {force_cat}" if force_cat else f" · {_t('log_auto')}"
        self.ilog.insert("end",f"\n{'='*40}\n{total} Dateien · {'Verknüpfen' if lo else 'Kopieren'}{cat_info}\n")

        def do():
            # ═══ PHASE 1: Import (schnell) ═══
            ok=0; err_count=0; imported_ids=[]
            for i,p in enumerate(paths):
                nm=Path(p).name
                self.after(0,lambda n=nm:self._imp_file_lbl.configure(text=n))
                self.after(0,lambda n=nm:self._ilog(f"  {n}..."))
                v=(i+1)/total
                self.after(0,lambda v=v,i=i:self._imp_pb.set(v))
                self.after(0,lambda v=v,i=i:self._imp_status.configure(
                    text=f"{int(v*100)}%  ({i+1}/{total})"))
                did,err=import_file(p,link_only=lo)
                if err:
                    err_count+=1; self.after(0,lambda e=err:self._ilog(f" ⚠{e}\n"))
                else:
                    ok+=1; imported_ids.append(did)
                    self.after(0,lambda:self._ilog(" ✓\n"))
            self.after(0,lambda:self._ilog(f"✅ {ok}/{total} importiert\n"))

            if not imported_ids:
                self.after(0,pw.destroy)
                self.after(0,self.refresh_list); self.after(0,self.refresh_stats)
                return

            # ═══ PHASE 2: OCR & Kategorisierung (langsam, sequenziell) ═══
            ocr_total=len(imported_ids)
            self.after(0,lambda:self._imp_phase.configure(text=_t("import_phase2")))
            self.after(0,lambda:self._imp_pb.set(0))
            self.after(0,lambda:self._imp_detail.configure(text=_t("import_wait")))

            for j,did in enumerate(imported_ids):
                v2=(j+1)/ocr_total
                self.after(0,lambda v=v2,j=j:self._imp_pb.set(v))
                self.after(0,lambda v=v2,j=j:self._imp_status.configure(
                    text=f"{int(v*100)}%  ({j+1}/{ocr_total})"))
                # Dateiname für Anzeige
                try:
                    with get_db() as c:
                        row=c.execute("SELECT original_name FROM documents WHERE id=?",(did,)).fetchone()
                        if row:
                            nm=row["original_name"]
                            self.after(0,lambda n=nm:self._imp_file_lbl.configure(text=f"OCR: {n}"))
                except Exception: pass
                # OCR synchron im selben Thread (KEIN separater Thread!)
                try:
                    process_document(did, force_category=force_cat)
                except Exception as e:
                    logger.error("OCR #%d: %s", did, e)

            # ═══ PHASE 3: Abschluss ═══
            self.after(0,self.refresh_list)
            self.after(0,self.refresh_stats)
            self.after(0,self._rebuild_cats)
            self.after(0,pw.destroy)
            if ok>0:
                self.after(100,lambda:messagebox.showinfo("Import abgeschlossen",
                    f"✅ {ok} von {total} Dateien importiert.\n"
                    f"🔤 {ocr_total} Dokumente mit OCR verarbeitet."
                    +(f"\n⚠️ {err_count} Fehler/Duplikate" if err_count else "")))

        threading.Thread(target=do,daemon=True).start()
    def _ilog(self,t): self.ilog.configure(state="normal"); self.ilog.insert("end",t); self.ilog.see("end")
    # Scanner
    def _refresh_scanners(self):
        for w in self.slist.winfo_children(): w.destroy()
        ctk.CTkLabel(self.slist,text=_t("scan_searching"),text_color=("gray50","gray55")).pack(pady=8)
        def do():
            devs=naps2_list_scanners()
            self.after(0,lambda:self._render_scanners(devs))
        threading.Thread(target=do,daemon=True).start()
    def _render_scanners(self,devs):
        for w in self.slist.winfo_children(): w.destroy()
        if not devs:
            ctk.CTkLabel(self.slist,text=_t("scan_none_found") if NAPS2_EXE else _t("scan_naps2_missing"),
                text_color=("gray50","gray55")).pack(pady=8)
            return
        for d in devs:
            is_active = d==self.sel_scanner_name
            bg=("#dbeafe","#1e3a5f") if is_active else ("gray95","#282c3a")
            f=ctk.CTkFrame(self.slist,corner_radius=8,fg_color=bg,height=38,
                border_width=2 if is_active else 0,border_color=("#4f8ff7","#4f8ff7"))
            f.pack(fill="x",padx=8,pady=2); f.pack_propagate(False)
            dot="🟢" if is_active else "⚪"
            ctk.CTkLabel(f,text=f"{dot} {d}",font=ctk.CTkFont(size=12,
                weight="bold" if is_active else "normal")).pack(side="left",padx=12)
            if is_active:
                ctk.CTkLabel(f,text=_t("scan_active"),font=ctk.CTkFont(size=11,weight="bold"),
                    text_color=("#2563eb","#60a5fa")).pack(side="right",padx=12)
            else:
                ctk.CTkButton(f,text="Wählen",width=70,height=26,
                    command=lambda name=d:self._select_scanner(name)).pack(side="right",padx=8)
    def _select_scanner(self,name):
        self.sel_scanner_name=name
        self._lc["scanner_name"]=name; self._save_lc()
        self._refresh_scanners()
    def _update_naps2_status(self):
        if NAPS2_EXE:
            self.naps2_status_lbl.configure(
                text=f"✅ {NAPS2_EXE}",
                text_color=("green","#34d399"))
        else:
            self.naps2_status_lbl.configure(
                text=_t("scan_naps2_notfound"),
                text_color=("red","#ef4444"))
            # Download-Link anzeigen
            if not hasattr(self,"_naps2_dl_btn"):
                self._naps2_dl_btn=ctk.CTkButton(self.naps2_status_lbl.master,
                    text="⬇ NAPS2 herunterladen (naps2.com)",width=250,height=26,
                    font=ctk.CTkFont(size=11),fg_color=("#dbeafe","#1e3a5f"),
                    text_color=("#1d4ed8","#60a5fa"),hover_color=("#bfdbfe","#2a4a7a"),
                    command=lambda: __import__("webbrowser").open("https://www.naps2.com/download"))
                self._naps2_dl_btn.pack(side="left",padx=8)

    def _change_naps2_path(self):
        """Dialog um den NAPS2.Console.exe Pfad zu wählen."""
        initial = os.path.dirname(NAPS2_EXE) if NAPS2_EXE else "C:\\"
        path = filedialog.askopenfilename(
            title="NAPS2.Console.exe wählen",
            initialdir=initial,
            filetypes=[("NAPS2 Console", "NAPS2.Console.exe"), ("Alle EXE", "*.exe")])
        if not path: return
        if not path.lower().endswith("naps2.console.exe"):
            messagebox.showwarning("NAPS2","Bitte 'NAPS2.Console.exe' wählen,\nnicht NAPS2.exe!")
            return
        if set_naps2_path(path):
            self._update_naps2_status()
            # Auch Einstellungsseite aktualisieren
            try: self._sett_naps2_lbl.configure(text=str(NAPS2_EXE))
            except Exception: pass
            messagebox.showinfo("NAPS2",f"NAPS2 Pfad gespeichert:\n{path}\n\nScanner werden neu geladen...")
            self._refresh_scanners()
        else:
            messagebox.showerror("NAPS2",f"Datei nicht gefunden:\n{path}")

    def _test_naps2_ocr(self):
        """Testet ob NAPS2 OCR funktioniert – erstellt Test-PDF mit Text und prüft OCR."""
        if not NAPS2_EXE:
            messagebox.showerror("Test","NAPS2 nicht gefunden!"); return
        import tempfile, time
        TEMP = tempfile.gettempdir()

        def do():
            self.after(0, lambda: self.scan_status.configure(text="⏳ NAPS2 OCR Test..."))

            # Schritt 1: Prüfe ob NAPS2 --enableocr unterstützt
            logger.info("═══ NAPS2 OCR DIAGNOSE ═══")

            # Schritt 2: Erstelle ein Test-Bild mit Text
            test_img = os.path.join(TEMP, "docvault_ocr_test.png")
            try:
                from PIL import Image, ImageDraw, ImageFont
                img = Image.new("RGB", (800, 200), "white")
                draw = ImageDraw.Draw(img)
                try:
                    font = ImageFont.truetype("arial.ttf", 36)
                except:
                    font = ImageFont.load_default()
                draw.text((50, 50), "DocVault OCR Test 12345 Hallo Welt", fill="black", font=font)
                img.save(test_img)
                logger.info("Test-Bild erstellt: %s", test_img)
            except Exception as e:
                logger.error("Test-Bild: %s", e)
                self.after(0, lambda: messagebox.showerror("Test", f"Konnte Test-Bild nicht erstellen: {e}"))
                return

            # Schritt 3: NAPS2 OCR darauf laufen lassen
            test_pdf = os.path.join(TEMP, "docvault_ocr_test.pdf")
            if os.path.exists(test_pdf):
                try: os.remove(test_pdf)
                except: pass

            cmd = [NAPS2_EXE, "-i", test_img,
                   "--enableocr", "--ocrlang", self.scan_ocr_lang.get(),
                   "-o", test_pdf, "--force"]
            logger.info("NAPS2 OCR Test: %s", " ".join(cmd))

            r = _run_subprocess(cmd, timeout=120, env=NAPS2_ENV)
            logger.info("NAPS2 stdout: %s", (r.stdout or "").strip()[:300])
            logger.info("NAPS2 stderr: %s", (r.stderr or "").strip()[:300])
            logger.info("NAPS2 returncode: %d", r.returncode)

            # Warte auf Datei
            for _ in range(20):
                if os.path.exists(test_pdf) and os.path.getsize(test_pdf) > 0: break
                time.sleep(0.5)

            if not os.path.exists(test_pdf):
                msg = "NAPS2 hat keine PDF erstellt!\n\nPrüfen Sie die Konsolenausgabe."
                logger.error(msg)
                self.after(0, lambda: messagebox.showerror("OCR Test", msg))
                return

            logger.info("Test-PDF: %d KB", os.path.getsize(test_pdf)//1024)

            # Schritt 4: Text extrahieren
            text = ""
            if HAS_FITZ:
                doc = fitz.open(test_pdf)
                text = "".join([page.get_text() for page in doc])
                logger.info("PyMuPDF: %d Zeichen: '%s'", len(text), text.strip()[:200])
                doc.close()

            try:
                with pdfplumber.open(test_pdf) as pdf:
                    pt = "".join([p.extract_text() or "" for p in pdf.pages])
                    logger.info("pdfplumber: %d Zeichen: '%s'", len(pt), pt.strip()[:200])
                    if len(pt) > len(text): text = pt
            except Exception as e:
                logger.info("pdfplumber: %s", e)

            # Aufräumen
            try: os.remove(test_img)
            except: pass
            try: os.remove(test_pdf)
            except: pass

            # Ergebnis anzeigen
            if len(text.strip()) > 5:
                msg = f"✅ NAPS2 OCR funktioniert!\n\nExtrahierter Text:\n{text.strip()[:200]}"
                logger.info("✅ OCR Test OK: %d Zeichen", len(text))
                self.after(0, lambda: self.scan_status.configure(text="✅ OCR Test OK"))
            else:
                msg = (f"❌ NAPS2 OCR liefert 0 Zeichen!\n\n"
                       f"NAPS2 OCR-Sprachpaket prüfen:\n"
                       f"1. NAPS2 GUI öffnen (nicht Console)\n"
                       f"2. Menü → Tools/Extras → OCR\n"
                       f"3. Sprache '{self.scan_ocr_lang.get()}' herunterladen\n"
                       f"4. Aktivieren und OK klicken\n\n"
                       f"Dann nochmal testen.")
                logger.warning("❌ OCR Test: 0 Zeichen – Sprachpaket fehlt?")
                self.after(0, lambda: self.scan_status.configure(text="❌ OCR: Sprachpaket fehlt?"))

            self.after(0, lambda: messagebox.showinfo("OCR Test", msg))

        threading.Thread(target=do, daemon=True).start()

    def _do_scan(self):
        """Scannen – mit Vorschau vor OCR."""
        if not NAPS2_EXE:
            messagebox.showerror("Scanner","NAPS2 nicht gefunden!\n\nBitte herunterladen:\nhttps://www.naps2.com/download"); return
        prof=self.scan_profile.get()
        use_profile=prof if prof and not prof.startswith("(Kein") else None
        if not use_profile and not self.sel_scanner_name:
            messagebox.showwarning("Scanner","Bitte zuerst einen Scanner wählen\noder ein NAPS2-Profil auswählen."); return
        self._save_scan_settings()
        dpi=int(self.scan_dpi.get())
        src={"Einzug (ADF)":"feeder","Flachbett":"glass"}.get(self.scan_source.get(),"feeder")
        if use_profile:
            # Farbmodus aus Profil-Daten lesen
            prof_clr = "gray"; bd = "?"
            for p in getattr(self,"_profile_data",[]):
                if p["name"]==use_profile:
                    bd = p.get("bitdepth","?")
                    bd_map = {"Color":"color","Grayscale":"gray","BlackWhite":"bw",
                              "C24Bit":"color","Gray8":"gray","BlackAndWhite":"bw"}
                    prof_clr = bd_map.get(bd, "gray")
                    break
            clr = prof_clr
            logger.info("Scan mit Profil: '%s' (bitdepth: %s→%s)", use_profile, bd, clr)
        else:
            clr={"Farbe":"color","Graustufen":"gray","SW":"bw"}.get(self.scan_color.get(),"color")
            logger.info("Scan-Einstellungen: DPI=%d, Farbe=%s→%s, Quelle=%s", dpi, self.scan_color.get(), clr, src)
        ocr_lang=self.scan_ocr_lang.get()
        ocr_fast=self.scan_ocr_mode.get()=="Schnell"
        do_deskew=bool(self.scan_deskew.get())

        # ═══ Flachbett: Mehrseitiger Sammel-Scan ═══
        if src == "glass" and not use_profile:
            self._do_flatbed_multipage(dpi, clr, ocr_lang, ocr_fast, do_deskew)
            return
        # Bei Profil prüfen ob Flachbett
        if use_profile:
            for p in getattr(self, "_profile_data", []):
                if p["name"] == use_profile:
                    psrc = p.get("source", "").lower()
                    if psrc in ("glass", "flatbed", "flachbett"):
                        self._do_flatbed_multipage(dpi, clr, ocr_lang, ocr_fast, do_deskew, profile=use_profile)
                        return
                    break

        self.scan_status.configure(text=f"⏳ Scanning ({use_profile or self.sel_scanner_name})..." if _LANG=="en" else f"⏳ Scanne ({use_profile or self.sel_scanner_name})...")

        # ═══ ADF: Mehrstapel-Scan (Dialog wie bei Flachbett) ═══
        self._do_adf_multipage(dpi, clr, ocr_lang, ocr_fast, do_deskew, src, use_profile)

    def _do_adf_multipage(self, dpi, clr, ocr_lang, ocr_fast, do_deskew, src, profile=None):
        """ADF-Modus: Stapel nacheinander scannen und zusammenführen."""
        collected_batches = []  # Liste von (pfad, ocr_text, seitenanzahl)
        batch_num = [1]
        total_pages = [0]

        # ═══ Sammel-Dialog ═══
        dlg = ctk.CTkToplevel(self)
        dlg.title(_t("adf_title"))
        _set_window_icon(dlg)
        dlg.transient(self); dlg.grab_set()
        center_window(dlg, 580, 450)
        dlg.protocol("WM_DELETE_WINDOW", lambda: None)

        ctk.CTkLabel(dlg, text="🖨️ " + _t("adf_title"),
            font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(14, 6))

        status_lbl = ctk.CTkLabel(dlg, text=_t("adf_collected").format(p=0, n=0),
            font=ctk.CTkFont(size=13), text_color=("gray40", "gray60"))
        status_lbl.pack(pady=(0, 4))

        info_lbl = ctk.CTkLabel(dlg, text=_t("adf_place_batch"),
            font=ctk.CTkFont(size=11), text_color=("gray50", "gray55"),
            justify="center")
        info_lbl.pack(pady=(4, 8))

        # Vorschau
        preview_lbl = ctk.CTkLabel(dlg, text="", width=240, height=190)
        preview_lbl.pack(pady=(0, 8))
        dlg._preview_ref = None

        pb = ctk.CTkProgressBar(dlg, width=440, mode="indeterminate")
        pb.pack(padx=30, pady=(0, 10))
        pb.stop()

        btn_fr = ctk.CTkFrame(dlg, fg_color="transparent")
        btn_fr.pack(padx=24, pady=(8, 18))

        def _update_preview(pdf_path):
            try:
                if HAS_FITZ:
                    doc = fitz.open(pdf_path)
                    pix = doc[0].get_pixmap(dpi=72)
                    img = _pix_to_pil(pix)
                    doc.close()
                    img.thumbnail((240, 190), Image.LANCZOS)
                    from PIL import ImageTk
                    tk_img = ImageTk.PhotoImage(img)
                    dlg._preview_ref = tk_img
                    preview_lbl.configure(image=tk_img, text="")
            except Exception: pass

        def _get_page_count(pdf_path):
            try:
                if HAS_FITZ:
                    d = fitz.open(pdf_path); n = len(d); d.close(); return n
            except Exception: pass
            return 1

        def _scan_batch():
            next_btn.configure(state="disabled")
            finish_btn.configure(state="disabled")
            info_lbl.configure(text=_t("adf_scanning").format(n=batch_num[0]))
            pb.start()

            def _do_single():
                scan_path, ocr_text, scan_err = naps2_scan(
                    self.sel_scanner_name, dpi=dpi, color=clr, source=src,
                    ocr_lang=ocr_lang, ocr_fast=ocr_fast, deskew=do_deskew,
                    profile=profile)

                def _on_batch_done():
                    pb.stop()
                    if scan_path:
                        pages = _get_page_count(scan_path)
                        collected_batches.append((scan_path, ocr_text, pages))
                        total_pages[0] += pages
                        n = len(collected_batches)
                        batch_num[0] = n + 1
                        status_lbl.configure(text=_t("adf_batch_done").format(n=n, p=pages))
                        info_lbl.configure(text=_t("adf_collected").format(
                            p=total_pages[0], n=len(collected_batches)) + "\n\n" + _t("adf_place_batch"))
                        _update_preview(scan_path)
                        logger.info("ADF Stapel %d: %d Seiten gescannt: %s", n, pages, scan_path)
                    else:
                        err = scan_err or "?"
                        info_lbl.configure(text=f"❌ {err[:60]}")
                        logger.warning("ADF Stapel %d fehlgeschlagen: %s", batch_num[0], err)
                    next_btn.configure(state="normal")
                    finish_btn.configure(state="normal" if collected_batches else "disabled")

                self.after(0, _on_batch_done)

            threading.Thread(target=_do_single, daemon=True).start()

        def _finish():
            if not collected_batches:
                dlg.destroy(); return

            if len(collected_batches) == 1:
                # Nur ein Stapel: direkt zur Vorschau
                scan_path, ocr_text, _ = collected_batches[0]
                dlg.destroy()
                self.scan_status.configure(
                    text=f"✅ {total_pages[0]} {_t('doc_pages')}")
                self._scan_preview(scan_path, ocr_text, ocr_lang, ocr_fast)
                return

            next_btn.configure(state="disabled")
            finish_btn.configure(state="disabled")
            info_lbl.configure(text=_t("adf_merging").format(n=len(collected_batches)))
            pb.start()

            def _do_merge():
                import tempfile
                ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                final_path = str(DOCS_DIR / f"Scan_{ts}.pdf")
                all_ocr = []
                try:
                    if HAS_FITZ:
                        merged = fitz.open()
                        for batch_path, batch_ocr, _ in collected_batches:
                            src_doc = fitz.open(batch_path)
                            merged.insert_pdf(src_doc)
                            src_doc.close()
                            all_ocr.append(batch_ocr or "")
                        merged.save(final_path)
                        merged.close()
                        logger.info("ADF: %d Stapel (%d Seiten) zusammengeführt → %s",
                            len(collected_batches), total_pages[0], final_path)
                    else:
                        import shutil
                        shutil.move(collected_batches[0][0], final_path)
                        all_ocr.append(collected_batches[0][1] or "")

                    combined_ocr = "\n\n".join(t for t in all_ocr if t)

                    # Einzelne Batch-Dateien aufräumen
                    for batch_path, _, _ in collected_batches:
                        try: os.remove(batch_path)
                        except OSError: pass

                    def _on_merged():
                        pb.stop()
                        dlg.destroy()
                        self.scan_status.configure(
                            text=f"✅ {total_pages[0]} {_t('doc_pages')} ({len(collected_batches)} batches)")
                        self._scan_preview(final_path, combined_ocr, ocr_lang, ocr_fast)

                    self.after(0, _on_merged)

                except Exception as e:
                    logger.error("ADF Merge-Fehler: %s", e, exc_info=True)
                    def _on_err():
                        pb.stop()
                        info_lbl.configure(text=f"❌ {e}")
                        next_btn.configure(state="normal")
                        finish_btn.configure(state="normal")
                    self.after(0, _on_err)

            threading.Thread(target=_do_merge, daemon=True).start()

        def _cancel():
            for batch_path, _, _ in collected_batches:
                try: os.remove(batch_path)
                except OSError: pass
            dlg.destroy()
            self.scan_status.configure(text="")

        next_btn = ctk.CTkButton(btn_fr, text=_t("adf_next_batch"), width=200, height=40,
            font=ctk.CTkFont(size=13, weight="bold"), command=_scan_batch)
        next_btn.pack(side="left", padx=(0, 12))

        finish_btn = ctk.CTkButton(btn_fr, text=_t("adf_finish"), width=160, height=40,
            font=ctk.CTkFont(size=13), fg_color=("#27ae60", "#2ecc71"),
            hover_color=("#219a52", "#27ae60"), state="disabled", command=_finish)
        finish_btn.pack(side="left", padx=(0, 12))

        ctk.CTkButton(btn_fr, text=_t("scan_cancel"), width=110, height=40,
            fg_color=("gray75", "#353a4a"), text_color=("gray30", "gray80"),
            command=_cancel).pack(side="left")

        # Ersten Stapel direkt starten
        self.after(300, _scan_batch)

    def _do_flatbed_multipage(self, dpi, clr, ocr_lang, ocr_fast, do_deskew, profile=None):
        """Flachbett-Modus: Seiten einzeln scannen und zu einem Dokument sammeln."""
        collected_pages = []  # Liste von Pfaden zu einzelnen PDFs
        page_num = [1]
        finished = [False]

        # ═══ Sammel-Dialog ═══
        dlg = ctk.CTkToplevel(self)
        dlg.title(_t("flat_title"))
        _set_window_icon(dlg)
        dlg.transient(self); dlg.grab_set()
        center_window(dlg, 580, 450)
        dlg.protocol("WM_DELETE_WINDOW", lambda: None)

        ctk.CTkLabel(dlg, text="🖨️ " + _t("flat_title"),
            font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(14, 6))

        status_lbl = ctk.CTkLabel(dlg, text=_t("flat_collected").format(n=0),
            font=ctk.CTkFont(size=13), text_color=("gray40", "gray60"))
        status_lbl.pack(pady=(0, 4))

        info_lbl = ctk.CTkLabel(dlg, text=_t("flat_place_page"),
            font=ctk.CTkFont(size=11), text_color=("gray50", "gray55"),
            justify="center")
        info_lbl.pack(pady=(4, 8))

        # Vorschau der letzten gescannten Seite
        preview_lbl = ctk.CTkLabel(dlg, text="", width=240, height=190)
        preview_lbl.pack(pady=(0, 8))
        dlg._preview_ref = None  # Referenz halten

        pb = ctk.CTkProgressBar(dlg, width=440, mode="indeterminate")
        pb.pack(padx=30, pady=(0, 10))
        pb.stop()  # Initial gestoppt

        btn_fr = ctk.CTkFrame(dlg, fg_color="transparent")
        btn_fr.pack(padx=24, pady=(8, 18))

        def _update_preview(pdf_path):
            """Zeigt Thumbnail der zuletzt gescannten Seite."""
            try:
                if HAS_FITZ:
                    doc = fitz.open(pdf_path)
                    pix = doc[0].get_pixmap(dpi=72)
                    img = _pix_to_pil(pix)
                    doc.close()
                    img.thumbnail((240, 190), Image.LANCZOS)
                    from PIL import ImageTk
                    tk_img = ImageTk.PhotoImage(img)
                    dlg._preview_ref = tk_img
                    preview_lbl.configure(image=tk_img, text="")
            except Exception:
                pass

        def _scan_next():
            """Scannt eine einzelne Seite."""
            next_btn.configure(state="disabled")
            finish_btn.configure(state="disabled")
            info_lbl.configure(text=_t("flat_scanning").format(n=page_num[0]))
            pb.start()

            def _do_single():
                scan_path, ocr_text, scan_err = naps2_scan(
                    self.sel_scanner_name, dpi=dpi, color=clr, source="glass",
                    ocr_lang=ocr_lang, ocr_fast=ocr_fast, deskew=do_deskew,
                    profile=profile)

                def _on_page_done():
                    pb.stop()
                    if scan_path:
                        collected_pages.append((scan_path, ocr_text))
                        n = len(collected_pages)
                        page_num[0] = n + 1
                        status_lbl.configure(text=_t("flat_page_done").format(n=n))
                        info_lbl.configure(text=_t("flat_place_page"))
                        _update_preview(scan_path)
                        logger.info("Flachbett: Seite %d gescannt: %s", n, scan_path)
                    else:
                        err = scan_err or "?"
                        info_lbl.configure(text=f"❌ {err[:60]}")
                        logger.warning("Flachbett Seite %d fehlgeschlagen: %s", page_num[0], err)
                    next_btn.configure(state="normal")
                    finish_btn.configure(state="normal" if collected_pages else "disabled")

                self.after(0, _on_page_done)

            threading.Thread(target=_do_single, daemon=True).start()

        def _finish():
            """Alle gesammelten Seiten zu einem PDF zusammenführen."""
            if not collected_pages:
                dlg.destroy(); return

            next_btn.configure(state="disabled")
            finish_btn.configure(state="disabled")
            info_lbl.configure(text=_t("flat_merging").format(n=len(collected_pages)))
            pb.start()

            def _do_merge():
                import tempfile
                ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                final_name = f"Scan_{ts}.pdf"
                final_path = str(DOCS_DIR / final_name)

                all_ocr = []
                try:
                    if HAS_FITZ and len(collected_pages) > 1:
                        # Mehrseitiges PDF aus einzelnen Seiten zusammenführen
                        merged = fitz.open()
                        for page_path, page_ocr in collected_pages:
                            src_doc = fitz.open(page_path)
                            merged.insert_pdf(src_doc)
                            src_doc.close()
                            all_ocr.append(page_ocr or "")
                        merged.save(final_path)
                        merged.close()
                        logger.info("Flachbett: %d Seiten zusammengeführt → %s", len(collected_pages), final_name)
                    elif len(collected_pages) == 1:
                        # Nur eine Seite: einfach verschieben
                        import shutil
                        shutil.move(collected_pages[0][0], final_path)
                        all_ocr.append(collected_pages[0][1] or "")
                    else:
                        # Ohne fitz: erste Seite nehmen (Fallback)
                        import shutil
                        shutil.move(collected_pages[0][0], final_path)
                        all_ocr.append(collected_pages[0][1] or "")

                    combined_ocr = "\n\n".join(t for t in all_ocr if t)

                    # Einzelne Scan-Dateien aufräumen (falls zusammengeführt)
                    if len(collected_pages) > 1:
                        for page_path, _ in collected_pages:
                            try: os.remove(page_path)
                            except OSError: pass

                    def _on_merged():
                        pb.stop()
                        dlg.destroy()
                        self.scan_status.configure(
                            text=f"✅ {len(collected_pages)} {_t('doc_pages')} → {final_name}")
                        self._scan_preview(final_path, combined_ocr, ocr_lang, ocr_fast)

                    self.after(0, _on_merged)

                except Exception as e:
                    logger.error("Flachbett Merge-Fehler: %s", e, exc_info=True)
                    def _on_err():
                        pb.stop()
                        info_lbl.configure(text=f"❌ {e}")
                        next_btn.configure(state="normal")
                        finish_btn.configure(state="normal")
                    self.after(0, _on_err)

            threading.Thread(target=_do_merge, daemon=True).start()

        def _cancel():
            """Abbrechen: Alle Temp-Dateien löschen."""
            for page_path, _ in collected_pages:
                try: os.remove(page_path)
                except OSError: pass
            dlg.destroy()
            self.scan_status.configure(text="")

        next_btn = ctk.CTkButton(btn_fr, text=_t("flat_next"), width=200, height=40,
            font=ctk.CTkFont(size=13, weight="bold"), command=_scan_next)
        next_btn.pack(side="left", padx=(0, 12))

        finish_btn = ctk.CTkButton(btn_fr, text=_t("flat_finish"), width=160, height=40,
            font=ctk.CTkFont(size=13), fg_color=("#27ae60", "#2ecc71"),
            hover_color=("#219a52", "#27ae60"), state="disabled", command=_finish)
        finish_btn.pack(side="left", padx=(0, 12))

        ctk.CTkButton(btn_fr, text=_t("scan_cancel"), width=110, height=40,
            fg_color=("gray75", "#353a4a"), text_color=("gray30", "gray80"),
            command=_cancel).pack(side="left")

        # Erste Seite direkt starten
        self.after(300, _scan_next)

    def _scan_preview(self, scan_path, ocr_text, ocr_lang, ocr_fast):
        """Zeigt Vorschau mit seitenweiser Navigation, selektiver Drehung, Zoom/Pan."""
        import shutil
        pw=ctk.CTkToplevel(self); pw.title("Scan-Vorschau")
        _set_window_icon(pw)
        pw.transient(self); pw.grab_set()
        center_window(pw, 650, 800)

        ctk.CTkLabel(pw,text=_t("scan_preview_lbl"),font=ctk.CTkFont(size=16,weight="bold")).pack(pady=(6,2))

        # Backup für Farbwiederherstellung
        scan_backup = scan_path + ".color_backup"
        if not os.path.exists(scan_backup):
            shutil.copy2(scan_path, scan_backup)

        # ═══ Canvas für Zoom/Pan ═══
        canvas_fr = ctk.CTkFrame(pw, fg_color=("gray90","#171921"), corner_radius=8)
        canvas_fr.pack(fill="both", expand=True, padx=12, pady=4)
        canvas = tk.Canvas(canvas_fr, bg="#1a1d27", highlightthickness=0, cursor="crosshair")
        canvas.pack(fill="both", expand=True, padx=2, pady=2)

        # Seitenzahl ermitteln
        total_pages = 1
        if HAS_FITZ:
            try: d=fitz.open(scan_path); total_pages=len(d); d.close()
            except: pass

        # State
        state = {"zoom":"fit","scale":1.0,"offset_x":0,"offset_y":0,
                 "drag_x":0,"drag_y":0,"modified":False,"pil_img":None,"tk_img":None,
                 "page":0,"total":total_pages}

        def render_page():
            """Rendert die aktuelle Seite als PIL Image."""
            if not HAS_FITZ: return None
            try:
                doc = fitz.open(scan_path)
                state["total"] = len(doc)
                pg_idx = min(state["page"], len(doc)-1)
                page = doc[pg_idx]
                pix = page.get_pixmap(dpi=150)
                img = _pix_to_pil(pix)
                w_pt, h_pt = page.rect.width, page.rect.height
                orient = "⬆ Hoch" if h_pt > w_pt else "⬅ Quer"
                rot = page.rotation
                info_lbl.configure(text=f"Seite {pg_idx+1}/{len(doc)} · {orient} · "
                    f"Rotation: {rot}° · {w_pt:.0f}×{h_pt:.0f}pt")
                doc.close()
                return img
            except Exception as e:
                info_lbl.configure(text=f"{_t('error')} {e}"); return None

        def show_on_canvas():
            canvas.delete("all")
            img = state["pil_img"]
            if img is None: return
            cw, ch = canvas.winfo_width(), canvas.winfo_height()
            if cw < 10: cw, ch = 600, 500
            if state["zoom"] == "fit":
                sx, sy = cw / img.width, ch / img.height
                state["scale"] = min(sx, sy)
                state["offset_x"] = 0; state["offset_y"] = 0
            s = state["scale"]
            nw, nh = int(img.width * s), int(img.height * s)
            resized = img.resize((nw, nh), Image.LANCZOS)
            from PIL import ImageTk
            tk_img = ImageTk.PhotoImage(resized)
            state["tk_img"] = tk_img
            canvas.create_image(cw//2 + int(state["offset_x"]),
                                ch//2 + int(state["offset_y"]), anchor="center", image=tk_img)
            zoom_lbl.configure(text=f"Zoom: {int(state['scale']*100)}%")

        def set_zoom_fit():
            state["zoom"]="fit"; state["offset_x"]=0; state["offset_y"]=0; show_on_canvas()
        def set_zoom_1to1():
            state["zoom"]="custom"; state["scale"]=1.0; state["offset_x"]=0; state["offset_y"]=0; show_on_canvas()

        def on_mousewheel(ev):
            if ev.delta > 0: state["scale"] *= 1.15
            else: state["scale"] /= 1.15
            state["scale"] = max(0.1, min(5.0, state["scale"]))
            state["zoom"] = "custom"; show_on_canvas()

        def on_drag_start(ev): state["drag_x"]=ev.x; state["drag_y"]=ev.y
        def on_drag_move(ev):
            state["offset_x"]+=ev.x-state["drag_x"]; state["offset_y"]+=ev.y-state["drag_y"]
            state["drag_x"]=ev.x; state["drag_y"]=ev.y; state["zoom"]="custom"; show_on_canvas()

        canvas.bind("<ButtonPress-2>", on_drag_start)
        canvas.bind("<B2-Motion>", on_drag_move)
        canvas.bind("<ButtonPress-3>", on_drag_start)
        canvas.bind("<B3-Motion>", on_drag_move)
        canvas.bind("<MouseWheel>", on_mousewheel)
        canvas.bind("<Configure>", lambda e: show_on_canvas())

        # Info-Zeile
        info_lbl = ctk.CTkLabel(pw, text="", font=ctk.CTkFont(size=10), text_color=("gray50","gray55"))
        info_lbl.pack()

        # Erstes Rendern
        state["pil_img"] = render_page()
        pw.after(100, show_on_canvas)

        # ═══ Seitennavigation + Zoom ═══
        nav_fr = ctk.CTkFrame(pw, fg_color="transparent"); nav_fr.pack(pady=(2,2))
        bs={"height":28,"corner_radius":6,"font":ctk.CTkFont(size=11),
            "fg_color":("gray80","#353a4a"),"text_color":("gray20","gray80")}

        def go_page(delta):
            state["page"] = max(0, min(state["total"]-1, state["page"]+delta))
            state["pil_img"] = render_page(); set_zoom_fit()

        ctk.CTkButton(nav_fr,text="◀",width=36,command=lambda:go_page(-1),**bs).pack(side="left",padx=2)
        page_lbl = ctk.CTkLabel(nav_fr,text=f"1/{total_pages}",font=ctk.CTkFont(size=11),width=60)
        page_lbl.pack(side="left",padx=4)
        ctk.CTkButton(nav_fr,text="▶",width=36,command=lambda:go_page(1),**bs).pack(side="left",padx=2)

        ctk.CTkFrame(nav_fr,width=1,height=20,fg_color=("gray70","#454a5a")).pack(side="left",padx=8,pady=4)
        ctk.CTkButton(nav_fr,text="Einpassen",width=72,command=set_zoom_fit,**bs).pack(side="left",padx=2)
        ctk.CTkButton(nav_fr,text="1:1",width=40,command=set_zoom_1to1,**bs).pack(side="left",padx=2)
        zoom_lbl = ctk.CTkLabel(nav_fr,text="100%",font=ctk.CTkFont(size=10),
            text_color=("gray50","gray55"),width=55)
        zoom_lbl.pack(side="left",padx=4)
        ctk.CTkLabel(nav_fr,text="Mausrad=Zoom  Mitteltaste=Verschieben",
            font=ctk.CTkFont(size=8),text_color=("gray55","gray50")).pack(side="left",padx=4)

        # Seitenzahl aktualisieren bei Navigation
        def update_page_lbl():
            page_lbl.configure(text=f"{state['page']+1}/{state['total']}")
            pw.after(200, update_page_lbl)
        update_page_lbl()

        # ═══ Dreh-Buttons (Seite / Alle) ═══
        rot_fr = ctk.CTkFrame(pw, fg_color="transparent"); rot_fr.pack(pady=(2,2))

        def rotate_current(degrees):
            """Aktuelle Seite drehen."""
            try:
                pdf = fitz.open(scan_path)
                pg = pdf[state["page"]]
                pg.set_rotation((pg.rotation + degrees) % 360)
                pdf.save(scan_path, incremental=True, encryption=0); pdf.close()
                state["modified"] = True
                state["pil_img"] = render_page(); set_zoom_fit()
                logger.info("Seite %d: %d° gedreht", state["page"]+1, degrees)
            except Exception as e: messagebox.showerror("Fehler", str(e))

        def rotate_all(degrees):
            """Alle Seiten drehen."""
            try:
                pdf = fitz.open(scan_path)
                for page in pdf: page.set_rotation((page.rotation + degrees) % 360)
                pdf.save(scan_path, incremental=True, encryption=0); pdf.close()
                state["modified"] = True
                state["pil_img"] = render_page(); set_zoom_fit()
                logger.info("Alle %d Seiten: %d° gedreht", state["total"], degrees)
            except Exception as e: messagebox.showerror("Fehler", str(e))

        ctk.CTkLabel(rot_fr,text="Diese Seite:",font=ctk.CTkFont(size=10,weight="bold"),
            text_color=("gray40","gray60")).pack(side="left",padx=(0,4))
        ctk.CTkButton(rot_fr,text="↻90°",width=50,command=lambda:rotate_current(90),**bs).pack(side="left",padx=1)
        ctk.CTkButton(rot_fr,text="↻180°",width=55,command=lambda:rotate_current(180),**bs).pack(side="left",padx=1)

        ctk.CTkFrame(rot_fr,width=1,height=20,fg_color=("gray70","#454a5a")).pack(side="left",padx=6,pady=4)

        ctk.CTkLabel(rot_fr,text=_t("scan_all_pages"),font=ctk.CTkFont(size=10,weight="bold"),
            text_color=("gray40","gray60")).pack(side="left",padx=(0,4))
        ctk.CTkButton(rot_fr,text="↻90°",width=50,command=lambda:rotate_all(90),**bs).pack(side="left",padx=1)
        ctk.CTkButton(rot_fr,text="↻180°",width=55,command=lambda:rotate_all(180),**bs).pack(side="left",padx=1)

        # ═══ Farb-Buttons ═══
        col_fr = ctk.CTkFrame(pw, fg_color="transparent"); col_fr.pack(pady=(2,4))

        def convert_color(mode):
            try:
                src = scan_backup if mode == "color" and os.path.exists(scan_backup) else scan_path
                pdf = fitz.open(src); new_pdf = fitz.open()
                for i in range(len(pdf)):
                    page = pdf[i]; pix = page.get_pixmap(dpi=int(self.scan_dpi.get()) or 150)
                    img = _pix_to_pil(pix)
                    if mode == "gray": img = img.convert("L").convert("RGB")
                    elif mode == "bw": img = img.convert("1").convert("RGB")
                    import io; buf = io.BytesIO(); img.save(buf, "JPEG", quality=92); buf.seek(0)
                    np = new_pdf.new_page(width=page.rect.width, height=page.rect.height)
                    np.insert_image(fitz.Rect(0,0,page.rect.width,page.rect.height), stream=buf.read())
                pdf.close(); new_pdf.save(scan_path); new_pdf.close()
                state["modified"] = True
                state["pil_img"] = render_page(); set_zoom_fit()
            except Exception as e: messagebox.showerror("Fehler", str(e))

        ctk.CTkButton(col_fr,text="🎨 Farbe",width=70,command=lambda:convert_color("color"),**bs).pack(side="left",padx=2)
        ctk.CTkButton(col_fr,text="🔲 Grau",width=65,command=lambda:convert_color("gray"),**bs).pack(side="left",padx=2)
        ctk.CTkButton(col_fr,text="⬛ SW",width=55,command=lambda:convert_color("bw"),**bs).pack(side="left",padx=2)

        # ═══ Aktions-Buttons ═══
        btn_fr = ctk.CTkFrame(pw, fg_color="transparent"); btn_fr.pack(pady=(4,8))

        # Keyboard: Pfeiltasten für Seitennavigation
        pw.bind("<Left>", lambda e: go_page(-1))
        pw.bind("<Right>", lambda e: go_page(1))

        def do_accept():
            pw.destroy()
            try:
                if os.path.exists(scan_backup): os.remove(scan_backup)
            except Exception: pass

            if not state["modified"]:
                # ═══ NICHT geändert → OCR-Text vom Scan direkt verwenden ═══
                logger.info("Scan unverändert – verwende OCR-Text vom Scan (%d Zeichen)", len(ocr_text))
                self.scan_status.configure(text="✅ OCR-Text vom Scan übernommen")
                self._finalize_scan(scan_path, ocr_text)
            else:
                # ═══ Geändert (gedreht/Farbe) → Text neu aus PDF extrahieren ═══
                self.scan_status.configure(text="⏳ Text aus bearbeitetem Scan extrahieren...")
                # Kurzer Progress-Dialog
                ocr_dlg = ctk.CTkToplevel(self); ocr_dlg.title("Texterkennung")
                ocr_dlg.transient(self); center_window(ocr_dlg, 420, 140)
                ocr_dlg.protocol("WM_DELETE_WINDOW", lambda: None)
                ctk.CTkLabel(ocr_dlg, text=_t("ocr_extracting"),
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(14,4))
                ctk.CTkLabel(ocr_dlg, text=_t("ocr_modified_hint"),
                    font=ctk.CTkFont(size=11), text_color=("gray50","gray55")).pack()
                ocr_pb = ctk.CTkProgressBar(ocr_dlg, width=360, mode="indeterminate")
                ocr_pb.pack(padx=20, pady=(10,8)); ocr_pb.start()

                def reextract():
                    new_text = ocr_text  # Fallback: Original-OCR-Text
                    try:
                        if HAS_FITZ:
                            doc = fitz.open(scan_path)
                            extracted = "".join([p.get_text() for p in doc])
                            doc.close()
                            if len(extracted.strip()) > len(new_text.strip()) * 0.5:
                                new_text = extracted
                                logger.info("Text nach Bearbeitung: %d Zeichen (PyMuPDF)", len(new_text))
                            else:
                                logger.info("PyMuPDF: nur %d Zeichen – behalte Original (%d)", len(extracted), len(new_text))
                    except Exception as e:
                        logger.warning("Text-Reextraktion: %s", e)

                    def finish():
                        try: ocr_pb.stop()
                        except: pass
                        try: ocr_dlg.destroy()
                        except: pass
                        self._finalize_scan(scan_path, new_text)
                    self.after(300, finish)

                threading.Thread(target=reextract, daemon=True).start()

        def do_cancel():
            pw.destroy()
            try: os.remove(scan_path)
            except: pass
            try:
                if os.path.exists(scan_backup): os.remove(scan_backup)
            except: pass
            self.scan_status.configure(text="❌ Scan verworfen")

        ctk.CTkButton(btn_fr,text=_t("scan_accept"),width=200,height=40,
            font=ctk.CTkFont(size=13,weight="bold"),command=do_accept).pack(side="left",padx=8)
        ctk.CTkButton(btn_fr,text=_t("scan_cancel"),width=120,height=40,
            fg_color=("gray80","#353a4a"),text_color=("gray20","gray80"),
            font=ctk.CTkFont(size=12),command=do_cancel).pack(side="left",padx=8)

    def _finalize_scan(self, scan_path, ocr_text):
        """Abschluss: ggf. WebP-Konvertierung, Hash, DB-Eintrag, Thumbnail, Index."""
        try:
            # ═══ WebP-Konvertierung wenn gewünscht ═══
            fmt_sel = self.scan_fmt.get().lower()
            use_webp = "webp" in fmt_sel
            if use_webp and scan_path.lower().endswith(".pdf"):
                self.scan_status.configure(text="⏳ PDF → WebP konvertieren...")
                webp_path = pdf_to_webp(scan_path, quality=82)
                if webp_path:
                    scan_path = webp_path
                else:
                    logger.warning("WebP-Konvertierung fehlgeschlagen, behalte PDF")

            fh = compute_hash(scan_path)
            with get_db() as c:
                dup = c.execute("SELECT id FROM documents WHERE file_hash=?",(fh,)).fetchone()
                if dup:
                    try: os.remove(scan_path)
                    except: pass
                    messagebox.showwarning("DocVault",_t("dup_detected"))
                    return

            page_count = 1
            ext = Path(scan_path).suffix.lower()
            if ext == ".pdf" and HAS_FITZ:
                try: d = fitz.open(scan_path); page_count = len(d); d.close()
                except: pass
            elif ext == ".webp":
                page_count = webp_page_count(scan_path)

            fn = Path(scan_path).name
            mime = "image/webp" if ext == ".webp" else "application/pdf"
            cat, conf, tags = categorize(ocr_text)

            # KI-Analyse: Name, Kategorie und Tags
            ai_name = fn  # Fallback: Dateiname
            ai = _ai_analyze_document(ocr_text, get_cat_names(), fn)
            if ai:
                if ai.get("name"):
                    ai_name = ai["name"]
                if ai.get("category"):
                    cat = _ensure_category(ai["category"]); conf = 0.95
                if ai.get("tags"):
                    tags = list(dict.fromkeys(tags + ai["tags"]))[:12]
                self.scan_status.configure(text=f"🤖 {ai_name}")

            with get_db() as c:
                cur = c.execute("""INSERT INTO documents
                    (filename, original_name, file_path, file_size, file_hash,
                     mime_type, source, category, confidence, tags,
                     ocr_text, page_count, thumbnail, processed)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,1)""",
                    (fn, ai_name, scan_path, os.path.getsize(scan_path), fh,
                     mime, "scan", cat, conf, json.dumps(tags),
                     ocr_text, page_count, ""))
                doc_id = cur.lastrowid

            thumb = gen_thumb(scan_path, doc_id)
            if thumb:
                with get_db() as c:
                    c.execute("UPDATE documents SET thumbnail=? WHERE id=?",(thumb, doc_id))
            index_document(doc_id, f"{ai_name} {cat} {' '.join(tags)} {ocr_text}")
            self.refresh_list(); self.refresh_stats(); self._rebuild_cats()

            sz = os.path.getsize(scan_path)
            fmt_info = f"WebP, {sz/1024:.0f} KB" if ext == ".webp" else f"PDF, {sz/1024:.0f} KB"
            info = f"✅ Scan OK! ({page_count} Seiten, {fmt_info}, {len(ocr_text)} Z. OCR)"
            logger.info("Scan archiviert: #%d, %s → %s, %d Seiten, %s, Kat: %s", doc_id, fn, ai_name, page_count, fmt_info, cat)
            self.scan_status.configure(text=info)
            messagebox.showinfo("DocVault", f"Scan erfolgreich archiviert!\n\n"
                f"Name: {ai_name}\n"
                f"Datei: {fn}\n"
                f"Format: {fmt_info}\n"
                f"Seiten: {page_count}\n"
                f"OCR-Text: {len(ocr_text)} Zeichen\n"
                f"Kategorie: {cat} ({int(conf*100)}%)")
        except Exception as e:
            logger.error("Scan archivieren: %s", e, exc_info=True)
            self.scan_status.configure(text=f"❌ {e}")
    # ═══════ EINSTELLUNGEN ═══════
    def _build_settings(self):
        self.sett_p=ctk.CTkScrollableFrame(self.content,fg_color="transparent")
        ctk.CTkLabel(self.sett_p,text=_t("sett_title"),font=ctk.CTkFont(size=20,weight="bold"),
            anchor="w").pack(fill="x",padx=20,pady=(16,12))

        # ═══ Sektion: Datenpfad (gemeinsam) ═══
        self._sett_section(self.sett_p,_t("sett_datapath"))
        sf1=self._sett_card(self.sett_p)
        self._sett_info_lbl=ctk.CTkLabel(sf1,text=f"{_t('sett_current')} {DATA_DIR}",
            font=ctk.CTkFont(size=11),text_color=("gray40","gray60"),wraplength=500,anchor="w")
        self._sett_info_lbl.pack(fill="x",padx=12,pady=(8,4))
        ctk.CTkLabel(sf1,text=_t("sett_datapath_hint"),

            font=ctk.CTkFont(size=11),text_color=("gray50","gray55"),wraplength=500).pack(padx=12,anchor="w")
        ctk.CTkButton(sf1,text=_t("sett_change_path"),width=180,height=32,
            command=self._change_data_path).pack(padx=12,pady=(6,10),anchor="w")

        # ═══ Sektion: Lokale Einstellungen (pro PC) ═══
        self._sett_section(self.sett_p,_t("sett_local"))
        sf2=self._sett_card(self.sett_p)
        ctk.CTkLabel(sf2,text=_t('sett_local_hint') + f"\n{LOCAL_SETTINGS_PATH}",
            font=ctk.CTkFont(size=11),text_color=("gray50","gray55"),wraplength=500).pack(padx=12,pady=(8,2),anchor="w")

        # NAPS2-Pfad
        nf=ctk.CTkFrame(sf2,fg_color="transparent"); nf.pack(fill="x",padx=12,pady=(8,4))
        ctk.CTkLabel(nf,text=_t("sett_naps2_path"),font=ctk.CTkFont(size=12,weight="bold")).pack(side="left")
        self._sett_naps2_lbl=ctk.CTkLabel(nf,text="",font=ctk.CTkFont(size=11),
            text_color=("gray40","gray60")); self._sett_naps2_lbl.pack(side="left",padx=8)
        ctk.CTkButton(nf,text=_t("sett_naps2_change"),width=80,height=26,
            command=self._change_naps2_path).pack(side="right")

        # Darstellung
        df=ctk.CTkFrame(sf2,fg_color="transparent"); df.pack(fill="x",padx=12,pady=(8,4))
        ctk.CTkLabel(df,text=_t("sett_appearance"),font=ctk.CTkFont(size=12,weight="bold")).pack(side="left")
        self._sett_app_var=ctk.StringVar(value=self._lc.get("appearance","dark"))
        for txt,val in [(_t("sett_dark"),"dark"),(_t("sett_light"),"light")]:
            ctk.CTkRadioButton(df,text=txt,variable=self._sett_app_var,value=val,
                command=self._sett_apply_appearance).pack(side="left",padx=(12,4))

        # Dokumente pro Seite
        psf=ctk.CTkFrame(sf2,fg_color="transparent"); psf.pack(fill="x",padx=12,pady=(8,4))
        ctk.CTkLabel(psf,text=_t("sett_pagesize"),font=ctk.CTkFont(size=12,weight="bold")).pack(side="left")
        self._sett_ps_var=ctk.StringVar(value=str(self._page_size))
        for v in ["5","10","20","50","100"]:
            ctk.CTkRadioButton(psf,text=v,variable=self._sett_ps_var,value=v,width=50,
                command=self._sett_apply_pagesize).pack(side="left",padx=(10,0))

        # Scanner (Zusammenfassung)
        scf=ctk.CTkFrame(sf2,fg_color="transparent"); scf.pack(fill="x",padx=12,pady=(8,4))
        ctk.CTkLabel(scf,text=_t("sett_scanner"),font=ctk.CTkFont(size=12,weight="bold")).pack(side="left")
        self._sett_scanner_lbl=ctk.CTkLabel(scf,text="",font=ctk.CTkFont(size=11),
            text_color=("gray40","gray60")); self._sett_scanner_lbl.pack(side="left",padx=8)

        # Scan-Einstellungen
        scn_f=ctk.CTkFrame(sf2,fg_color="transparent"); scn_f.pack(fill="x",padx=12,pady=(4,10))
        self._sett_scan_lbl=ctk.CTkLabel(scn_f,text="",font=ctk.CTkFont(size=11),
            text_color=("gray50","gray55")); self._sett_scan_lbl.pack(anchor="w")

        # ═══ Sektion: Gemeinsame Einstellungen ═══
        self._sett_section(self.sett_p,_t("sett_shared"))
        sf3=self._sett_card(self.sett_p)
        ctk.CTkLabel(sf3,text=_t("sett_shared_hint").format(path=DATA_DIR/"settings.json"),
            font=ctk.CTkFont(size=11),text_color=("gray50","gray55"),wraplength=500).pack(padx=12,pady=(8,2),anchor="w")

        # OCR-Sprache
        of=ctk.CTkFrame(sf3,fg_color="transparent"); of.pack(fill="x",padx=12,pady=(8,4))
        ctk.CTkLabel(of,text=_t("sett_ocrlang"),font=ctk.CTkFont(size=12,weight="bold")).pack(side="left")
        self._sett_ocr_var=ctk.StringVar(value=self._s.get("ocr_lang","deu"))
        ctk.CTkOptionMenu(of,values=["deu","eng","fra","ita","deu+eng"],
            variable=self._sett_ocr_var,width=120,height=28,
            fg_color=("#e8eef8","#353a4a"),text_color=("gray10","gray90"),
            dropdown_fg_color=("#f8faff","#2a2e3b"),dropdown_text_color=("gray10","gray90"),
            command=self._sett_save_ocr).pack(side="left",padx=8)

        # Import-Modus
        imf=ctk.CTkFrame(sf3,fg_color="transparent"); imf.pack(fill="x",padx=12,pady=(4,10))
        ctk.CTkLabel(imf,text=_t("sett_importmode"),font=ctk.CTkFont(size=12,weight="bold")).pack(side="left")
        self._sett_link_var=ctk.IntVar(value=1 if self._s.get("link_only") else 0)
        ctk.CTkRadioButton(imf,text=_t("import_copy"),variable=self._sett_link_var,value=0,
            command=self._sett_save_import).pack(side="left",padx=(12,4))
        ctk.CTkRadioButton(imf,text=_t("import_link"),variable=self._sett_link_var,value=1,
            command=self._sett_save_import).pack(side="left",padx=4)

        # ═══ Sektion: Suchindex ═══
        self._sett_section(self.sett_p,_t("sett_searchidx"))
        sf_idx=self._sett_card(self.sett_p)
        ctk.CTkLabel(sf_idx,text=_t("sett_idx_hint"),
            font=ctk.CTkFont(size=11),text_color=("gray50","gray55"),wraplength=500).pack(padx=12,pady=(8,6),anchor="w")

        idx_s = _get_index_settings()

        # Max OCR-Zeichen
        r1=ctk.CTkFrame(sf_idx,fg_color="transparent"); r1.pack(fill="x",padx=12,pady=2)
        ctk.CTkLabel(r1,text=_t("sett_max_chars"),font=ctk.CTkFont(size=12,weight="bold"),width=230,anchor="w").pack(side="left")
        self._sett_ocr_chars=ctk.StringVar(value=str(idx_s["max_ocr_chars"]))
        for v,lbl in [("10000","10'000"),("50000","50'000"),("100000","100'000"),("200000","200'000"),("500000","500'000")]:
            ctk.CTkRadioButton(r1,text=lbl,variable=self._sett_ocr_chars,value=v,width=80,
                font=ctk.CTkFont(size=11),command=self._sett_save_index).pack(side="left",padx=(6,0))
        ctk.CTkLabel(sf_idx,text=_t("sett_max_chars_h"),
            font=ctk.CTkFont(size=10),text_color=("gray50","gray55")).pack(padx=12,anchor="w")

        # Max Index-Wörter
        r2=ctk.CTkFrame(sf_idx,fg_color="transparent"); r2.pack(fill="x",padx=12,pady=(6,2))
        ctk.CTkLabel(r2,text=_t("sett_max_words"),font=ctk.CTkFont(size=12,weight="bold"),width=230,anchor="w").pack(side="left")
        self._sett_idx_words=ctk.StringVar(value=str(idx_s["max_index_words"]))
        for v,lbl in [("1000","1'000"),("5000","5'000"),("10000","10'000"),("20000","20'000"),("50000","50'000")]:
            ctk.CTkRadioButton(r2,text=lbl,variable=self._sett_idx_words,value=v,width=80,
                font=ctk.CTkFont(size=11),command=self._sett_save_index).pack(side="left",padx=(6,0))
        ctk.CTkLabel(sf_idx,text=_t("sett_max_words_h"),
            font=ctk.CTkFont(size=10),text_color=("gray50","gray55")).pack(padx=12,anchor="w")

        # Min. Wortlänge
        r3=ctk.CTkFrame(sf_idx,fg_color="transparent"); r3.pack(fill="x",padx=12,pady=(6,2))
        ctk.CTkLabel(r3,text=_t("sett_min_wlen"),font=ctk.CTkFont(size=12,weight="bold"),width=230,anchor="w").pack(side="left")
        self._sett_min_wlen=ctk.StringVar(value=str(idx_s["min_word_len"]))
        for v in ["2","3","4"]:
            ctk.CTkRadioButton(r3,text=f"{v} {_t('sett_chars')}",variable=self._sett_min_wlen,value=v,width=90,
                font=ctk.CTkFont(size=11),command=self._sett_save_index).pack(side="left",padx=(6,0))
        ctk.CTkLabel(sf_idx,text=_t("sett_min_wlen_h").format(n=len(STOP)),
            font=ctk.CTkFont(size=10),text_color=("gray50","gray55")).pack(padx=12,anchor="w",pady=(0,8))

        # ═══ Sektion: Plugins ═══
        self._sett_section(self.sett_p,_t("sett_plugins"))
        sf_plug=self._sett_card(self.sett_p)
        ctk.CTkLabel(sf_plug,text=f"{_t('sett_plugin_dir')} {PLUGINS_DIR}",
            font=ctk.CTkFont(size=10),text_color=("gray50","gray55")).pack(padx=12,pady=(8,4),anchor="w")
        self._plugin_fr=ctk.CTkFrame(sf_plug,fg_color="transparent")
        self._plugin_fr.pack(fill="x",padx=12,pady=(0,4))
        self._render_plugin_list()
        bf=ctk.CTkFrame(sf_plug,fg_color="transparent"); bf.pack(fill="x",padx=12,pady=(0,8))
        ctk.CTkButton(bf,text=_t("plug_reload"),width=150,height=28,
            font=ctk.CTkFont(size=11),fg_color=("gray85","#353a4a"),
            text_color=("gray20","gray80"),command=self._reload_plugins).pack(side="left",padx=4)
        ctk.CTkButton(bf,text=_t("plug_folder"),width=150,height=28,
            font=ctk.CTkFont(size=11),fg_color=("gray85","#353a4a"),
            text_color=("gray20","gray80"),command=lambda:self._open_folder(str(PLUGINS_DIR))).pack(side="left",padx=4)

        # ═══ Sektion: KI-Schlagwörter ═══
        self._sett_section(self.sett_p,_t("sett_ai_tags"))
        sf_ai=self._sett_card(self.sett_p)
        ctk.CTkLabel(sf_ai,text=_t("sett_ai_hint"),
            font=ctk.CTkFont(size=10),text_color=("gray50","gray55"),wraplength=540,justify="left").pack(padx=12,pady=(8,6),anchor="w")

        # Status
        ai_prov = self._lc.get("ai_provider","")
        ai_tok = self._lc.get("ai_token","")
        ai_active = bool(ai_prov and ai_tok)
        ai_status_txt = _t("sett_ai_active").format(prov=ai_prov) if ai_active else _t("sett_ai_inactive")
        self._sett_ai_status = ctk.CTkLabel(sf_ai,text=ai_status_txt,
            font=ctk.CTkFont(size=11,weight="bold"),
            text_color=("#27ae60","#2ecc71") if ai_active else ("gray50","gray55"))
        self._sett_ai_status.pack(padx=12,pady=(0,6),anchor="w")

        # Anbieter-Auswahl
        pf=ctk.CTkFrame(sf_ai,fg_color="transparent"); pf.pack(fill="x",padx=12,pady=(0,4))
        ctk.CTkLabel(pf,text=_t("sett_ai_provider"),font=ctk.CTkFont(size=12,weight="bold"),width=90,anchor="w").pack(side="left")
        self._sett_ai_prov_var = ctk.StringVar(value=ai_prov or "DeepSeek")
        ctk.CTkOptionMenu(pf,values=["DeepSeek","OpenAI","Anthropic"],
            variable=self._sett_ai_prov_var,width=150,height=28,
            fg_color=("#e8eef8","#353a4a"),text_color=("gray10","gray90"),
            dropdown_fg_color=("#f8faff","#2a2e3b"),dropdown_text_color=("gray10","gray90")).pack(side="left",padx=8)

        # Token-Eingabe
        tf=ctk.CTkFrame(sf_ai,fg_color="transparent"); tf.pack(fill="x",padx=12,pady=(0,4))
        ctk.CTkLabel(tf,text=_t("sett_ai_token"),font=ctk.CTkFont(size=12,weight="bold"),width=90,anchor="w").pack(side="left")
        self._sett_ai_token_entry = ctk.CTkEntry(tf,width=320,height=28,
            font=ctk.CTkFont(size=11),placeholder_text=_t("sett_ai_token_ph"),show="•")
        self._sett_ai_token_entry.pack(side="left",padx=8)
        if ai_tok:
            self._sett_ai_token_entry.insert(0, ai_tok)

        # Buttons
        abf=ctk.CTkFrame(sf_ai,fg_color="transparent"); abf.pack(fill="x",padx=12,pady=(4,10))
        ctk.CTkButton(abf,text=_t("sett_ai_save"),width=100,height=28,
            font=ctk.CTkFont(size=11),command=self._sett_save_ai).pack(side="left",padx=(0,6))
        ctk.CTkButton(abf,text=_t("sett_ai_test"),width=100,height=28,
            font=ctk.CTkFont(size=11),fg_color=("gray85","#353a4a"),
            text_color=("gray20","gray80"),command=self._sett_test_ai).pack(side="left",padx=6)
        # Token löschen
        del_txt = "Token löschen" if _LANG == "de" else "Delete token"
        ctk.CTkButton(abf,text=del_txt,width=110,height=28,
            font=ctk.CTkFont(size=11),fg_color=("#e74c3c","#c0392b"),
            hover_color=("#c0392b","#a93226"),text_color="white",
            command=self._sett_delete_ai).pack(side="left",padx=6)

        # ═══ Sektion: Sprache ═══
        self._sett_section(self.sett_p,_t("sett_language"))
        sf_lang=self._sett_card(self.sett_p)
        lf=ctk.CTkFrame(sf_lang,fg_color="transparent"); lf.pack(fill="x",padx=12,pady=(8,10))
        self._sett_lang_var=ctk.StringVar(value=_LANG)
        for txt,val in [(_t("sett_lang_de"),"de"),(_t("sett_lang_en"),"en")]:
            ctk.CTkRadioButton(lf,text=txt,variable=self._sett_lang_var,value=val,
                command=self._sett_apply_language).pack(side="left",padx=(12,8))
        ctk.CTkLabel(lf,text=_t("sett_restart_hint"),
            font=ctk.CTkFont(size=10),text_color=("gray50","gray55")).pack(side="left",padx=8)

        # ═══ Sektion: Lizenz ═══
        self._sett_section(self.sett_p,_t("sett_license"))
        sf_lic=self._sett_card(self.sett_p)
        lic_status = _t("sett_license_ok") if self._licensed else _t("sett_license_free")
        self._sett_lic_status=ctk.CTkLabel(sf_lic,text=lic_status,
            font=ctk.CTkFont(size=12,weight="bold"),
            text_color=("#27ae60","#2ecc71") if self._licensed else ("gray50","gray55"))
        self._sett_lic_status.pack(padx=12,pady=(8,0),anchor="w")
        # Ablaufdatum anzeigen
        self._sett_lic_expiry=ctk.CTkLabel(sf_lic,text="",
            font=ctk.CTkFont(size=10),text_color=("gray50","gray55"))
        self._sett_lic_expiry.pack(padx=12,pady=(0,4),anchor="w")
        if self._licensed:
            exp = _get_license_expiry(self._lc.get("license_key",""))
            if exp:
                self._sett_lic_expiry.configure(
                    text=_t("sett_license_expiry").format(date=exp.strftime("%d.%m.%Y")))
        lic_fr=ctk.CTkFrame(sf_lic,fg_color="transparent"); lic_fr.pack(fill="x",padx=12,pady=(4,10))
        ctk.CTkLabel(lic_fr,text=_t("sett_license_enter"),font=ctk.CTkFont(size=11)).pack(side="left")
        self._sett_lic_entry=ctk.CTkEntry(lic_fr,width=220,height=28,
            font=ctk.CTkFont(size=12),placeholder_text="TIMESTAMP-HASH")
        self._sett_lic_entry.pack(side="left",padx=8)
        # Vorhandene Lizenz anzeigen
        saved_lic = self._lc.get("license_key","")
        if saved_lic: self._sett_lic_entry.insert(0, saved_lic)
        ctk.CTkButton(lic_fr,text=_t("sett_license_activate"),width=100,height=28,
            command=self._sett_activate_license).pack(side="left")

        # ═══ Sektion: Info ═══
        self._sett_section(self.sett_p,_t("sett_sysinfo"))
        sf4=self._sett_card(self.sett_p)
        mode = "EXE (PyInstaller)" if getattr(sys, 'frozen', False) else "Python-Skript"
        info_lines = [
            f"Version: DocVault v{VERSION}",
            f"Modus: {mode}",
            f"Programm: {BASE_DIR}",
            f"Lokale Settings: {LOCAL_SETTINGS_PATH}",
            f"Gemeinsame Settings: {DATA_DIR/'settings.json'}",
            f"Datenbank: {DB_PATH}",
            f"PyMuPDF: {'Ja' if HAS_FITZ else 'Nein'}",
            f"NAPS2: {NAPS2_EXE or 'Nicht gefunden'}",
            f"Plugins: {len([p for p in get_plugins() if p['enabled']])} aktiv / {len(get_plugins())} geladen ({PLUGINS_DIR})",
            f"Python: {sys.version.split()[0]}",
        ]
        ctk.CTkLabel(sf4,text="\n".join(info_lines),font=ctk.CTkFont(family="Consolas",size=11),
            text_color=("gray40","gray60"),justify="left",wraplength=600).pack(padx=12,pady=10,anchor="w")

    def _render_plugin_list(self):
        for w in self._plugin_fr.winfo_children(): w.destroy()
        plugins = get_plugins()
        if not plugins:
            ctk.CTkLabel(self._plugin_fr,text=_t("plug_none"),
                font=ctk.CTkFont(size=11),text_color=("gray50","gray55")).pack(anchor="w",pady=4)
            return
        for p in plugins:
            info = p["info"]
            f = ctk.CTkFrame(self._plugin_fr, fg_color="transparent", height=32)
            f.pack(fill="x", pady=1); f.pack_propagate(False)
            # Checkbox zum Aktivieren
            var = tk.BooleanVar(value=p["enabled"])
            cb = ctk.CTkCheckBox(f, text="", variable=var, width=24,
                command=lambda v=var, pl=p: self._toggle_plugin(pl, v.get()))
            cb.pack(side="left", padx=(0,4))
            if p["enabled"]: cb.select()
            # Info
            exts = ", ".join(info.get("extensions",[])[:8])
            prefixes = info.get("extension_prefixes",[])
            if prefixes: exts += ", " + ", ".join(f"{p}*" for p in prefixes)
            ctk.CTkLabel(f, text=f"{info.get('name','')} v{info.get('version','?')}",
                font=ctk.CTkFont(size=11, weight="bold")).pack(side="left")
            ctk.CTkLabel(f, text=f"  {exts}",font=ctk.CTkFont(size=10),
                text_color=("gray50","gray55")).pack(side="left")
            ctk.CTkLabel(f, text=f"  – {info.get('description','')}",
                font=ctk.CTkFont(size=10),text_color=("gray50","gray55")).pack(side="left",fill="x")

    def _toggle_plugin(self, plugin, enabled):
        plugin["enabled"] = enabled
        # Alle aktivierten Plugin-Dateinamen speichern
        enabled_list = [p["file"] for p in get_plugins() if p["enabled"]]
        self._lc["enabled_plugins"] = enabled_list
        self._save_lc()
        logger.info("Plugin '%s': %s", plugin["info"]["name"], "aktiviert" if enabled else "deaktiviert")

    def _reload_plugins(self):
        _load_plugins()
        self._render_plugin_list()
        messagebox.showinfo("Plugins", f"{len(get_plugins())} Plugin(s) geladen.")

    def _open_folder(self, path):
        if platform.system()=="Windows":
            os.startfile(path)
        else:
            subprocess.Popen(["xdg-open", path])

    def _sett_section(self,parent,title):
        ctk.CTkLabel(parent,text=title,font=ctk.CTkFont(size=10,weight="bold"),
            text_color=("gray50","gray55")).pack(anchor="w",padx=20,pady=(12,4))

    def _sett_card(self,parent):
        f=ctk.CTkFrame(parent,corner_radius=10,fg_color=("white","#21242f"))
        f.pack(fill="x",padx=16,pady=(0,4)); return f

    def _refresh_settings(self):
        """Aktualisiert die Anzeigen auf der Einstellungsseite."""
        try:
            self._sett_info_lbl.configure(text=f"{_t('sett_current')} {DATA_DIR}")
            self._sett_naps2_lbl.configure(text=str(NAPS2_EXE or "Nicht konfiguriert"))
            self._sett_scanner_lbl.configure(text=self._lc.get("scanner_name","") or ("(none)" if _LANG=="en" else "(keiner)"))
            scan_info = (f"DPI: {self._lc.get('scan_dpi','150')}, "
                f"Farbe: {self._lc.get('scan_color','Farbe')}, "
                f"Quelle: {self._lc.get('scan_source','Einzug (ADF)')}, "
                f"Format: {self._lc.get('scan_fmt','PDF')}")
            self._sett_scan_lbl.configure(text=scan_info)
            self._sett_app_var.set(self._lc.get("appearance","dark"))
            self._sett_ocr_var.set(self._s.get("ocr_lang","deu"))
            self._sett_link_var.set(1 if self._s.get("link_only") else 0)
        except Exception: pass

    def _sett_apply_appearance(self):
        m=self._sett_app_var.get(); ctk.set_appearance_mode(m)
        self._lc["appearance"]=m; self._save_lc()
        if hasattr(self,"msw"):
            if m=="dark": self.msw.select()
            else: self.msw.deselect()

    def _sett_apply_pagesize(self):
        try: self._page_size=int(self._sett_ps_var.get())
        except ValueError: self._page_size=10
        self._lc["page_size"]=self._page_size; self._save_lc()
        self._page=0; self.refresh_list()

    def _sett_save_ocr(self,_=None):
        lang=self._sett_ocr_var.get(); set_ocr_lang(lang)
        self._s["ocr_lang"]=lang; self._save_s()

    def _sett_save_index(self):
        """Speichert Suchindex-Einstellungen."""
        try: self._lc["max_ocr_chars"]=int(self._sett_ocr_chars.get())
        except: pass
        try: self._lc["max_index_words"]=int(self._sett_idx_words.get())
        except: pass
        try: self._lc["min_word_len"]=int(self._sett_min_wlen.get())
        except: pass
        global _local; _local=self._lc; self._save_lc()
        logger.info("Index-Settings: max_ocr=%s, max_words=%s, min_len=%s",
            self._lc.get("max_ocr_chars"), self._lc.get("max_index_words"), self._lc.get("min_word_len"))

    def _sett_save_import(self):
        lo=bool(self._sett_link_var.get())
        self._s["link_only"]=lo; self._save_s()
        self.import_link.set(1 if lo else 0)

    def _sett_apply_language(self):
        """Sprache ändern und speichern (Neustart nötig)."""
        new_lang = self._sett_lang_var.get()
        self._lc["language"] = new_lang
        self._save_lc()
        _set_language(new_lang)
        msg = "Sprache geändert. Bitte DocVault neu starten." if new_lang == "de" else \
              "Language changed. Please restart DocVault."
        messagebox.showinfo("DocVault", msg)

    def _sett_save_ai(self):
        """Speichert KI-Anbieter und API-Token."""
        prov = self._sett_ai_prov_var.get()
        token = self._sett_ai_token_entry.get().strip()
        self._lc["ai_provider"] = prov
        self._lc["ai_token"] = token
        self._save_lc()
        active = bool(prov and token)
        status_txt = _t("sett_ai_active").format(prov=prov) if active else _t("sett_ai_inactive")
        self._sett_ai_status.configure(text=status_txt,
            text_color=("#27ae60","#2ecc71") if active else ("gray50","gray55"))

    def _sett_test_ai(self):
        """Testet die KI-Verbindung mit einem kurzen Text."""
        self._sett_save_ai()
        prov = self._lc.get("ai_provider", "")
        token = self._lc.get("ai_token", "")
        if not prov or not token:
            messagebox.showwarning("KI-Test", _t("sett_ai_inactive"))
            return
        test_text = "Rechnung Nr. 2024-001 für die Lieferung von 10 Stück Schrauben M8x20 an die Firma Müller AG, Zürich."
        self._sett_ai_status.configure(text="⏳ Teste API...", text_color=("gray40","gray60"))
        self.update_idletasks()
        def _do():
            tags = _generate_ai_tags(test_text, max_tags=5)
            def _show():
                if tags:
                    tag_str = ", ".join(tags)
                    self._sett_ai_status.configure(
                        text=f"✅ {prov} OK: {tag_str}",
                        text_color=("#27ae60","#2ecc71"))
                else:
                    self._sett_ai_status.configure(
                        text=f"❌ {prov}: Keine Tags empfangen – Token prüfen",
                        text_color=("#e74c3c","#ef4444"))
            self.after(0, _show)
        threading.Thread(target=_do, daemon=True).start()

    def _sett_delete_ai(self):
        """Löscht den gespeicherten API-Token."""
        self._lc["ai_provider"] = ""
        self._lc["ai_token"] = ""
        self._save_lc()
        self._sett_ai_token_entry.delete(0, "end")
        self._sett_ai_status.configure(text=_t("sett_ai_inactive"),
            text_color=("gray50","gray55"))

    def _sett_activate_license(self):
        """Lizenznummer prüfen und speichern."""
        key = self._sett_lic_entry.get().strip()
        if _check_license(key):
            self._lc["license_key"] = key
            self._save_lc()
            self._licensed = True
            exp = _get_license_expiry(key)
            exp_str = exp.strftime("%d.%m.%Y") if exp else ""
            self._sett_lic_status.configure(text=_t("sett_license_ok"),
                text_color=("#27ae60","#2ecc71"))
            if exp_str:
                self._sett_lic_expiry.configure(
                    text=_t("sett_license_expiry").format(date=exp_str))
            ok_msg = _t("sett_license_ok")
            if exp_str:
                ok_msg += f"\n{_t('sett_license_expiry').format(date=exp_str)}"
            messagebox.showinfo("DocVault", ok_msg)
        else:
            self._sett_lic_status.configure(text=_t("sett_license_invalid"),
                text_color=("#e74c3c","#e74c3c"))
            self._sett_lic_expiry.configure(text="")
            messagebox.showwarning("DocVault", _t("sett_license_invalid"))

    def _open_naps2_gui(self):
        """Startet das NAPS2 GUI zum Verwalten von Profilen."""
        gui = naps2_find_gui()
        if gui:
            try:
                subprocess.Popen([gui], creationflags=_NOCONSOLE)
                logger.info("NAPS2 GUI gestartet: %s", gui)
            except Exception as e:
                messagebox.showerror("NAPS2",f"Konnte NAPS2 nicht starten:\n{e}")
        else:
            # Versuche den Ordner zu öffnen
            if NAPS2_EXE:
                d=os.path.dirname(NAPS2_EXE)
                messagebox.showinfo("NAPS2",f"NAPS2.exe nicht neben Console gefunden.\n\nBitte manuell starten aus:\n{d}")
            else:
                messagebox.showwarning("NAPS2","NAPS2 nicht konfiguriert.")

    def _refresh_profiles(self):
        """Lädt NAPS2-Profile und aktualisiert das Dropdown."""
        self._profile_data, profiles_path = naps2_list_profiles()
        names=["(Kein Profil – manuelle Einstellungen)"]+[p["name"] for p in self._profile_data]
        self.scan_profile.configure(values=names)
        saved=self._lc.get("scan_profile","")
        if saved and saved in [p["name"] for p in self._profile_data]:
            self.scan_profile.set(saved)
            self._show_profile_details(saved)
        else:
            self.scan_profile.set("(Kein Profil – manuelle Einstellungen)")
            self._prof_detail_lbl.configure(text="")
        if profiles_path:
            n=len(self._profile_data)
            self.scan_status.configure(text=_t("scan_profiles_ok").format(n=n, path=profiles_path))
        elif NAPS2_EXE:
            self.scan_status.configure(text=_t("scan_no_profiles"))
        # Manuelle Optionen je nach aktivem Profil ein-/ausblenden
        self._toggle_manual_scan_opts()

    def _on_profile_change(self, value):
        """Wird aufgerufen wenn ein Profil ausgewählt wird."""
        self._show_profile_details(value)
        self._toggle_manual_scan_opts(value)
        self._save_scan_settings()

    def _toggle_manual_scan_opts(self, profile_value=None):
        """Aktiviert/deaktiviert manuelle Scan-Einstellungen je nach Profil-Auswahl."""
        if profile_value is None:
            profile_value = self.scan_profile.get()
        is_manual = profile_value.startswith("(Kein")
        state = "normal" if is_manual else "disabled"
        # Optionsmenüs und Label ein-/ausblenden
        for om in [self.scan_dpi, self.scan_color, self.scan_source, self.scan_fmt]:
            try: om.configure(state=state)
            except Exception: pass
        # Visuelles Feedback: ausgegrauter Look
        if is_manual:
            self._manual_opts.configure(fg_color=("#f0f5ff","#21242f"))
            self._manual_opts_lbl.configure(text=_t("scan_manual"),
                text_color=("gray30","gray70"))
        else:
            self._manual_opts.configure(fg_color=("#e8e8e8","#181b22"))
            self._manual_opts_lbl.configure(text=_t('scan_manual_off'),
                text_color=("gray55","gray50"))

    def _show_profile_details(self, profile_name):
        """Zeigt die Details des gewählten Profils."""
        if profile_name.startswith("(Kein"):
            self._prof_detail_lbl.configure(text="")
            return
        for p in self._profile_data:
            if p["name"]==profile_name:
                bd_map={"Color":"Farbe","Grayscale":"Graustufen","BlackWhite":"SW",
                         "C24Bit":"Farbe","Gray8":"Graustufen","BlackAndWhite":"SW"}
                src_map={"Glass":"Flachbett","Feeder":"Einzug (ADF)","Duplex":"Duplex",
                          "Auto":"Automatisch"}
                bd=bd_map.get(p.get("bitdepth",""),"") or p.get("bitdepth","?")
                src=src_map.get(p.get("source",""),"") or p.get("source","?")
                dpi=p.get("dpi","?")
                dev=p.get("device","?")
                drv=p.get("driver","")
                details=f"📋 Gerät: {dev}  |  Farbe: {bd}  |  DPI: {dpi}  |  Quelle: {src}"
                if drv: details+=f"  |  Treiber: {drv}"
                self._prof_detail_lbl.configure(text=details)
                return
        self._prof_detail_lbl.configure(text="")

    def _save_scan_settings(self):
        """Speichert Scanner-Einstellungen sofort bei Änderung."""
        if getattr(self,"_restoring_scan",False): return
        self._lc["scan_dpi"]=self.scan_dpi.get()
        self._lc["scan_color"]=self.scan_color.get()
        self._lc["scan_source"]=self.scan_source.get()
        self._lc["scan_fmt"]=self.scan_fmt.get()
        self._lc["scan_ocr_lang"]=self.scan_ocr_lang.get()
        self._lc["scan_ocr_mode"]=self.scan_ocr_mode.get()
        self._lc["scan_deskew"]=bool(self.scan_deskew.get())
        prof=self.scan_profile.get()
        self._lc["scan_profile"]=prof if not prof.startswith("(Kein") else ""
        self._save_lc()

    def _restore_scan_settings(self):
        self._restoring_scan=True
        for om,key,default in [(self.scan_dpi,"scan_dpi","150"),
                                (self.scan_color,"scan_color","Graustufen"),
                                (self.scan_source,"scan_source","Einzug (ADF)"),
                                (self.scan_fmt,"scan_fmt","PDF"),
                                (self.scan_ocr_lang,"scan_ocr_lang","deu"),
                                (self.scan_ocr_mode,"scan_ocr_mode","Am besten")]:
            val=self._lc.get(key,default)
            try: om.set(val)
            except Exception: pass
        self.sel_scanner_name=self._lc.get("scanner_name","")
        if self._lc.get("scan_deskew"): self.scan_deskew.select()
        # Migration: alte scan_store_fmt → scan_fmt
        old_sfmt = self._lc.get("scan_store_fmt", "")
        if "WebP" in old_sfmt and self._lc.get("scan_fmt","PDF") == "PDF":
            self._lc["scan_fmt"] = "WebP (klein)"
            try: self.scan_fmt.set("WebP (klein)")
            except: pass
        # Profile laden und wiederherstellen
        self._refresh_profiles()
        self._restoring_scan=False
        # Manuelle Optionen je nach Profil ein-/ausblenden
        self._toggle_manual_scan_opts()

def main():
    mode = "EXE (PyInstaller)" if getattr(sys, 'frozen', False) else "Python-Skript"
    print(f"\n  DocVault v{VERSION} [{mode}]")
    print(f"  Programm: {BASE_DIR}")
    print(f"  Daten: {DATA_DIR}")
    print(f"  PyMuPDF: {'Ja' if HAS_FITZ else 'Nein'}")
    print(f"  NAPS2: {'Ja (' + str(NAPS2_EXE) + ')' if NAPS2_EXE else 'Nicht gefunden'}")
    pcount = len(get_plugins())
    pactive = len([p for p in get_plugins() if p["enabled"]])
    print(f"  Plugins: {pactive} aktiv / {pcount} geladen ({PLUGINS_DIR})")
    for p in get_plugins():
        st = "✓" if p["enabled"] else "✗"
        print(f"    {st} {p['info']['name']} v{p['info'].get('version','?')} ({', '.join(p['info'].get('extensions',[]))})")

    # Kommandozeilen-Suchbegriff(e)
    search_query = None
    args = sys.argv[1:]
    if args:
        # --search "begriff" oder einfach DocVault.exe rechnung steuer
        if args[0] in ("--search", "-s", "/s") and len(args) > 1:
            search_query = " ".join(args[1:])
        elif not args[0].startswith("-"):
            search_query = " ".join(args)
        if search_query:
            print(f"  Suche: \"{search_query}\"")
    print()
    init_db(); DocVaultApp(search_query=search_query).mainloop()
if __name__=="__main__": main()
