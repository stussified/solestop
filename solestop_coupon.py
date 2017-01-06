from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


coupons = ["4W4GTK0595KF","SI09SSAG7M85","NG8MLH2AKRS2","GL0IA6VTNMOE",
		   "40RDAKEOQK66","DRGCVA8N9YWV","K0LK2BKRRXF5","OKO2PWZXLKNL",
		   "QUHPFEFCQE5C","QHW5NTY6UTCD","V305AT18I3FN","HTW82LJIB9MI",
		   "RYKPXICPRN89","1GIM3YTSWM05","HGV6OW4JQXIE","JDG66JP17UDL",
		   "AOJZ6CFCKQZX","263ZFOI7DHVJ","P7WFCI0CLSQS","SI1PG74L2GI5",
		   "59UR2LIUPU39","90LN26S2N1UY","8MFOGITGRN7R","2KFOBXWT0SCU",
		   "Y1FW66S4X0RA","GHL45K5SPN51","ELR5M1QSH451","WUVE8SJR2PM1",
		   "U9BJGUBC4O14","1CDZ7IR14CQM"]



def driver(code):
	# url = "https://www.solestop.com/cart/31454413188:1" actual shoe
	url = "https://www.solestop.com/cart/33076305796:1"
	driver = webdriver.Firefox()
	driver.get(url)
	coupon_text = driver.find_element_by_id("checkout_reduction_code")
	coupon_text.send_keys(code)
	submit_button = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div/div[2]/form[1]/div/div/div/button").click()
	try:
		time.sleep(5)
		discount_applied = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[1]/form/span[2]/span")
		if discount_applied:
			price = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[2]/span").text.replace("-","").replace("$", "").replace(" ","")
			discount_off = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[2]/span").text.replace("-","").replace("$", "").replace(" ","")
			print "Coupon:", code, "Percentage:", (float(discount_off)/float(price)) * 100
			driver.quit()
	# except Exception, e:
	# 	print e
	except NoSuchElementException:
		print code, "didn't work"
		driver.quit()
		pass
	except Exception, e:
		print e
		driver.quit()
		pass

def main():
	for coupon in coupons:
		driver(coupon)

	# driver("Y1FW66S4X0RA")

if __name__ == "__main__":
	main()