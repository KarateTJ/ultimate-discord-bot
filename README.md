# 🤖 Ultimate Discord Bot

Ein vollständig ausgestatteter Discord Bot mit ALLEN Features!

---

## ✨ Features

| Kategorie | Befehle |
|-----------|---------|
| 🛡️ **Moderation** | ban, kick, mute, unmute, warn, warnings, purge, slowmode, lock, unlock, nuke, role, nick |
| 🤖 **AutoMod** | Anti-Spam, Anti-Links, Anti-Invites, Anti-Caps, Bad-Words, Anti-Raid |
| 🎫 **Tickets** | Panel, Erstellen, Schließen, Transcript, Claim, Add/Remove User |
| 🎮 **Spiele** | Trivia, TicTacToe, Hangman, Zahlenraten, RPS, Coinflip, Würfel, Slots, Yahtzee |
| ⭐ **Leveling** | XP-System, Level-Up-Nachrichten, Rangliste, Level-Rollen |
| 💰 **Economy** | Balance, Daily, Work, Crime, Pay, Gamble, Rob, Shop, Spin |
| 🎵 **Musik** | Play, Pause, Skip, Queue, Loop, Shuffle, Volume, NowPlaying |
| 🎁 **Giveaways** | Start, End, Reroll, Liste |
| 🎭 **Reaktionsrollen** | Panel, Hinzufügen, Entfernen, Liste |
| 👋 **Welcome** | Willkommensnachrichten, DM-Welcome, Leave-Nachrichten |
| 📝 **Logging** | Nachrichten, Member, Bans, Channels, Rollen, Voice |
| ⚙️ **Utility** | Help, Ping, Userinfo, Serverinfo, Avatar, Poll, AFK, Reminder |
| 😂 **Fun** | Memes, Witze, Fakten, Katzen, Hunde, Roast, Compliment, Ship, IQ |

---

## 🚀 Installation & Setup

