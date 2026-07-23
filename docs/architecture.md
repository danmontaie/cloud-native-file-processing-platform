# Architecture

```text
Cloud Storage
      │
      ▼
Eventarc
      │
      ▼
Cloud Run Function
      │
      ▼
Firestore
```

## Components

- Cloud Storage stores uploaded files.
- Eventarc listens for upload events.
- Cloud Run processes uploaded files.
- Firestore stores metadata.