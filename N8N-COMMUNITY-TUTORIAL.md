# 🚀 N8N Community Tutorial - AI Tools Extended

> **Vollständige Anleitung für die Nutzung aller AI Tools Endpoints in N8N**

## 📋 Inhaltsverzeichnis

1. [🏃‍♂️ Quick Start](#quick-start)
2. [🔧 Basis Setup](#basis-setup)
3. [🎯 Original AI Tools Endpoints](#original-ai-tools-endpoints)
4. [🎥 YouTube Extension Endpoints](#youtube-extension-endpoints)
5. [🛠️ Praktische Workflow-Beispiele](#praktische-workflow-beispiele)
6. [💡 Community Use Cases](#community-use-cases)
7. [🐛 Troubleshooting](#troubleshooting)
8. [📚 API Reference](#api-reference)

---

## 🏃‍♂️ Quick Start

### 1. N8N Dashboard öffnen
- **URL**: `https://workflows.deine-domain.com`
- **Kein Login nötig** - direkt loslegen! 🎉

### 2. Ersten Workflow erstellen
1. **"New Workflow"** klicken
2. **"Manual Trigger"** Node hinzufügen
3. **"HTTP Request"** Node hinzufügen
4. API Endpoint konfigurieren
5. **"Execute Workflow"** testen

---

## 🔧 Basis Setup

### HTTP Request Node Grundkonfiguration

Für **ALLE** AI Tools Endpoints:

```
Method: POST
URL: http://ai-tools:8000/[ENDPOINT]
Headers:
  Content-Type: application/json
Body: JSON
```

### Interne Service URLs

```bash
# Original AI Tools API
http://ai-tools:8000

# YouTube Extension API  
http://ai-tools:8080

# Redis Cache (optional)
http://redis:6379
```

---

## 🎯 Original AI Tools Endpoints

### 1. 🗣️ Text-to-Speech

**Endpoint**: `POST http://ai-tools:8000/text-to-speech`

#### N8N Konfiguration:
```json
{
  "method": "POST",
  "url": "http://ai-tools:8000/text-to-speech",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "text": "{{ $json.text }}",
    "voice": "{{ $json.voice || 'de-DE-KatjaNeural' }}",
    "speed": 1.0
  }
}
```

#### Verfügbare Stimmen:
- **Deutsch**: `de-DE-KatjaNeural`, `de-DE-ConradNeural`
- **Englisch**: `en-US-JennyNeural`, `en-US-GuyNeural`
- **Französisch**: `fr-FR-DeniseNeural`, `fr-FR-HenriNeural`
- **Spanisch**: `es-ES-ElviraNeural`, `es-ES-AlvaroNeural`

#### Response:
```json
{
  "file_id": "uuid-string",
  "download_url": "http://ai-tools:8000/download/uuid-string",
  "duration": 5.2,
  "voice_used": "de-DE-KatjaNeural"
}
```

---

### 2. 🎤 Speech-to-Text

**Endpoint**: `POST http://ai-tools:8000/speech-to-text`

#### N8N Workflow:
1. **File Upload** → Media Storage
2. **Speech-to-Text** mit file_id
3. **Process Result**

#### Konfiguration:
```json
{
  "method": "POST",
  "url": "http://ai-tools:8000/speech-to-text",
  "body": {
    "file_id": "{{ $json.file_id }}",
    "language": "{{ $json.language || 'de' }}"
  }
}
```

#### Supported Languages:
- `de` - Deutsch
- `en` - Englisch  
- `fr` - Französisch
- `es` - Spanisch
- `auto` - Automatische Erkennung

---

### 3. 📁 Media Storage

#### Upload File
**Endpoint**: `POST http://ai-tools:8000/upload`

```json
{
  "method": "POST", 
  "url": "http://ai-tools:8000/upload",
  "sendBody": true,
  "bodyParameters": {
    "file": "{{ $binary.data }}"
  }
}
```

#### Download File
**Endpoint**: `GET http://ai-tools:8000/download/{file_id}`

#### File Status
**Endpoint**: `GET http://ai-tools:8000/status/{file_id}`

#### Delete File
**Endpoint**: `DELETE http://ai-tools:8000/delete/{file_id}`

---

### 4. 🎬 Generate Captioned Video

**Endpoint**: `POST http://ai-tools:8000/generate-captioned-video`

#### N8N Konfiguration:
```json
{
  "method": "POST",
  "url": "http://ai-tools:8000/generate-captioned-video",
  "body": {
    "image_id": "{{ $json.image_id }}",
    "text": "{{ $json.text }}",
    "style": "{{ $json.style || 'gradient' }}",
    "add_music": true,
    "ken_burns": true
  }
}
```

#### Verfügbare Styles:
- `minimal` - Einfacher Text
- `bold` - Fetter Text mit Schatten
- `gradient` - Farbverlauf
- `neon` - Neon-Effekt

---

### 5. 🎞️ Merge Videos

**Endpoint**: `POST http://ai-tools:8000/merge-videos`

#### N8N Konfiguration:
```json
{
  "method": "POST",
  "url": "http://ai-tools:8000/merge-videos",
  "body": {
    "video_ids": ["{{ $json.video1_id }}", "{{ $json.video2_id }}"],
    "add_music": true,
    "transition": "fade",
    "output_format": "mp4"
  }
}
```

---

## 🎥 YouTube Extension Endpoints

### 1. 📝 YouTube Transcription

**Endpoint**: `POST http://ai-tools:8080/youtube/transcribe`

#### N8N Konfiguration:
```json
{
  "method": "POST",
  "url": "http://ai-tools:8080/youtube/transcribe",
  "body": {
    "url": "{{ $json.youtube_url }}",
    "language": "{{ $json.language || 'auto' }}"
  }
}
```

#### Beispiel Input:
```json
{
  "youtube_url": "https://youtube.com/watch?v=dQw4w9WgXcQ",
  "language": "de"
}
```

#### Response:
```json
{
  "title": "Video Title",
  "duration": 360,
  "transcription": {
    "text": "Das ist der transkribierte Text...",
    "language": "de",
    "confidence": 0.95
  }
}
```

---

### 2. 🎵 YouTube to TTS

**Endpoint**: `POST http://ai-tools:8080/youtube/to-tts`

#### N8N Konfiguration:
```json
{
  "method": "POST",
  "url": "http://ai-tools:8080/youtube/to-tts",
  "body": {
    "youtube_url": "{{ $json.youtube_url }}",
    "voice": "{{ $json.voice || 'de-DE-KatjaNeural' }}",
    "speed": 1.0
  }
}
```

---

### 3. 🎬 YouTube to Captioned Video

**Endpoint**: `POST http://ai-tools:8080/youtube/to-captioned-video`

#### N8N Konfiguration:
```json
{
  "method": "POST",
  "url": "http://ai-tools:8080/youtube/to-captioned-video",
  "body": {
    "youtube_url": "{{ $json.youtube_url }}",
    "style": "{{ $json.style || 'gradient' }}",
    "music": true
  }
}
```

---

### 4. 🖼️ Extract YouTube Thumbnail

**Endpoint**: `POST http://ai-tools:8080/youtube/extract-thumbnail`

#### N8N Konfiguration:
```json
{
  "method": "POST",
  "url": "http://ai-tools:8080/youtube/extract-thumbnail",
  "body": {
    "url": "{{ $json.youtube_url }}"
  }
}
```

---

## 🛠️ Praktische Workflow-Beispiele

### 🔥 Workflow 1: YouTube → Blog Post Generator

```
1. Manual Trigger
   ↓
2. HTTP Request: YouTube Transcribe
   ↓  
3. Code Node: Text Processing
   ↓
4. HTTP Request: Text-to-Speech (Summary)
   ↓
5. Set Node: Format Blog Post
```

#### Code Node Beispiel:
```javascript
// Text zu Blog Post formatieren
const transcription = items[0].json.transcription.text;
const title = items[0].json.title;

// Blog Post erstellen
const blogPost = {
  title: `📝 ${title}`,
  introduction: transcription.substring(0, 300) + '...',
  content: transcription,
  wordCount: transcription.split(' ').length,
  readingTime: Math.ceil(transcription.split(' ').length / 200)
};

return [{ json: blogPost }];
```

---

### 🔥 Workflow 2: Social Media Content Factory

```
1. Webhook (YouTube URL Input)
   ↓
2. YouTube Transcribe
   ↓
3. Split into 3 branches:
   ├── Twitter Thread (280 chars)
   ├── LinkedIn Post (1300 chars)  
   └── Instagram Caption (2200 chars)
   ↓
4. Merge Results
```

#### Twitter Thread Code:
```javascript
const text = items[0].json.transcription.text;
const sentences = text.split(/[.!?]+/);

// Create Twitter thread
const tweets = [];
let currentTweet = "";

sentences.forEach(sentence => {
  if ((currentTweet + sentence).length < 250) {
    currentTweet += sentence + ". ";
  } else {
    tweets.push(currentTweet.trim());
    currentTweet = sentence + ". ";
  }
});

if (currentTweet) tweets.push(currentTweet.trim());

return tweets.map((tweet, index) => ({
  json: {
    thread_number: index + 1,
    tweet: `${index + 1}/${tweets.length} ${tweet}`,
    hashtags: "#AI #ContentCreation #Community"
  }
}));
```

---

### 🔥 Workflow 3: Multi-Language Content Pipeline

```
1. Manual Trigger
   ↓
2. YouTube Transcribe (Original Language)
   ↓
3. Split Node (Multiple Languages)
   ├── DE: Text-to-Speech (German Voice)
   ├── EN: Text-to-Speech (English Voice)
   ├── FR: Text-to-Speech (French Voice)
   └── ES: Text-to-Speech (Spanish Voice)
   ↓
4. Merge + Create Captioned Videos
```

---

### 🔥 Workflow 4: Educational Content Processor

```
1. Webhook (Educational Video URL)
   ↓
2. YouTube Transcribe
   ↓
3. Parallel Processing:
   ├── Extract Key Points (Code Node)
   ├── Generate Quiz Questions (Code Node)
   ├── Create Summary (Code Node)
   └── Extract Timestamps (Code Node)
   ↓
4. Create Educational Package
```

#### Key Points Extraction:
```javascript
const transcription = items[0].json.transcription.text;

// Split into sentences and find important ones
const sentences = transcription.split(/[.!?]+/);
const keyPoints = sentences
  .filter(sentence => {
    // Find sentences with keywords
    const keywords = ['wichtig', 'bedeutend', 'hauptsächlich', 'zentral', 'key', 'important', 'essential'];
    return keywords.some(keyword => 
      sentence.toLowerCase().includes(keyword)
    );
  })
  .slice(0, 5)
  .map((point, index) => ({
    number: index + 1,
    point: point.trim(),
    importance: 'high'
  }));

return [{ json: { keyPoints } }];
```

---

## 💡 Community Use Cases

### 🎓 **Bildungseinrichtungen**

#### Vorlesungs-Aufbereitung:
```
YouTube Vorlesung → Transcription → 
├── Deutsche Untertitel
├── Englische Übersetzung  
├── Zusammenfassung
├── Podcast Version
└── Lernkarten
```

#### N8N Workflow:
1. **YouTube Transcribe** der Vorlesung
2. **Text Processing** für Kapitel
3. **Multi-Language TTS** für internationale Studenten
4. **Captioned Video** für Untertitel
5. **Summary Generation** für Lernhilfen

---

### 📱 **Content Creator**

#### Video Repurposing Pipeline:
```
1 YouTube Video →
├── 5 Instagram Posts
├── 10 Twitter Threads
├── 1 LinkedIn Artikel
├── 3 TikTok Scripts
└── 1 Podcast Episode
```

#### N8N Implementation:
```
1. YouTube URL Input
2. Transcribe + Extract Thumbnail
3. Split Content by Platform:
   ├── Instagram: Visual Quotes + Captions
   ├── Twitter: Thread Creation
   ├── LinkedIn: Professional Summary
   ├── TikTok: Hook Extraction
   └── Podcast: Audio Generation
4. Format + Export
```

---

### 🏢 **Business Automation**

#### Meeting Documentation:
```
Recorded Meeting → 
├── Transcription
├── Action Items
├── Summary Email
├── Task Creation
└── Follow-up Reminders
```

#### Customer Support:
```
Support Call Recording →
├── Transcription
├── Sentiment Analysis
├── Issue Classification
├── Knowledge Base Update
└── Follow-up Actions
```

---

## 🐛 Troubleshooting

### ❌ **Häufige Fehler**

#### 1. "Connection Refused" Fehler
```
Error: connect ECONNREFUSED 127.0.0.1:8000
```

**Lösung**: Falsche URL verwenden
```
❌ Falsch: http://localhost:8000
✅ Richtig: http://ai-tools:8000
```

#### 2. "Invalid YouTube URL" Fehler
```
Error: Invalid YouTube URL format
```

**Lösung**: URL Format prüfen
```
✅ Gültige Formate:
- https://youtube.com/watch?v=VIDEO_ID
- https://youtu.be/VIDEO_ID
- https://www.youtube.com/watch?v=VIDEO_ID&t=120s
```

#### 3. "File Upload Failed" Fehler
```
Error: File size exceeds limit
```

**Lösung**: Datei-Limits beachten
- **Max. Dateigröße**: 500MB
- **Max. Video-Länge**: 10 Minuten
- **Unterstützte Formate**: MP4, MP3, WAV, M4A

#### 4. "TTS Voice Not Found" Fehler
```
Error: Voice 'invalid-voice' not supported
```

**Lösung**: Gültige Voice verwenden
```javascript
// Verfügbare Stimmen testen
const availableVoices = [
  'de-DE-KatjaNeural',
  'en-US-JennyNeural', 
  'fr-FR-DeniseNeural',
  'es-ES-ElviraNeural'
];
```

---

### 🔧 **Performance Optimierung**

#### 1. Parallele Verarbeitung nutzen
```
❌ Sequenziell:
Video → Transcribe → TTS → Caption → Done

✅ Parallel:
Video → Transcribe
       ├── TTS (parallel)
       ├── Thumbnail Extract (parallel)
       └── Caption Create (parallel)
```

#### 2. Caching implementieren
```javascript
// Cache Check vor API Call
const cacheKey = `youtube_${videoId}`;
const cached = await redis.get(cacheKey);

if (cached) {
  return JSON.parse(cached);
} else {
  const result = await apiCall();
  await redis.setex(cacheKey, 3600, JSON.stringify(result));
  return result;
}
```

#### 3. Error Handling
```javascript
// Robuste API Calls
try {
  const response = await $http.request({
    method: 'POST',
    url: 'http://ai-tools:8000/text-to-speech',
    body: requestBody,
    timeout: 300000 // 5 Minuten
  });
  
  return response;
} catch (error) {
  if (error.response?.status === 429) {
    // Rate Limit - warten und retry
    await new Promise(resolve => setTimeout(resolve, 5000));
    return retry();
  }
  throw error;
}
```

---

## 📚 API Reference

### 🔗 **Endpoint Übersicht**

| Service | Endpoint | Method | Beschreibung |
|---------|----------|--------|--------------|
| **Original AI Tools** | | | |
| TTS | `/text-to-speech` | POST | Text zu Sprache |
| STT | `/speech-to-text` | POST | Sprache zu Text |
| Upload | `/upload` | POST | Datei hochladen |
| Download | `/download/{id}` | GET | Datei downloaden |
| Status | `/status/{id}` | GET | Datei Status |
| Delete | `/delete/{id}` | DELETE | Datei löschen |
| Caption Video | `/generate-captioned-video` | POST | Video mit Untertiteln |
| Merge Videos | `/merge-videos` | POST | Videos zusammenführen |
| Extract Frame | `/extract-frame` | POST | Frame aus Video |
| **YouTube Extension** | | | |
| Transcribe | `/youtube/transcribe` | POST | YouTube transkribieren |
| YT to TTS | `/youtube/to-tts` | POST | YouTube zu Audio |
| YT to Video | `/youtube/to-captioned-video` | POST | YouTube zu Caption-Video |
| Thumbnail | `/youtube/extract-thumbnail` | POST | Thumbnail extrahieren |

---

### 📋 **Request/Response Schemas**

#### Text-to-Speech Request:
```json
{
  "text": "string (required, max 1000 chars)",
  "voice": "string (optional, default: de-DE-KatjaNeural)",
  "speed": "number (optional, 0.5-2.0, default: 1.0)"
}
```

#### Text-to-Speech Response:
```json
{
  "file_id": "uuid-string",
  "download_url": "string",
  "duration": "number (seconds)",
  "voice_used": "string",
  "text_length": "number"
}
```

#### YouTube Transcribe Request:
```json
{
  "url": "string (required, valid YouTube URL)",
  "language": "string (optional, ISO code or 'auto')"
}
```

#### YouTube Transcribe Response:
```json
{
  "title": "string",
  "duration": "number (seconds)",
  "transcription": {
    "text": "string",
    "language": "string", 
    "confidence": "number (0-1)"
  },
  "thumbnail_url": "string",
  "video_id": "string"
}
```

---

### 🚀 **Rate Limits**

| Endpoint | Limit | Zeitfenster |
|----------|--------|-------------|
| YouTube APIs | 5 requests | pro Minute |
| TTS APIs | 20 requests | pro Minute |
| Upload APIs | 10 requests | pro Minute |
| Download APIs | Unlimited | - |

---

### 💾 **File Limits**

| Typ | Max. Größe | Max. Dauer | Formate |
|-----|------------|------------|---------|
| Audio | 100MB | 30 Min | MP3, WAV, M4A |
| Video | 500MB | 10 Min | MP4, AVI, MOV |
| Image | 10MB | - | JPG, PNG, GIF |
| Text | 10KB | - | TXT, JSON |

---

## 🎉 Community Beitrag

### 🔀 **Workflows teilen**

1. **Workflow exportieren** (JSON)
2. **GitHub Repository** forken
3. **Workflow** in `/community-workflows/` hinzufügen
4. **Pull Request** erstellen

### 📝 **Dokumentation verbessern**

- **Use Cases** hinzufügen
- **Beispiele** erweitern  
- **Troubleshooting** ergänzen
- **Übersetzungen** beitragen

### 💬 **Support & Community**

- **GitHub Issues** für Bug Reports
- **GitHub Discussions** für Feature Requests
- **Discord/Slack** für Community Chat
- **Wiki** für erweiterte Dokumentation

---

<div align="center">

**🚀 Happy Automating! Bau die coolsten Workflows für die Community! 🎯**

[GitHub Repository](https://github.com/oliverhees/ai-tools-extended) • [API Docs](./README.md) • [Community Guide](./community-guide.md)

</div>