### 1. Discord Bot erstellen
1. Gehe zu [Discord Developer Portal](https://discord.com/developers/applications)
2. Klicke **"New Application"** → gib einen Namen ein
3. Gehe zu **"Bot"** → klicke **"Add Bot"**
4. Unter **"Token"** → klicke **"Reset Token"** und kopiere ihn
5. Aktiviere unter **"Privileged Gateway Intents"** ALLE 3 Intents:
   - ✅ `PRESENCE INTENT`
   - ✅ `SERVER MEMBERS INTENT`
   - ✅ `MESSAGE CONTENT INTENT`

### 2. Bot einladen
1. Gehe zu **"OAuth2"** → **"URL Generator"**
2. Wähle **"bot"** und **"applications.commands"**
3. Wähle Berechtigungen: **"Administrator"** (oder manuell alles auswählen)
4. Öffne den Link und lade den Bot ein

### 3. Bot starten

```bash
# 1. Python 3.10+ installieren (https://python.org)

# 2. Abhängigkeiten installieren
pip install -r requirements.txt

# 3. FFmpeg installieren (für Musik)
# Windows: https://ffmpeg.org/download.html
# Linux: sudo apt install ffmpeg
# Mac: brew install ffmpeg

# 4. Token in config.json eintragen
# Öffne config.json und ersetze "DEIN_BOT_TOKEN_HIER" mit deinem Token

# 5. Bot starten
python main.py
```

---

## ⚙️ Erstkonfiguration

Nach dem Start den Bot einrichten:

```
!setlogchannel #log-channel          → Logging aktivieren
!setmodlog #mod-log                   → Mod-Log setzen
!welcome channel #welcome             → Welcome-Channel
!welcome leavechannel #leave          → Leave-Channel
!ticket panel #support                → Ticket-Panel erstellen
!automod                              → AutoMod-Status anzeigen
!setlevelchannel #level-up            → Level-Up-Nachrichten
```

---

## 📋 Alle Befehle

### 🛡️ Moderation
```
!ban @user [Grund]              → User bannen
!unban <ID>                     → User entbannen
!kick @user [Grund]             → User kicken
!mute @user [Zeit] [Grund]      → User stummschalten (10m, 1h, 1d)
!unmute @user                   → Stummschaltung aufheben
!warn @user [Grund]             → User verwarnen
!warnings @user                 → Verwarnungen anzeigen
!clearwarnings @user            → Verwarnungen löschen
!purge [Anzahl] [@user]         → Nachrichten löschen
!slowmode [Sekunden]            → Slowmode setzen
!lock [#channel]                → Channel sperren
!unlock [#channel]              → Channel entsperren
!nuke                           → Channel löschen & neu erstellen
!role @user @role               → Rolle hinzufügen/entfernen
!nick @user [Name]              → Nickname ändern
!banlist                        → Alle Bans anzeigen
```

### 🤖 AutoMod
```
!automod                        → Einstellungen anzeigen
!automod toggle                 → An/Ausschalten
!automod antispam               → Anti-Spam umschalten
!automod antilinks              → Anti-Links umschalten
!automod antiinvites            → Anti-Invites umschalten
!automod addword <wort>         → Wort zur Blacklist hinzufügen
!automod removeword <wort>      → Wort entfernen
!automod words                  → Blacklist anzeigen
!automod whitelist [#ch/@role]  → Whitelist verwalten
!automod logchannel [#channel]  → Log-Channel setzen
```

### 🎫 Tickets
```
!ticket panel [#channel]        → Ticket-Panel erstellen
!ticket setup                   → Einstellungen
!ticket close                   → Ticket schließen
!ticket add @user               → User hinzufügen
!ticket remove @user            → User entfernen
!ticket transcript              → Transcript erstellen
```

### 🎮 Spiele
```
!trivia                         → Trivia-Frage
!8ball <Frage>                  → Magische 8-Ball
!coinflip [kopf/zahl]           → Münzwurf
!roll [XdY]                     → Würfeln (z.B. 2d6)
!guess [Max]                    → Zahlenraten
!hangman                        → Hangman-Spiel
!ttt @user                      → TicTacToe
!rps [@user]                    → Schere Stein Papier
!slots                          → Spielautomat
!yahtzee                        → Kniffel/Yahtzee
```

### ⭐ Leveling
```
!rank [@user]                   → Rang anzeigen
!leaderboard                    → Top 10
!addxp @user <Menge>            → XP geben (Admin)
!setlevel @user <Level>         → Level setzen (Admin)
!resetxp @user                  → XP zurücksetzen (Admin)
!levelrole                      → Level-Rollen anzeigen
!levelrole add <Level> @role    → Level-Rolle hinzufügen
!setlevelchannel [#channel]     → Level-Up-Channel
```

### 💰 Economy
```
!balance [@user]                → Guthaben anzeigen
!daily                          → Tägliche Belohnung
!work                           → Arbeiten (1h Cooldown)
!crime                          → Verbrechen (2h Cooldown)
!pay @user <Betrag>             → Geld überweisen
!deposit <Betrag/all>           → In Bank einzahlen
!withdraw <Betrag/all>          → Aus Bank abheben
!gamble <Betrag/all/half>       → Gambling
!rob @user                      → Raub versuchen
!spin                           → Glücksrad drehen
!richlist                       → Reichste User
!shop                           → Shop anzeigen
```

### 🎵 Musik
```
!play <Song/URL>                → Song abspielen
!pause                          → Pausieren
!resume                         → Fortsetzen
!skip                           → Überspringen
!stop                           → Stoppen & Disconnect
!queue                          → Queue anzeigen
!nowplaying                     → Aktueller Song
!volume <0-100>                 → Lautstärke
!loop [song/queue/off]          → Loop-Modus
!shuffle                        → Queue mischen
!clearqueue                     → Queue leeren
```

### 🎁 Giveaways
```
!gstart <Zeit> <Nw> <Preis>     → Giveaway starten (z.B. !gstart 1h 1w Nitro)
!gend <Nachrichten-ID>          → Giveaway beenden
!greroll <Nachrichten-ID>       → Neuen Gewinner wählen
!glist                          → Aktive Giveaways
```

### 🎭 Reaktionsrollen
```
!rradd <ID> <Emoji> @role       → Reaction Role hinzufügen
!rrremove <ID> <Emoji>          → Reaction Role entfernen
!rrlist                         → Alle Reaction Roles
!rrpanel [#channel]             → Panel erstellen
!rrclear [Nachrichten-ID]       → Reaction Roles löschen
```

### 😂 Fun
```
!joke / !witz                   → Witz
!fact / !fakt                   → Interessanter Fakt
!cat / !dog                     → Tierbilder
!meme                           → Zufälliges Meme
!quote / !zitat                 → Inspirations-Zitat
!roast [@user]                  → Roast
!compliment [@user]             → Kompliment
!ship @user1 [@user2]           → Ship-Meter
!hack [@user]                   → Fake-Hack
!iq [@user]                     → IQ-Meter
!howgay [@user]                 → Gay-Ometer
!rate <Ding>                    → Bewertung
!truth                          → Wahrheit-oder-Pflicht
!dare                           → Pflicht
!wyr                            → Würdest du lieber
```

### ⚙️ Utility
```
!help [Befehl]                  → Hilfe
!ping                           → Latenz
!botinfo                        → Bot-Info
!userinfo [@user]               → User-Info
!serverinfo                     → Server-Info
!avatar [@user]                 → Avatar
!roleinfo @role                 → Rollen-Info
!membercount                    → Mitgliederzahl
!poll "Frage" "Opt1" "Opt2"     → Umfrage erstellen
!vote <Frage>                   → Ja/Nein-Abstimmung
!afk [Grund]                    → AFK setzen
!reminder <Zeit> <Text>         → Erinnerung setzen
!embed #channel Titel | Text    → Embed senden
!announce #channel Text         → Ankündigung
!math <Ausdruck>                → Rechner
!snipe                          → Letzte gelöschte Nachricht
!invites [@user]                → Einladungen anzeigen
```

---

## 🔧 Konfiguration

Die Datei `config.json` enthält die grundlegenden Einstellungen:

```json
{
    "token": "DEIN_BOT_TOKEN",
    "prefix": "!",
    "description": "Mein Bot"
}
```

---

## 📝 Hinweise

- **FFmpeg** muss für Musik installiert sein
- Der Bot benötigt **Administrator-Rechte** für alle Features
- Datenbankdatei: `data/bot.db` (SQLite)
- Log-Datei: `data/bot.log`

---

## 🐛 Probleme?

- Stelle sicher, dass alle **Privileged Intents** aktiviert sind
- **FFmpeg** für Musik-Feature installieren
- **Python 3.10+** wird benötigt
- Bei Errors: Schaue in `data/bot.log`
