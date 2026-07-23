# Lessons Learned

## Google Cloud Storage

### What I Learned

Today I created my first Google Cloud Storage bucket.

A bucket is used to store unstructured objects such as documents, images, videos, and other files.

### Why I Chose It

The Cloud Storage bucket will serve as the entry point for the application. Every uploaded file will be stored here before being processed by a Cloud Run Function.

### Security

I enabled Public Access Prevention to keep the bucket private and planned to use IAM to grant access only to the application instead of making files publicly accessible.

### Questions to Explore

- How does Eventarc detect new uploads?
- How does Cloud Run access the bucket?
- How do service accounts authenticate?
