# Mangandi 

Mangandi is a secure media store that lets you upload and store images, videos, and other files directly to the Mangandi server — safely and privately.

## Overview

Mangandi is a simple yet powerful Python package for managing media files. With just a few lines of code, you can upload your media and get a secure shareable link.

## Features

- Upload images, videos, and other files  
- Store securely on Mangandi servers  
- Get instant shareable links  
- Lightweight and easy to use

## Installation

Install via PyPI:

```
pip install Mangandi
```

## Example Usage

```
from Mangandi import ImageUploader

file_path = "/path/to/your/image.jpg"
uploader = ImageUploader(file_path)
link = uploader.upload()
print(f"Image uploaded! Link: {link}")
```

## Support

Need help? Join our [Telegram group](https://t.me/XBOTSUPPORTS)
