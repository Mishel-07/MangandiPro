# mangandi sample code of image to link

from Mangandi import ImageUploader

k = "/path/to/your/file.jpg"
up = ImageUploader(k)
link = up.upload()
print(f"Image uploaded! {link}")
