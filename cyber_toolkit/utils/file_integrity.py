import hashlib
import os

def calculate_sha256(filepath):
    """Calculates the SHA-256 hash of a given file."""
    sha256_hash = hashlib.sha256()
    
    # Check if the file actually exists before trying to read it
    if not os.path.exists(filepath):
        return None
        
    try:
        with open(filepath, "rb") as f:
            # Read the file in small blocks (4KB) so large files don't crash your RAM
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"[-] Error reading file: {e}")
        return None
