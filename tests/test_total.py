from conftest import *
from config import *


@allure.feature("Тестирование сайта Pizzeria")
@allure.story("Проверка функционала сайта от покупки до оформления заказа")
class TestResult:
    @allure.title("Выбор двух товаров из слайдера и перенос в корзину")
    def test_pizza_1(self, set_up_browser):
        driver = set_up_browser
        with allure.step("Открытие главной страницы"):
            driver.get("https://pizzeria.skillbox.cc/")
        with allure.step("Кладём два товара в корзину"):
            el_1 = driver.find_element(
                By.XPATH,
                '(//img[@src="http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-natasha-filippovskaya-4394612-300x300.jpg"])[1]',
            )
            el_2 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[5]",
            )
            el_3 = driver.find_element(
                By.XPATH,
                "(//img[@src='http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-katerina-holmes-5908222-300x300.jpg'])[2]",
            )
            el_4 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[6]",
            )
            actions = ActionChains(driver)
            actions.move_to_element(el_1).pause(2)
            actions.click(el_2).pause(2)
            actions.perform()
            sleep(1)
            actions.move_to_element(el_3).pause(2)
            actions.click(el_4).pause(2)
            actions.perform()
            sleep(1)

    @allure.title("Прокручивание карусели и выбор одного товара")
    def test_pizza_2(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://pizzeria.skillbox.cc/")
        wait = WebDriverWait(driver, timeout=20)
        wait.until(
            lambda driver: driver.find_element(
                By.XPATH,
                '(//img[@src="http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-natasha-filippovskaya-4394612-300x300.jpg"])[1]',
            )
        )
        el_1 = driver.find_element(
            By.XPATH,
            '(//img[@src="http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-natasha-filippovskaya-4394612-300x300.jpg"])[1]',
        )
        with allure.step("Прокручиваем карусель два раза влево"):
            el_2 = driver.find_element(By.CLASS_NAME, "slick-prev")
        with allure.step("Прокручиваем карусель три раза вправо"):
            el_3 = driver.find_element(By.CLASS_NAME, "slick-next")
            actions = ActionChains(driver)
            actions.move_to_element(el_1).pause(1)
            actions.click(el_2).pause(1)
            actions.click(el_2).pause(1)
            actions.click(el_3).pause(1)
            actions.click(el_3).pause(1)
            actions.click(el_3).pause(1)
            actions.perform()
            sleep(1)
        with allure.step("Положили один товар в корзину"):
            el_4 = driver.find_element(
                By.XPATH,
                '(//img[@src="http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-cottonbro-4004422-300x300.jpg"])[2]',
            )
            el_5 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[9]",
            )
            actions = ActionChains(driver)
            actions.move_to_element(el_4).pause(2)
            actions.click(el_5).pause(2)
            actions.perform()
            sleep(2)

    @allure.title("Переход в карточку товара")
    def test_pizza_3(self, set_up_browser):
        driver = set_up_browser
        with allure.step("Открытие главной страницы"):
            driver.get("https://pizzeria.skillbox.cc/")
        with allure.step("Перешли в карточку выбранного товара"):
            wait = WebDriverWait(driver, 10)
            wait.until(
                lambda driver: driver.find_element(
                    By.XPATH,
                    "(//img[@src='http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-katerina-holmes-5908222-300x300.jpg'])[2]",
                )
            )
            driver.find_element(
                By.XPATH,
                "(//img[@src='http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-katerina-holmes-5908222-300x300.jpg'])[2]",
            ).click()
            sleep(3)

    @allure.title("Работа с товаром в корзине")
    def test_pizza_4(self, set_up_browser):
        driver = set_up_browser
        with allure.step("Переход в карточку товара"):
            driver.get(
                "https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-%d0%ba%d0%b0%d0%ba-%d1%83-%d0%b1%d0%b0%d0%b1%d1%83%d1%88%d0%ba%d0%b8/"
            )
        with allure.step("Выбор опции (Сырный)"):
            driver.find_element(By.ID, "board_pack").click()
            driver.find_element(By.XPATH, '//option[@value="55.00"]').click()
            driver.find_element(By.ID, "board_pack").click()
        with allure.step("Положили этот товар в корзину"):
            driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
        with allure.step("Перешли на страницу Корзина"):
            wait = WebDriverWait(driver, 10)
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//i[@class='fa fa-shopping-cart']")
                )
            )
            driver.find_element(By.XPATH, "//i[@class='fa fa-shopping-cart']").click()
        with allure.step("Увеличили товар на 3 ед."):
            driver.find_element(By.XPATH, "//*[@class='input-text qty text']").clear()
            driver.find_element(
                By.XPATH, "//*[@class='input-text qty text']"
            ).send_keys("3")
        with allure.step("Обновили корзину"):
            driver.find_element(By.XPATH, "//button[@name='update_cart']").click()
            sleep(3)
        with allure.step("Удалили товар из корзины"):
            driver.find_element(By.XPATH, "//a[@class='remove']").click()
            sleep(3)

    @allure.title("Переход на страницу Десерты")
    def test_pizza_5(self, set_up_browser):
        driver = set_up_browser
        with allure.step("Открыли страницу корзины"):
            driver.get("https://pizzeria.skillbox.cc/cart/")
        with allure.step("В главном меню выбрали раздел Десерты"):
            el_1 = driver.find_element(By.XPATH, "//*[contains(text(), 'Меню')]")
            el_2 = driver.find_element(By.XPATH, "// *[contains(text(), 'Десерты')]")
        with allure.step("Перешли в раздел Десерты"):
            actions = ActionChains(driver)
            actions.move_to_element(el_1).pause(1)
            actions.click(el_2).pause(1)
            actions.perform()
            sleep(3)

    @allure.title("Использование фильтра и заказ товара")
    def test_pizza_6(self, set_up_browser):
        driver = set_up_browser
        with allure.step("Открыли раздел Десерты"):
            driver.get("https://pizzeria.skillbox.cc/product-category/menu/deserts/")
        with allure.step("В фильтре по цене установили 130руб."):
            el = driver.find_element(
                By.XPATH,
                "(//span[@class='ui-slider-handle ui-state-default ui-corner-all'])[2]",
            )
            actions = ActionChains(driver)
            actions.click_and_hold(el)
            actions.move_by_offset(-250, 0)
            actions.perform()
        with allure.step("Кликнули на кнопку Применить"):
            driver.find_element(By.CSS_SELECTOR, "button[class='button']").click()
        with allure.step("Кликнули на кнопку В Корзину"):
            driver.find_element(By.XPATH, "//a[@data-product_id = '437']").click()
            sleep(2)
        with allure.step("Кликнули на кнопку Корзина в верхнем меню"):
            driver.find_element(By.XPATH, "//i[@class = 'fa fa-shopping-cart']").click()
            sleep(2)
        with allure.step("Перешли на страницу Корзина"):
            driver.find_element(By.LINK_TEXT, "ПЕРЕЙТИ К ОПЛАТЕ").click()
            sleep(2)

    @allure.title("Переход на страницу Регистрации")
    def test_pizza_7(self, set_up_browser):
        driver = set_up_browser
        with allure.step("Открытие главной страницы"):
            driver.get("https://pizzeria.skillbox.cc/")
        with allure.step("Клик на кнопку Мой аккаунт"):
            driver.find_element(
                By.XPATH, "//*[contains(text(), 'Мой аккаунт')]"
            ).click()
        with allure.step("Клик на кнопку Регистрация"):
            driver.find_element(
                By.CSS_SELECTOR, "button[class='custom-register-button']"
            ).click()

    @allure.title("Регистрация пользователя")
    def test_pizza_8(self, set_up_browser):
        driver = set_up_browser
        with allure.step("Открытие страницы Регистрация"):
            driver.get("https://pizzeria.skillbox.cc/register/")
        with allure.step("Заполнение полей регистрации"):
            driver.find_element(By.ID, "reg_username").send_keys(login)
            driver.find_element(By.ID, "reg_email").send_keys(email)
            driver.find_element(By.ID, "reg_password").send_keys(password)
        with allure.step("Кликаем на кнопку Зарегистрироваться"):
            driver.find_element(
                By.CSS_SELECTOR,
                'button[class="woocommerce-Button woocommerce-button button woocommerce-form-register__submit"]',
            ).click()
        with allure.step("Кликаем на кнопку Мой аккаунт в меню"):
            driver.find_element(
                By.XPATH, "//*[contains(text(), 'Мой аккаунт')]"
            ).click()
            sleep(2)

    @allure.title("Оформление покупки")
    def test_pizza_9(self, set_up_browser):
        driver = set_up_browser
        with allure.step("Открытие главной страницы"):
            driver.get("https://pizzeria.skillbox.cc/")
        with allure.step("Выбираем товар и кладём в корзину"):
            el_1 = driver.find_element(
                By.XPATH,
                '(//img[@src="http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-natasha-filippovskaya-4394612-300x300.jpg"])[1]',
            )
            el_2 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[5]",
            )
            actions = ActionChains(driver)
            actions.move_to_element(el_1).pause(2)
            actions.click(el_2).pause(2)
            actions.perform()
            sleep(1)
        with allure.step("Входим в свой аккаунт"):
            driver.find_element(By.LINK_TEXT, "Войти").click()
        with allure.step("Вводим логин и пароль"):
            driver.find_element(By.ID, "username").send_keys(login)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(
                By.CSS_SELECTOR,
                'button[class="woocommerce-button button woocommerce-form-login__submit"]',
            ).click()
            sleep(2)
        with allure.step("Кликаем на корзину в меню"):
            driver.find_element(By.XPATH, "//i[@class = 'fa fa-shopping-cart']").click()
        with allure.step("Кликаем на кнопку Перейти к оплате"):
            driver.find_element(By.LINK_TEXT, "ПЕРЕЙТИ К ОПЛАТЕ").click()
            sleep(2)
        with allure.step("Заполняем все поля"):
            driver.find_element(By.ID, "billing_first_name").send_keys("Andrey")
            sleep(1)
            driver.find_element(By.ID, "billing_last_name").send_keys("Petrov")
            sleep(1)
            driver.find_element(By.ID, "billing_address_1").send_keys(
                "3-я ул.Строителей"
            )
            sleep(1)
            driver.find_element(By.ID, "billing_city").send_keys("Санкт-Петербург")
            sleep(1)
            driver.find_element(By.ID, "billing_state").send_keys("Ленинградская")
            sleep(1)
            driver.find_element(By.ID, "billing_postcode").send_keys("198207")
            sleep(1)
            driver.find_element(By.ID, "billing_phone").send_keys("89119000000")
            sleep(1)
            driver.find_element(By.ID, "order_date").send_keys("01092024")
            sleep(1)
            comment = driver.find_element(By.ID, "order_comments")
            text = "Хочу получить пиццу завтра после 12-ти. Вход в подъезд со двора"
            for i in text:
                comment.send_keys(i)
                sleep(0.1)
            sleep(1)
        with allure.step("Выбираем метод оплаты"):
            driver.find_element(By.ID, "payment_method_cod").click()
            sleep(1)
        with allure.step("Кликаем на Чекбокс Соглашения"):
            driver.find_element(By.ID, "terms").click()
            sleep(1)
        with allure.step("Кликаем на кнопку Оформить заказ"):
            driver.find_element(By.ID, "place_order").click()
            sleep(5)


