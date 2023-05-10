from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

options = Options()
options.accept_insecure_certs = True

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://localhost:18306")

addchance = [0] * 10
#addchance += [1] * 1


def buy_product(first_product: bool, category: int):
    buttonup = driver.find_element(By.CSS_SELECTOR,
                                   "button[class = \"btn btn-touchspin js-touchspin bootstrap-touchspin-up\"]")
    ifbought = 1
    if first_product:
        # how much product will the program add
        addnumber = 1
    else:
        addnumber = (random.choice(addchance))
    for _ in range(addnumber):
        buttonup.click()
    try:
        element = driver.find_element(By.CSS_SELECTOR, "i[class='material-icons product-unavailable']")
        ifbought = 0
    except NoSuchElementException:
        addtocart = driver.find_element(By.CSS_SELECTOR, "button[class = \"btn btn-primary add-to-cart\"]")
        addtocart.click()
        time.sleep(2)
        try:
            continueshopping = driver.find_element(By.CSS_SELECTOR, "button[class = 'btn btn-secondary']")
            continueshopping.click()
        except NoSuchElementException:
            time.sleep(4)
            continueshopping = driver.find_element(By.CSS_SELECTOR, "button[class = 'btn btn-secondary']")
            continueshopping.click()
        time.sleep(2)
    driver.find_elements(By.CSS_SELECTOR, ".top-menu[data-depth=\"0\"] > .category")[category].click()
    return ifbought


def buy_products_in_category(first: bool, quantity_of_sec_category: int, category: int):
    elements = driver.find_elements(By.CSS_SELECTOR, "article[data-id-product]")
    howmany = min(len(elements), 2) if first else quantity_of_sec_category
    first_product = True if first else False
    ilosc = 0
    indeks = 0
    while ilosc < howmany:
        goin = 1
        elements = driver.find_elements(By.CSS_SELECTOR, "article[data-id-product]")
        cena = 0
        try:
            cena = elements[indeks].find_element(By.CSS_SELECTOR, "span[class='price']")
            cena = cena.text[0:3] if cena.text[1] != ' ' else cena.text[0] + cena.text[2:5]
        except NoSuchElementException:
            goin = 0
        if int(cena) < 445 and goin == 1:
            elements[indeks].click()
            if_bought = buy_product(first_product, category)
            if if_bought == 1:
                ilosc += 1
        first_product = False if True else first_product
        indeks += 1
        if indeks == len(elements):
            nextpage = driver.find_element(By.CSS_SELECTOR, "a[rel='next']")
            nextpage.click()
            time.sleep(4)
            indeks = 0
    return 3 - howmany


def buy_products():
    time.sleep(3)
    # znajdz kategorie produktow(bez podkategorii)
    elements = driver.find_elements(By.CSS_SELECTOR, ".top-menu[data-depth=\"0\"] > .category")
    ile_w_drugim = 3
    for i in range(2):
        elements = driver.find_elements(By.CSS_SELECTOR, ".top-menu[data-depth=\"0\"] > .category")
        elements[i].click()
        ile_w_drugim = buy_products_in_category(True if i == 0 else False, ile_w_drugim, i)


def remove_product_from_cart():
    tocart = driver.find_element(By.CSS_SELECTOR, "i[class = \"material-icons shopping-cart\"")
    tocart.click()
    productsincart = driver.find_elements(By.CSS_SELECTOR, ".cart-item")

    canceledproduct = productsincart[1].find_element(By.CSS_SELECTOR, ".remove-from-cart")
    time.sleep(2)
    canceledproduct.click()

    time.sleep(3)
    productsincart = driver.find_elements(By.CSS_SELECTOR, ".cart-item")


