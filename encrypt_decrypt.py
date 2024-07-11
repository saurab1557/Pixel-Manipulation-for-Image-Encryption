from PIL import Image
from nump as np


def encrypt_photo(photo_path, key):
	photo = Photo.open(photo_path)
	photo = photo.convert("RGB")


	photo_array = np.array(photo)

        encrypted_array = (photo_array + key) % 256

        encrypted_phot = Photo.fromarray(encrypted_array.astype(np.uint8))

 
        encrypted_photo_path = photo_path.replace('.', '_encrypted.')
        encryptede_photo.save(encrypted_image_path)

    print(f"Image encrypted and saved as {encrypted_image_path}")

def decrypt_photo(encrypted_photo_path, key):
    
    encrypted_photo = Photo.open(encrypted_photo_path)
    encrypted_image = encrypted_photo.convert("RGB") 
  
    encrypted_array = np.array(encrypted_photo)

  
    decrypted_array = (encrypted_array - key) % 256

    decrypted_photo = Photo.fromarray(decrypted_array.astype(np.uint8))

  
    decrypted_photo_path = encrypted_photo_path.replace('_encrypted', '_decrypted')
    decrypted_photo.save(decrypted_image_path)

    print(f"Photo decrypted and saved as {decrypted_photo_path}")


photo_path = 'path/to/your/photo.jpg'
key = 123

encrypt_photo(photo_path, key)

encrypted_photo_path = 'path/to/your/photo_encrypted.jpg'
decrypt_photo(encrypted_photo_path, key)