@allure.feature("Использование промокода")
@allure.story("Проверка валидного промокода")
class TestAddition:
    @allure.title("Использование валидного промокода")
    def test_pizza_10(self, set_up_browser):
        driver = set_up_browser
        with allure.step("Открытие главной страницы"):
            driver.get("https://pizzeria.skillbox.cc/")
        with allure.step("Выбор товаров из карусели"):
            el_1 = driver.find_element(
                By.XPATH,
                '(//img[@src="http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-natasha-filippovskaya-4394612-300x300.jpg"])[1]',
            )
            el_2 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[5]",
            )
            el_3 = driver.find_element(
                By.XPATH,
                "(//img[@src='http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-katerina-holmes-5908222-300x300.jpg'])[2]",
            )
            el_4 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[6]",
            )
            actions = ActionChains(driver)
            actions.move_to_element(el_1).pause(2)
            actions.click(el_2).pause(2)
            actions.perform()
            actions.move_to_element(el_3).pause(2)
            actions.click(el_4).pause(2)
            actions.perform()
        with allure.step("Кликаем на ссылку Корзина, в меню"):
            driver.find_element(By.XPATH, "//i[@class = 'fa fa-shopping-cart']").click()
            sleep(1)
        with allure.step("На странице Корзина вводим валидный промокод"):
            driver.find_element(By.ID, "coupon_code").send_keys("GIVEMEHALYAVA")
            sleep(1)
        with allure.step("Кликаем на кнопку Применить купон"):
            driver.find_element(By.XPATH, "//button[@name='apply_coupon']").click()
            sleep(5)

    @allure.title("Использование невалидного промокода")
    def test_pizza_11(self, set_up_browser):
        driver = set_up_browser
        with allure.step("Открытие главной страницы"):
            driver.get("https://pizzeria.skillbox.cc/")
        with allure.step("Выбор товаров из карусели"):
            el_1 = driver.find_element(
                By.XPATH,
                '(//img[@src="http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-natasha-filippovskaya-4394612-300x300.jpg"])[1]',
            )
            el_2 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[5]",
            )
            el_3 = driver.find_element(
                By.XPATH,
                "(//img[@src='http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-katerina-holmes-5908222-300x300.jpg'])[2]",
            )
            el_4 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[6]",
            )
            actions = ActionChains(driver)
            actions.move_to_element(el_1).pause(1)
            actions.click(el_2).pause(1)
            actions.perform()
            actions.move_to_element(el_3).pause(1)
            actions.click(el_4).pause(1)
            actions.perform()
            sleep(1)
        with allure.step("Кликаем на ссылку Корзина, в меню"):
            driver.find_element(By.XPATH, "//i[@class = 'fa fa-shopping-cart']").click()
            sleep(1)
        with allure.step("На странице Корзина вводим невалидный промокод"):
            driver.find_element(By.ID, "coupon_code").send_keys("DC120")
            sleep(1)
        with allure.step("Кликаем на кнопку Применить купон"):
            driver.find_element(By.XPATH, "//button[@name='apply_coupon']").click()
            sleep(5)

    @allure.title("Использование валидного промокода два раза")
    def test_pizza_12(self, set_up_browser):
        driver = set_up_browser
        with allure.step("Открываем страницу Регистрации"):
            driver.get("https://pizzeria.skillbox.cc/register/")
            sleep(2)
        with allure.step("Вводим в поля логин, почту, пароль"):
            driver.find_element(By.ID, "reg_username").send_keys(login_3)
            sleep(2)
            driver.find_element(By.ID, "reg_email").send_keys(email_3)
            sleep(2)
            driver.find_element(By.ID, "reg_password").send_keys(password_3)
            sleep(2)
        with allure.step("Кликаем на кнопку Зарегистрироваться"):
            driver.find_element(
                By.CSS_SELECTOR,
                'button[class="woocommerce-Button woocommerce-button button woocommerce-form-register__submit"]',
            ).click()
            sleep(2)
        with allure.step("Переходим на главную страницу"):
            driver.find_element(By.LINK_TEXT, "Главная").click()
        with allure.step("Кладём товар в корзину из карусели"):
            el_1 = driver.find_element(
                By.XPATH,
                '(//img[@src="http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-natasha-filippovskaya-4394612-300x300.jpg"])[1]',
            )
            el_2 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[5]",
            )
            actions = ActionChains(driver)
            actions.move_to_element(el_1).pause(2)
            actions.click(el_2).pause(2)
            actions.perform()
        with allure.step("Переходим на страницу Корзина"):
            driver.find_element(By.XPATH, "//i[@class = 'fa fa-shopping-cart']").click()
        with allure.step("Вводим валидный промокод"):
            driver.find_element(By.ID, "coupon_code").send_keys("GIVEMEHALYAVA")
            sleep(1)
        with allure.step("Кликаем на кнопку Применить купон"):
            driver.find_element(By.XPATH, "//button[@name='apply_coupon']").click()
            sleep(2)
        with allure.step("Кликаем на кнопку Перейти к оплате"):
            driver.find_element(By.LINK_TEXT, "ПЕРЕЙТИ К ОПЛАТЕ").click()
            sleep(2)
        with allure.step("Заполняем все поля"):
            driver.find_element(By.ID, "billing_first_name").send_keys("Andrey")
            sleep(1)
            driver.find_element(By.ID, "billing_last_name").send_keys("Petrov")
            sleep(1)
            driver.find_element(By.ID, "billing_address_1").send_keys(
                "5-ая ул.Строителей"
            )
            sleep(1)
            driver.find_element(By.ID, "billing_city").send_keys("Санкт-Петербург")
            sleep(1)
            driver.find_element(By.ID, "billing_state").send_keys("Ленинградская")
            sleep(1)
            driver.find_element(By.ID, "billing_postcode").send_keys("198207")
            sleep(1)
            driver.find_element(By.ID, "billing_phone").send_keys("89119000000")
            sleep(1)
        with allure.step("Кликаем на Чекбокс Соглашения"):
            driver.find_element(By.ID, "terms").click()
            sleep(1)
        with allure.step("Кликаем на кнопку Оформить заказ"):
            driver.find_element(By.ID, "place_order").click()
            sleep(1)
        with allure.step("Переходим на главную страницу"):
            driver.find_element(By.LINK_TEXT, "Главная").click()
        with allure.step("Кладём товар в корзину из карусели"):
            el_1 = driver.find_element(
                By.XPATH,
                "(//img[@src='http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-katerina-holmes-5908222-300x300.jpg'])[2]",
            )
            el_2 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[6]",
            )
            actions = ActionChains(driver)
            actions.move_to_element(el_1).pause(2)
            actions.click(el_2).pause(2)
            actions.perform()
        with allure.step("Переходим на страницу Корзина"):
            driver.find_element(By.XPATH, "//i[@class = 'fa fa-shopping-cart']").click()
        with allure.step("Вводим валидный промокод"):
            driver.find_element(By.ID, "coupon_code").send_keys("GIVEMEHALYAVA")
            sleep(1)
        with allure.step("Кликаем на кнопку Применить купон"):
            driver.find_element(By.XPATH, "//button[@name='apply_coupon']").click()
            sleep(5)

    @allure.title("Активация бонусной программы")
    def test_pizza_14(self, set_up_browser):
        driver = set_up_browser
        with allure.step("Переход на страницу бонусная программа"):
            driver.get("https://pizzeria.skillbox.cc/bonus/")
        with allure.step("Заполнение поля Имя"):
            driver.find_element(By.ID, "bonus_username").send_keys("Andrey")
        with allure.step("Заполнение поля Телефон"):
            driver.find_element(By.ID, "bonus_phone").send_keys("89119998877")
        with allure.step("Кликаем на кнопку Оформить карту"):
            driver.find_element(By.XPATH, "//button[@name='bonus']").click()
            sleep(1)
        with allure.step("Закрываем всплывающее окно (alert)"):
            WebDriverWait(driver, 15).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            sleep(5)


@allure.feature("Перехват промокода")
@allure.story("Использование промокода на уязвимость")
class TestAdditionPlaywright:
    @allure.title("Ввод промокода и его перехват")
    def test_cupon(self, browser):
        page = browser
        with allure.step("Блокировка ссылки на активацию промокода"):
            page.route("**/?wc-ajax=apply_coupon", lambda route: route.abort())
        with allure.step("Открываем карточку товара"):
            page.goto(
                "https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-4-%d0%b2-1/"
            )
        with allure.step("Кладём товар в корзину"):
            page.locator('//button[@name="add-to-cart"]').click()
        with allure.step("Переходим на страницу Корзина"):
            page.locator('//i[@class="fa fa-shopping-cart"]').click()
            page.wait_for_timeout(2000)
        with allure.step("Вводим валидный промокод"):
            page.locator("//input[@name='coupon_code']").fill("GIVEMEHALYAVA")
        with allure.step("Кликаем на кнопку Применить купон"):
            page.locator("//button[@name='apply_coupon']").click()
            page.wait_for_timeout(3000)
