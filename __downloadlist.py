import os

# while True:
#     website_dict = {}





# BUFFERING .TXT
# count = 0
# thefile = open(thefilepath, 'rb')
# while 1:
#     buffer = thefile.read(8192*1024)
#     if not buffer: break
#     count += buffer.count('\n')
# thefile.close(  )
#as_list = l.split(", ")



website_list = []
count = 0
hrefdata = 'hrefdata.txt'
cwd = os.getcwd()
href_loc = str(cwd) + f'/{hrefdata}'
href_str = f'[SYSTEM]** Dump The Text Data To: [{href_loc}] ** [SYSTEM]'
print(href_str)

with open(href_loc) as f:
	for href in open(href_loc):
		website_list = f.readlines(count)
		#website_list = [x.strip() for x in content] 
		index = 0 
		count += 1
		for iterate in website_list:
			if index < count:
				print(f'[SYS]** ADDED {iterate}')
			else:
				break
		print(f'[SYSTEM] Found {count} items in .txt')

		break


		# while index != count:
		# 	website_list.append(href)
		# 	if index == count: 
		# 		break
		# count += 1 
		# index += 1



# website_list = []
# my_file = open("/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/hrefdata.txt", "r")
# content = my_file.readlines()
# print(content)
# #
# print(website_list)
# my_file.close()





# website_list = []
# with open("/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/hrefdata.txt", "r") as f:
# 	for href in f:
# 		index = 0
# 		while index != count:
# 			if index == count:
# 				break
			
# 			index += 1
# 		print (website_list)


		#website_list = website_list.split(",")


# website_list = [
# 	"https://archive.org/download/redump.dc.revival/Boku%20Doraemon%20%28Japan%29.zip",
# 	"https://archive.org/download/redump.dc.revival/Broadband%20Passport%20%28Japan%29.zip",
# 	"https://archive.org/download/redump.dc.revival/Bust-A-Move%204%20%28Europe%29.zip",

#     "https://archive.org/download/PS3_NOINTRO_USA_1/Call%20of%20Duty%20-%20Black%20Ops%20%28USA%29.zip/",

#     "http://itorrents.org/torrent/BDB7B86A1099FE63B2575DAB4DAF6E7F5B4BA1FB.torrent",
#     "http://itorrents.org/torrent/5CD438F8A555FF86823F828373F15C876928CECE.torrent",
#     "http://itorrents.org/torrent/A2E3CD875D1E180F541DEB15F1A23F32ECD18505.torrent",
#     "http://torrage.info/torrent.php?h=A2E3CD875D1E180F541DEB15F1A23F32ECD18505",
#    # "http://btcache.me/torrent/5CD438F8A555FF86823F828373F15C876928CECE",
# ]

# #
