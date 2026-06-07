"""
Problem 10 of 10 — "concurrent.futures pipeline"
This is a realistic Netflix-style problem — fetch data concurrently, process results as they complete.
Scenario: You have 8 video IDs. For each, simulate fetching metadata (I/O-bound, ~1s). As each result comes in, print it immediately — don't wait for all to finish first. Use ThreadPoolExecutor with max 3 workers.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time

VIDEO_IDS = [101, 102, 103, 104, 105, 106, 107, 108]

def fetch_metadata(video_id):
    # simulates an API call
    time.sleep(1)
    return {"id": video_id, "title": f"Video {video_id}", "duration": video_id * 10}

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(fetch_metadata, id) for id in VIDEO_IDS]
    
        for future in as_completed(futures):
            result = future.result()
            print(result)

if __name__ == '__main__':
    main()