def registeraccount():
    goToCheckout = driver.find_element(By.CSS_SELECTOR,
                                       "a[class='btn btn-primary']")
    goToCheckout.click()
    time.sleep(3)
    gender = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='1']")
    gender.click()
    firstname = driver.find_element(By.CSS_SELECTOR, "input[type='text'][id='field-firstname']")
    firstname.send_keys("Diego")
    lastname = driver.find_element(By.CSS_SELECTOR, "input[type='text'][id='field-lastname']")
    lastname.send_keys("Wick")
    email = driver.find_element(By.CSS_SELECTOR, "input[type='email'][id='field-email']")
    email.send_keys("czerminskikuba@gmail.com")
    password = driver.find_element(By.CSS_SELECTOR, "input[type='password'][id='field-password']")
    password.send_keys("Xie1Hua2Piao3Piao4")
    dateOfBirth = driver.find_element(By.CSS_SELECTOR, "input[id='field-birthday'][name='birthday']")
    dateOfBirth.send_keys("1970-05-31")
    personaldatacheckbox = driver.find_element(By.CSS_SELECTOR, "input[name='customer_privacy'][type='checkbox']")
    personaldatacheckbox.click()
    acceptconditions = driver.find_element(By.CSS_SELECTOR, "input[name='psgdpr'][type='checkbox']")
    acceptconditions.click()
    submit = driver.find_element(By.CSS_SELECTOR, "button[name='continue'][type='submit']")
    submit.click()
    time.sleep(3)


def addresses():
    addr = driver.find_element(By.CSS_SELECTOR, "input[id='field-address1'][name='address1']")
    addr.send_keys("Alabama, 180.32.45.76")
    postal = driver.find_element(By.CSS_SELECTOR, "input[id='field-postcode'][name='postcode']")
    postal.send_keys("01-460")
    city = driver.find_element(By.CSS_SELECTOR, "input[id='field-city'][name='city']")
    city.send_keys("Warsawcon")
    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit'][name='confirm-addresses']")
    # delete_cache()
    submit.click()
    time.sleep(3)


def courrier():
    time.sleep(3)
    chosenCourrier = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][id='delivery_option_13']")
    chosenCourrier.click()
    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit'][name='confirmDeliveryOption']")
    submit.click()
    time.sleep(5)
    try:
        element = driver.find_element(By.CSS_SELECTOR,
                                      "section[id='checkout-delivery-step']" +
                                      "[class='checkout-step -current -reachable js-current-step -clickable']")
        submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit'][name='confirmDeliveryOption']")
        submit.click()
    except NoSuchElementException:
        pass

    time.sleep(5)


def payment():
    webPayment = driver.find_element(By.CSS_SELECTOR, "input[id='payment-option-2'][type='radio']")
    webPayment.click()
    agreement = driver.find_element(By.CSS_SELECTOR,
                                    "input[type='checkbox'][id='conditions_to_approve[terms-and-conditions]']")
    agreement.click()
    confirmPayment = driver.find_element(By.CSS_SELECTOR, "div[id='payment-confirmation']")
    confirmPayment = confirmPayment.find_element(By.CSS_SELECTOR,
                                                 "button[type='submit'][class='btn btn-primary center-block']")
    confirmPayment.click()
    time.sleep(5)


def checkOrder():
    account = driver.find_element(By.CSS_SELECTOR, "a[class='account']")
    account.click()
    time.sleep(3)
    history = driver.find_element(By.CSS_SELECTOR, "a[id='history-link']")
    history.click()
    time.sleep(3)
    orders = driver.find_element(By.CSS_SELECTOR, "section[id='content']")
    numoforders = orders.find_elements(By.CSS_SELECTOR, "tr")
    if len(numoforders) > 0:
        print("Zamowienie przeszlo przez system")


buy_products()
print("Kupilo")
remove_product_from_cart()
print("Usunelo produkt")
registeraccount()
print("Zarejestrowało")
addresses()
print("Podało adres")
courrier()
print("Zaznaczyło kuriera")
payment()
print("Zaznaczyło zapłatę")
checkOrder()

driver.close()
