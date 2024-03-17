# python3 -m venv .venv
# source .venv/bin/activate
# python3 -m pip install -r requirements.txt

import aiohttp
import asyncio
import time
import requests
import os



start_time = time.time()
max = 1
url = "http://localhost:5000"
url_upload = "http://localhost:5000/upload"


async def simple_get(session, url):
     async with session.get(url) as resp:
          sometext = await resp.text()
          return sometext

# the f is for futures
async def fget(session, url):
        tasks = []
        for number in range(1, max + 1):
            tasks.append(asyncio.ensure_future(simple_get(session, url)))

        aggr = await asyncio.gather(*tasks)
        for item in aggr:
            print(item)


def send_file_to_server(filename, server_url):
    # Open the file to be sent
    with open(filename, 'rb') as file:
        files = {'file': (filename, file)}

        # Send the POST request with the file attached
        response = requests.post(server_url, files=files)

        # Print the server's response
        print("Server's response:", response.text)


def send_files_to_server(folder_path, server_url):
    # Initialize counter
    file_counter = 0

    # Iterate over the files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if the item is a file
        if os.path.isfile(file_path):
            # Increment file counter
            file_counter += 1

            # Open the file to be sent
            with open(file_path, 'rb') as file:
                files = {'file': (filename, file)}

                # Send the POST request with the file attached
                response = requests.post(server_url, files=files)

                # Print the server's response
                print(f"File {file_counter}: {filename}, Server's response:", response.text)



async def main():

    async with aiohttp.ClientSession() as session:

        # await fget(session, url)

        if __name__ == "__main__":
            # Specify the filename and the server URL
            # filename = './payload.pdf'  # Replace with the path to your file
            folder_path = './payload'
            # Send the file to the server
            # send_file_to_server(filename, url_upload)
            send_files_to_server(folder_path, url_upload)

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))

