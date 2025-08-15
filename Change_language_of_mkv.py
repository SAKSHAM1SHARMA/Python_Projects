import os
import subprocess

def change_default_language_to_english(folder_path):
    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".mkv"):
            full_path = os.path.join(folder_path, file_name)
            print(f"Processing: {file_name}")

            # Run mkvpropedit to change audio track(s) to English and set default flag
            try:
                # First, get track info using mkvmerge to find audio track IDs
                cmd_info = ['mkvmerge', '-i', full_path]
                result = subprocess.run(cmd_info, capture_output=True, text=True)
                audio_tracks = []

                for line in result.stdout.splitlines():
                    if 'audio' in line.lower():
                        # Extract track ID, e.g., "Track ID 1: audio"
                        parts = line.split()
                        if "ID" in parts:
                            index = parts.index("ID")
                            track_id = parts[index + 1].strip(':')
                            audio_tracks.append(track_id)

                # Edit each audio track to set language to English and default flag
                for tid in audio_tracks:
                    cmd_edit = [
                        'mkvpropedit', full_path,
                        '--edit', f'track:a{tid}',
                        '--set', 'language=japanese',
                        '--set', 'flag-default=1'
                    ]
                    subprocess.run(cmd_edit, check=True)
                print(f"✔ Updated audio language and default flag in: {file_name}")

            except subprocess.CalledProcessError as e:
                print(f"✖ Error processing {file_name}: {e}")
            except Exception as e:
                print(f"⚠ Unexpected error: {e}")

# Change this to your actual folder path
folder = r"C:\Users\saksh\Downloads\Telegram Desktop\test_subject"
change_default_language_to_english(folder)
