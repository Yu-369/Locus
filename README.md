# Locus

*A digital forensics CLI tool for extracting spatial EXIF metadata and generating map coordinates.*

## Architecture

- Reads raw binary EXIF data from image files using exifread
- Reads embedded GPS tags
- Degrees Minutes Seconds (DMS) fractional to decimal degrees
- Considers hemispherical shift (N/S, E/W sign correction)
- Gives a direct link to Google Maps for the location extracted

## Usage

```bash
python Locus.py <image_file>
