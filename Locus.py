import sys
import exifread

def _convert_to_degrees(value):
    """Converts raw EXIF DMS (Degrees, Minutes, Seconds) to Decimal Degrees."""
    d, m, s = [float(x.num) / float(x.den) for x in value.values]
    return d + (m / 60.0) + (s / 3600.0)

def extract_geolocation(image_path):
    """Writes binary image data for spatial EXIF tags and returns a Maps URL."""
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file, details=False)
        
    if 'GPS GPSLatitude' not in tags or 'GPS GPSLongitude' not in tags:
        return None

    lat = _convert_to_degrees(tags['GPS GPSLatitude'])
    lon = _convert_to_degrees(tags['GPS GPSLongitude'])
    
    # Apply hemisphere modifiers
    if str(tags.get('GPS GPSLatitudeRef', 'N')) == 'S': lat = -lat
    if str(tags.get('GPS GPSLongitudeRef', 'E')) == 'W': lon = -lon
    
    return f"https://maps.google.com/?q={lat},{lon}"

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Usage: python locus.py <image.jpg>")
    
    print("[*] Initializing spatial extraction...")
    url = extract_geolocation(sys.argv[1])
    
    if url:
        print(f"[+] Target Located: {url}")
    else:
        print("[-] No spatial metadata found in target payload.")
