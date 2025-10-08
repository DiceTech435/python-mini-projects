import random
import urllib.request as request

# DOWNLOAD FILES FROM THE WEB
csv = 'enter url here'
def download_csv(csv_url):
    connect = request.urlopen(csv_url)
    file = connect.read()
    csv_str = str(file)
    lines = csv_str.split("\\n")
    save = r'file.csv'
    fr = open(save, 'w')
    for line in lines:
        fr.write(line + "\n")
        fr.close()
    
download_csv(csv)

# DOWNLOAD IMAGE FROM WEB
# def download_image(url):
#     name = random.randrange(1, 1000)
#     file_name = str(name) + ".jpg"
#     urllib.request.urlretrieve(url, file_name)

# download_image('https://myentrepreneursguide.com')
